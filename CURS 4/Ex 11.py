email = input("Enter your email: ")
if "@" in email:
    print(email[email.find("@"):])
else:
    print("Fara domeniu")
