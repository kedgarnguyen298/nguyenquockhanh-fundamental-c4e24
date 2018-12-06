# read file => str
f = open("data.json")
text = f.read()
# Loas, parse, str => dict
import json

# Make a dictionary:
english_number = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
}
print(*english_number)

# User looking up and checking, hỏi user có muốn update không? Nếu có thì hỏi là từ gì rồi cập nhật

while True:
    user = input()
    if user in english_number:
        upd = input("Do you want to update (Y/N)? ").upper()
        if upd == "N":
            break
        elif upd == "Y":
            new = input("Your translation? ")
            english_number[user] = new
            print(english_number)
            break
    else:
        print("Not found !")
        add = input("Do you want to contribute? (Y/N)").upper()
        if add == "N":
            break
        if add == "Y":
            new2 = input("What does it mean?")
            english_number[user] = new2
            print(english_number)
            break


    
        

