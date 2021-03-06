from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(16), unique=True, index=True)
    hashed_password = Column(String(16))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(16), index=True)
    description = Column(String(16), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")


class dataMqtt(Base):
    __tablename__ = "dataMqtt"

    Id = Column(Integer, primary_key=True, index=True)
    RunTime = Column(Integer, index=True)
    HeldTime = Column(Integer, index=True)
    MCStatus = Column(Integer, index=True)   
    Avaibility = Column(Integer, index=True)  
    Amp = Column(Integer, index=True)
    Vol = Column(Integer, index=True)
    Pow = Column(Integer, index=True)

