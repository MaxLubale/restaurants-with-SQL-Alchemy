from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Session
import sqlalchemy.orm  # Import the declarative_base function
from sqlalchemy.ext.declarative import declarative_base

Base = sqlalchemy.orm.declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship('Review', back_populates='restaurant', cascade='all, delete-orphan')

    @classmethod
    def fanciest(cls, session):
        fanciest_restaurant = session.query(cls).order_by(cls.price.desc()).first()
        return f"The fanciest restaurant is {fanciest_restaurant.name} with a price of {fanciest_restaurant.price}."

    def all_reviews(self):
        return [review.full_review() for review in self.reviews if review.customer is not None]

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews = relationship('Review', back_populates='customer', cascade='all, delete-orphan')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        if not self.reviews:
            return None
        return max(self.reviews, key=lambda review: review.star_rating).restaurant

    def add_review(self, restaurant, rating):
        review = Review(restaurant=restaurant, customer=self, star_rating=rating)
        self.reviews.append(review)

    def delete_reviews(self, restaurant):
        self.reviews = [review for review in self.reviews if review.restaurant != restaurant]

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."

# Create an SQLite database in memory for testing
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Create a session
session = Session(engine)

# Sample data
restaurant1 = Restaurant(name='Best Food Place', price=3)
restaurant2 = Restaurant(name='Sarova Skies', price=4)
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')
review1 = Review(restaurant=restaurant1, customer=customer1, star_rating=5)
review2 = Review(restaurant=restaurant2, customer=customer2, star_rating=4)

# Add objects to the session
session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])

# Commit the session to the database
session.commit()

# Test the implemented methods
print(restaurant1.fanciest(session))
print(restaurant1.all_reviews())
print(customer1.full_name())
favorite_restaurant = customer1.favorite_restaurant()
if favorite_restaurant:
    print(f"{customer1.full_name()}'s favorite restaurant is {favorite_restaurant.name}.")
else:
    print(f"{customer1.full_name()} has no favorite restaurant.")
customer1.add_review(restaurant2, 3)
print(customer1.reviews[1].full_review())
customer1.delete_reviews(restaurant1)
print(restaurant1.all_reviews())
