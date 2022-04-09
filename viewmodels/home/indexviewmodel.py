from starlette.requests import Request
from services import city_service
from viewmodels.shared.viewmodel import ViewModelBase

class IndexViewModel(ViewModelBase):
  def __init__(self, request: Request):
    super().__init__(request)
    self.cities: List = city_service.cities(limit=10)
