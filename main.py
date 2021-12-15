import fastapi
import fastapi_chameleon
import uvicorn
from starlette.staticfiles import StaticFiles

from views import home
from views import account
from views import packages


app = fastapi.FastAPI()


def main():
    configure()
    uvicorn.run(app, host='127.0.0.1', port=8001)


def configure():
    configure_templates()
    configure_routes()


def configure_templates():

    fastapi_chameleon.global_init('templates')


def configure_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


if __name__ == '__main__':
    main()
else:                       # production
    configure()







