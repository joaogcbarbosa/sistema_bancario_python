def verifica_usuario(usuarios, cpf):
    if not verifica_cpf(usuarios, cpf):
        return
    else:
        print('Nenhuma conta vinculada. Primeiro crie um usuário:')
        criar_usuario(usuarios)
        return


def verifica_cpf(usuarios, cpf):

    for u in usuarios:
        if u['CPF'] == cpf:
            return False

    return True


def criar_usuario(usuarios):
    cpf = input('CPF (somente números): ').strip()

    if verifica_cpf(usuarios, cpf):
        nome = input('Nome: ').strip().upper()
        nascimento = input('Data de Nascimento (dd/mm/aa): ').strip()
        endereco = input('Logradouro - número, bairro, cidade - sigla UF: ').strip().upper()

        usuarios.append({'Nome': nome,
                         'Data de Nascimento': nascimento,
                         'Endereço': endereco,
                         'CPF': cpf})

        print('Usuário criado com sucesso.')

    else:
        print(f'O CPF {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]} já consta como cadastrado.')


def criar_cc(usuarios, contas, numero_conta, agencia):
    cpf = input('Informe seu CPF (somente números) para checar se já existe alguma conta vinculada: ')

    verifica_usuario(usuarios, cpf)

    usuario = input('Usuário: ').strip().upper()
    numero_conta += 1
    contas.append({'Usuário': usuario,
                   'Número da Conta': numero_conta,
                   'Agência': agencia})

    print('Conta criada com sucesso.')

    return contas, numero_conta


def listar_contas(contas):
    for conta in contas:
        print('=~' * 10)
        for k, v in conta.items():
            print(f'{k}: {v}')
        print('=~'* 10)


def depositar(saldo, valor, extrato, /):
    if valor < 0:
        print('Operação inválida.')
    else:
        saldo += valor
        extrato += f'Depósito: R${valor:.2f}\n'
        print(f'Valor de R${valor:.2f} depositado.')

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, limite_saques):
    if saldo < valor:
        print('Saldo insuficiente.')
    elif valor > limite:
        print('Limite de saque de R$500,00')
    elif valor < 0:
        print('Impossível sacar valores menores que R$0,00')
    elif limite_saques <= 0:
        print('Limite diário de saques atingido.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R${valor:.2f}\n'
        limite_saques -= 1
        print(f'Valor de R${valor:.2f} sacado.')
    else:
        print('Operação inválida.')

    return saldo, extrato, limite_saques


def exibir_extrato(saldo, /, *, extrato):
    print('=~' * 10)
    print(f'{"EXTRATO": ^20}')
    print('~=' * 10)
    print('Nenhuma movimentação' if not extrato else extrato)
    print(f'Saldo: R${saldo:.2f}')
    print('=~' * 10)

    return extrato


def menu():
    print('''
    [0] - DEPÓSITO
    [1] - SAQUE
    [2] - EXTRATO
    [3] - CRIAR USUÁRIO
    [4] - CRIAR CONTA CORRENTE
    [5] - LISTAR CONTAS
    [6] - SAIR
        ''')

    return int(input())


def main():

    numero_conta = 0
    AGENCIA = '0001'
    LIMITE_SAQUES = 3
    saldo = 0
    extrato = ''
    limite = 500
    usuarios = []
    contas = []

    while True:

        escolha = menu()

        if escolha == 0:
            valor = float(input('Valor do depósito: R$'))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif escolha == 1:
            valor = float(input('Valor a sacar: R$'))

            saldo, extrato, LIMITE_SAQUES = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                limite_saques=LIMITE_SAQUES
            )

        elif escolha == 2:

            exibir_extrato(saldo, extrato=extrato)

        elif escolha == 3:
            criar_usuario(usuarios)

        elif escolha == 4:
            contas, numero_conta = criar_cc(usuarios, contas, numero_conta, AGENCIA)

        elif escolha == 5:
            listar_contas(contas)

        elif escolha == 6:
            print('Volte sempre.')
            break

        else:
            print('Operação inválida.')


main()
