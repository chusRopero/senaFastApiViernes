from sqlalchemy.orm import Session

from app.models.user_model import User

from app.schemas.login_schema import LoginSchema

from app.utils.hash import verify_password

from app.utils.security import create_access_token

from app.utils.response import api_response

def login(
    credentials: LoginSchema,
    db: Session
):

    user = db.query(User).filter(
        User.correo == credentials.correo
    ).first()

    if not user:
        return api_response(
            success=False,
            message="Correo o contraseña incorrectos"
        )

    if not verify_password(
        credentials.password,
        user.password
    ):
        return api_response(
            success=False,
            message="Correo o contraseña incorrectos"
        )

    token = create_access_token(
        {
            "id": user.id,
            "correo": user.correo
        }
    )

    return api_response(
        success=True,
        message="Login exitoso",
        data={
            "access_token": token,
            "token_type": "Bearer",
            "usuario": {
                "id": user.id,
                "nombre": user.nombre,
                "correo": user.correo
            }
        }
    )