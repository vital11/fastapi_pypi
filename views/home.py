import fastapi
from fastapi_chameleon import template


router = fastapi.APIRouter()


@router.get('/')
@template(template_file='home/index.pt')
def index(user: str = 'Vitalii'):
    return {
        'package_count': 345_248,
        'release_count': 3_087_548,
        'files_count': 5_293_484,
        'user_count': 557_265,
        'user_name': user,
        'packages': [
            {'id': 'fastapi', 'summary': 'A great web framework.'},
            {'id': 'uvicorn', 'summary': 'Your favorite ASGI server.'},
            {'id': 'gunicorn', 'summary': 'Your favorite WSGI server.'},
            {'id': 'httpx', 'summary': 'Requests for an async world.'},
            {'id': 'pydantic', 'summary': 'Data validation and settings management using python type annotations.'},
            {'id': 'chameleon', 'summary': 'Chameleon is an HTML/XML template engine for Python.'},
        ]
    }


@router.get('/about')
@template(template_file='home/about.pt')
def about():
    return {}
