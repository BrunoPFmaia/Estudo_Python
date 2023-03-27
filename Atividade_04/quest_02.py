#   Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma
#   mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior a 6 o aluno é
#   aprovado). Escrever também o resultado da média calculada.

nota1 = float(input('informe a primeira nota do aluno:\n'))
nota2 = float(input('informe a segunda nota do aluno:\n'))

media = (nota1 + nota2) / 2

if media >= 6:
    print('O aluno foi aprovado')
elif media < 6:
    print('O aluno foi reprovado')
