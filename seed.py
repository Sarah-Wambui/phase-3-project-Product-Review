#!usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Product, User, Review, product_user

if __name__ == "__main__":
    engine = create_engine("sqlite:///product.db")
    Session = sessionmaker(bind = engine)
    session = Session()

    fake = Faker()

    products = []
    


