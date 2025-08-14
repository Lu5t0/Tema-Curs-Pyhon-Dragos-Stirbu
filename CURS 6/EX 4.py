# viarianta1 = [5, 3, 100, 1, 435, 1000]
# viarianta1.sort()
# print(viarianta1)
# rezul = viarianta1[0] + viarianta1[1]
#
# print(rezul)




varianta2 = [1, -4, 10, 18, -53, -33]
numere_neg = []
numere_pos = []
for  number in varianta2:
    if number < 0:
        numere_neg.append(number)
    else:
        numere_pos.append(number)
numere_neg.sort()
print(numere_pos)
print(numere_pos[0] + numere_pos[1])





