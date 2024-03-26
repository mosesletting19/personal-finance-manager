from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Income, Expense, Savings

# Create an SQLite database (you can change this to another database type)
engine = create_engine('sqlite:///finance.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Method to add new income
def add_income(amount, source, date):
    income = Income(amount=amount, source=source, date=date)
    session.add(income)
    session.commit()

# Method to add new expense
def add_expense(amount, category, description, date):
    expense = Expense(amount=amount, category=category, description=description, date=date)
    session.add(expense)
    session.commit()

# Method to add new savings
def add_savings(amount, date):
    savings = Savings(amount=amount, date=date)
    session.add(savings)
    session.commit()

# Method to get total income
def get_total_income():
    total_income = session.query(Income).with_entities(Income.amount).all()
    return sum(income[0] for income in total_income)

# Method to get total expenses
def get_total_expenses():
    total_expenses = session.query(Expense).with_entities(Expense.amount).all()
    return sum(expense[0] for expense in total_expenses)

# Method to get total savings
def get_total_savings():
    total_savings = session.query(Savings).with_entities(Savings.amount).all()
    return sum(saving[0] for saving in total_savings)

# Method to update income by ID
def update_income_by_id(income_id, new_amount):
    income = session.query(Income).filter_by(id=income_id).first()
    if income:
        income.amount = new_amount
        session.commit()

# Method to delete expense by ID
def delete_expense_by_id(expense_id):
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        session.delete(expense)
        session.commit()

# Method to get income by source
def get_income_by_source(source):
    return session.query(Income).filter_by(source=source).all()

# Method to get expenses by category
def get_expenses_by_category(category):
    return session.query(Expense).filter_by(category=category).all()

# Method to close the session
def close_session():
    session.close()
