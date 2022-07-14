

email = input("Enter your email ")
if '@' in email:
    password = input("Enter your password ")

    if email == "ok@email.com" and password == "1234":
        print("Welcome!!")
    elif email == "ok@email.com" and password != "1234":
        print("Password Incorrect")
        password = input("Enter password again ")
        if password == "1234":
            print("Welcome!!")
        else:
            print("Still incorrect")
    else:
        print("Incorrect credentials")
else:
    print("Not a valid email")
