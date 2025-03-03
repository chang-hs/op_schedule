from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import String, Date, Time, Integer
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

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

    def __repr__(self) -> str:
        return f"Op {self.patient_id} {self.name} {self.op_date} {self.preop_date}"
    
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name
        self.diagnosis = ''
        self.op_duration = ''
        self.urgency = 0
        self.op_date = None
        self.preop_date = None
        
        
    
if __name__ == '__main__':
    engine = create_engine("sqlite://", echo=True)
    print(engine)