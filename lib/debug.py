#!/usr/bin/env python3

from sqlalchemy.orm import sessionmaker
from mydatabase import Base, engine
from models import Company, Dev, Freebie

Session = sessionmaker(bind=engine)
session = Session()

def create_data():
    # Create Companies
    google = Company(name="Google", founding_year=1998)
    apple = Company(name="Apple", founding_year=1976)

    # Create Devs
    alice = Dev(name="Alice")
    bob = Dev(name="Bob")

    # Add to session
    session.add_all([google, apple, alice, bob])
    session.commit()

    # Create Freebies
    freebie1 = Freebie(item_name="Sticker", value=5, dev=alice, company=google)
    freebie2 = Freebie(item_name="T-Shirt", value=20, dev=bob, company=apple)

    session.add_all([freebie1, freebie2])
    session.commit()

def read_data():
    companies = session.query(Company).all()
    print("\nCompanies:")
    for c in companies:
        print(f" - {c.name} (Founded {c.founding_year})")

    devs = session.query(Dev).all()
    print("\nDevs:")
    for d in devs:
        print(f" - {d.name}")

    freebies = session.query(Freebie).all()
    print("\nFreebies:")
    for f in freebies:
        print(f" - {f.print_details()}")

def update_data():
    alice = session.query(Dev).filter_by(name="Alice").first()
    if alice:
        alice.name = "Alice Cooper"
        session.commit()
        print(f"\nUpdated Dev name to {alice.name}")

def delete_data():
    freebie = session.query(Freebie).filter_by(item_name="Sticker").first()
    if freebie:
        session.delete(freebie)
        session.commit()
        print(f"\nDeleted Freebie: {freebie.item_name}")

if __name__ == '__main__':
    # Create tables (if they don't exist)
    Base.metadata.create_all(engine)

    # Clear existing data (optional - to keep script idempotent)
    session.query(Freebie).delete()
    session.query(Dev).delete()
    session.query(Company).delete()
    session.commit()

    # Run CRUD operations
    create_data()
    read_data()
    update_data()
    read_data()
    delete_data()
    read_data()
