words = ["fring", "frumos", "frate"]
words2 = ['Python' , 'Pasare', 'Politie']
com_words = []
W1 = (words[0].lower())
W2 = (words[1].lower())
W3 = (words[2].lower())

for litera in W1:
    if litera in W2 and litera in W3 and litera not in com_words:
        com_words.append(litera)
    if litera in W3 and  W2 and litera not in com_words:
        com_words.append(litera)
for litera in W2:
    if litera in W1 and litera in  W3 and litera not in com_words:
        com_words.append(litera)
    if litera in W3 and W1 and litera not in com_words:
        com_words.append(litera)
for litera in W1:
    if litera in W2 and W3 and litera not in com_words:
        com_words.append(litera)
    if litera in W3 and W2 and litera not in com_words:
        com_words.append(litera)


print("".join(com_words))