# # restaurant.py
# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class Restaurant(Base):
#     __tablename__ = 'restaurants'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     price = Column(Integer)
#     reviews = relationship('Review', back_populates='restaurant', cascade='all, delete-orphan')

#     @classmethod
#     def fanciest(cls, session):
#         fanciest_restaurant = session.query(cls).order_by(cls.price.desc()).first()
#         return f"The fanciest restaurant is {fanciest_restaurant.name} with a price of {fanciest_restaurant.price}."

#     def all_reviews(self):
#         return [review.full_review() for review in self.reviews if review.customer is not None]

#     def customers(self):
#         return [review.customer for review in self.reviews]

#     def restaurant_reviews(self):
#         return self.reviews
    
#     def __repr__(self):
#         return f"Customer's favourite restaurant is {self.name} with a price of {self.price}"
