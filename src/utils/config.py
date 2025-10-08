import os
from time import sleep

MENU_PRINCIPAL = """
================== MENU PRINCIPAL ==================
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Excluir Registros
5 - Sair
===================================================="""

MENU_RELATORIOS = """
-- Menu de Relatórios --
1 - Relatório de Campanhas
2 - Relatório de Pessoas com Endereço
"""

MENU_ENTIDADES = """
-- Escolha uma entidade --
1 - Pessoa
2 - Endereço
3 - Campanha
"""

QUERY_COUNT = 'SELECT COUNT(1) AS total_{tabela} FROM {tabela}'

def clear_console(wait_time:int=1):
    sleep(wait_time)
    os.system('cls' if os.name == 'nt' else 'clear')