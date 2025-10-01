"""Main FastAPI application module."""

from contextlib import asynccontextmanager
from datetime import datetime, timezone
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.exceptions import setup_exception_handlers
from app.core.middleware import RequestLoggingMiddleware
from app.core.resources import resources
from app.schemas.common import HealthResponse, ReadyResponse, RootResponse


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan manager."""
    # Startup
    await resources.initialize()
    yield
    # Shutdown
    await resources.cleanup()


# Create FastAPI application with enhanced metadata
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
    contact={
        "name": settings.CONTACT_NAME,
        "email": settings.CONTACT_EMAIL,
        "url": settings.CONTACT_URL,
    } if any([settings.CONTACT_NAME, settings.CONTACT_EMAIL, settings.CONTACT_URL]) else None,
    license_info={
        "name": settings.LICENSE_NAME,
        "url": settings.LICENSE_URL,
    } if any([settings.LICENSE_NAME, settings.LICENSE_URL]) else None,
    terms_of_service=settings.TERMS_OF_SERVICE,
    servers=[
        {"url": "http://localhost:8000", "description": "Development server"},
        {"url": "https://api.example.com", "description": "Production server"},
    ] if not settings.is_production else [
        {"url": "https://api.example.com", "description": "Production server"},
    ],
)

# Setup exception handlers
setup_exception_handlers(app)

# Add request logging middleware
app.add_middleware(RequestLoggingMiddleware)

# Set up CORS middleware with production restrictions
cors_origins = settings.cors_origins_list
if settings.is_production and "*" in cors_origins:
    # In production, don't allow all origins
    cors_origins = ["https://yourdomain.com"]  # Replace with actual production domains

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Setup Prometheus metrics
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app, endpoint="/metrics")

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/", response_model=RootResponse)
async def root() -> RootResponse:
    """Root endpoint."""
    return RootResponse(
        message="Welcome to GA Python Template API",
        version=settings.VERSION,
        docs_url="/docs"
    )


@app.get("/health", response_model=HealthResponse, tags=["health"])
async def health_check() -> HealthResponse:
    """Health check endpoint (liveness probe)."""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now(timezone.utc).isoformat()
    )


@app.get("/health/ready", response_model=ReadyResponse, tags=["health"])
async def readiness_check() -> ReadyResponse:
    """Readiness check endpoint (readiness probe)."""
    checks = {}
    
    # Check HTTP client
    if resources.http_client:
        checks["http_client"] = "healthy"
    else:
        checks["http_client"] = "unhealthy"
    
    # Add more checks as needed (database, external services, etc.)
    checks["application"] = "healthy"
    
    all_healthy = all(status == "healthy" for status in checks.values())
    
    return ReadyResponse(
        status="ready" if all_healthy else "not_ready",
        checks=checks,
        timestamp=datetime.now(timezone.utc).isoformat()
    )
