from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from config import settings
from mcp_server import create_mcp_server
from routers.health import router as health_router
from routers.projects import router as projects_router


def create_app() -> FastAPI:
    mcp = create_mcp_server()
    mcp_http_app = mcp.streamable_http_app(
        streamable_http_path="/mcp",
        json_response=True,
        stateless_http=True,
    )

    @asynccontextmanager
    async def lifespan(_: FastAPI) -> AsyncGenerator[None]:
        async with mcp.session_manager.run():
            yield

    app = FastAPI(
        title=settings.name,
        description="FastAPI REST endpoints plus MCP Streamable HTTP on /mcp.",
        version=settings.version,
        lifespan=lifespan,
    )

    app.include_router(health_router)
    app.include_router(projects_router)

    for route in mcp_http_app.routes:
        app.router.routes.append(route)

    return app


app = create_app()
