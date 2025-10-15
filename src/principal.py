from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_pessoa import Controller_Pessoa
from controller.controller_campanha import Controller_Campanha


tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_pessoa = Controller_Pessoa()
ctrl_campanha = Controller_Campanha()


def reports(opcao_relatorio: int = 0):
    if opcao_relatorio == 1:
        relatorio.get_relatorio_campanhas()
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_doacoes()


def inserir(opcao_inserir: int = 0):
    if opcao_inserir == 1:
        ctrl_pessoa.inserir_pessoa()

    elif opcao_inserir == 2:
        ctrl_campanha.inserir_campanha()


def atualizar(opcao_atualizar: int = 0):
    if opcao_atualizar == 1:
        relatorio.get_relatorio_pessoas()
        ctrl_pessoa.atualizar_pessoa()

    elif opcao_atualizar == 2:
        relatorio.get_relatorio_campanhas()
        ctrl_campanha.atualizar_campanha()


def excluir(opcao_excluir: int = 0):
    if opcao_excluir == 1:
        relatorio.get_relatorio_pessoas()
        ctrl_pessoa.excluir_pessoa()

    elif opcao_excluir == 2:
        relatorio.get_relatorio_campanhas()
        ctrl_campanha.desativar_campanha()


def run():
    print(tela_inicial.get_updated_screen())

    input("\nPressione Enter para continuar...")
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)

        try:

            opcao = int(input("Escolha uma opção [1-5]: "))

        except ValueError:

            print("Entrada inválida. Por favor, digite um número.")
            continue

        config.clear_console()

        if opcao == 1:
            print(config.MENU_RELATORIOS)

            try:
                opcao_relatorio = int(input("Escolha uma opção: "))
                reports(opcao_relatorio)

            except ValueError:
                print("Entrada inválida.")

        elif opcao == 2:
            print(config.MENU_ENTIDADES)

            try:
                opcao_inserir = int(input("Escolha uma opção: "))
                inserir(opcao_inserir)
                config.clear_console()
                print(tela_inicial.get_updated_screen())

            except ValueError:
                print("Entrada inválida.")

        elif opcao == 3:
            print(config.MENU_ENTIDADES)

            try:
                opcao_atualizar = int(input("Escolha uma opção: "))
                atualizar(opcao_atualizar)

            except ValueError:
                print("Entrada inválida.")

        elif opcao == 4:
            print(config.MENU_ENTIDADES)

            try:
                opcao_excluir = int(input("Escolha uma opção: "))
                excluir(opcao_excluir)
                config.clear_console()
                print(tela_inicial.get_updated_screen())

            except ValueError:
                print("Entrada inválida.")

        elif opcao == 5:
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")
        config.clear_console()


if __name__ == "__main__":

    run()
