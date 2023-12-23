# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class Customer(Base):
#     __tablename__ = 'customers'
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     reviews = relationship('Review', back_populates='customer', cascade='all, delete-orphan')

#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     def favorite_restaurant(self):
#         if not self.reviews:
#             return None
#         return max(self.reviews, key=lambda review: review.star_rating).restaurant

#     def add_review(self, restaurant, rating):
#         review = Review(restaurant=restaurant, customer=self, star_rating=rating)
#         self.reviews.append(review)

#     def delete_reviews(self, restaurant):
#         self.reviews = [review for review in self.reviews if review.restaurant != restaurant]

#     def customer_reviews(self):
#         return self.reviews

#     def reviewed_restaurants(self):
#         return [review.restaurant for review in self.reviews]
