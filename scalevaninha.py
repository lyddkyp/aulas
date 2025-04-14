nome = input('digite seu nome')
idade = int(input('digite sua idade'))
if idade >= 18:
    print('cadastro permitido')
else:
    print('cadastro negado')


saldo = int(input('digite seu saldo'))
saque = int(input('digite seu saque'))
if saque <= saldo:
    print('transação permitida')
else:
    print('saldo insuficiente')
