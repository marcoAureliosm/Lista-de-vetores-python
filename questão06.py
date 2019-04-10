q = []
p = []
fatur=0;total=0;soma_fat=0;baixo=0
while True:
    for i in range(20):
        produto=int(input("Digite a quantidade do produto"))
        q.append(produto)
        valor=float(input("Digite o valor do produto"))
        p.append(valor)
        while produto <0 or valor<0:
            print("valor invalido")
            i-=1
    print("========================LISTA DE PRODUTOS===================")
    for i in range(20):
        print("Quantidade do {}ª produto:  {}".format(i+1,q[i]))
        print("Valor do {}ª produto: {}".format(i+1,p[i]))
        fat=q[i]*p[i]
        soma_fat=soma_fat+fat
        fatur=fat+(produto*valor)
        total=fatur+total
    media_fat=soma_fat/(i+1)
    for i in range(20):
        if q[i]*p[i]<media_fat:
            baixo+=1
    print("=======================FATURAMENTO============================")
    print("FATURAMENTO DO PRODUTO{}: {} ".format(i+1,fat))
    print("Faturamento do produto a baixo da media: ",baixo)
    print("Valor faturamento",fatur)
    print("Valor total faturado",total)
    print("Media dos faturamentos",media_fat)
    print("==============================================================")

    pessoa = int(input("DESEJA COMPRAR NOVAMENTE [N]= 0"))
    if pessoa == 0:
        break



