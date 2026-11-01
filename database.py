from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine('sqlite:///biblioteca.db')

session = Session(bind=engine)

class Base(DeclarativeBase):
    pass

def banco_de_dados():
    Base.metadata.create_all(bind=engine)
