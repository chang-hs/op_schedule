from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import String, Date, Time, Integer, Boolean
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from db import Base

# db = SQLAlchemy(model_class=Base)

class Op(Base):
    __tablename__ = "op"
    id: Mapped[int] = mapped_column(primary_key=True)
    patient_id: Mapped[String] = mapped_column(String[8])
    name: Mapped[String] = mapped_column(String)
    diagnosis: Mapped[String] = mapped_column(String)
    op_duration: Mapped[String] = mapped_column(String)
    urgency: Mapped[Integer] = mapped_column(Integer)
    op_date: Mapped[Date] = mapped_column(Date, nullable=True)
    preop_date: Mapped[Date] = mapped_column(Date, nullable=True)
    date_set: Mapped[Boolean] = mapped_column(Boolean, default=False)
    patient_notified: Mapped[Boolean] = mapped_column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"Op {self.patient_id} {self.name} {self.op_date} {self.preop_date}"
    

        
        