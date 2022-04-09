from starlette.requests import Request
from services import city_service
from typing import List
from viewmodels.shared.viewmodel import ViewModelBase

class IndexViewModel(ViewModelBase):
  def __init__(self, request: Request):
    super().__init__(request)
    self.cities: List = []

  async def set_cities(self):
    self.cities = await city_service.cities(limit=10)
