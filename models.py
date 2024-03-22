from sqlalchemy import create_engine, Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

# Define the User model for user authentication
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(Date, default=datetime.now)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"

# Define the Category model for transaction categories
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"

# Define the Transaction model to store financial transactions
class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    date = Column(Date, default=datetime.now)
    description = Column(String(255), nullable=False)
    amount = Column(Integer, nullable=False)
    type = Column(Enum('income', 'expense'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    user = relationship('User', backref='transactions')
    category = relationship('Category', backref='transactions')

    def __repr__(self):
        return f"<Transaction(id={self.id}, date={self.date}, description={self.description}, amount={self.amount}, type={self.type})>"
