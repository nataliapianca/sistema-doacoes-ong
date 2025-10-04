class Relatorio:
    def __init__(self):
        with open("sql/relatorio_pessoas.sql") as f:
            self.query_relatorio_pessoas = f.read()

        with open("sql/relatorio_doacoes.sql") as f:
            self.query_relatorio_doacoes = f.read()

        with open("sql/relatorio_campanhas.sql") as f:
            self.query_relatorio_campanhas = f.read()

"""falta terminar os metodos de relatorio, pra isso tem q mexer no controller"""