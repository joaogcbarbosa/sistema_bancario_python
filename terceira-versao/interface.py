from helpers import operacao, gera_nro_conta, verifica_cpf
from models import ContaCorrente


def depositar(contas: list, cpf: str):
    operacao(ContaCorrente.depositar, contas, cpf)


def sacar(contas: list, cpf: str):
    operacao(ContaCorrente.sacar, contas, cpf)


def exibir_extrato(contas: list, cpf: str):
    operacao(ContaCorrente.historico, contas, cpf)


def criar_cc(usuarios: list, contas: list, cpf: str):
    nro_conta = gera_nro_conta()

    usuario = verifica_cpf(usuarios, cpf)
    while True:
        escolha = input('\nDeseja mudar o Limite padrão de operação e saque de R$500,00 e 3 saques por dia? ['
                        'S/N] ').strip().upper()[0]
        if escolha in 'S':
            limite = float(input('\nNovo limite de operações: R$'))
            limite_saques = int(input('Novo limite de saques: '))
            contas.append(ContaCorrente(nro_conta, usuario, limite, limite_saques))
            break
        elif escolha in 'N':
            contas.append(ContaCorrente(nro_conta, usuario))
            break
        else:
            print('\nCOMANDO INVÁLIDO.')
            continue

    print(f'\nCONTA CRIADA COM SUCESSO.\nO NÚMERO DA CONTA É {nro_conta}')


def listar_contas(usuarios: list, cpf: str):
    usuario = verifica_cpf(usuarios, cpf)
    print(f'{usuario.contas}')


def informacoes_usuario(usuarios: list, cpf: str):
    usuario = verifica_cpf(usuarios, cpf)
    print(f'\nCPF: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}\nNome: {usuario.nome}'
          f'\nNascimento: {usuario.data_nascimento}\nEndereço: {usuario.endereco}\n')


def encerrar_sessao(usuarios: list, cpf: str):
    usuario = verifica_cpf(usuarios, cpf)
    print(f'\nSESSÃO DE {usuario.nome} ENCERRADA.\n')
