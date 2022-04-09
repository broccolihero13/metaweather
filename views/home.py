import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()

@router.get('/')
@template()
def index(user: str = 'anonymous'):
  return {
    'username': user
  }

@router.get('/about')
@template()
def about():
  return {}
