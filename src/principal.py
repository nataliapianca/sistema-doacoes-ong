from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_pessoa import Controller_Pessoa
from controller.controller_campanha import Controller_Campanha
from controller.valida_login import ValidaLogin  
from controller.controller_doacao import Controller_Doacao
from controller.controller_formaPagamento import Controller_FormaPagamento
from conexion.connection import PostgresQueries

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_pessoa = Controller_Pessoa()
ctrl_campanha = Controller_Campanha()
ctrl_doacao = Controller_Doacao()
ctrl_formaPagamento = Controller_FormaPagamento()
login = ValidaLogin()
postGree = PostgresQueries()

def reports(opcao_relatorio: int = 0):
    if opcao_relatorio == 1:
        relatorio.get_relatorio_campanhas()
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_doacoes()

def inserir(opcao_inserir: int = 0):
    if opcao_inserir == 1:
        if tipo_usuario == "doador":
            print("❌ Acesso negado: doadores não podem criar pessoas.")
            return
        ctrl_pessoa.inserir_pessoa()
    elif opcao_inserir == 2:
        if tipo_usuario == "doador":
            print("❌ Acesso negado: doadores não podem criar campanhas.")
            return
        relatorio.get_relatorio_campanhas()
        ctrl_campanha.inserir_campanha()
    elif opcao_inserir == 3:
        relatorio.get_relatorio_doacoes()
        ctrl_doacao.inserir_doacao()

def atualizar(opcao_atualizar: int = 0):
    if opcao_atualizar == 1:
        relatorio.get_relatorio_pessoas()
        ctrl_pessoa.atualizar_pessoa()
    elif opcao_atualizar == 2:
        if tipo_usuario == "doador":
            print("❌ Acesso negado: doadores não podem atualizar campanhas.")
            return
        relatorio.get_relatorio_campanhas()
        ctrl_campanha.atualizar_campanha()
    elif opcao_atualizar == 3:
        ctrl_doacao.listar_doacoes(postGree, need_connect=True)
        ctrl_doacao.atualizar_doacao()
    elif opcao_atualizar == 4:
        if tipo_usuario == "doador":
            print("❌ Acesso negado: doadores não podem atualizar a forma de pagamento de uma campanha.")
            return
        ctrl_formaPagamento.listar_campanhas_formaPag(postGree, need_connect=True)
        ctrl_formaPagamento.executar_atualizar_formaPagamento(postGree)

def excluir(opcao_excluir: int = 0):
    if opcao_excluir == 1:
        if tipo_usuario == "usuario":
            relatorio.get_relatorio_pessoas()
        
        ctrl_pessoa.excluir_pessoa()
        
    elif opcao_excluir == 2:
        if tipo_usuario == "doador":
            print("❌ Acesso negado: doadores não podem desativar campanhas.")
            return
        relatorio.get_relatorio_campanhas()
        ctrl_campanha.desativar_campanha()
    elif opcao_excluir == 3:
        if tipo_usuario == "doador":
            print("❌ Acesso negado: doadores não podem excluir doações.")
            return
        ctrl_doacao.listar_doacoes(postGree, need_connect=True)
        ctrl_doacao.excluir_doacao()

def run():
    print(tela_inicial.get_updated_screen())
    input("\nPressione Enter para continuar...")
    config.clear_console()

    #  Etapa de Login ou Cadastro
tipo_usuario, nome_usuario = login.iniciar_programa()


while True:
    print(config.MENU_PRINCIPAL)

    try:
        opcao = int(input("Escolha uma opção [1-5]: "))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        continue

    config.clear_console()

    if opcao == 1:
        print(config.MENU_RELATORIOS)
        try:
            opcao_relatorio = int(input("Escolha uma opção: "))
            reports(opcao_relatorio)
        except ValueError:
            print("Entrada inválida.")

    elif opcao == 2:  # Inserir
        print(config.MENU_ENTIDADES)
        try:
            opcao_inserir = int(input("Escolha uma opção: "))
            inserir(opcao_inserir)
        except ValueError:
            print("Entrada inválida.")

    elif opcao == 3:  # Atualizar
        print(config.MENU_ATUALIZAR_ENTIDADES)
        try:
            opcao_atualizar = int(input("Escolha uma opção: "))
            atualizar(opcao_atualizar)
        except ValueError:
            print("Entrada inválida.")

    elif opcao == 4:  # Excluir
        print(config.MENU_ENTIDADES)
        try:
            opcao_excluir = int(input("Escolha uma opção: "))
            excluir(opcao_excluir)
        except ValueError:
            print("Entrada inválida.")

    elif opcao == 5:
        print("Obrigado por utilizar o sistema!")
        exit(0)

    else:
        print("Opção inválida. Tente novamente.")

    input("\nPressione Enter para continuar...")
    config.clear_console()

    if __name__ == "__main__":
        run()
