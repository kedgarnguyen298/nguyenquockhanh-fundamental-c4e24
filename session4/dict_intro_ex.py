# Make a dictionary:
english_number = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
}
print(*english_number)

# User looking up and check
while True:
    user = input()
    if user in english_number:
        print(english_number[user])
    else:
        print("Syntax error !")
    
