import time
from fastapi import FastAPI, Request
from routers.userrouters import router as user_router
from database.database import Base,engine
import logging
from logging_config import setup_logging

setup_logging()
logger=logging.getLogger(__name__)

app = FastAPI()

app.include_router(user_router)

Base.metadata.create_all(bind=engine)

logger = logging.getLogger(__name__)


@app.middleware("http")
async def request_logging_middleware(
    request: Request,
    call_next
):
    start_time = time.perf_counter()

    logger.info(
        "Request started: %s %s",
        request.method,
        request.url.path
    )

    try:
        response = await call_next(request)

        process_time = time.perf_counter() - start_time

        logger.info(
            "Request completed: %s %s → %s (%.4fs)",
            request.method,
            request.url.path,
            response.status_code,
            process_time
        )

        return response

    except Exception:
        process_time = time.perf_counter() - start_time

        logger.exception(
            "Request failed: %s %s (%.4fs)",
            request.method,
            request.url.path,
            process_time
        )

        raise

