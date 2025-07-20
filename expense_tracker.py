import csv
import datetime

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    note = input("Enter note (optional): ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, note])
    print("✅ Expense added successfully!\n")

def view_expenses():
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found.\n")

def show_total():
    total = 0
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[1])
        print(f"💰 Total Spent: ₹{total}\n")
    except:
        print("Could not calculate total.\n")

def main():
    while True:
        print("📌 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            show_total()
        elif choice == '4':
            break
        else:
            print("Invalid option!\n")

if __name__ == "__main__":
    main()
