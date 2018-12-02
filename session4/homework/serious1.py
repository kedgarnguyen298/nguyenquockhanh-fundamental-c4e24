items = ["T-Shirt", "Sweater"]

user = input("Welcome to our shop, what do you want (C, R, U, D)?").upper()

if user == "R":
    print("Our items: ", end = " ")
    print(*items, sep = ", ")
elif user == "C":
    newi = input("Enter a item: ")
    items.append(newi)
    print("Our items: ", end = " ")
    print(*items, sep = ", ")
elif user == "U":
    updi = input("Update position: ")
    if updi.isdigit():
        updi = int(updi)
        if 0 < updi < 3:
            newi = input("New item? ")
            items[updi - 1] = newi
            print("Our items: ", end = " ")
            print(*items, sep = ", ")
        else:
            print("This item is not available !")
    else:
        print("Enter a number !")
elif user == "D":
    deli = input("Delete position? ")
    if deli.isdigit():
        deli = int(deli)
        if 0 < deli < 3:
            items.pop(deli - 1)
            print("Our items: ", end = " ")
            print(*items, sep = ", ")
        else:
            print("Not available !")
    else:
        print("Enter a number!")
