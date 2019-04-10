d = list(range(5))
e=[]
i=0
while i <5:
    try:
        d[i]=int(input("DIGITE O {} VALOR".format(i+1)))
    except:
            print("Valor invalido.Digite novamente ")
            i-=1
    i+=1
j=4
for i in range(5):
    e.append(d[j])
    j-=1
print("lista D: ",d)
print("Lista E: ",e)
