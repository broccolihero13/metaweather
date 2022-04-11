from starlette.requests import Request
from services import city_service
from typing import List
from viewmodels.shared.viewmodel import ViewModelBase

class IndexViewModel(ViewModelBase):
  def __init__(self, request: Request):
    super().__init__(request)
    self.cities: List = []

  def set_cities(self):
    self.cities = sorted(city_service.cities(), key=lambda c: c['title'])
