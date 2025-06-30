from pydantic import BaseModel, Field
from typing import Annotated

class BodyInfo(BaseModel):
    height: Annotated[float, "Height in cm", Field(ge=1, le=300)]
    weight: Annotated[float, "Weight in kg", Field(ge=0, le=200)]