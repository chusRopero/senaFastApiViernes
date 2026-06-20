from fastapi import FastAPI


from app.routes.user_routes import router as user_routers
from app.routes.auth_route import router as auth_router

from app.config.database import Base
from app.config.database import engine

# ==========================================
# CREATE TABLES
# ==========================================
Base.metadata.create_all(bind=engine)

# ==========================================
# FASTAPI
# ==========================================
app = FastAPI(
    title="API ADSO SENA",
    version="1.0.0"
)

# ==========================================
# ROUTES
# ==========================================
app.include_router(auth_router)
app.include_router(user_routers)

# ==========================================
# HOME
# ==========================================
@app.get("/")
def home():
    return {
        "success": True,
        "message": "API funcionando correctamente"
    }