from models.family import FamilyMember, FamilyDetail
from typing import List

def get_family_members() -> List[FamilyMember]:
    return [
        FamilyMember(id=1, name="Me"),
        FamilyMember(id=2, name="Mom"),
        FamilyMember(id=3, name="Dad"),
        FamilyMember(id=4, name="Sister"),
    ]

def get_family_info_by_id(id: int) -> FamilyDetail:
    if id == 1:
        return FamilyDetail(id=1, name="Me", job="Developer", hate_food="Seashell")
    elif id == 2:
        return FamilyDetail(id=2, name="Mom", job="Teacher", hate_food="Lamb meat")
    elif id == 3:
        return FamilyDetail(id=3, name="Dad", job="Doctor", hate_food="Spicy food")
    elif id == 4:
        return FamilyDetail(id=4, name="Sister", job="Student", hate_food="Raw fish")
