from sqlalchemy import Column, Integer, String, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define the Income model
class Income(Base):
    __tablename__ = 'income'

    id = Column(Integer, primary_key=True)
    amount = Column(Numeric(10, 2))
    source = Column(String(100))
    date = Column(Date)

# Define the Expense model
class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    amount = Column(Numeric(10, 2))
    category = Column(String(100))
    description = Column(String)
    date = Column(Date)

# Define the Savings model
class Savings(Base):
    __tablename__ = 'savings'

    id = Column(Integer, primary_key=True)
    amount = Column(Numeric(10, 2))
    date = Column(Date)
