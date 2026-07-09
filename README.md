<p align="center">
  <a href="https://github.com/BeaverHouse/mcp-rest-sample">
    <img src="logo.png" alt="Logo" width="100" height="100">
  </a>
</p>

<h1 align="center">mcp-rest-sample</h1>

<p align="center">
  FastAPI backend template with MCP Streamable HTTP.
</p>

## What This Is

This repository is a small backend template for services that need both:

- human/API-client access through REST endpoints
- agent access through Model Context Protocol tools, resources, and prompts

The app exposes one mock domain through both surfaces:

- REST: `/health`, `/projects`, `/projects/{project_id}`, ticket triage, release notes
- MCP: `/mcp` using Streamable HTTP, with matching project/ticket tools and resources

The mock data is intentionally in memory. Add a database only after the REST and
MCP boundaries are clear.

## MCP Status

This template targets the MCP Python SDK v2 beta and the 2026-07-28 release
candidate direction. That means:

- Streamable HTTP is the primary transport.
- `/mcp` is stateless HTTP in this sample.
- The SDK version is pinned exactly because v2 is still a pre-release.
- This is a template and learning sample, not a production MCP compatibility claim.

## Layout

```text
app/
  main.py              # FastAPI app and /mcp route wiring
  mcp_server.py        # MCP tools, resources, prompts
  schemas.py           # Pydantic request/response models
  config.py            # pydantic-settings config
  internal/
    catalog.py         # mock domain logic
  routers/
    health.py
    projects.py
  tests/
```

## Run Locally

```bash
cd app
uv sync --python 3.14 --prerelease allow
uv run uvicorn main:app --reload --host 127.0.0.1 --port 8001
```

Open:

- REST docs: `http://127.0.0.1:8001/docs`
- MCP endpoint: `http://127.0.0.1:8001/mcp`

## Checks

Run the public checks directly with uv:

```bash
cd app
uv run ruff check .
uv run ruff format --check .
uv run mypy .
uv run pytest
uv audit
```

`uv audit` is included as the modern dependency-health command to run against
the lockfile. Keep it visible, but treat upstream advisory availability and the
current uv release status as operational context.

## Template Notes

- Keep REST routers thin: validate transport input, call internal logic, return typed models.
- Keep MCP tools model-friendly: small arguments, clear docstrings, structured outputs.
- Prefer MCP resources for read-only snapshots and tools for actions/workflows.
- Keep mock fixtures until a real persistence boundary is needed.
- Add auth, database, background work, and external clients as separate layers.
