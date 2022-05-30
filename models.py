# -------------------------------------------------------------------
# Class: Models.py
# Purpose: Represents our base class SQLAlchemy Model All of our 
# models have to inherit from this class. Alembic maps them to specific
# table columns in our database
# -------------------------------------------------------------------

from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base() 

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)

# Inserting some records into the database
# user = [
#     User(first_name='John', last_name='Smith'),
#     User(first_name='Richard', last_name='Hamilton'),
# ]