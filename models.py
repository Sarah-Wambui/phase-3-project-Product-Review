from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///product.db")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer(), primary_key = True)
    name = Column(String())

    def __repr__(self):
        return f"Product: {self.id} Name: {self.name}"
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key = True)
    first_name = Column(String())
    last_name = Column(String())

    def __repr__(self):
        return f"User: {self.id} Name: {self.first_name} {self.last_name}"
