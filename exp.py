def add_expense(expenses):
    amount = float(input("Enter expense amount: ₹"))
    category = input("Enter category: ")

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print("Expense Added Successfully!")


def view_expenses(expenses):

    if len(expenses) == 0:
        print("No Expenses Found")
        return

    print("\n------ ALL EXPENSES ------")

    count = 1

    for expense in expenses:
        print(f"\nExpense {count}")
        print(f"Amount: ₹{expense['amount']}")
        print(f"Category: {expense['category']}")

        count += 1


def total_expense(expenses):

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expense: ₹{total}")


expenses = []

while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        total_expense(expenses)

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")