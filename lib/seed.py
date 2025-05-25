#!/usr/bin/env python3

# Script goes here!
# seed.py
from mydatabase import session, Base, engine
from models import Company, Dev, Freebie

# Drop and recreate tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create companies
google = Company(name="Google", founding_year=1998)
apple = Company(name="Apple", founding_year=1976)

# Create devs
alice = Dev(name="Alice")
bob = Dev(name="Bob")

# Add to session and commit
session.add_all([google, apple, alice, bob])
session.commit()

# Create freebies
freebie1 = google.give_freebie(alice, "Tote Bag", 10)
freebie2 = apple.give_freebie(bob, "Sticker", 2)
freebie3 = google.give_freebie(bob, "Water Bottle", 5)

session.add_all([freebie1, freebie2, freebie3])
session.commit()
