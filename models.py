from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite3:///product.db")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer(), primary_key = True)
    name = Column(String())

    def __repr__(self):
        return f"Product: {self.id} Name: {self.name}"
