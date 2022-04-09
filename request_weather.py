import asyncio
import aiohttp
import timeit

loop = asyncio.get_event_loop()
locations = ['2487610', '2442047', '2366355', '2487956', '2487889', '2488042', '2487796', '2488853', '349859']

async def gather_task(loc, q: asyncio.Queue):
  # set async client session to gather json from the web for each location
  async with aiohttp.ClientSession() as session:
    async with session.get(f'https://www.metaweather.com/api/location/{loc}/') as response:
      # check if response was successful
      if response.status == 200:
        j = await response.json()

        loc_average = sum(day['max_temp'] for day in j['consolidated_weather']) / len(j['consolidated_weather'])
        await q.put({'title': j['title'], 'avg': loc_average})
      else:
        return f"Error: {response.status} - `{loc}` ID is invalid"

async def main():
  q = asyncio.Queue()
  # set task for each request to run concurrently
  loc_dicts = [asyncio.create_task(gather_task(loc,q)) for loc in locations]
  await asyncio.gather(*loc_dicts)
  for i in q._queue:
    print(f"{i['title']} Average Max Temp: {'{:.2f}'.format(i['avg'])}")

if __name__ == '__main__':
  start = timeit.default_timer()
  loop.run_until_complete(main())
  stop = timeit.default_timer()
  print(f'process took {stop - start} to complete')

