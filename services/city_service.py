from typing import List

def cities(limit:int=10) -> List:
  return [
      {'title':'Salt Lake City', 'max_temp_avg': 8.70},
      {'title':'Boise', 'max_temp_avg': 23.40},
      {'title':'Los Angeles', 'max_temp_avg': 8.09}
    ][:limit]