gab=['a','a','e','b','c',]
n_alunos = int(input('DIGITE O NUMERO DE ALUNOS DA TURMA: '))
for i in range(n_alunos):
    numero_do_aluno = int(input("Digite o numero do(a) "))
    acerto = 0
    for j in range(30):
        resposta=input("DIGITE A RESPOSTA DA QUESTÃO {}".format(j+1))
        if resposta == gab[j]:
            acerto +=1
print("O aluno de numero {} teve {} acertos".format(numero_do_aluno,acerto))


