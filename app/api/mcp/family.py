from typing import List

# Custom module import
from models.family import FamilyMember, FamilyDetail
from logic.family import get_family_members, get_family_info_by_id

def tool_get_family_members() -> List[FamilyMember]:
    """
    Get the all family members and their IDs.
    Use this tool "FIRST" to get the ID of the family member.
    """
    return get_family_members()

def tool_get_family_info_by_id(id: int) -> FamilyDetail:
    """
    Get the information of the family member. It contains the name, job, and hate food.
    Use this tool after getting the ID of the family member.
    """
    return get_family_info_by_id(id)
