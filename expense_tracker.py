import csv
import os
from datetime import datetime

FILE_NAME = "/Users/himeshtak/Desktop/expenses.csv"


def create_file():
    """Create the CSV file if it doesn't already exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])


def add_expense():
    print("\n--- Add Expense ---")

    try:
        date = input("Enter date (DD-MM-YYYY): ")

        # Check whether the date is valid
        datetime.strptime(date, "%d-%m-%Y")

        category = input("Enter category: ").strip()

        if category == "":
            print("Category cannot be empty.")
            return

        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount should be greater than 0.")
            return

        note = input("Enter note (optional): ").strip()

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, note])

        print("Expense added successfully.")

    except ValueError:
        print("Please enter a valid date and amount.")


def view_expenses():
    print("\n--- All Expenses ---")

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            total = 0
            found = False

            for expense in reader:
                found = True

                print(
                    f"Date: {expense['Date']} | "
                    f"Category: {expense['Category']} | "
                    f"Amount: ₹{float(expense['Amount']):.2f} | "
                    f"Note: {expense['Note']}"
                )

                total += float(expense["Amount"])

            if found:
                print("-" * 50)
                print(f"Total amount spent: ₹{total:.2f}")
            else:
                print("No expenses have been added yet.")

    except FileNotFoundError:
        print("Expense file does not exist.")


def category_summary():
    print("\n--- Category-wise Summary ---")

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            categories = {}

            for expense in reader:
                category = expense["Category"]
                amount = float(expense["Amount"])

                if category in categories:
                    categories[category] += amount
                else:
                    categories[category] = amount

            if not categories:
                print("No expenses have been recorded.")
                return

            for category, amount in categories.items():
                print(f"{category}: ₹{amount:.2f}")

    except FileNotFoundError:
        print("Expense file does not exist.")


def main():
    create_file()

    while True:
        print("\n========== Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category-wise Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            category_summary()

        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()