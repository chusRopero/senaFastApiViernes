from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.schemas.login_schema import LoginSchema

from app.controllers.auth_controller import login

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/login")
def login_user(
    user: LoginSchema,
    db: Session = Depends(get_db)
):
    return login(user, db)