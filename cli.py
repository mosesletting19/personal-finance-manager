from datetime import datetime
from orm_methods import (
    add_income, add_expense, add_savings,
    get_total_income, get_total_expenses, get_total_savings,
    update_income_by_id, delete_expense_by_id,
    get_income_by_source, get_expenses_by_category,
    close_session
)

# ANSI color codes for formatting
class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def show_options():
    print(Color.BOLD + "Options:" + Color.ENDC)
    print("1. " + Color.OKBLUE + "Add Income" + Color.ENDC)
    print("2. " + Color.OKBLUE + "Add Expense" + Color.ENDC)
    print("3. " + Color.OKBLUE + "Add Savings" + Color.ENDC)
    print("4. " + Color.OKGREEN + "Total Income" + Color.ENDC)
    print("5. " + Color.OKGREEN + "Total Expenses" + Color.ENDC)
    print("6. " + Color.OKGREEN + "Total Savings" + Color.ENDC)
    print("7. " + Color.WARNING + "Update Income" + Color.ENDC)
    print("8. " + Color.WARNING + "Delete Expense" + Color.ENDC)
    print("9. " + Color.OKBLUE + "Income by Source" + Color.ENDC)
    print("10. " + Color.OKBLUE + "Expenses by Category" + Color.ENDC)
    print("11. " + Color.FAIL + "Exit" + Color.ENDC)

def print_divider():
    print("*" * 50)  # Print a line of asterisks for visual separation

def main():
    while True:
        show_options()
        print_divider()
        choice = input("Enter your choice (1-11): ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            source = input("Enter income source: ")
            date_str = input("Enter income date (YYYY-MM-DD): ")
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            add_income(amount, source, date)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            description = input("Enter expense description: ")
            date_str = input("Enter expense date (YYYY-MM-DD): ")
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            add_expense(amount, category, description, date)
        elif choice == '3':
            amount = float(input("Enter savings amount: "))
            date_str = input("Enter savings date (YYYY-MM-DD): ")
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            add_savings(amount, date)
        elif choice == '4':
            print_divider()
            total_income = get_total_income()
            print(f"{Color.OKGREEN}Total Income: ${total_income}{Color.ENDC}")
        elif choice == '5':
            print_divider()
            total_expenses = get_total_expenses()
            print(f"{Color.OKGREEN}Total Expenses: ${total_expenses}{Color.ENDC}")
        elif choice == '6':
            print_divider()
            total_savings = get_total_savings()
            print(f"{Color.OKGREEN}Total Savings: ${total_savings}{Color.ENDC}")
        elif choice == '7':
            income_id = int(input("Enter income ID to update: "))
            new_amount = float(input("Enter new income amount: "))
            update_income_by_id(income_id, new_amount)
        elif choice == '8':
            expense_id = int(input("Enter expense ID to delete: "))
            delete_expense_by_id(expense_id)
        elif choice == '9':
            source = input("Enter income source: ")
            incomes = get_income_by_source(source)
            if incomes:
                for income in incomes:
                    print(f"Income ID: {income.id}, Amount: ${income.amount}, Source: {income.source}, Date: {income.date}")
            else:
                print(f"No income found for source: {source}")
        elif choice == '10':
            category = input("Enter expense category: ")
            expenses = get_expenses_by_category(category)
            if expenses:
                for expense in expenses:
                    print(f"Expense ID: {expense.id}, Amount: ${expense.amount}, Category: {expense.category}, Description: {expense.description}, Date: {expense.date}")
            else:
                print(f"No expenses found for category: {category}")
        elif choice == '11':
            close_session()
            print(f"{Color.FAIL}Exiting the program. Goodbye!{Color.ENDC}")
            break
        else:
            print(f"{Color.FAIL}Invalid choice. Please choose a number from 1 to 11.{Color.ENDC}")

if __name__ == "__main__":
    main()
