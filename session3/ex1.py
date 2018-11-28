#Password có số ký tự >8
while True:
    pas = input("Password: ")
    if len(pas) <= 8:
        print("Password is wrong!")
    else:
        print("Password is correct")
        break