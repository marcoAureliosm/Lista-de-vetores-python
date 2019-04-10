l=[]
for i in range(10):
    num=int(input("DIGITE UM VALOR"))
    l.append(num)
valor=int(input("DIGITE O VALOR Q DESEJA PESQUISAR NA LISTA"))

for i in l:
    if i==valor:
        print("Elemento encontrado!")
        break
else:
    print("Elemento não encontrado.")
