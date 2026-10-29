from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, session

engine = create_engine('sqlite:///biblioteca.db')

class Base(DeclarativeBase):
    pass

def criar_banco():
    Base.metadata.create_all(engine)

session = session(bind=engine)