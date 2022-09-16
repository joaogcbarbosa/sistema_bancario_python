print('=~'*10)
print(f'{"Banco DIO": ^20}')
print('~='*10)

saldo = 0
LIMITE_SAQUE = 3
extrato = ''

while True:
    print('''
[0] - DEPÓSITO
[1] - SAQUE
[2] - EXTRATO
[3] - SAIR
    ''')

    escolha = int(input('Qual operação deseja realizar? '))

    if escolha == 0:
        deposito = float(input('Valor do depósito: R$'))

        while deposito < 0:
            print('Não é possível depositar um valor negativo. Tente novamente.')
            deposito = float(input('Valor do depósito: R$'))

        saldo += deposito
        extrato += f'Depósito: R${deposito:.2f}\n'
        print(f'Valor de R${deposito:.2f} depositado.')

    elif escolha == 1:
        if LIMITE_SAQUE > 0:

            saque = float(input('Valor a sacar: R$'))

            if saque > saldo:
                print(f'Seu saldo é de R${saldo:.2f}. Não foi possível realizar o saque de R${saque:.2f}')
                continue

            elif saque < 0:
                print('Não é possível sacar um valor negativo.')
                continue

            elif saque > 500.00:
                print('Não é possível sacar valores maiores que R$500.00')
                continue

            LIMITE_SAQUE -= 1
            saldo -= saque
            extrato += f'Saque: R${saque:.2f}\n'
            print(f'Valor de R${saque:.2f} sacado.')

        else:
            print('Limite de saque diário atingido. Tente novamente amanhã.')

    elif escolha == 2:
        print('=~' * 10)
        print(f'{"EXTRATO": ^20}')
        print('~=' * 10)
        print('Nenhuma movimentação' if not extrato else extrato)
        print(f'Saldo: R${saldo:.2f}')
        print('=~' * 10)

    elif escolha == 3:
        print('Volte sempre.')
        break

    else:
        print('Operação inválida. Tente novamente.')

print('Programa encerrado.')
