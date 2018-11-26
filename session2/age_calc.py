youb = int(input("The year you was borned? "))
age = 2018 - youb
print(age)

if age < 10:
    print("baby")
elif age < 18:
    print("teenager")
else:
    print("adult")
print("Bye bye")