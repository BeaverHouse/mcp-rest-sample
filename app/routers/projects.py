from typing import Annotated

from fastapi import APIRouter, HTTPException, Query

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

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("", response_model=list[ProjectSummary])
def api_list_projects(
    status: Annotated[ProjectStatus | None, Query()] = None,
) -> list[ProjectSummary]:
    return list_projects(status)


@router.get("/{project_id}", response_model=ProjectDetail)
def api_get_project(project_id: str) -> ProjectDetail:
    try:
        return get_project(project_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/{project_id}/tickets", response_model=list[Ticket])
def api_list_project_tickets(project_id: str) -> list[Ticket]:
    try:
        get_project(project_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return list_tickets(project_id)


@router.get("/tickets/{ticket_id}/triage", response_model=TicketTriage)
def api_triage_ticket(ticket_id: str) -> TicketTriage:
    try:
        return triage_ticket(ticket_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/{project_id}/release-notes", response_model=ReleaseNoteDraft)
def api_draft_release_notes(project_id: str) -> ReleaseNoteDraft:
    try:
        return draft_release_notes(project_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
