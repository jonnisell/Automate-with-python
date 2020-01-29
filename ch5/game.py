inventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory( inventory ):
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print(k + ' ' + str(v))
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

def addToInventory(inv, dragonLoot ):
    for item in dragonLoot:
        if item in inv.keys():
            inv[item] += 1
        else:
            inv[item] = 1 
    return inv

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inventory, dragonLoot)
displayInventory( inv )
