items = ["coca", "pepsi", "fanta"]

user = input("What do you want? (C, R, U or D) ").upper()

if user == "C":
    cre = input("What do  you want to append? ")
    items.append(cre)
    print(*items, sep = ", ")

elif user == "R":
    for index, item in enumerate(items):
        print(index + 1, item, sep = ". ")

elif user == "U":
    print(*items, sep = ", ")
    while True:
        upd = int(input("What position you want to update? "))
        if upd <= len(items):
            items[upd - 1] = input("Your replacing fav? ")
            print(*items, sep = ", ")
            break
        else:
            print("The number was wrong!")

elif user == "D":
    print(*items, sep = ", ")
    while True:
        dele = input("Favourite drink you want to delete? ")
        if dele.isdigit():
            dele = int(dele)    
            if (dele - 1) >= len(items):
                    print("The number was wrong")
            else:
                items.pop(dele - 1)
                print(*items, sep = ", ")
                break
        elif dele.isalpha():
            items.remove(dele)
            print(*items, sep = ", ")
            break



