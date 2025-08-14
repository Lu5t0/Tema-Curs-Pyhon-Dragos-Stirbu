text = input("Scerie un text: ")
char = 0
digits = 0
simbols = 0
spaces = 0
for i in text:
    if i in "0123456789":
        digits += 1
    elif i in "!#$%&'^_()*+,-.":
        simbols += 1
    elif i in " ":
        spaces += 1
    else:
        char += 1
print(f"Avem {digits} digits,  {simbols} symbols,  {spaces} spaces si {char} characters")



        


