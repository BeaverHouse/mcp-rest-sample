<p align="center">
  <a href="https://github.com/BeaverHouse/mcp-rest-sample">
    <img src="logo.png" alt="Logo" height="100"> 
  </a>

  <p align="center">
    FastAPI backend template with MCP Streamable HTTP.
  </p>

  <p align="center">
    <a href="https://python.org/">
      <img src="https://img.shields.io/badge/Python-00ADD8.svg?style=flat&logo=python&logoColor=white" alt="Python">
    </a>
    <a href="https://fastapi.tiangolo.com/">
      <img src="https://img.shields.io/badge/FastAPI-5391FE.svg?style=flat&logo=FastAPI&logoColor=white" alt="FastAPI">
    </a>
    <a href="https://uv.astral.sh/">
      <img src="https://img.shields.io/badge/uv-004354.svg?style=flat&logo=uv&logoColor=white" alt="uv">
    </a>
    <a href="https://modelcontextprotocol.io">
      <img src="https://img.shields.io/badge/MCP-111111.svg?style=flat&logo=modelcontextprotocol&logoColor=white" alt="MCP">
    </a>
    <a href="./LICENSE">
      <img src="https://img.shields.io/github/license/BeaverHouse/mcp-rest-sample" alt="License">
    </a>
  </p>
</p>

## Description

This repository is a small backend template for services that need both:

- human/API-client access through REST endpoints
- agent access through MCP (Model Context Protocol) tools, resources, and prompts

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

## Auth Discovery

This sample does not implement OAuth or OpenID Connect discovery. Some MCP
clients may probe `.well-known` URLs before calling `/mcp`, such as:

- `/.well-known/oauth-protected-resource/mcp`
- `/mcp/.well-known/oauth-protected-resource`
- `/.well-known/oauth-authorization-server/mcp`
- `/.well-known/openid-configuration/mcp`

Those requests can return `404 Not Found` in this local sample. That is expected
as long as JSON-RPC requests to `/mcp` return `200 OK` or `202 Accepted`.

To turn this into an authenticated HTTP MCP server, add:

- OAuth 2.0 Protected Resource Metadata for the MCP resource server.
- Authorization Server Metadata or a documented external authorization server.
- `WWW-Authenticate` headers on `401 Unauthorized` responses that point clients
  to the protected resource metadata.
- Bearer token validation on every MCP HTTP request, including audience checks
  so tokens are scoped to this MCP server.
- Tests for anonymous access, invalid tokens, valid tokens, metadata discovery,
  and token audience failures.

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

## Key Notes

- Keep REST/MCP layers thin: validate transport input, call internal logic, return typed models.
- Be cautious when you make MCP for irreversible or destructive actions.
- Add auth, database, background work, and external clients as separate layers.
