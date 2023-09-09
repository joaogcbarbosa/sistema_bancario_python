from random import randint
from models import PessoaFisica, ContaCorrente


def verifica_cpf(usuarios: list[PessoaFisica], cpf: str) -> PessoaFisica | bool:
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario

    return False


def gera_nro_conta() -> str:
    nro_conta = str(randint(100, 999)) + '-' + str(randint(0, 9))
    return nro_conta


def criar_usuario(usuarios: list, cpf: str):
    if not verifica_cpf(usuarios, cpf):
        nome = input('Nome: ').strip().upper()
        nascimento = input('Data de Nascimento (dd/mm/aa): ').strip()
        endereco = input('Logradouro - número, bairro, cidade - sigla UF: ').strip().upper()

        usuarios.append(PessoaFisica(endereco, cpf, nome, nascimento))

        print('\nUSUÁRIO CRIADO COM SUCESSO.')


def operacao(tipo_operacao: ContaCorrente.historico, contas: list, cpf: str):
    contas_vinculadas = [conta for conta in contas if conta.cliente.cpf == cpf]
    tot_contas_vinculadas = len(contas_vinculadas)
    nros_contas_vinculadas = ", ".join([f"{contas_vinculadas[i].numero}" for i in range(len(contas_vinculadas))])

    if tot_contas_vinculadas == 0:
        print('\nNENHUMA CONTA CONSTA NO CPF INFORMADO.')

    elif tot_contas_vinculadas == 1:
        if tipo_operacao == ContaCorrente.depositar:
            valor = float(input('Valor do depósito: R$'))
            print(tipo_operacao(contas_vinculadas[0], valor))
        elif tipo_operacao == ContaCorrente.sacar:
            valor = float(input('Valor do saque: R$'))
            print(tipo_operacao(contas_vinculadas[0], valor))
        else:
            print(contas_vinculadas[0].historico)

    elif tot_contas_vinculadas > 1:
        print(f'\nNESTE CPF ESTÃO VINCULADAS AS CONTAS {nros_contas_vinculadas}')
        escolha = input('EM QUAL DELAS GOSTARIA DE REALIZAR A OPERACAO? DIGITAR NO FORMATO XXX-X: ')
        for i in range(len(contas_vinculadas)):
            if escolha in contas_vinculadas[i].numero:
                if tipo_operacao == ContaCorrente.depositar:
                    valor = float(input('Valor do depósito: R$'))
                    print(tipo_operacao(contas_vinculadas[i], valor))
                    return
                elif tipo_operacao == ContaCorrente.sacar:
                    valor = float(input('Valor do saque: R$'))
                    print(tipo_operacao(contas_vinculadas[i], valor))
                    return
                elif tipo_operacao == ContaCorrente.historico:
                    print(contas_vinculadas[i].historico)
                    return
                else:
                    print('\nCONTA NÃO IDENTIFICADA. OPERACAO NÃO FOI REALIZADA')
                    return
