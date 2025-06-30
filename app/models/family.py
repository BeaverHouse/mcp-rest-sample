from pydantic import BaseModel
from typing import Annotated

class FamilyMember(BaseModel):
    id: Annotated[int, "Family member id"]
    name: Annotated[str, "Family member name"]

class FamilyDetail(BaseModel):
    id: Annotated[int, "Family member id"]
    name: Annotated[str, "Family member name"]
    job: Annotated[str, "Family member job"]
    hate_food: Annotated[str, "Family member hate food"]
