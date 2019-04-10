x = list(range(5))
y=[]
i=0
while i<5:
    try:
        x[i]=int(input("Digite o {} numero".format( i+1 )))
        if i % 2 ==0:
            y.append(x[i] / 2 )
        else:
            y.append(x[i]*3)
    except:
        print("Valoe invalido. Digite Novamente")
        i-=1

print("lista X: ",x )
print("Lista Y:",y)

