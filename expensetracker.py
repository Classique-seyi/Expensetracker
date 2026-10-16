import sys

expenses = []


def add_expense():
    while True:
        description = input("Description: ").strip().capitalize()
        if description:
            break
        print("Description cannot be empty. Please try again ")

    while True:      
        category = input("Category: ").strip().title()

        if category:
            break
        print("Category cannot be empty. Please try again")

    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be a positive number.")
                continue

        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue
        break
            
                

    expense = {
        "description": description,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print('\n' + '=' * 66)
    print('All Expenses'.center(66))
    print('=' * 66)

    print(f"{"S/n":^6} | {"Description":^20} | {"Category":^15} | {"Amount":^10}(₦)")

    for index, expense in enumerate(expenses, 1):
        print(f"{index:^6} | {expense['description']:<20} | {expense['category']:<15} |{expense['amount']:>10.2f}")

    print('=' * 66)


def view_summary():
    if not expenses:
        print("No expenses available to summarize.")
        return

    total = 0
    category_totals = {}

    for expense in expenses:
        amount = expense["amount"]
        category = expense["category"]
        
        total += amount
      
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    
    max_expense = max(expense["amount"] for expense in expenses)
    top_expenses = [expense for expense in expenses if expense["amount"] == max_expense]

    print("\n===== Expense Summary =====")
    print(f"Total spent: ₦ {total:.2f}")

    print("\nSpending by category:")

    for category, amount in category_totals.items():
        print(f"{category}: ₦ {amount:.2f}\n")

    
    print("===== Most Expensive Expense =====")
    print(f"{"S/n":^6} | {"Category":^15} | {"Description":^20} | {"Amount":^10}(₦)")

    for index, most_expensive in enumerate(top_expenses, 1):
        print(f"{index:^6} | {most_expensive['category']:<15} | {most_expensive['description']:<20} |{most_expensive['amount']:>10.2f}")


def main():
    while True:
        print("""
===== Expense Tracker =====
1. Add expense
2. View expenses
3. View summary
4. Quit
===========================
""")
       
        choice = input("Choose an option: ").strip()

        if not choice:
            print("Choice can't be empty")
            continue

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            view_summary()

        elif choice == "4":
            print("Thank you for using the Expense Tracker!")
            sys.exit(0)

        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


main()



#Category: food; Description: lunch; amt: 2000
#: rent; : house rent; : 4500000
#: fashion; : shoes; : 30000