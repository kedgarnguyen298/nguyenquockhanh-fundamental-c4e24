items = ["coca", "fanta", "pepsi"]
print(*items, sep = ",")

user = input("Favourite drink you want to delete? ")

items.remove(user)
print(items)