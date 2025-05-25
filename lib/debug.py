#!/usr/bin/env python3

from sqlalchemy import create_engine
from mydatabase import Base, engine
from models import Company, Dev

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)
    import ipdb; ipdb.set_trace()
