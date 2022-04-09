import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()

@router.get('/account')
@template()
def account(user: str = 'anonymous'):
  return {
    'username': user
  }

@router.get('/account/login')
@template()
def login():
  return {}
