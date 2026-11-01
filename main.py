import json
from expense import Expense
from json_handiling import JsonHandiling
from expense_manager import ExpenseManager


def main():
    print('-' * len('EXPENSE TRACKER CLI'))
    print('EXPENSE TRACKER CLI')
    print('-' * len('EXPENSE TRACKER CLI'))

    print('Welcome to Expense Tracker!')

    while True:
        print('''
Menu:
    1. Add Expense
    2. View All Expenses
    3. Update Expense
    4. Delete Expense
    5. View Total Spending
    6. Search an Expense by ID
    7. Sort Expenses by Date or Category
    8. Exit
''')

        choice = input("Enter your choice: ")

        if choice == '8':
            print("Thank you for using Expense Tracker!")
            break

        
        elif choice == '1':
            print("Add Expense selected")
            print('--------------------')

            from datetime import date
            manager = ExpenseManager("expenses.json")
            whole_date=manager.get_all_expenses()
            id=0
            for data in whole_date:
                if data['id']>= id:
                    id=data['id']
            expense_id = id+1
            amount = float(input("Enter amount: "))
            category = input("Category: ")
            expense_date = str(date.today())
            description = input("Description: ")

            # Create an Expense object
            expense = Expense(
                expense_id,
                amount,
                category,
                expense_date,
                description
            )

            # Pass it to ExpenseManager
            result = manager.add_expense(expense)

            if result:
                print("Expense added successfully!")
            else:
                print("Failed to add expense.")

            


        elif choice == '2':
            print("View All Expenses selected")
            print("--------------------------")
            print('\n')
            manager = ExpenseManager("expenses.json")
            whole_data=manager.get_all_expenses()
            for data in whole_data : 
                for key,value in data.items():
                    print(f"{key:10} : {value}")
                print()


        elif choice == '3':
            print("Update Expense selected")
            print("-----------------------")

            manager = ExpenseManager("expenses.json")

            change_id = int(input("Enter ID of expense to be updated: "))

            whole_data = manager.get_all_expenses()

            id_list = []

            for data in whole_data:
                id_list.append(data["id"])

            if change_id in id_list:

                print('''Enter the fields to be changed:
(amount/category/date/description)

If multiple changes are required, separate the field names with commas.''')

                changes = input("Fields: ").lower()
                changes = changes.split(',')

                updated_values = {}

                for change in changes:
                    change = change.strip()

                    if change in ["amount", "category", "date", "description"]:

                        correction = input(f"Enter the correction in {change}: ")

                        if change == "amount":
                            correction = float(correction)

                        updated_values[change] = correction

                    else:
                        print(f"Invalid field: {change}")

                if updated_values:
                    '''result = manager.update_expense(change_id, **updated_values)

                    if result:
                        print("Expense updated successfully!")
                    else:
                        print("Update failed.")'''

                    valid, is_updated = manager.update_expense(change_id, **updated_values)

                    if is_updated:
                        print("Expense updated successfully!")

                    elif not valid:
                        print("Update failed due to invalid data.")

            else:
                print("Expense ID not found.")

        elif choice == '4':
            print("Delete Expense selected")
            print("-----------------------")

            manager = ExpenseManager("expenses.json")

            delete_id = int(input("Enter ID of expense to be deleted: "))

            whole_data = manager.get_all_expenses()

            id_list = []

            for data in whole_data:
                id_list.append(data["id"])

            if delete_id in id_list:

                confirm = input("Are you sure you want to delete this expense? (y/n): ")

                if confirm.lower() == 'y':
                    result = manager.delete_expense(delete_id)

                    if result:
                        print("Expense deleted successfully!")
                    else:
                        print("Deletion failed.")

                else:
                    print("Deletion cancelled.")

            else:
                print("Expense ID not found.")
        

        elif choice == '5':
            print("View Total Spending selected")
            print("-----------------------------")

            manager = ExpenseManager("expenses.json")

            whole_data = manager.get_all_expenses()

            if whole_data:
                total = manager.Total_spend()
                print(f"Total Spending: ₹{total:.2f}")

            else:
                print("No expenses recorded yet.")
        elif choice == '6':
            print("Search Expense selected")
            print('-----------------------')

            manager=ExpenseManager("expenses.json")

            search_id=int(input('Enter ID whose expense to be searched : '))
            search,data=manager.search_expense(search_id)
            if search==True:
                print('Search Successful')
                for key,value in data.items():
                    print(f'{key} : {value}')
            elif search==False:
                print(f'There is no expense recorded with ID: {search_id}')

        elif choice == '7':
            print("Filter Expenses selected")
            print("----------------------")

            manager = ExpenseManager("expenses.json")

            print('''1. Filter by category
2. Filter by date''')

            ch = int(input("Choice: "))

            if ch == 1:
                category = input("Enter category: ")

                search, filtered = manager.filter_expenses_cat(category)

            elif ch == 2:
                date = input("Enter date (YYYY-MM-DD): ")

                search, filtered = manager.filter_expenses_date(date)

            else:
                print("Invalid choice")
                search = False

            if search:
                print("\nMatching Expenses:")
                print("------------------")

                for data in filtered:
                    for key, value in data.items():
                        print(f"{key} : {value}")
                    print("------------------")

            elif ch in [1, 2]:
                print("No matching expenses found.")

        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()