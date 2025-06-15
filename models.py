from typing import List
from sqlalchemy import func
from sqlalchemy import String, Date, Time, Integer, Boolean, DateTime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from db import Base
from flask_login import UserMixin


class Op(Base):
    __tablename__ = "op"
    id: Mapped[int] = mapped_column(primary_key=True)
    patient_id: Mapped[String] = mapped_column(String[8])
    name: Mapped[String] = mapped_column(String)
    age: Mapped[Integer] = mapped_column(Integer, nullable=True)
    phone: Mapped[String] = mapped_column(String, nullable=True)
    email: Mapped[String] = mapped_column(String, nullable=True)
    diagnosis: Mapped[String] = mapped_column(String)
    op_duration: Mapped[String] = mapped_column(String)
    urgency: Mapped[Integer] = mapped_column(Integer)
    memo: Mapped[String] = mapped_column(String, nullable=True)
    op_date: Mapped[Date] = mapped_column(Date, nullable=True)
    preop_date: Mapped[Date] = mapped_column(Date, nullable=True)
    date_set: Mapped[Boolean] = mapped_column(Boolean, default=False)
    patient_notified: Mapped[Boolean] = mapped_column(Boolean, default=False)
    orders_committed: Mapped[Boolean] = mapped_column(Boolean, default=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    active: Mapped[Boolean] = mapped_column(Boolean, default=True, nullable=True)

    def __repr__(self) -> str:
        return f"Op {self.patient_id} {self.name} {self.op_date} {self.preop_date}"
    
class User(Base, UserMixin):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)

    def __repr__(self) -> str:
        return f"User {self.username}"
    

        
        