from fastapi import APIRouter, HTTPException
from app.models.user import UserModel

router = APIRouter()

# Dummy admin credentials (FYP safe)
ADMIN_EMAIL = "admin@fyp.com"
ADMIN_PASSWORD = "admin123"

@router.post("/login")
def login(user: UserModel):
    if user.email == ADMIN_EMAIL and user.password == ADMIN_PASSWORD:
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
