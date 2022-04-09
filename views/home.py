import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()

@router.get('/')
@template()
def index(user: str = 'anonymous'):
  return {
    'username': user,
    'cities': [
      {'title':'Salt Lake City', 'max_temp_avg': 8.70},
      {'title':'Boise', 'max_temp_avg': 23.40},
      {'title':'Los Angeles', 'max_temp_avg': 8.09}

    ]
  }

@router.get('/about')
@template()
def about():
  return {}
