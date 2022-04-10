from typing import List
import asyncio
import aiohttp

async def gather_task(url, q: asyncio.Queue):
  # set async client session to gather json from the web for each location
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
      # check if response was successful
      if response.status == 200:
        j = await response.json()
        
        await q.put(j)
      else:
        return f"Error: {response.status} for `{url}`, check your permissions and URL"

