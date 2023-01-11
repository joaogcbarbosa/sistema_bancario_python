from abc import ABC
from abc import abstractmethod
from random import randint


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @property
    def endereco(self):
        return self._endereco

    @property
    def contas(self):
        dados = ''
        if not self._contas:
            dados += '\nNENHUMA CONTA VINCULADA AO CPF INFORMADO.'
        else:
            for conta in self._contas:
                dados += f'\n{"-" * 18}\n'
                for k, v in conta.items():
                    dados += f'{k}: {v}\n'

        return dados

    def adicionar_conta(self, conta):
        self._contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @property
    def data_nascimento(self):
        return self._data_nascimento


class Conta(ABC):
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @property
    @abstractmethod
    def saldo(self):
        ...

    @property
    @abstractmethod
    def numero(self):
        ...

    @property
    @abstractmethod
    def agencia(self):
        ...

    @property
    @abstractmethod
    def cliente(self):
        ...

    @property
    @abstractmethod
    def historico(self):
        ...

    @abstractmethod
    def sacar(self, valor):
        ...

    @abstractmethod
    def depositar(self, valor):
        ...


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500.00, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        Cliente.adicionar_conta(cliente, {
            'Número': numero,
            'Limite': f'R${limite:.2f}',
            'Limite de Saque': limite_saques,
            'Agência': self.agencia
        })

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        extrato = ''
        if not self._historico.transacoes:
            extrato += '\nNENHUMA MOVIMENTAÇÃO REALIZADA.\n'
        else:
            for t in self._historico.transacoes:
                extrato += f'{"-" * 18}\n'
                for k, v in t.items():
                    extrato += f'{k}: {v}\n'

        extrato += f'{"-" * 18}\nSALDO DISPONÍVEL: R${self.saldo:.2f}'

        return extrato

    @property
    def limite(self):
        return self._limite

    @property
    def limite_saques(self):
        return self._limite_saques

    def sacar(self, valor):
        if self.limite_saques == 0:
            return f'\nLIMITE DE SAQUES DIÁRIOS ATINGIDO.'
        elif self.saldo < valor:
            return f'\nVALOR EXCEDE O SALDO DE R${self.saldo:.2f}.'
        elif valor < 0:
            return '\nVALOR NEGATIVO INSERIDO.'
        elif valor > self.limite:
            return f'\nVALOR EXCEDE O LIMITE DE OPERAÇÃO DE R${self.limite:.2f} DESSA CONTA.'
        else:
            self._limite_saques -= 1
            self._saldo -= valor
            self._historico.adicionar_transacao('Saque', f'R${valor:.2f}')
            return f'\nSAQUE DE R${valor:.2f} REALIZADO DA CONTA {self.numero}.'

    def depositar(self, valor):
        if valor <= 0:
            return '\nVALOR NEGATIVO INSERIDO.'
        elif valor > self.limite:
            return f'\nVALOR EXCEDE O LIMITE DE OPERAÇÃO DE R${self.limite:.2f} DESSA CONTA.'
        else:
            self._saldo += valor
            self._historico.adicionar_transacao('Depósito', f'R${valor:.2f}')
            return f'\nDEPÓSITO DE R${valor:.2f} REALIZADO NA CONTA {self.numero}.'


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao, valor):
        self.transacoes.append({
            'Tipo': transacao,
            'Valor': valor
        })


def verifica_cpf(usuarios, cpf):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario

    return False


def gera_nro_conta():
    nro_conta = str(randint(100, 999)) + '-' + str(randint(0, 9))
    return nro_conta


def criar_usuario(usuarios, cpf):
    if not verifica_cpf(usuarios, cpf):
        nome = input('Nome: ').strip().upper()
        nascimento = input('Data de Nascimento (dd/mm/aa): ').strip()
        endereco = input('Logradouro - número, bairro, cidade - sigla UF: ').strip().upper()

        usuarios.append(PessoaFisica(endereco, cpf, nome, nascimento))

        print('\nUSUÁRIO CRIADO COM SUCESSO.')


def criar_cc(usuarios, contas, cpf):
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


def listar_contas(usuarios, cpf):
    usuario = verifica_cpf(usuarios, cpf)
    print(f'{usuario.contas}')


def operacao(tipo_operacao, contas, cpf):
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


def depositar(contas, cpf):
    operacao(ContaCorrente.depositar, contas, cpf)


def sacar(contas, cpf):
    operacao(ContaCorrente.sacar, contas, cpf)


def exibir_extrato(contas, cpf):
    operacao(ContaCorrente.historico, contas, cpf)


def informacoes_usuario(usuarios, cpf):
    usuario = verifica_cpf(usuarios, cpf)
    print(f'\nCPF: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}\nNome: {usuario.nome}'
          f'\nNascimento: {usuario.data_nascimento}\nEndereço: {usuario.endereco}\n')


def encerrar_sessao(usuarios, cpf):
    usuario = verifica_cpf(usuarios, cpf)
    print(f'\nSESSÃO DE {usuario.nome} ENCERRADA.\n')


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


def main():
    nova_sessao = False
    cpf = input('Informe seu CPF (somente números): ')

    while True:
        if verifica_cpf(lista_usuarios, cpf):
            escolha = menu_com_usuario()

            if escolha == 0:
                depositar(lista_contas, cpf)
            elif escolha == 1:
                sacar(lista_contas, cpf)
            elif escolha == 2:
                exibir_extrato(lista_contas,cpf)
            elif escolha == 3:
                criar_cc(lista_usuarios, lista_contas, cpf)
            elif escolha == 4:
                listar_contas(lista_usuarios, cpf)
            elif escolha == 5:
                informacoes_usuario(lista_usuarios, cpf)
            elif escolha == 6:
                encerrar_sessao(lista_usuarios, cpf)
                nova_sessao = True
                break
            elif escolha == 7:
                break
            else:
                print('\nOPERAÇÃO INVÁLIDA.')

        else:
            escolha = menu_sem_usuario()

            if escolha == 0:
                criar_usuario(lista_usuarios, cpf)
            elif escolha == 1:
                break
            else:
                print('\nOPERAÇÃO INVÁLIDA.')

    if nova_sessao:
        titulo()
        main()


lista_usuarios = []
lista_contas = []
titulo()
main()
