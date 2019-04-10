w = list(range(5))
i=0
while i <5:
    try:
        w[i] = input("Digite o {} valor".format(i+1))
    except:
        print("VALOR INVALIDO DIGITADO")
        i-=1

    i+=1
v = input("DIGITE UM VALOR QUAL QUER PARA PESQUISAR NA LISTA")
c=0
for i in range(5):
    if v == w[i]:
        c+=1
print("O VALOR {} APARECE {} VAZES NA LISTA W".format(v,c))
print("LISTA W",w)




