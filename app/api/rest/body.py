from fastapi import APIRouter

# Custom module import
from models.body import BodyInfo
from logic.body.bmi import check_obesity

body_router = APIRouter(prefix="/body", tags=["Body"])

@body_router.post(
    "/check_obesity",
    response_model=str,
    description="Check the obesity of the person.",
)
def api_check_obesity(info: BodyInfo):
    return check_obesity(info)
