Meniu = """
Press 1 to enter user name
Press 2 to enter the password
Press 3 to enter the email
Press 4 to show the details (user, password, e-mail)
Press E/e to exit the program"""
print(Meniu)
print("-" * 60)
user_name = None
password = None
email = None
while True:
    press = input("Alege un numar:")
    if press == "1":
        user_name = input("Enter user name:")
    elif press == "2":
        password = input("Enter password:")
    elif press == "3":
        email = input("Enter e-mail address:")
    elif press == "4":
        if user_name is None or password is None or email is None:
            print("Nu ai introdus toate datele.")
        else:
            print(f"Username={user_name} Pass={password} Email={email}")
    elif press.lower() == "e":
        break
    else:
        print("Comanda invalida!")




