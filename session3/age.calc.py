while True:
    yob_str = input("Write your year of birthday: ")
    if yob_str.isdigit():
        break

age = 2018 - int(yob_str)

print("Your age: ", age)

