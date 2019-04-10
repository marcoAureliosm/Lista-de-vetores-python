l=list(range(10))
contneg=0; contposi=0
for i in range(10):
    l[i]=float(input("Digite um valor: "))
    if l[i] < 0:
        contneg+=1
        print("Negativo")
    else:
        contposi+=l[i]
        print("POSITIVO")
print("Quantidade de numeros negativos: {} quatidade soma dos numeros positivos:{}".format(contneg,contposi))
        
