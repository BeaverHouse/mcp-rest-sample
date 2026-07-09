from schemas import ProjectDetail, ProjectSummary, ReleaseNoteDraft, Ticket, TicketTriage

PROJECTS: tuple[ProjectDetail, ...] = (
    ProjectDetail(
        id="atlas-api",
        name="Atlas API",
        status="active",
        tags=["fastapi", "mcp", "template"],
        description="Reference backend that exposes the same domain through REST and MCP.",
        owner="platform",
        next_actions=[
            "Keep REST endpoints thin and typed.",
            "Expose model-friendly workflows as MCP tools.",
            "Add persistence only after the boundary is stable.",
        ],
        known_risks=[
            "MCP 2026-07-28 support is currently based on the Python SDK v2 beta.",
            "Auth is intentionally omitted from this sample.",
        ],
    ),
    ProjectDetail(
        id="docs-buddy",
        name="Docs Buddy",
        status="paused",
        tags=["search", "docs", "mock"],
        description="Mock documentation assistant used to demonstrate read-only resources.",
        owner="developer-experience",
        next_actions=[
            "Replace fixtures with a real index.",
            "Keep tool outputs small enough for agent context.",
        ],
        known_risks=["Search scoring is mocked and deterministic."],
    ),
)

TICKETS: tuple[Ticket, ...] = (
    Ticket(
        id="TCK-101",
        title="Expose backend health through REST and MCP",
        project_id="atlas-api",
        priority="medium",
        summary="Consumers need a cheap health signal before calling heavier tools.",
    ),
    Ticket(
        id="TCK-202",
        title="Document Streamable HTTP client setup",
        project_id="atlas-api",
        priority="high",
        summary="The old SSE docs are obsolete and confuse new backend consumers.",
    ),
    Ticket(
        id="TCK-303",
        title="Prototype docs search ranking",
        project_id="docs-buddy",
        priority="low",
        summary="A deterministic mock ranking is enough before a real vector store exists.",
    ),
)


def list_projects(status: str | None = None) -> list[ProjectSummary]:
    projects = PROJECTS
    if status is not None:
        projects = tuple(project for project in projects if project.status == status)
    return [
        ProjectSummary(
            id=project.id,
            name=project.name,
            status=project.status,
            tags=project.tags,
            description=project.description,
        )
        for project in projects
    ]


def get_project(project_id: str) -> ProjectDetail:
    for project in PROJECTS:
        if project.id == project_id:
            return project
    raise ValueError(f"unknown project id: {project_id}")


def list_tickets(project_id: str | None = None) -> list[Ticket]:
    if project_id is None:
        return list(TICKETS)
    return [ticket for ticket in TICKETS if ticket.project_id == project_id]


def triage_ticket(ticket_id: str) -> TicketTriage:
    ticket = _get_ticket(ticket_id)
    project = get_project(ticket.project_id)
    next_action = {
        "high": "Handle before the next public documentation update.",
        "medium": "Schedule in the next backend maintenance pass.",
        "low": "Keep as a backlog item until a real user asks for it.",
    }[ticket.priority]
    return TicketTriage(
        ticket_id=ticket.id,
        priority=ticket.priority,
        suggested_owner=project.owner,
        reasoning=f"{ticket.title}: {ticket.summary}",
        next_action=next_action,
    )


def draft_release_notes(project_id: str) -> ReleaseNoteDraft:
    project = get_project(project_id)
    tickets = list_tickets(project_id)
    highlights = [ticket.title for ticket in tickets] or project.next_actions[:1]
    return ReleaseNoteDraft(
        project_id=project.id,
        title=f"{project.name} backend update",
        highlights=highlights,
        risks=project.known_risks,
    )


def _get_ticket(ticket_id: str) -> Ticket:
    for ticket in TICKETS:
        if ticket.id == ticket_id:
            return ticket
    raise ValueError(f"unknown ticket id: {ticket_id}")
