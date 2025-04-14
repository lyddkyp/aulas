saldo = int(input('digite seu saldo'))
saque = int(input('digite seu saque'))
if saque <= saldo:
    print('transação permitida')
else:
    print('saldo insuficiente')
