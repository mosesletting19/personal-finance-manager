from datetime import datetime
from sqlalchemy.orm import sessionmaker
from models import Category, User, Transaction


Session = sessionmaker()

# Initialize the session
def init_session(engine):
    Session.configure(bind=engine)

# ORM methods for User model
def create_user(username, password, email):
    session = Session()
    user = User(username=username, password=password, email=email, created_at=datetime.now())
    session.add(user)
    session.commit()
    return user

def authenticate_user(username, password):
    session = Session()
    user = session.query(User).filter_by(username=username, password=password).first()
    return user

# ORM methods for Category model
def add_category(name):
    session = Session()
    category = Category(name=name)
    session.add(category)
    session.commit()
    return category

def update_category(category_id, new_name):
    session = Session()
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        category.name = new_name
        session.commit()
        return category
    return None

def delete_category(category_id):
    session = Session()
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        session.delete(category)
        session.commit()
        return True
    return False

# ORM methods for Transaction model
def add_transaction(user_id, category_id, date, description, amount, type):
    session = Session()
    transaction = Transaction(user_id=user_id, category_id=category_id, date=date,
                              description=description, amount=amount, type=type)
    session.add(transaction)
    session.commit()
    return transaction

def update_transaction(transaction_id, new_data):
    session = Session()
    transaction = session.query(Transaction).filter_by(id=transaction_id).first()
    if transaction:
        for key, value in new_data.items():
            setattr(transaction, key, value)
        session.commit()
        return transaction
    return None

def delete_transaction(transaction_id):
    session = Session()
    transaction = session.query(Transaction).filter_by(id=transaction_id).first()
    if transaction:
        session.delete(transaction)
        session.commit()
        return True
    return False

def get_transactions_by_user(user_id):
    session = Session()
    transactions = session.query(Transaction).filter_by(user_id=user_id).all()
    return transactions
