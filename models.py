from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///product.db")

product_user = Table(
    "product_users",
    Base.metadata,
    Column("product_id", ForeignKey("products.id", primary_key= True)),
    Column("user_id", ForeignKey("users.id", primary_key = True)),
    extend_existing = True,
)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    reviews = relationship("Review", backref= backref("product"))
    users = relationship("User", secondary = product_user, back_populates = "products")

    def __repr__(self):
        return f"Product: {self.id} Name: {self.name}"
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key = True)
    first_name = Column(String())
    last_name = Column(String())
    reviews = relationship("Review", backref = backref("user"))
    products = relationship("Product", secondary = product_user, back_populates = "users")

    def __repr__(self):
        return f"User: {self.id} Name: {self.first_name} {self.last_name}"
    
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer(), primary_key = True)
    rating = Column(Integer())

    product_id = Column(Integer(), ForeignKey("products.id"))
    user_id = Column(Integer(), ForeignKey("users.id"))

    def __repr__(self):
        return f"Review: {self.id} Rate: {self.rating}"
