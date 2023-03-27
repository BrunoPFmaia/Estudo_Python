# Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e
# escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior
# ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

conta = float(input('informe o número da conta:\n'))
sal = float(input('informe o saldo:\n'))
deb = float(input('informe o débito:\n'))
cred = float(input('informe o crédito:\n'))

saldo_at = sal - deb + cred

if saldo_at >= 0:
    print('Saldo positivo')
elif saldo_at < 0:
    print('Saldo negativo')
