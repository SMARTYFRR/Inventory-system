from src.inventory_functions import (
    add_item, view_items, update_item,
    delete_item, search_item
)

def main():
    while True:
        print("\n=== INVENTORY MANAGEMENT SYSTEM ===")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item Quantity")
        print("4. Delete Item")
        print("5. Search Item")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter item name: ")
            qty = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            add_item(name, qty, price)
            print("Item added successfully!")

        elif choice == "2":
            items = view_items()
            print("\n--- INVENTORY ITEMS ---")
            for item in items:
                print(item)

        elif choice == "3":
            item_id = int(input("Enter item ID: "))
            qty = int(input("Enter new quantity: "))
            update_item(item_id, qty)
            print("Quantity updated!")

        elif choice == "4":
            item_id = int(input("Enter item ID to delete: "))
            delete_item(item_id)
            print("Item deleted!")

        elif choice == "5":
            name = input("Enter item name to search: ")
            items = search_item(name)
            print("\n--- SEARCH RESULTS ---")
            for item in items:
                print(item)

        elif choice == "6":
            print("Goodbye ")
            break

        else:
            print("Invalid choice ngga 💀")

if __name__ == "__main__":
    main()
