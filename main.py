from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship

# Use sqlalchemy.orm.declarative_base() instead of deprecated declarative_base()
Base = declarative_base()

class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship("Review", back_populates="restaurant")
    customers = relationship("Customer", secondary="reviews", back_populates="restaurants")

    def __repr__(self):
        return f"<Restaurant(name='{self.name}', price={self.price})>"

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews = relationship("Review", back_populates="customer")
    restaurants = relationship("Restaurant", secondary="reviews", back_populates="customers")

    def __repr__(self):
        return f"<Customer(name='{self.first_name} {self.last_name}')>"

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

    def __repr__(self):
        return f"<Review for {self.restaurant.name} by {self.customer.first_name} {self.customer.last_name}: {self.star_rating} stars.>"

def print_data(session):
    # Print customer's information
    customers = session.query(Customer).all()
    print("\nCustomers:")
    for customer in customers:
        print(customer)

    # Print restaurants and associated reviews
    print("\nCustomers' Restaurants:")
    for customer in customers:
        print(f"{customer}'s Restaurants:", customer.restaurants)

    # Print reviews and associated customer
    print("\nReviews:")
    reviews = session.query(Review).all()
    for review in reviews:
        print(review)

    # Print the fanciest restaurant
    fanciest_restaurant = session.query(Restaurant).order_by(Restaurant.price.desc()).first()
    print("\nFanciest Restaurant:", fanciest_restaurant)

    # Print customer's favorite restaurant
    for customer in customers:
        favorite_restaurant = (
            session.query(Restaurant)
            .join(Review)
            .filter(Review.customer_id == customer.id)
            .order_by(Review.star_rating.desc())
            .first()
        )
        print(f"\n{customer}'s Favorite Restaurant:", favorite_restaurant)

    # Print customer's reviews
    print("\nCustomers' Reviews:")
    for customer in customers:
        customer_reviews = (
            session.query(Review)
            .filter(Review.customer_id == customer.id)
            .all()
        )
        for review in customer_reviews:
            print(review)

    # Print restaurant's reviews
    print("\nRestaurant's All Reviews:")
    for restaurant in session.query(Restaurant).all():
        restaurant_reviews = (
            session.query(Review)
            .filter(Review.restaurant_id == restaurant.id)
            .all()
        )
        for review in restaurant_reviews:
            print(review)

if __name__ == "__main__":
    # Use an SQLite :memory: database for this example
    engine = create_engine("sqlite:///:memory:", echo=True)

    # Create the tables
    Base.metadata.create_all(bind=engine)

    # Create a session
    session = Session(engine)

    # Add data to the database
    customer1 = Customer(first_name="John", last_name="Doe")
    customer2 = Customer(first_name="Jane", last_name="Smith")
    restaurant1 = Restaurant(name="Restaurant A", price=3)
    restaurant2 = Restaurant(name="Restaurant B", price=4)
    review1 = Review(star_rating=5, restaurant=restaurant1, customer=customer1)
    review2 = Review(star_rating=4, restaurant=restaurant2, customer=customer1)
    review3 = Review(star_rating=3, restaurant=restaurant1, customer=customer2)

    session.add_all([customer1, customer2, restaurant1, restaurant2, review1, review2, review3])
    session.commit()

    # Print concise data
    print_data(session)

