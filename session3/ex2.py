#Password có cả chữ hoa và chữ thường và ký tự >8:

while True:
    pw_admin = "kedgarnguyen298"
    pw = input("Pass word: ")
    
    if pw == pw_admin:
        break
    else:
        if len(pw) > 8:
            if (not pw.isdigit() and not pw.isupper() and not pw.islower()):
                print("Password was wrong!")
            else:
                print("Password was illegal!")
        elif pw == "":
            print("You didn't fill pw")
        else:
            print("Password is too short!")
            

print("Login successful!")