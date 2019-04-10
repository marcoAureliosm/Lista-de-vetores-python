l=list(range(5))
for i in range(5):
    l[i]=int(input('DIGITE O {}ª NUMERO'.format(i+1)))
maior = l[0]; menor= l[0]; menor=1; pos_menor=0
for i in range (1,5):
    if l[i]> maior:
        maior=l[i]
        pos_maior=i+1
    if l[i]<menor:
        menor=l[i]
        pos_menor=i+1
print("MAIOR NUMERO {} POSIÇÃO {}".format(maior,pos_maior))
print("MENOR NUMERO {} POSIÇÃO {}".format(menor,pos_menor))
