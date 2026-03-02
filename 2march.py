filename = 'expenses.txt'

def add_expense():
    item = input("enter item: ")
    cat = input("enter category: ")
    amt = input("enter amount: ")
    
    with open(filename, 'a') as f:
        f.write(f"{item},{cat},{amt}\n")
    print("added!")

def view_summary():
    total = 0
    print("\n--- your expenses ---")
    with open(filename, 'r') as f:
        lines = f.readlines()
        
        for line in lines[1:]:
            item, cat, amt = line.strip().split(',')
            print(f"{item} ({cat}): {amt}")
            total += float(amt)
    print(f"total: {total:.2f}\n")

while True:
    choice = input("1: add, 2: view, 3: exit. choose: ")
    if choice == '1': add_expense()
    elif choice == '2': view_summary()
    elif choice == '3': break