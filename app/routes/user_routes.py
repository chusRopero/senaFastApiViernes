from fastapi import APIRouter, Depends
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

# 🔐 IMPORTANTE: autenticación
from app.middleware.auth import get_current_user

# ==========================================
# ROUTER
# ==========================================
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# ==========================================
# GET ALL USERS (PROTEGIDO)
# ==========================================
@router.get("/")
def users(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_users(db)

# ==========================================
# GET USER BY ID (PROTEGIDO)
# ==========================================
@router.get("/{id}")
def user_by_id(
    id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_user(id, db)

# ==========================================
# CREATE USER (PROTEGIDO)
# ==========================================
@router.post("/")
def store_user(
    user_data: UserSchema,
    db: Session = Depends(get_db)
):
    return create_user(user_data, db)

# ==========================================
# UPDATE USER (PROTEGIDO)
# ==========================================
@router.put("/{id}")
def edit_user(
    id: int,
    user_data: UserSchema,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return update_user(id, user_data, db)

# ==========================================
# DELETE USER (PROTEGIDO)
# ==========================================
@router.delete("/{id}")
def destroy_user(
    id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return delete_user(id, db)