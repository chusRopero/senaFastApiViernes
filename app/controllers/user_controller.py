from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.user_schema import UserSchema
from app.utils.response import api_response


# ==========================================
# GET ALL USERS
# ==========================================

def get_users(db: Session):

    users = db.query(User).order_by(User.id).all()

    if not users:
        return api_response(
            success=False,
            message="No hay usuarios registrados",
            data=[]
        )

    data = [
        {
            "id": u.id,
            "nombre": u.nombre,
            "correo": u.correo
        }
        for u in users
    ]

    return api_response(
        success=True,
        message="Lista de usuarios",
        data=data
    )

# ==========================================
# GET USER BY ID
# ==========================================

def get_user(id: int, db: Session):

    user = db.query(User).filter(User.id == id).first()

    if not user:
        return api_response(
            success=False,
            message=f"Usuario con id {id} no encontrado"
        )

    return api_response(
        success=True,
        message="Usuario encontrado",
        data={
            "id": user.id,
            "nombre": user.nombre,
            "correo": user.correo
        }
    )

# ==========================================
# CREATE USER
# ==========================================

def create_user(user: UserSchema, db: Session):

    # validar correo duplicado
    exists = db.query(User).filter(User.correo == user.correo).first()

    if exists:
        return api_response(
            success=False,
            message="El correo ya está registrado"
        )

    new_user = User(
        nombre=user.nombre,
        correo=user.correo
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return api_response(
        success=True,
        message="Usuario creado correctamente",
        data={
            "id": new_user.id,
            "nombre": new_user.nombre,
            "correo": new_user.correo
        }
    )

# ==========================================
# UPDATE USER
# ==========================================

def update_user(id: int, user: UserSchema, db: Session):

    db_user = db.query(User).filter(User.id == id).first()

    if not db_user:
        return api_response(
            success=False,
            message=f"Usuario con id {id} no encontrado"
        )

    # validar correo duplicado en otro usuario
    email_exists = db.query(User).filter(
        User.correo == user.correo,
        User.id != id
    ).first()

    if email_exists:
        return api_response(
            success=False,
            message="El correo ya está en uso por otro usuario"
        )

    db_user.nombre = user.nombre
    db_user.correo = user.correo

    db.commit()
    db.refresh(db_user)

    return api_response(
        success=True,
        message="Usuario actualizado correctamente",
        data={
            "id": db_user.id,
            "nombre": db_user.nombre,
            "correo": db_user.correo
        }
    )

# ==========================================
# DELETE USER
# ==========================================
def delete_user(id: int, db: Session):

    db_user = db.query(User).filter(User.id == id).first()

    if not db_user:
        return api_response(
            success=False,
            message=f"Usuario con id {id} no encontrado"
        )

    db.delete(db_user)
    db.commit()

    return api_response(
        success=True,
        message="Usuario eliminado correctamente"
    )