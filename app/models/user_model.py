from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

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
        unique=True
    )