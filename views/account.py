from starlette.requests import Request
import fastapi
from fastapi_chameleon import template
from viewmodels.account.accountviewmodel import AccountViewModel
from viewmodels.account.loginviewmodel import LoginViewModel
from viewmodels.account.registerviewmodel import RegisterViewModel

router = fastapi.APIRouter()

@router.get('/account')
@template()
def account(request: Request):
  vm = AccountViewModel(request)
  return vm.to_dict()

@router.get('/account/register')
@template()
def login(request: Request):
  vm = RegisterViewModel(request)
  return vm.to_dict()

@router.get('/account/login')
@template()
def login(request: Request):
  vm = LoginViewModel(request)
  return vm.to_dict()


