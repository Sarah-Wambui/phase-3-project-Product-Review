#!usr/bin/env python3

import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Product, User, Review, product_user

engine = create_engine("sqlite:///product.db")
Session = sessionmaker(bind=engine)
session = Session()

# the @click.group decorator defines a group of commands.
# the cli() function creates a Click command group 
@click.group()
def cli():
    """ CLI for interacting with the database. The CLI is written within the following commands"""
    pass

# the @click.command decorator defines a function as a command to be run.
# this DSA algorithm outputs all the products that match the given name. 
# Run this algorithm as a command to see output like this:
#      python3 cli.py search-product "Reed LLC" 
# this command return the product if found and prints "No product found matching the name you have provided" if there is no such product in the database
@click.command()
@click.option("--name", prompt="Enter a product name", help="Name of the product")
def search_product(name):
    """Search for a product by name"""
    products = session.query(Product).filter(Product.name.ilike(f"%{name}%")).all()

    if products:
        click.echo(f"Found {len(products)} product(s) matching the name '{name}':")
        for product in products:
            click.echo(f"Product: {product.name}, Price: {product.price}")
    else:
        click.echo(f"No products found matching the name '{name}'.")


# this algorithm helps a user to add a User into the database. 
# Run this algorithm as a command to see output like this:
#   python3 cli.py add-user
# this will give two prompts one asking for first_name and one for last_name
# when a user is added the program prints user added successfully
@click.command()
@click.option("--first-name", prompt="Enter the user's first name", help="First name of the user")
@click.option("--last-name", prompt="Enter the user's last name", help="Last name of the user")
def add_user(first_name, last_name):
    """Add a new user to the database"""
    if not first_name or not last_name:
        click.echo("First name and last name are required.")
        return

    user = User(first_name=first_name, last_name=last_name)
    session.add(user)
    session.commit()
    click.echo("User added successfully!")

# this algorith prints all the products in the database each as as a python list. 
# Run this algorithm as a command to see output like this:
#     python3 cli.py list-products
@click.command()
def list_products():
    """List all products"""
    products = session.query(Product).all()

    click.echo("Products:")
    for product in products:
        product_list = [f"ID: {product.id}", f"Name: {product.name}", f"Price: {product.price}"]
        product_str = ', '.join(product_list)
        click.echo(f"[{product_str}]")

    # Display the prompt
    input("Press Enter to continue...")


# this DSA algorithm lists all the users in python dictionaries. 
# Run this algorithm as a command to see the output like this:
#    python3 cli.py list-users
@click.command()
def list_users():
    """List all users"""
    users = session.query(User).all()

    if users:
        click.echo("Users:")
        for user in users:
            user_dict = {
                "ID": user.id,
                "First Name": user.first_name,
                "Last Name": user.last_name
            }
            click.echo(user_dict)
    else:
        click.echo("No users found.")

 

# This DSA algorithm gives all the reviews and each review is a tuple. To run this algorithm as a command run this:
#       python3 cli.py list-reviews
@click.command()
def list_reviews():
    """List all reviews"""
    reviews = session.query(Review).all()

    if reviews:
        click.echo("Reviews:")
        for review in reviews:
            review_tuple = (review.id, review.product_id, review.user_id, review.rating)
            click.echo(f"Review: {review_tuple}")
    else:
        click.echo("No reviews found.")




# this DSA algorithm deletes a user from the database. Run this command
#     python cli.py delete-user
#  this will prompt the user to enter the first name and last name of the user and when the user has been deleted it prints the user deleted successfully
@click.command()
@click.option("--first-name", prompt="Enter the user's first name", help="First name of the user")
@click.option("--last-name", prompt="Enter the user's last name", help="Last name of the user")
def delete_user(first_name, last_name):
    """Delete a user from the database"""
    user = session.query(User).filter_by(first_name=first_name, last_name=last_name).first()

    if user:
        session.delete(user)
        session.commit()
        click.echo("User deleted successfully!")
    else:
        click.echo("User not found.")

# add each command into the command group
cli.add_command(search_product)
cli.add_command(add_user)
cli.add_command(list_users)
cli.add_command(delete_user)
cli.add_command(list_products)
cli.add_command(list_reviews)

# executing this file will print all the commands one should run to see the different outputs
if __name__ == "__main__":
    cli()
    