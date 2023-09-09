# user_mapper.py

from sqlalchemy import Column, Integer, String, create_engine, declarative_base
from user import User

Base = declarative_base()

class UserMapper(User, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String, index=True)
