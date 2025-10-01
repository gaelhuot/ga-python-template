"""Custom exceptions and error handlers."""

import logging
from typing import Any

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.schemas.common import ErrorResponse

logger = logging.getLogger(__name__)


def generate_request_id() -> str:
    """Generate a unique request ID."""
    import uuid

    return str(uuid.uuid4())[:8]


async def http_exception_handler(request: Request, exc: HTTPException) -> Any:
    """Handle HTTP exceptions."""
    request_id = getattr(request.state, "request_id", generate_request_id())

    logger.error(
        f"HTTP {exc.status_code} error: {exc.detail}",
        extra={"request_id": request_id, "status_code": exc.status_code},
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            error=f"HTTP_{exc.status_code}",
            message=exc.detail,
            detail=None,
            request_id=request_id,
        ).dict(),
    )


async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> Any:
    """Handle validation exceptions."""
    request_id = getattr(request.state, "request_id", generate_request_id())

    logger.error(
        f"Validation error: {exc.errors()}", extra={"request_id": request_id}
    )

    return JSONResponse(
        status_code=422,
        content=ErrorResponse(
            error="VALIDATION_ERROR",
            message="Request validation failed",
            detail=exc.errors(),
            request_id=request_id,
        ).dict(),
    )


async def general_exception_handler(request: Request, exc: Exception) -> Any:
    """Handle general exceptions."""
    request_id = getattr(request.state, "request_id", generate_request_id())

    logger.error(
        f"Unhandled exception: {str(exc)}",
        extra={"request_id": request_id},
        exc_info=True,
    )

    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error="INTERNAL_SERVER_ERROR",
            message="An unexpected error occurred",
            detail=None,
            request_id=request_id,
        ).dict(),
    )


def setup_exception_handlers(app: FastAPI) -> None:
    """Setup global exception handlers."""
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(
        RequestValidationError, validation_exception_handler
    )
    app.add_exception_handler(Exception, general_exception_handler)
