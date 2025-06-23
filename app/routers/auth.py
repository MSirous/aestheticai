from fastapi import APIRouter, Depends, HTTPException, Response, Query
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ..database import SessionLocal, get_db
from ..models import User
from ..schemas import UserCreate, UserLogin
from ..core.security import hash_password, verify_password, create_access_token, get_current_user


router = APIRouter(prefix="/auth", tags=["auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed = hash_password(user.password)
    new_user = User(
        email=user.email,
        password_hash=hashed,
        role="artist"  # نقش ثابت برای همه
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
    "msg": "User registered. Please verify your code.",
    "user_id": str(new_user.user_id),
    "verification_code": new_user.verification_code  # فقط برای تست، در آینده باید ایمیل بشه
}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not db_user.is_verified:
        raise HTTPException(status_code=403, detail="Account not verified. Please verify your account first.")

    token = create_access_token(data={
        "user_id": str(db_user.user_id), 
        "role": db_user.role,
        "email": db_user.email
    })
    return {"access_token": token, "token_type": "bearer"}


@router.post("/verify")
def verify_user(email: str = Query(...), code: str = Query(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.verification_code != code:
        raise HTTPException(status_code=400, detail="Invalid verification code")
    
    user.is_verified = True
    user.verification_code = None  # کد رو پاک کن برای امنیت
    db.commit()
    return {"msg": "Account verified successfully. You can now log in."}


class MeResponse(BaseModel):
    msg: str
    user_id: str
    role: str

@router.get("/me", response_model=MeResponse)
def get_profile(current_user: dict = Depends(get_current_user)):
    return MeResponse(
        msg=f"Welcome {current_user['email']}",
        user_id=current_user["user_id"],
        role=current_user["role"]
    )

