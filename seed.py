#!usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker
from models import Product, User, Review, product_user

if __name__ == "__main__":
    engine = create_engine("sqlite:///product.db")
    Session = sessionmaker(bind = engine)
    session = Session()\
    
    session.query(Product).delete()
    session.query(User).delete()
    session.query(Review).delete()

    fake = Faker()

    products = []
    for i in range(30):
        product = Product(
            name = fake.company(),
            price = random.randint(10, 100)
        )
        session.add(product)
        products.append(product)

    for i in range(30):
        user = User(
            first_name = fake.first_name(),
            last_name = fake.last_name()
        )
        session.add(user)

    for i in range(30):
        review = Review(
            rating = random.randint(1, 10),
            product_id = random.randint(1, 30),
            user_id = random.randint(1,30)
        )
        session.add(review)

    combination = set()
    for _ in range(30):
        product_id = random.randint(1, 30)
        user_id = random.randint(1,30)
        if (product_id, user_id) in combination:
            continue 
        combination.add((product_id, user_id))
        product_user_data = {"product_id": product_id, "user_id": user_id}
        statement = insert(product_user).values(product_user_data)
        session.execute(statement)
        session.commit()

    session.commit()
    session.close()     



