import fastapi
from fastapi_chameleon import template


router = fastapi.APIRouter()


@router.get('/account')
@template(template_file='index.pt')
def account():
    return {}


@router.get('/account/register')
@template(template_file='index.pt')
def register():
    return {}


@router.get('/account/login')
@template(template_file='index.pt')
def login():
    return {}


@router.get('/account/logout')
@template(template_file='index.pt')
def logout():
    return {}

