from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from api import router
from time import time
from exceptions.base import CustomException


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router, prefix="/api")


def init_listeners(app_: FastAPI) -> None:
    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


def init_middlewares(app_: FastAPI) -> None:
    @app_.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        start_time = time()
        response = await call_next(request)
        process_time = time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response


def create_app() -> FastAPI:
    app_ = FastAPI()
    init_routers(app_)
    init_listeners(app_)
    init_middlewares(app_)
    return app_


app = create_app()


async def init_models():
    from database.base import Base
    from database.session import engine
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("startup")
async def on_startup():
    await init_models()
    pass


@app.on_event("shutdown")
async def on_shutdown():
    pass
