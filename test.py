from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Op, Base

engine = create_engine('sqlite:///op_schedule.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)