# personal expense tracker

expenses = []
print("welcome to personal expense tracker")

while True:
    print("----MENU----")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View Total expense")
    print("4. Exit")
    choice = int(input("please enter your choice:"))

    if choice == 1:
        date = input("Enter the date of expense (DDMMYYYY):")
        amount = float(input("Enter the amount of expense:"))
        category = input("Enter the category of expense:")

        expense = {"date": date, "amount": amount, "category": category}
        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            for i, expense in enumerate(expenses, start=1):
                print(f"Expense {i}:")
                print(f"Date: {expense['date']}")
                print(f"Amount: {expense['amount']}")
                print(f"Category: {expense['category']}")
                print("--------------------")

    elif choice == 3:
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total expense: {total}")

    elif choice == 4:
        print("Thank you for using personal expense tracker!")
        break

    else:
        print("Invalid choice. Please try again.")





     