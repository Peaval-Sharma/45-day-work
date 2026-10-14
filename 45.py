
import csv
import os
from datetime import datetime
from collections import defaultdict

EXPENSE_FILE = "expenses.csv"
BUDGET_FILE = "budget.txt"


# Create CSV file if it does not exist
def initialize_file():
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


# Add a new expense
def add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
        if date == "":
            date = datetime.now().strftime("%Y-%m-%d")
        else:
            datetime.strptime(date, "%Y-%m-%d")

        category = input("Enter category (Food/Travel/Shopping/Bills/Other): ").strip()
        if not category:
            print("Category cannot be empty!")
            return

        description = input("Enter description: ").strip()
        if not description:
            description = "General expense"

        amount = float(input("Enter amount (Rs.): "))
        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        with open(EXPENSE_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, amount])

        print("Expense added successfully!")

    except ValueError:
        print("Invalid input! Please enter a valid date and amount.")


# View all expenses
def view_expenses():
    try:
        with open(EXPENSE_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)
            expenses = list(reader)

        if not expenses:
            print("No expenses recorded yet.")
            return

        print("\n--- ALL EXPENSES ---")
        for expense in expenses:
            print(
                f"Date: {expense['Date']} | "
                f"Category: {expense['Category']} | "
                f"Description: {expense['Description']} | "
                f"Amount: Rs. {float(expense['Amount']):.2f}"
            )

    except (OSError, ValueError, KeyError) as error:
        print("Unable to read expenses:", error)


# Set monthly budget
def set_budget():
    try:
        budget = float(input("Enter your monthly budget (Rs.): "))

        if budget <= 0:
            print("Budget must be greater than zero!")
            return

        with open(BUDGET_FILE, "w") as file:
            file.write(str(budget))

        print(f"Monthly budget set to Rs. {budget:.2f}")

    except ValueError:
        print("Please enter a valid budget amount.")


# Read monthly budget
def get_budget():
    try:
        with open(BUDGET_FILE, "r") as file:
            return float(file.read().strip())
    except (OSError, ValueError):
        return 0.0


# Generate monthly spending summary
def spending_summary():
    month = input("Enter month (YYYY-MM), or press Enter for current month: ")

    if month == "":
        month = datetime.now().strftime("%Y-%m")

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month format!")
        return

    category_totals = defaultdict(float)
    total = 0.0

    try:
        with open(EXPENSE_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)

            for expense in reader:
                if expense["Date"].startswith(month):
                    amount = float(expense["Amount"])
                    category_totals[expense["Category"]] += amount
                    total += amount

        print(f"\n--- SPENDING SUMMARY: {month} ---")
        print(f"Total spending: Rs. {total:.2f}")

        if category_totals:
            print("\nCategory-wise expenses:")
            for category, amount in sorted(category_totals.items()):
                print(f"{category}: Rs. {amount:.2f}")
        else:
            print("No expenses found for this month.")

        budget = get_budget()

        if budget > 0:
            remaining = budget - total
            print(f"\nMonthly budget: Rs. {budget:.2f}")
            print(f"Remaining budget: Rs. {remaining:.2f}")

            if remaining < 0:
                print("WARNING: You have exceeded your budget!")
            else:
                print("You are within your budget.")

    except (OSError, ValueError, KeyError) as error:
        print("Unable to generate summary:", error)


# Main menu
def main():
    initialize_file()

    while True:
        print("\n===== PERSONAL EXPENSE & BUDGET TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Set Monthly Budget")
        print("4. View Monthly Spending Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            set_budget()
        elif choice == "4":
            spending_summary()
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice! Please select 1 to 5.")


if __name__ == "__main__":
    main()
