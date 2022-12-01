# -------------------------------------------------------------------
# Class: Models.py
# Purpose: Represents our base class SQLAlchemy Model All of our 
# models have to inherit from this class. Alembic maps them to specific
# table columns in our database
# -------------------------------------------------------------------

from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import config as vconfig

Base = declarative_base() 

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # representing data when querying
    def __repr__(self):
        return (
            f'User(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, created={self.created}'
        )

class Forecast(Base):
    __tablename__ = 'forecast'

    id = Column(Integer, primary_key=True)
    

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
#   INSERTING RECORDS INTO DATABASE (run code using python3 models.py)
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------

# (1) Create test users
# users = [
#     User(first_name='John', last_name='Smith'),
#     User(first_name='Richard', last_name='Hamilton'),
# ]

# (2) Create session to connect to database (so thread safe, one at a time)
# session_maker = sessionmaker(bind=create_engine(f'sqlite:///.{vconfig.DATA_FOLDER}/sqlite.db'))

# (3) Function to create these users
# def create_users():
#     with session_maker() as session:
#         for user in users:
#             session.add(user)
#         session.commit()

# (4) Call the above function
# create_users()