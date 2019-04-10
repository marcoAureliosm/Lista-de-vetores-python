l = list(range(5))
l2 = []
for i in range (5):
     l[i] = int(input("Digite o número {}: " .format(i + 1)))
j=4
for i in range(5):
     l2.append(l[j])
     j-=1

print("Lista normal   : ", l)
print("Lista invertida: ", l2)
