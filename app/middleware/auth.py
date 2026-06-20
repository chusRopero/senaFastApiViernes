from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from jose import jwt, JWTError

from app.utils.security import SECRET_KEY, ALGORITHM

# ==========================================
# ESQUEMA DE AUTENTICACIÓN (Bearer Token)
# ==========================================
security = HTTPBearer()


# ==========================================
# OBTENER USUARIO DESDE TOKEN
# ==========================================
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials  # <-- solo el token sin "Bearer"

    try:
        # Decodificar token
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload  # devuelve datos del token (user, id, etc.)

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"}
        )