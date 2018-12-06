inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# Add a key to inventory called 'pocket' and set the value
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# remove('dagger') from the list
backpack = inventory["backpack"]
backpack.pop(1)

# Add 50 to the number stored under the 'gold' key
inventory["gold"] += 50

print(inventory)


