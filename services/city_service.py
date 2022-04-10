from typing import List
import asyncio
import aiohttp
from services.async_service import gather_task

global_locations = ['2487610', '2442047', '2366355']

async def get_weather_data(locations = global_locations):
  q = asyncio.Queue()
  # set task for each request to run concurrently
  loc_dicts = [asyncio.create_task(gather_task(f'https://www.metaweather.com/api/location/{loc}/',q)) for loc in locations]
  await asyncio.gather(*loc_dicts)
  data = []
  for i in q._queue:
    cw = i['consolidated_weather']
    lst = [abr['weather_state_abbr'] for abr in cw]
    most_common = max(lst, key=lst.count)
    loc_average = sum(day['max_temp'] for day in cw) / len(cw)
    data.append({'title': i['title'], 'avg': loc_average, 'common_occ': most_common})
  return data

def cities(limit:int=3) -> List:
  return get_weather_data()
