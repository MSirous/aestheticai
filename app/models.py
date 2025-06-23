from sqlalchemy import Column, String, TIMESTAMP, Boolean, String, Column
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from .database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, index=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)
    is_verified = Column(Boolean, default=False)
    verification_code = Column(String, default=lambda: str(uuid4()))
    created_at = Column(TIMESTAMP)
    last_login = Column(TIMESTAMP, nullable=True)
