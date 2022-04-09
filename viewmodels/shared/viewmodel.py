from typing import Optional
from services import user_service
from starlette.requests import Request

class ViewModelBase:
  def __init__(self, request: Request):
    self.request: Request = request
    self.error: Optional[str] = None
    self.user_id: Optional[int] = user_service.user()
  
  def to_dict(self) -> dict:
    return self.__dict__
