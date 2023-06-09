from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///product.db")

product_user = Table(
    "product_users",
    Base.metadata,
    Column("product_id", ForeignKey("products.id"), primary_key = True),
    Column("user_id", ForeignKey("users.id"),primary_key = True),
    extend_existing = True,
)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    price = Column(Integer())
    reviews = relationship("Review", backref= backref("product"))
    users = relationship("User", secondary = product_user, back_populates = "products")

    def __repr__(self):
        return f"Product: {self.id} Name: {self.name}"
    # return the reviews for a product
    def product_reviews(self):
        return self.reviews
    # return the user who reviewed a product
    def prod_users(self):
        return self.users
    # returns an list of all reviews about a product
    def all_review(self):
        return[review.full_review() for review in self.reviews]
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key = True)
    first_name = Column(String())
    last_name = Column(String())
    reviews = relationship("Review", backref = backref("user"))
    products = relationship("Product", secondary = product_user, back_populates = "users")

    def __repr__(self):
        return f"User: {self.id} Name: {self.first_name} {self.last_name}"
    #  return the reviews for a user
    def user_reviews(self):
        return self.reviews
    # return products reviewed by users
    def user_restaurant(self):
        return self.products
    # string format to join first name and last name
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    # return the product with highest rating
    def favorite_product(self):
        return max(self.reviews, key=lambda review: review.rating).product
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer(), primary_key = True)
    rating = Column(Integer())
    product_id = Column(Integer(), ForeignKey("products.id"))
    user_id = Column(Integer(), ForeignKey("users.id"))
    # return the first user that reviewed
    def user_review(self):
        return self.user
    # return the first product reviewed
    def product_review(self):
        return self.product
    # return full review
    def full_review(self):
        return f"Review for {self.product.name} by {self.user.full_name()}: {self.rating} stars"

    def __repr__(self):
        return f"Review: {self.id} Rate: {self.rating}"
    
