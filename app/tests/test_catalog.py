import pytest

from internal.catalog import draft_release_notes, get_project, list_projects, triage_ticket


def test_list_projects_returns_summaries() -> None:
    projects = list_projects()

    assert [project.id for project in projects] == ["atlas-api", "docs-buddy"]


def test_get_project_rejects_unknown_id() -> None:
    with pytest.raises(ValueError, match="unknown project id"):
        get_project("missing")


def test_triage_ticket_uses_project_owner() -> None:
    triage = triage_ticket("TCK-202")

    assert triage.priority == "high"
    assert triage.suggested_owner == "platform"


def test_release_notes_use_project_tickets() -> None:
    notes = draft_release_notes("atlas-api")

    assert notes.title == "Atlas API backend update"
    assert "Document Streamable HTTP client setup" in notes.highlights
