import json

from mcp.server import CacheHint, MCPServer

from config import settings
from internal.catalog import (
    draft_release_notes,
    get_project,
    list_projects,
    list_tickets,
    triage_ticket,
)
from schemas import (
    ProjectDetail,
    ProjectStatus,
    ProjectSummary,
    ReleaseNoteDraft,
    Ticket,
    TicketTriage,
)


def create_mcp_server() -> MCPServer[object]:
    mcp = MCPServer(
        name="mcp-rest-sample",
        title=settings.name,
        description=(
            "Backend template sample exposing the same mock domain through REST and "
            "MCP Streamable HTTP."
        ),
        version=settings.version,
        cache_hints={
            "tools/list": CacheHint(ttl_ms=60_000, scope="public"),
            "resources/list": CacheHint(ttl_ms=60_000, scope="public"),
        },
    )

    @mcp.tool()
    def search_projects(status: ProjectStatus | None = None) -> list[ProjectSummary]:
        """List mock backend projects, optionally filtered by lifecycle status."""
        return list_projects(status)

    @mcp.tool()
    def inspect_project(project_id: str) -> ProjectDetail:
        """Return project details, risks, and next actions for a known project id."""
        return get_project(project_id)

    @mcp.tool()
    def find_tickets(project_id: str | None = None) -> list[Ticket]:
        """List mock tickets, optionally scoped to one project id."""
        return list_tickets(project_id)

    @mcp.tool()
    def triage_ticket_for_agent(ticket_id: str) -> TicketTriage:
        """Explain priority, ownership, and next action for a mock ticket."""
        return triage_ticket(ticket_id)

    @mcp.tool()
    def draft_project_release_notes(project_id: str) -> ReleaseNoteDraft:
        """Draft short release notes from the mock project and ticket catalog."""
        return draft_release_notes(project_id)

    @mcp.resource("project://{project_id}", mime_type="application/json")
    def project_resource(project_id: str) -> str:
        """Read one project as a cacheable JSON resource."""
        return get_project(project_id).model_dump_json(indent=2)

    @mcp.resource("tickets://all", mime_type="application/json")
    def tickets_resource() -> str:
        """Read the full mock ticket list as a JSON resource."""
        payload = [ticket.model_dump(mode="json") for ticket in list_tickets()]
        return json.dumps(payload, indent=2)

    @mcp.prompt()
    def plan_backend_iteration(project_id: str) -> str:
        """Create an agent prompt for planning the next backend iteration."""
        project = get_project(project_id)
        actions = "\n".join(f"- {action}" for action in project.next_actions)
        risks = "\n".join(f"- {risk}" for risk in project.known_risks)
        return (
            f"Plan the next backend iteration for {project.name}.\n\n"
            f"Known next actions:\n{actions}\n\n"
            f"Known risks:\n{risks}\n\n"
            "Return a concise implementation plan with verification steps."
        )

    return mcp
