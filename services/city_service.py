from typing import List
import asyncio
import aiohttp

global_locations = ['2487610', '2442047', '2366355']

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

async def get_weather_data(locations = global_locations):
  q = asyncio.Queue()
  # set task for each request to run concurrently
  loc_dicts = [asyncio.create_task(gather_task(loc,q)) for loc in locations]
  await asyncio.gather(*loc_dicts)
  data = []
  for i in q._queue:
    data.append(i)
  return data

def cities(limit:int=10) -> List:
  return get_weather_data()