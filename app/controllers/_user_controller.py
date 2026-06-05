from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.user_schema import UserSchema

# ==========================================
# GET ALL USERS
# ==========================================
def get_users(
    db: Session
):
    users = db.query(User).all()

    return {
        "success": True,
        "message": "Lista usuarios",
        "data": users
    }

# ==========================================
# GET USER
# ==========================================
def get_user(
    id: int,
    db: Session
):
    user = db.query(User).filter(
        User.id == id
    ).first()

    if not user:
        return {
            "success": False,
            "message": "Usuario no encontrado"
        }

    return {
        "success": True,
        "data": user
    }

# ==========================================
# CREATE USER
# ==========================================
def create_user(
    user: UserSchema,
    db: Session
):
    new_user = User(
        nombre=user.nombre,
        correo=user.correo
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "success": True,
        "message": "Usuario creado",
        "data": new_user
    }

# ==========================================
# UPDATE USER
# ==========================================
def update_user(
    id: int,
    user: UserSchema,
    db: Session
):
    user_db = db.query(User).filter(
        User.id == id
    ).first()

    if not user_db:
        return {
            "success": False,
            "message": "Usuario no encontrado"
        }

    user_db.nombre = user.nombre
    user_db.correo = user.correo

    db.commit()
    db.refresh(user_db)

    return {
        "success": True,
        "message": "Usuario actualizado",
        "data": user_db
    }

# ==========================================
# DELETE USER
# ==========================================
def delete_user(
    id: int,
    db: Session
):
    user = db.query(User).filter(
        User.id == id
    ).first()

    if not user:
        return {
            "success": False,
            "message": "Usuario no encontrado"
        }

    db.delete(user)
    db.commit()

    return {
        "success": True,
        "message": "Usuario eliminado"
    }