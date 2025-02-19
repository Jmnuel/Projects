from abc import ABC, abstractmethod
from typing import Optional

class Item(ABC):
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

    def __str__(self):
        pass

class InventoryManagement(ABC):
    @abstractmethod
    def add_item(self, item: 'Item'):
        pass

    @abstractmethod
    def remove_item(self, item: 'Item'):
        pass

    @abstractmethod
    def get_inventory(self):
        pass

class StoreItem(Item, InventoryManagement):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.items = []  # List to store items if needed for inheritance

    def add_item(self, item: 'Item'):
        self.items.append(item)

    def remove_item(self, item: 'Item'):
        if item in self.items:
            self.items.remove(item)

    def get_inventory(self):
        return self.items

    def get_inventory_value(self):
        return self.get_total_price()
    
    def __str__(self):
        return f"{self.name}: {self.quantity} x P{self.get_total_price()}"

class SevenEleven(InventoryManagement):
    def __init__(self):
        self.inventory = []

    def add_item(self, item: StoreItem):
        self.inventory.append(item)
        print(f"Added {item.name} to inventory.")

    def remove_item(self, item: StoreItem):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"Removed {item.name} from inventory.")
        else:
            print(f"Item {item.name} not found in inventory.")

    def get_inventory(self):
        return self.inventory

    def get_inventory_value(self):
        total_value = 0
        for item in self.inventory:
            total_value += item.get_inventory_value()
        return total_value
    
    def get_item_by_name(self, name: str) -> Optional[StoreItem]:
        for item in self.inventory:
            if item.name.lower() == name.lower():
                return item
        return None
    
    def __str__(self) -> str:
        if not self.inventory:
            return "7-11 Store Inventory: Empty"
        inventory_str = "\n".join(str(item) for item in self.inventory)
        return f"7-11 Store Inventory:\n{inventory_str}\nTotal Value: P{self.get_inventory_value()}"

def main():
    store = SevenEleven()
    print("Welcome to the 7-11 Inventory Management System!")

    while True:
        print("\nMenu:")
        print("1. Add a new item")
        print("2. Remove an item")
        print("3. View inventory")
        print("4. Check total inventory value")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter item name: ")
            try:
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                if price < 0 or quantity < 0:
                    print("Price and quantity must be non-negative!")
                    continue
                new_item = StoreItem(name, price, quantity)
                store.add_item(new_item)
            except ValueError:
                print("Invalid input! Price must be a number, and quantity must be an integer.")

        elif choice == '2':
            name = input("Enter the name of the item to remove: ")
            item_to_remove = store.get_item_by_name(name)
            if item_to_remove:
                store.remove_item(item_to_remove)
            else:
                print(f"Item '{name}' not found in inventory.")

        elif choice == '3':
            print(store)

        elif choice == '4':
            total_value = store.get_inventory_value()
            print(f"Total Inventory Value: P{total_value}")

        elif choice == '5':
            print("Exiting 7-11 Inventory Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()