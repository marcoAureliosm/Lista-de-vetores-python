l=list(range(11))
par=[]; impar=[]
contpar=0; contimpar=0
for i in range(1,11):
    l[i]=int(input("Digite o {}ª valor".format(i)))
    if l[i] % 2==0:
        contpar += 1
        par.append(l[i])
    else:
        contimpar += 1
        impar.append(l[i])
print("Numeros pares: {} Quantidade PAR: {} Numeros impar: {} Quantidade IMPAR: {}".format(par,contpar,impar,contimpar))         

