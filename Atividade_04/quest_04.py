#Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente

num1 = float(input('informe o primeiro valor:\n'))

num2 = float(input('informe o segundo valor:\n'))

if num1 > num2:
    print(f'Os numeros informados são: {num1} e {num2}')
elif num2 > num1:
    print(f'OS numeros informados são: {num2} e {num1}')