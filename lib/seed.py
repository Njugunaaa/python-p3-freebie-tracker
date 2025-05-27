from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie
from sqlalchemy import create_engine

engine = create_engine("sqlite:///freebies.db")
Session = sessionmaker(bind=engine)
session = Session()

company1 = Company(name="Google", founding_year=1998)
company2 = Company(name="Apple", founding_year=1976)

dev1 = Dev(name="Njuguna")
dev2 = Dev(name="Kimani")

freebie1 = Freebie(item_name="Sticker", value=1, company=c1, dev=d1)
freebie2 = Freebie(item_name="T-Shirt", value=10, company=c2, dev=d1)
freebie3 = Freebie(item_name="Mug", value=5, company=c1, dev=d2)

session.add_all([company1, company2, dev1, dev2, freebie1 , freebie2, freebie3])
session.commit()
