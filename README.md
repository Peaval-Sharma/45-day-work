# 💰 Personal Expense & Budget Tracker

## 📌 Project Overview

The **Personal Expense & Budget Tracker** is a Python-based project that helps users manage their daily expenses and monthly budgets. It allows users to record expenses, view all recorded transactions, set a monthly budget, and generate a monthly spending summary.

The project uses a CSV file to store expense records and a text file to save the monthly budget. It is a simple, menu-driven application designed for beginners to understand Python programming, file handling, and data management.

## 🎯 Objectives

* To record daily expenses.
* To view all recorded expenses.
* To set a monthly budget.
* To calculate total monthly spending.
* To display category-wise expenses.
* To calculate the remaining budget.
* To warn users when their spending exceeds the budget.

## ✨ Features

### 1. Add Expense

* Enter the expense date or use today's date.
* Select an expense category.
* Add a description.
* Enter the expense amount.
* Validate the date and amount before saving.

### 2. View All Expenses

* Display all recorded transactions.
* Show the date, category, description, and amount of each expense.

### 3. Set Monthly Budget

* Set a monthly spending limit.
* Save the budget in a text file.
* Update the budget whenever required.

### 4. Monthly Spending Summary

* Select a month in `YYYY-MM` format.
* Calculate the total spending for that month.
* Display category-wise spending.
* Calculate the remaining budget.
* Display a warning if spending exceeds the saved budget.

### 5. Data Storage

* Store expenses in `expenses.csv`.
* Store the monthly budget in `budget.txt`.
* Preserve saved data when the program is closed.

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Module:** `csv`
* **Module:** `os`
* **Module:** `datetime`
* **Module:** `collections`
* **Data Storage:** CSV and TXT files

## 📂 Project Structure

```text
Personal-Expense-Budget-Tracker/
│
├── expense_tracker.py
├── expenses.csv
├── budget.txt
└── README.md
```

**Note:** The program automatically creates `expenses.csv` if it does not exist. The `budget.txt` file is created when you set your monthly budget.

## ⚙️ Requirements

* Python 3.x
* A code editor such as VS Code
* A terminal or command prompt

No external Python packages are required because the project uses built-in Python modules.

## 🚀 How to Run the Project

**Step 1:** Install Python on your computer.

**Step 2:** Save the Python code in a file named:

```text
expense_tracker.py
```

**Step 3:** Open the project folder in VS Code.

**Step 4:** Open the terminal and run:

```bash
python expense_tracker.py
```

If your system uses the Python launcher, you can also run:

```bash
py expense_tracker.py
```

**Step 5:** Select an option from the main menu.

## 🖥️ Main Menu

```text
===== PERSONAL EXPENSE & BUDGET TRACKER =====
1. Add Expense
2. View All Expenses
3. Set Monthly Budget
4. View Monthly Spending Summary
5. Exit

Enter your choice (1-5):
```

## 📊 Example Usage

### Adding an Expense

```text
Enter date (YYYY-MM-DD) or press Enter for today: 2026-10-14
Enter category (Food/Travel/Shopping/Bills/Other): Food
Enter description: Lunch
Enter amount (Rs.): 150

Expense added successfully!
```

### Setting a Monthly Budget

```text
Enter your monthly budget (Rs.): 5000

Monthly budget set to Rs. 5000.00
```

### Monthly Spending Summary

Suppose the recorded expenses for October total ₹1,500 and the saved budget is ₹5,000.

```text
--- SPENDING SUMMARY: 2026-10 ---
Total spending: Rs. 1500.00

Category-wise expenses:
Food: Rs. 500.00
Shopping: Rs. 1000.00

Monthly budget: Rs. 5000.00
Remaining budget: Rs. 3500.00
You are within your budget.
```

*The output above is an illustrative example. Actual results depend on the data entered by the user.*

## 🧠 Concepts Used

This project demonstrates the following Python concepts:

* Variables and data types
* Functions
* Conditional statements (`if`, `elif`, `else`)
* Loops (`while`)
* Exception handling (`try`, `except`)
* File handling
* CSV file operations
* Lists and dictionaries
* Date and time handling
* Dictionary-based grouping with `defaultdict`
* Input validation
* Menu-driven programming

## 🔮 Future Enhancements

* Add expense editing and deletion.
* Generate graphical reports and charts.
* Support separate budgets for different categories.
* Export monthly reports to PDF.
* Add a graphical user interface (GUI).
* Add password-protected user accounts.
* Compare spending across multiple months.

## 🎓 Learning Outcomes

By developing this project, students can learn how to:

* Build a menu-driven Python application.
* Store and retrieve data using files.
* Process CSV records.
* Handle invalid user input.
* Calculate totals and category-wise spending.
* Apply basic financial tracking concepts in programming.

## 👨‍💻 Author

**Project Name:** Personal Expense & Budget Tracker

**Language:** Python

**Project Type:** Beginner-Level Python Project

## 📄 License

This project is intended for educational and learning purposes.
