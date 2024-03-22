from datetime import datetime
from sqlalchemy import create_engine
from orm_methods import *
from models import Base

# Create the database engine and initialize the session
engine = create_engine('sqlite:///finance.db')
Base.metadata.create_all(engine)
init_session(engine)

# CLI functionality
def main():
    print("Welcome to Personal Finance Manager CLI")

    while True:
        print("\nOptions:")
        print("1. Register")
        print("2. Login")
        print("3. Add Transaction")
        print("4. List Transactions")
        print("5. Add Category")
        print("6. Update Category")
        print("7. Delete Category")
        print("8. Logout")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            user = create_user(username, password, email)
            if user:
                print("User registered successfully!")
            else:
                print("Username or email already exists.")

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = authenticate_user(username, password)
            if user:
                print("Login successful!")
                # Additional actions after login can be added here
            else:
                print("Invalid username or password.")

        elif choice == '3':
            user_id = int(input("Enter user ID: "))  # Assuming the user is already logged in
            description = input("Enter transaction description: ")
            amount = int(input("Enter transaction amount: "))
            type = input("Enter transaction type (income/expense): ")
            category_id = int(input("Enter category ID: "))
            add_transaction(user_id, category_id, datetime.now(), description, amount, type)
            print("Transaction added successfully!")

        elif choice == '4':
            user_id = int(input("Enter user ID: "))  # Assuming the user is already logged in
            transactions = get_transactions_by_user(user_id)
            if transactions:
                for transaction in transactions:
                    print(f"ID: {transaction.id}, Description: {transaction.description}, Amount: {transaction.amount}")
            else:
                print("No transactions found.")

        elif choice == '5':
            name = input("Enter category name: ")
            category = add_category(name)
            print(f"Category '{category.name}' added successfully!")

        elif choice == '6':
            category_id = int(input("Enter category ID to update: "))
            new_name = input("Enter new category name: ")
            category = update_category(category_id, new_name)
            if category:
                print(f"Category updated successfully: {category.name}")
            else:
                print("Category not found.")

        elif choice == '7':
            category_id = int(input("Enter category ID to delete: "))
            result = delete_category(category_id)
            if result:
                print("Category deleted successfully.")
            else:
                print("Category not found.")

        elif choice == '8':
            print("Logout successful.")
            # Additional logout actions can be added here

        elif choice == '9':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
