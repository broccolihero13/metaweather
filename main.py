import fastapi
import uvicorn
import fastapi_chameleon
from starlette.staticfiles import StaticFiles
from views import home
from views import account

def main():
  configure()
  uvicorn.run(app, host='localhost', port=3000)

app = fastapi.FastAPI()

def configure():
  fastapi_chameleon.global_init('templates')
  configure_routes()

def configure_routes():
  app.mount('/static', StaticFiles(directory='static'))
  app.include_router(home.router)
  # app.include_router(account.router)

if __name__ == '__main__':
  main()
else:
  configure()
