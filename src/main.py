from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter
from src.config import settings
from src.routing.router import router as some_router

app = FastAPI(
    openapi_url=f"{settings.BASE_ROUTE_PATH}/openapi.json",
    docs_url=f"{settings.BASE_ROUTE_PATH}/docs"
)
router = APIRouter(prefix=settings.BASE_ROUTE_PATH)

router.include_router(some_router, prefix='/cow')

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True
    )
