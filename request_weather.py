import asyncio
import sys
import aiohttp
import json
import timeit

loop = asyncio.get_event_loop()
locations = ['2487610', '2442047', '2366355']

async def gather_task(loc):
  # set async client session to gather json from the web for each location
  async with aiohttp.ClientSession() as session:
    async with session.get(f'https://www.metaweather.com/api/location/{loc}/') as response:
      # check if response was successful
      if response.status == 200:
        j = await response.json()

        loc_average = round(sum(day['max_temp'] for day in j['consolidated_weather']) / len(j['consolidated_weather']),2)
        return f"{j['title']} Average Max Temp: {'%.2f' % loc_average}"
      else:
        return f"Error: {response.status} - `{loc}` ID is invalid"

async def main():
  for loc in locations:
    # set task for each request to run concurrently
    task = await asyncio.create_task(gather_task(loc))
    print(task)

if __name__ == '__main__':
  # start = timeit.default_timer()
  loop.run_until_complete(main())
  # stop = timeit.default_timer()
  # print(f'process took {stop - start} to complete')

