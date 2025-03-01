# Inventory Tracking System

# Global inventory list
inventory = []


# Function to add a new item to the inventory list
def add_item(item_name, quantity, description):
    try: 
        quantity = int(quantity)
        new_item = {
            'name': item_name,
            'quantity': quantity,
            'description': description
        }
        inventory.append(new_item)
        print(f'{item_name} has been added to the inventory')
    except:
        print('Please enter a valid quantity')

# Function to remove an item from the inventory list
def remove_item(item_name):
    for item in inventory:
        if item['name'] == item_name:
            inventory.remove(item)
            print(f'{item_name} has been removed from the inventory')
            return
    print(f'{item_name} is not in the inventory')

# Function to update the quantity of an item in the inventory list
def update_quantity(item_name, new_quantity):
    try:
        new_quantity = int(new_quantity)
    except:
        print('Please enter a valid quantity')
        return
    
    for item in inventory:
        if item['name'] == item_name:
            item['quantity'] = new_quantity
            print(f'The quantity of {item_name} has been updated to {new_quantity}')
            return
    print(f'{item_name} is not in the inventory')

# Function to display the current inventory list in a readable format
def display_inventory():
    print('Current Inventory:')
    for item in inventory:
        print('----------------------------------------')
        print(f'Name: {item["name"]}, Quantity: {item["quantity"]}, Description: {item["description"]}')
        print('----------------------------------------')