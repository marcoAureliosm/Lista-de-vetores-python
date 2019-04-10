c = list(range(5))
for i in range(5):
    c[i] = int(input("Digite o {}ª numero".formate(i+1)))
    if c[i]<0:
        c[i]=0
print('LISTA',c)
