l1 = list(range(5))
l2 = list(range(5))
l3 = []
for i in range (5):
     l1[i] = int(input("Digite o {}º número da Lista 1: " .format(i + 1)))
     l2[i] = int(input("Digite o {}º número da Lista 2: ".format(i + 1)))

for i in range(5):
    l3.append(l1[i])
    l3.append(l2[i])

print("Lista 1: ", l1)
print("Lista 2: ", l2)
print("Lista intercalada: ", l3)