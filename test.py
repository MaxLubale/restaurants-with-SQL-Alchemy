# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session
# from sqlalchemy.ext.declarative import declarative_base
# from restaurant import Restaurant
# from customer import Customer
# from review import Review

# Base = declarative_base()


# # Create an SQLite database in memory for testing
# engine = create_engine('sqlite:///:memory:')
# Base.metadata.create_all(engine)

# # Create a session
# session = Session(engine)

# # Sample data
# restaurant1 = Restaurant(name='Best Food Place', price=3)
# restaurant2 = Restaurant(name='Sarova Skies', price=4)

# customer1 = Customer(first_name='John', last_name='Doe')
# customer2 = Customer(first_name='Jane', last_name='Smith')

# review1 = Review(restaurant=restaurant1, customer=customer1, star_rating=5)
# review2 = Review(restaurant=restaurant2, customer=customer2, star_rating=4)
# review3 = Review(restaurant=restaurant2, customer=customer1, star_rating=3)

# # Add objects to the session
# session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2, review3])

# # Commit the session to the database
# session.commit()

# # Print all customers
# all_customers = session.query(Customer).all()
# print("\nAll Customers:")
# for customer in all_customers:
#     print(f"{customer.full_name()}")

# print("\n" + "="*50 + "\n")

# # Print all reviews
# all_reviews = session.query(Review).all()
# print("\nAll Reviews:")
# for review in all_reviews:
#     print(f"{review.full_review()}")

# print("\n" + "="*50 + "\n")

# # Print all restaurants
# all_restaurants = session.query(Restaurant).all()
# print("\nAll Restaurants:")
# for restaurant in all_restaurants:
#     print(f"{restaurant.name}, Price: {restaurant.price}")

# print("\n" + "="*50 + "\n")

# # Display restaurant information
# print("\nDisplay restaurant information:")
# print(f"\nRestaurant: {restaurant1.name}, Price: {restaurant1.price}")
# print("Reviews for the restaurant:")
# for review in restaurant1.reviews:
#     print(f"- {review.full_review()}\n")


# print(f"\nRestaurant: {restaurant2.name}, Price: {restaurant2.price}")
# print("Reviews for the restaurant:")
# for review in restaurant2.reviews:
#     print(f"- {review.full_review()}")

# print("\n" + "="*50 + "\n")

# # Display customer information
# print("Display customer information:")
# print(f"\nCustomer: {customer1.full_name()}")
# print(customer1.favorite_restaurant())
# print("Reviews by the customer:")
# for review in customer1.reviews:
#     print(f"- {review.full_review()}\n")


# print(f"\nCustomer: {customer2.full_name()}")
# print(customer2.favorite_restaurant())
# print("Reviews by the customer:")
# for review in customer2.reviews:
#     print(f"- {review.full_review()}")

# print("\n" + "="*50 + "\n")

# # Display information about the first review
# print("Display information about the first review:")
# first_review = session.query(Review).first()
# print(f"\nReview: {first_review.full_review()}")
# print(f"Restaurant: {first_review.restaurant.name}")
# print(f"Customer: {first_review.customer.full_name()}\n")

# print("\n" + "="*50 + "\n")

# # fanciest restaurant
# print(restaurant1.fanciest(session))

# print("\n" + "="*50 + "\n")
# # adding and deleting a review
# print("Adding a Review:")
# customer2.add_review(restaurant1, 3)
# print(customer2.reviews[1].full_review())

# print("\n" + "="*50 + "\n")

# print("\nBefore Deleting Review:")
# print(restaurant1.all_reviews())

# print("\nAfter Deleting Review:")
# customer2.delete_reviews(restaurant1)
# print(restaurant1.all_reviews())

# print("\n" + "="*50 + "\n")