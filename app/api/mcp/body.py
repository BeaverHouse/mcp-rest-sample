# Custom module import
from models.body import BodyInfo
from logic.body.bmi import check_obesity

def tool_check_obesity(height: float, weight: float) -> str:
    """
    Check the obesity of the person.
    Height's unit is cm, and weight's unit is kg.
    """
    return check_obesity(BodyInfo(height=height, weight=weight))

