q=[]
maior=0
indice=0
for i in range(10):
    try:
        n=int(input("digite o {}ª valor".format(i+1)))
    except:
          print("Valor invalido")
    while n < 0:
          print("VALOR INVALIDO")
          i-=1
          n=int(input("digite o {}ª valor".format(i+1)))
    else:
        q.append(n)
        if q[i]> maior:
          maior=q[i]
          indice=i
print("lista",q)
print("Maior valor {} posiçao {}".format(maior,indice))
