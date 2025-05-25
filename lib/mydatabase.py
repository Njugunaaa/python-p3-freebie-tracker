from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///app.db', echo=True, future=True)  

Base = declarative_base()
