from contextlib import asynccontextmanager
from fastapi import FastAPI
from api import router as api_router

from core.config import settings
from core.models import db_helper

from core.models import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App is started")
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        # await conn.run_sync(Base.metadata.create_all)
    print("Database is started")
    yield
    print('dispose db engine')
    await db_helper.dispose()


app = FastAPI(
    lifespan=lifespan,
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
