"""Main FastAPI application entry point."""

from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.api.v1.visualization import router as visualization_router
from src.config import config
from src.system.resources import IoCContainer


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager for startup and shutdown events."""
    # Startup: Initialize IoC container
    container = IoCContainer()
    container.config.from_dict(config.model_dump())
    app.state.container = container

    yield

    # Shutdown: No cleanup needed



# Create FastAPI application
app = FastAPI(
    title="Data Visualizer API",
    description="API for visualizing CSV data as interactive charts",
    version="0.1.0",
    debug=config.app_debug,
    lifespan=lifespan
    )


# Include routers
app.include_router(
    visualization_router,
    prefix="/api/v1",
    tags=["visualization"]
    )


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Data Visualizer API",
        "version": "0.1.0",
        "docs_url": "/docs"
        }


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host=config.app_host,
        port=config.app_port,
        reload=config.app_debug
    )
