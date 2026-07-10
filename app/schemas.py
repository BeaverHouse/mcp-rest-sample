from typing import Literal

from pydantic import BaseModel, Field

ProjectStatus = Literal["active", "paused", "archived"]
TicketPriority = Literal["low", "medium", "high"]


class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: str
    version: str


class ProjectSummary(BaseModel):
    id: str
    name: str
    status: ProjectStatus
    tags: list[str]
    description: str


class ProjectDetail(ProjectSummary):
    owner: str
    next_actions: list[str]
    known_risks: list[str]


class Ticket(BaseModel):
    id: str
    title: str
    project_id: str
    priority: TicketPriority
    summary: str


class TicketTriage(BaseModel):
    ticket_id: str
    priority: TicketPriority
    suggested_owner: str
    reasoning: str
    next_action: str


class ReleaseNoteDraft(BaseModel):
    project_id: str
    title: str
    highlights: list[str] = Field(min_length=1)
    risks: list[str]
