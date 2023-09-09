from abc import ABC, abstractmethod


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
