l=list(range(15))
maior=0; menor=1; cont1=0; cont2=0
for i in range(15):
    l[i]=int(input("Digite um valor"))
    if l[i]> maior:
        maior=(l[i])
        cont2=i+1
         
    elif l[i]< menor:
        menor=(l[i])
        cont1=i+1

         
print("Maior valor",maior)
print("menor valor",menor)
print("Posição menor",cont2)
print("Posição menor",cont1)
print(l)
