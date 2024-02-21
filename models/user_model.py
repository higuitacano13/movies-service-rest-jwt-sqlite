from config.database import Base
from sqlalchemy import Column, String, Integer

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)