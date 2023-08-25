from sqlalchemy import create_engine, Column, String, REAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select, MetaData, Table, and_

Base = declarative_base()


class Table(Base):
    __tablename__ = 'service'

    name = Column('name', String, primary_key=True)
    amount = Column('amount', REAL)

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __repr__(self):
        return f'[{self.name}] [{self.amount}]'


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(bind=engine)
