from contextlib import asynccontextmanager
from fastapi import FastAPI
from api import router as api_router

from core.config import settings
from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    print('dispose db engine')
    await db_helper.dispose()


app = FastAPI(
    lifrespan=lifespan,
)
app.include_router(
    api_router,
    prefix=settings.api.prefix,
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True
    )
