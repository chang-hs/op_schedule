from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import current_app

def init_db(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    Session = sessionmaker(bind=engine)
    return Session