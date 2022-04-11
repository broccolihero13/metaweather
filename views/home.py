import fastapi
from fastapi_chameleon import template
from starlette.requests import Request
from viewmodels.home.indexviewmodel import IndexViewModel
from viewmodels.shared.viewmodel import ViewModelBase
router = fastapi.APIRouter()

@router.get('/')
@template()
async def index(request: Request):
  vm = IndexViewModel(request)
  vm.set_cities()
  return vm.to_dict()

@router.get('/about')
@template()
def about(request: Request):
  vm = ViewModelBase(request)
  return vm.to_dict()
