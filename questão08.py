x=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","W","Y","Z"]

pesquisar=str(input("DIGITE A LETRA QUE DESEJA PESQUISAR"))

for i in x:
    if i == pesquisar:      
        print("Valor encontrado")
        break
    else:
        print("VALOR NÃO ENCONTRADO")


