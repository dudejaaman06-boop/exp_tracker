def add_expense():

    amount = input("Enter expense amount: Rs ")
    category = input("Enter category: ")

    file = open("expenses.txt", "a")

    file.write(amount + "," + category + "\n")

    file.close()

    print("Expense Added Successfully!")


def view_expenses():

    try:
        file = open("expenses.txt", "r")

        expenses = file.readlines()

        file.close()

        if len(expenses) == 0:
            print("No Expenses Found")
            return

        print("\n------ ALL EXPENSES ------")

        count = 1

        for expense in expenses:

            data = expense.strip().split(",")

            print(f"\nExpense {count}")
            print(f"Amount: Rs {data[0]}")
            print(f"Category: {data[1]}")

            count += 1

    except FileNotFoundError:
        print("No Expense File Found")


def total_expense():

    try:
        file = open("expenses.txt", "r")

        expenses = file.readlines()

        file.close()

        total = 0

        for expense in expenses:

            data = expense.strip().split(",")

            total += float(data[0])

        print(f"\nTotal Expense: Rs {total}")

    except FileNotFoundError:
        print("No Expenses Found")


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
