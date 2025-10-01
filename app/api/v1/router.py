"""Main API router for v1."""

from fastapi import APIRouter

from app.api.v1.endpoints import hello

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(hello.router, prefix="/hello", tags=["hello"])
