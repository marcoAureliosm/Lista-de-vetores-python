l=[]
print("===============MENU===============")
print('[1]Cadastrar Nome \n[2]Pesquisar nome\n[3]listar todos os nome\n[0]sair do programa')
while True:
    n=int(input("Digite qual funçao deseja usar: "))
    if n == 1:
        nome=str(input("Digire seu nome"))
        l.append(nome)
    elif n == 2:
        nome=str(input("Digire seu nome que deseja pesquisar"))
        elemento = l.index(nome)
        print("Posiçao do nome na lista:",elemento)

    elif n == 3:
        print(l)
    elif n == 0:
        break
    else:
        print("VALOR INVALIDO")
  
