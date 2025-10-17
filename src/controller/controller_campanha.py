from datetime import date, datetime
from controller.controller_pessoa import Controller_Pessoa
from model.campanha import Campanha
from conexion.connection import PostgresQueries
from model.pessoa import Pessoa


class Controller_Campanha:
    def __init__(self):
        self.control_pessoa = Controller_Pessoa()

    def inserir_campanha(self) -> Campanha:
        from controller.controller_formaPagamento import Controller_FormaPagamento
        postGree = PostgresQueries()

        self.listar_campanhas_pessoas(postGree, need_connect=True)
        print()

        cpf_pessoa = str(input("Digite o CPF da Pessoa: "))
        pessoa = self.validar_pessoa(postGree, cpf_pessoa)
        if pessoa == None:
            return None

        id_pessoa = int(pessoa.get_id_pessoa())

        nome = str(input("Informe o nome da Campanha: "))
        descricao = str(input("Descrição da Campanha: "))

        data_i = input("Data de início(dd/mm/aaaa): ")
        data_inicio = datetime.strptime(data_i, "%d/%m/%Y").date()

        data_f = input("Data de término(dd/mm/aaaa): ")
        data_fim = datetime.strptime(data_f, "%d/%m/%Y").date()

        forma_de_pagamento = str(
            input("Informa a forma de Pagamento(obs* Apenas uma): "))

        cursor = postGree.connect()
        cursor.execute("SELECT nextval('CAMPANHA_ID_CAMPANHA_SEQ')")
        id_campanha_pk = cursor.fetchone()[0]


        dado = dict(id_campanha=id_campanha_pk, id_pessoa=id_pessoa, nome=nome,
                    descricao=descricao, data_inicio=data_inicio, data_fim=data_fim, forma_de_pagamento=forma_de_pagamento)
        cursor.execute("""
        INSERT INTO Campanha (id_campanha, id_pessoa, nome, descricao, data_inicio, data_fim, formapagamento) 
        VALUES (%(id_campanha)s, %(id_pessoa)s, %(nome)s, %(descricao)s, %(data_inicio)s, %(data_fim)s, %(forma_de_pagamento)s);         
        """, dado)

        postGree.conn.commit()

        nova_campanha = Campanha(id_campanha_pk, pessoa, nome, descricao, data_inicio, data_fim, forma_de_pagamento)

        """tenho que criar a forma Pagamento só depois de ter criado a Campanha, se não dá conflito"""
        control_formaPagamento = Controller_FormaPagamento()
        formaPagamento_obj = control_formaPagamento.inserir_formaPagamento(
            postGree, nova_campanha)

        if formaPagamento_obj is None:
            print("Erro ao adicionar a forma de pagamento")
            return None
        
        print("\nCampanha criada com sucesso!")
        print(nova_campanha.toString())

        return nova_campanha

    def atualizar_campanha(self) -> Campanha:
        postGree = PostgresQueries(can_write=True)
        postGree.connect()
        from controller.controller_formaPagamento import Controller_FormaPagamento

        id_campanha = int(input("Informe o ID da Campanha que irá alterar: "))

        if self.verifica_existencia_campanha(postGree, id_campanha):

            cpf_pessoa = str(input("Digite o CPF da Pessoa Responsável: "))
            pessoa = self.validar_pessoa(postGree, cpf_pessoa)
            if pessoa == None:
                return None

            id_pessoa_respon = pessoa.get_id_pessoa()

            df_campanha = postGree.sqlToDataFrame(
                f"select id_campanha, id_pessoa, nome, descricao, data_inicio, data_fim, formaPagamento from campanha where id_campanha = {id_campanha}")
            
            if df_campanha.empty:
                print("Erro: Campanha não encontrada após verificação de existência.")
                return None
            
            nome = df_campanha.nome[0]
            descricao = df_campanha.descricao[0]
            data_inicio = df_campanha.data_inicio[0]
            data_fim = df_campanha.data_fim[0]
            formaPagamento = df_campanha.formapagamento[0]

            if (input("Você quer alterar o nome da Campanha?(s/n) ").lower() == "s"):
                nome = str(input("Informe o nome da Campanha: "))

            if (input("Você quer alterar a descrção da Campanha?(s/n) ").lower() == "s"):
                descricao = str(input("Descrição da Campanha: "))

            if (input("Você quer alterar a data de início da Campanha?(s/n) ").lower() == "s"):
                data_i = input("Data de início(dd/mm/aaaa): ")
                data_inicio = datetime.strptime(data_i, "%d/%m/%Y").date()

            if (input("Você quer alterar a data de término da Campanha?(s/n) ").lower() == "s"):
                data_f = input("Data de término(dd/mm/aaaa): ")
                data_fim = datetime.strptime(data_f, "%d/%m/%Y").date()

            if (input("Você quer alterar a forma de pagamento da Campanha?(s/n) ").lower() == "s"):
                formaPagamento = str(
                    input("Informe a Forma de Pagamento(obs* Apenas uma): "))
                control_formaPagamento = Controller_FormaPagamento()
                formaPagamento_obj = control_formaPagamento.atualizar_formaPagamento(
                    id_campanha, id_pessoa_respon, formaPagamento)

                if formaPagamento_obj is None:
                    print("Erro ao adicionar a forma de pagamento")
                    return None

            postGree.write(
                f"update Campanha set id_pessoa = {id_pessoa_respon}, nome = '{nome}', descricao = '{descricao}', data_inicio = '{data_inicio}', data_fim = '{data_fim}', formaPagamento = '{formaPagamento}' where id_campanha = {id_campanha}")

            campanha_atualizada = Campanha(
                id_campanha, pessoa, nome, descricao, data_inicio, data_fim, formaPagamento)
            print(campanha_atualizada.toString())

            return campanha_atualizada
        else:
            print(f"A campanha de ID {id_campanha} não existe.")
            return None

    def desativar_campanha(self):
        postGree = PostgresQueries(can_write=True)
        postGree.connect()

        id_campanha = int(
            input("Informe o ID da Campanha que irá desativar: "))

        if self.verifica_existencia_campanha(postGree, id_campanha):
            df_campanha = postGree.sqlToDataFrame(
                f"select id_pessoa, nome, descricao, data_inicio, data_fim, formaPagamento from campanha where id_campanha = {id_campanha}")

            if df_campanha.empty:
                print("Campanha não encontrada, apesar da verificação de existência.")
                return None
            
            id_pessoa = df_campanha.id_pessoa.values[0]
            sql_cpf = f"select cpf from Pessoa where id_pessoa = {id_pessoa}"
            df_pessoa = postGree.sqlToDataFrame(sql_cpf)

            if df_pessoa.empty:
                print("Pessoa responsável não encontrada.")
                return None
            

            cpf_pessoa = df_pessoa.cpf.values[0]
            pessoa = self.validar_pessoa(postGree, cpf_pessoa)

            opcao_desativar = input(
                f"Tem certeza que deseja desativar a campanha {id_campanha} [S ou N]? ")
            if opcao_desativar.lower() == "s":
                postGree.write(
                    f"update Campanha set status = False where id_campanha = {id_campanha}")
                campanha_desativada = Campanha(id_campanha, pessoa, df_campanha.nome[0], df_campanha.descricao[
                                               0], df_campanha.data_inicio[0], df_campanha.data_fim[0], df_campanha.formapagamento[0])
                
                campanha_desativada.desativar()

                print("Campanha desativada com Sucesso!")
                print(campanha_desativada.toString())
                return campanha_desativada
            return None

        else:
            print(
                f"A campanha de ID {id_campanha} não existe ou está inativa.")
            return None

    def verifica_existencia_campanha(self, postGree: PostgresQueries, id_campanha: int = None) -> bool:
        df_campanha = postGree.sqlToDataFrame(
            f"select id_campanha from Campanha where id_campanha = {id_campanha} and status = TRUE")
        return not df_campanha.empty

    def listar_campanhas_pessoas(self, postGree: PostgresQueries, need_connect: bool = False):
        query = """
        SELECT 
            c.id_campanha,
            c.nome AS nome_campanha,
            c.descricao,
            c.data_inicio,
            c.data_fim,
            c.status,
            d.id_doacao,
            p.nome AS nome_doador,
            d.valor AS valor_doacao,
            c.formapagamento AS forma_pagamento_campanha
        FROM campanha c
        INNER JOIN doacao d ON c.id_campanha = d.id_campanha
        INNER JOIN pessoa p ON d.id_pessoa = p.id_pessoa
        LEFT JOIN formapagamento fp ON c.id_campanha = fp.id_campanha
        ORDER BY c.data_inicio DESC, nome_campanha, d.data_doacao;
        """
        if need_connect:
            postGree.connect()
        print(postGree.sqlToDataFrame(query))

    def validar_pessoa(self, postGree: PostgresQueries, cpf_pessoa: str = None) -> Pessoa:
        if not self.control_pessoa.verifica_existencia_pessoa(postGree, cpf_pessoa):
            print(f"A pessoa de CPF: {cpf_pessoa} informado não existe.")
            return None

        postGree.connect()
        df_pessoa = postGree.sqlToDataFrame(
            f"select id_pessoa, nome, cpf, email, senha, tipo_pessoa from Pessoa where cpf = '{cpf_pessoa}'")

        if df_pessoa.empty:
            print("Erro interno: Pessoa não encontrada.")
            return None

        pessoa = Pessoa(df_pessoa.id_pessoa.values[0], df_pessoa.nome.values[0], cpf_pessoa,
                        df_pessoa.email.values[0], df_pessoa.senha.values[0], df_pessoa.tipo_pessoa.values[0])

        return pessoa
