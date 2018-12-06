
print("If x = 3, then what is value of: x + 5? ")

anss = [5, 6, 7, 8]

for i,anss in enumerate(anss, 1):
    print(i, anss, sep = ".")

user = input("Your choice: ")

if user == "4":
    print("Hura")
else:
    print(":(")