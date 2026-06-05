from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.controllers.user_controller import (
    get_users,
    get_user,
    create_user,
    update_user,
    delete_user
)

from app.schemas.user_schema import UserSchema

# ==========================================
# ROUTER
# ==========================================
router = APIRouter()

# ==========================================
# GET ALL USERS
# ==========================================
@router.get("/users")
def users(
    db: Session = Depends(get_db)
):
    return get_users(db)

# ==========================================
# GET USER BY ID
# ==========================================
@router.get("/users/{id}")
def user(
    id: int,
    db: Session = Depends(get_db)
):
    return get_user(id, db)

# ==========================================
# CREATE USER
# ==========================================
@router.post("/users")
def store_user(
    user: UserSchema,
    db: Session = Depends(get_db)
):
    return create_user(user, db)

# ==========================================
# UPDATE USER
# ==========================================
@router.put("/users/{id}")
def edit_user(
    id: int,
    user: UserSchema,
    db: Session = Depends(get_db)
):
    return update_user(
        id,
        user,
        db
    )

# ==========================================
# DELETE USER
# ==========================================
@router.delete("/users/{id}")
def destroy_user(
    id: int,
    db: Session = Depends(get_db)
):
    return delete_user(id, db)