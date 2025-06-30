from fastapi import APIRouter
from typing import List

# Custom module import
from models.family import FamilyDetail, FamilyMember
from logic.family import get_family_members, get_family_info_by_id

family_router = APIRouter(prefix="/family", tags=["Family"])

@family_router.get(
    "/",
    response_model=List[FamilyMember],
    description="Get the all family members and their IDs.",
)
def api_get_family_members() -> List[FamilyMember]:
    return get_family_members()

@family_router.get(
    "/{id}",
    response_model=FamilyDetail,
    description="Get the information of the family member. It contains the name, job, and hate food.",
)
def api_get_family_info_by_id(id: int) -> FamilyDetail:
    return get_family_info_by_id(id)
