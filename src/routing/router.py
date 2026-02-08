from fastapi.routing import APIRouter
from src.config import settings
from src.service.serv import Service

router = APIRouter(prefix='/hihihih')


@router.get('/hello-world')
async def hello_world():
    return "ipweiorwep!"

@router.get('/hello-world/{o}')
async def hello_world():
    return "Hi mam!"

@router.post('/object/{object_id}')
async def get_object(object_id: int, body: dict):
    return Service.f(1)

@router.delete('/hello-world')
async def get_object(object_id: int, body: dict):
    return Service.f(1)