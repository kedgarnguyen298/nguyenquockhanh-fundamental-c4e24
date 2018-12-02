items = ["coca", "fanta", "pepsi"]
print(*items, sep = ",")

while True:

    user = int(input("Favourite drink you want to delete? "))
    if (user - 1) >= len(items):
        print("The number was wrong")
    else:
        break

items.pop(user - 1)
print(items)