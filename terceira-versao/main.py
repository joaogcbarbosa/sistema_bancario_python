from interface import depositar, sacar, exibir_extrato, criar_cc, listar_contas, informacoes_usuario, encerrar_sessao
from helpers import verifica_cpf, criar_usuario
from headers import menu_sem_usuario, menu_com_usuario, titulo


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
                exibir_extrato(lista_contas, cpf)
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


if __name__ == '__main__':
    lista_usuarios = []
    lista_contas = []
    titulo()
    main()
