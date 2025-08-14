def char_unic(cuvant):
    return len(set(cuvant)) != len(cuvant)

if __name__ == "__main__":
    print(char_unic("extraterestru"))
    print(char_unic("mar"))
    print(char_unic("albastru"))
    print(char_unic("alb"))

