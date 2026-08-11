import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])


def add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD): ")

        datetime.strptime(date, "%Y-%m-%d")

        category = input("Enter category: ").strip()

        if not category:
            print("Category cannot be empty.")
            return

        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        note = input("Enter note (optional): ").strip()

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, note])

        print("Expense added successfully.")

    except ValueError:
        print("Invalid input. Please enter a valid date and amount.")
    except Exception as e:
        print("An error occurred:", e)


def view_expenses():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            expenses = list(reader)

            if not expenses:
                print("No expenses recorded.")
                return

            total = 0

            print("\n========== All Expenses ==========")

            for expense in expenses:
                print(
                    f"Date: {expense['Date']} | "
                    f"Category: {expense['Category']} | "
                    f"Amount: ₹{float(expense['Amount']):.2f} | "
                    f"Note: {expense['Note']}"
                )

                total += float(expense["Amount"])

            print("----------------------------------")
            print(f"Total Amount Spent: ₹{total:.2f}")

    except FileNotFoundError:
        print("Expense file not found.")
    except ValueError:
        print("Invalid amount found in the CSV file.")
    except Exception as e:
        print("An error occurred:", e)


def category_summary():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            summary = {}

            for expense in reader:
                category = expense["Category"]
                amount = float(expense["Amount"])

                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount

            if not summary:
                print("No expenses recorded.")
                return

            print("\n====== Category-wise Summary ======")

            for category, amount in summary.items():
                print(f"{category}: ₹{amount:.2f}")

    except FileNotFoundError:
        print("Expense file not found.")
    except ValueError:
        print("Invalid amount found in the CSV file.")
    except Exception as e:
        print("An error occurred:", e)


def main():
    initialize_file()

    while True:
        print("\n========== Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
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
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()