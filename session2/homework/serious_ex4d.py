n = int(input("Enter the number: "))

if n%2 == 0:
    for i in range(0, n-1, 2):
        print("x ", end = "")
        print("* ", end = "")
else:
    for i in range(0, n-1, 2):
        print("x ", end = "")
        print("* ", end = "")

    print("x")