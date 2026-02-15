from fastapi import Query
from fastapi.routing import APIRouter
from src.container import spisok_cow

from random import randint

from src.schemas import LivestockCreate, LivestockChange, LivestockFilter
from src.const import stateEnum

router = APIRouter()


@router.post('/list')
async def get_all(filter: LivestockFilter):
    output = []
    for i, v in spisok_cow.items():
        is_ok = True
        if filter.string_search is not None:
            if not filter.string_search in v['name']:
                is_ok = False
        if filter.type is not None:
            if not filter.type == v['type']:
                is_ok = False
        if is_ok:
            output.append(v)
    return output


@router.get('/get/{cow_vin}')
async def get_cow_by_vin(cow_vin:str):
    return spisok_cow.get(cow_vin)


@router.post('/add')
async def add_cow(
    body: LivestockCreate = Query(...)
):
    vin_n = f'vin{randint(0,10000)}'
    spisok_cow[vin_n] = {**body.__dict__}
        # 'name': body.name,
        # 'type': body.type,
        # 'sex': body.sex,
        # 'weight': body.weight,
        # 'state': body.state
    return spisok_cow[vin_n]


@router.patch('/state_patch/{cow_vin}')
async def get_cow_by_vin(cow_vin:str, state:stateEnum):
    spisok_cow[cow_vin]['state'] = state
    return spisok_cow[cow_vin]


@router.put('/state_put/{cow_vin}')
async def changing_information(cow_vin:str, body: LivestockChange = Query(...)):
    spisok_cow[cow_vin].update(
        {
            key:value for key, value in body if value is not None 
        }
    )
    return spisok_cow[cow_vin]


@router.delete('/delete/{cow_vin}')
async def delete_livestock(cow_vin):
    return spisok_cow.pop(cow_vin, None)

