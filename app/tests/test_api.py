from fastapi.testclient import TestClient

from main import create_app

BASE_URL = "http://127.0.0.1:8001"
MCP_META = {
    "io.modelcontextprotocol/protocolVersion": "2026-07-28",
    "io.modelcontextprotocol/clientInfo": {"name": "pytest", "version": "0.1.0"},
    "io.modelcontextprotocol/clientCapabilities": {},
}


def test_health_endpoint() -> None:
    with TestClient(create_app(), base_url=BASE_URL) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_project_detail_endpoint() -> None:
    with TestClient(create_app(), base_url=BASE_URL) as client:
        response = client.get("/projects/atlas-api")

    assert response.status_code == 200
    assert response.json()["owner"] == "platform"


def test_project_status_filter() -> None:
    with TestClient(create_app(), base_url=BASE_URL) as client:
        response = client.get("/projects", params={"status": "active"})

    assert response.status_code == 200
    assert [project["id"] for project in response.json()] == ["atlas-api"]


def test_unknown_project_returns_404() -> None:
    with TestClient(create_app(), base_url=BASE_URL) as client:
        response = client.get("/projects/missing")

    assert response.status_code == 404


def test_ticket_triage_endpoint() -> None:
    with TestClient(create_app(), base_url=BASE_URL) as client:
        response = client.get("/projects/tickets/TCK-202/triage")

    assert response.status_code == 200
    assert response.json()["suggested_owner"] == "platform"


def test_unknown_ticket_returns_404() -> None:
    with TestClient(create_app(), base_url=BASE_URL) as client:
        response = client.get("/projects/tickets/missing/triage")

    assert response.status_code == 404


def test_release_notes_endpoint() -> None:
    with TestClient(create_app(), base_url=BASE_URL) as client:
        response = client.get("/projects/atlas-api/release-notes")

    assert response.status_code == 200
    assert "Document Streamable HTTP client setup" in response.json()["highlights"]


def test_mcp_tools_list_over_streamable_http() -> None:
    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/list",
        "params": {"_meta": MCP_META},
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "mcp-protocol-version": "2026-07-28",
        "mcp-method": "tools/list",
    }

    with TestClient(create_app(), base_url=BASE_URL) as client:
        response = client.post("/mcp", json=request, headers=headers)

    assert response.status_code == 200
    tool_names = {tool["name"] for tool in response.json()["result"]["tools"]}
    assert {"search_projects", "inspect_project", "triage_ticket_for_agent"} <= tool_names


def test_mcp_tool_call_over_streamable_http() -> None:
    request = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {
            "name": "search_projects",
            "arguments": {"status": "active"},
            "_meta": MCP_META,
        },
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "mcp-protocol-version": "2026-07-28",
        "mcp-method": "tools/call",
        "mcp-name": "search_projects",
    }

    with TestClient(create_app(), base_url=BASE_URL) as client:
        response = client.post("/mcp", json=request, headers=headers)

    assert response.status_code == 200
    result = response.json()["result"]
    assert result["isError"] is False
    assert "atlas-api" in result["content"][0]["text"]
