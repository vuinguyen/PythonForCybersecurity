# An example of how to use the inventory class and its methods

from inventories import Inventory

inventory = Inventory()

inventory.add_item('Apples', 10, 'A fruit')
inventory.add_item('Bananas', 5, 'Another fruit')
inventory.add_item('Carrots', 3, 'A vegetable')
inventory.display_inventory()       

inventory.remove_item('Apples')
inventory.display_inventory()

inventory.update_quantity('Bananas', 20)
inventory.display_inventory()


