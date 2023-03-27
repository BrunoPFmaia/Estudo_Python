# Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles

num1 = float(input('informe o primeiro valor:\n'))

num2 = float(input('informe o segundo valor:\n'))

if num1 > num2:
    print(f'O maior número é {num1}')
elif num2 > num1:
    print(f'O maior número é {num2}')