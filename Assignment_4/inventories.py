# Inventory Tracking System
# Implemented as Classes

class InventoryItem:
    def __init__(self, name, quantity, description):
        self.name = name
        self.quantity = quantity
        self.description = description

class Inventory:
    def __init__(self):
        self.items = []

    # Function to add a new item to the inventory list
    def add_item(self, item_name, quantity, description):
        try: 
            quantity = int(quantity)
            new_item = InventoryItem(item_name, quantity, description)
            self.items.append(new_item)
            print(f'{item_name} has been added to the inventory')
        except ValueError:
            print('Please enter a valid quantity')

    # Function to remove an item from the inventory list
    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f'{item_name} has been removed from the inventory')
                return
        print(f'{item_name} is not in the inventory')

    # Function to update the quantity of an item in the inventory list
    def update_quantity(self, item_name, new_quantity):
        try:
            new_quantity = int(new_quantity)
        except ValueError:
            print('Please enter a valid quantity')
            return
        
        for item in self.items:
            if item.name == item_name:
                item.quantity = new_quantity
                print(f'The quantity of {item_name} has been updated to {new_quantity}')
                return
        print(f'{item_name} is not in the inventory')

    # Function to display the current inventory list in a readable format
    def display_inventory(self):
        print('Current Inventory:')
        for item in self.items:
            print('----------------------------------------')
            print(f'Name: {item.name}, Quantity: {item.quantity}, Description: {item.description}')
            print('----------------------------------------')