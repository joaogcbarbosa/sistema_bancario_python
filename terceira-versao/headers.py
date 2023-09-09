def titulo():
    print('=' * 34)
    print('BANCO'.center(34))
    print('=' * 34)


def menu_com_usuario():
    print('''
[0] - DEPÓSITO
[1] - SAQUE
[2] - EXTRATO
[3] - CRIAR CONTA CORRENTE
[4] - LISTAR CONTAS
[5] - INFORMAÇÕES DO USUÁRIO
[6] - ENCERRAR SESSÃO
[7] - SAIR
        ''')

    return int(input('Insira o número correspondente a operação que deseja realizar: '))


def menu_sem_usuario():
    print('''
[0] - CRIAR USUÁRIO
[1] - SAIR
        ''')

    return int(input('Insira o número correspondente a operação que deseja realizar: '))
