import uvicorn
from fastapi import FastAPI, Request, Depends
from app.v1.router.user_route import router as user_router
from app.v1.router.symbol_router import router as symbol_router
from loguru import logger

logger.remove()
logger.add("app/v1/logs/app.log", colorize=False, format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {message}")  # noqa: E501

app = FastAPI()


async def logging_dependency(request: Request):
    logger.debug(f"{request.method} {request.url}")
    logger.debug("Params:")
    try:
        _json_dict = await request.json()
        for name, value in _json_dict.items():
            logger.debug(f"\t{name}: {value}")
    except Exception:
        logger.debug("not json params")

    logger.debug("Headers:")
    for name, value in request.headers.items():
        logger.debug(f"\t{name}: {value}")


app.include_router(user_router, dependencies=[Depends(logging_dependency)])
app.include_router(symbol_router, dependencies=[Depends(logging_dependency)])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
