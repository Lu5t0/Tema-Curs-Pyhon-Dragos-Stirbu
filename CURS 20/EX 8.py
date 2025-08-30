# Generator pentru caracterele unui șir
# Fă un generator care primește un șir de caractere și le returnează unul câte unul.
def generator_caractere(sir):
    for caracter in sir:
        yield caracter

if __name__ == '__main__':
    sir = "Ana are mere"
    for caracter in generator_caractere(sir):
        print(caracter)