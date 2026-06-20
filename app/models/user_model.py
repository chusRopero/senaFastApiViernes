from sqlalchemy import Column, Integer, String
from app.config.database import Base

# ==========================================
# USER MODEL
# ==========================================
class User(Base):

    __tablename__ = "usuarios"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    nombre = Column(
        String(100),
        nullable=False
    )

    correo = Column(
        String(100),
        nullable=False,
        unique=True,
        index=True
    )

    password = Column(
        String(255),
        nullable=False
    )