x=list(range(10))
r=[]
for i in range(10):
    x[i]=int(input("Digite um numero"))
   
    if x[i] < 0:
        r.append(x[i])
print("LISTA X",x)
print("LISTA R",r)

