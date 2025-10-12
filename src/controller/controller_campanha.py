from datetime import date, datetime
from controller_pessoa import Controller_Pessoa
from model.campanha import Campanha
from conexion.connection import PostgresQueries
from model.pessoa import Pessoa
from controller_formaPagamento import Controller_FormaPagamento


class Controller_Campanha:
    def __init__(self):
        self.control_pessoa = Controller_Pessoa()
        

    def inserir_campanha(self) -> Campanha:
        postGree = PostgresQueries()

        self.listar_pessoas(postGree, need_connect= True)
        cpf_pessoa = str(input("Digite o CPF da Pessoa: "))
        pessoa = self.valida_pessoa(postGree, cpf_pessoa)
        if pessoa == None:
            return None
        
        id_pessoa_respon = int(pessoa.get_id_pessoa())

        nome = str(input("Informe o nome da Campanha: "))
        descricao = str(input("Descrição da Campanha: "))

        data_i = input("Data de início(dd/mm/aaaa): ")
        data_inicio = datetime.strptime(data_i, "%d/%m/%Y").date()

        data_f = input("Data de término(dd/mm/aaaa): ")
        data_fim = datetime.strptime(data_f, "%d/%m/%Y").date()

        formaPagamento = str(input("Informa a forma de Pagamento(obs* Apenas uma): "))

        cursor = postGree.connect()
        output_value = cursor.var(int)
        
        cursor.execute("SELECT nextval('CAMPANHA_ID_CAMPANHA_SEQ') AS id", {}, out_vars=[output_value])
        id_campanha_pk = output_value.getvalue()

        control_formaPagamento = Controller_FormaPagamento()
        formaPagamento_obj = control_formaPagamento.inserir_formaPagamentopo(postGree, id_campanha_pk, id_pessoa_respon, formaPagamento)

        if formaPagamento_obj is None:
            print("Erro ao adicionar a forma de pagamento")
            return None
        

        dado = dict(id_campanha=output_value, id_pessoa_respon=id_pessoa_respon, nome=nome, descricao=descricao, data_inicio=data_inicio, data_fim=data_fim, formaPagamento=formaPagamento)
        cursor.execute("""
        begin
            insert into Campanha (id_campanha, id_pessoa, nome, descricao, data_inicio, data_fim values (:id_campanha, :id_pessoa, :nome, :descricao, :data_inicio, :data_fim, :formaPagamento);
        end;          
        """, dado)

        
        postGree.conn.commit()
        df_campanha = postGree.sqlToDataFrame(f"select id_campanha, id_pessoa, nome, descricao, data_inicio, data_fim, formaPagamento from campanha where id_campanha = '{id_campanha_pk}'")

        nova_campanha = Campanha(df_campanha.id_campanha[0], pessoa ,df_campanha.nome[0], df_campanha.descricao[0], df_campanha.data_inicio[0], df_campanha.data_fim[0], df_campanha.formaPagamento[0])

        print(nova_campanha.toString())

        return nova_campanha
    

    def atualizar_campanha(self) -> Campanha:
        postGree = PostgresQueries(can_write=True)
        postGree.connect  

        id_campanha = int(input("Informe o ID da Campanha que irá alterar: "))

        if self.verifica_existencia_campanha(postGree, id_campanha):

            self.listar_pessoas(postGree, need_connect=True)
            cpf_pessoa = str(input("Digite o CPF da Pessoa Responsável: "))
            pessoa = self.validar_pessoa(postGree, cpf_pessoa)
            if pessoa == None:
                return None
            
            id_pessoa_respon = pessoa.get_id_pessoa()

            df_campanha = postGree.sqlToDataFrame(f"select id_campanha, id_pessoa, nome, descricao, data_inicio, data_fim, formaPagamento from campanha where id_campanha = '{id_campanha}'")
            nome = df_campanha.nome[0]
            descricao = df_campanha.descricao[0]
            data_inicio = df_campanha.data_inicio[0]
            data_fim = df_campanha.data_fim[0]
            formaPagamento = df_campanha.formaPagamento[0]


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
                formaPagamento = str(input("Informe a Forma de Pagamento(obs* Apenas uma): "))
                control_formaPagamento = Controller_FormaPagamento()
                formaPagamento_obj = control_formaPagamento.atualizar_formaPagamento(postGree, id_campanha, id_pessoa_respon, formaPagamento)

                if formaPagamento_obj is None:
                    print("Erro ao adicionar a forma de pagamento")
                    return None
        

            postGree.write(f"update Campanha set id_pessoa = '{id_pessoa_respon}', nome = '{nome}', descricao = '{descricao}', data_inicio = '{data_inicio}', data_fim = '{data_fim}', formaPagamento = '{formaPagamento}' where id_campanha = '{id_campanha}'")

            campanha_atualizada = Campanha(df_campanha.id_campanha[0], pessoa, df_campanha.nome[0], df_campanha.descricao[0] ,df_campanha.data_inicio[0], df_campanha.data_fim[0], df_campanha.formaPagamento[0])
            print(campanha_atualizada.toString())

            return campanha_atualizada
        else:
            print(f"A campanha de ID {id_campanha} não existe.")
            return None
        

    def excluir_campanha(self):
        postGree = PostgresQueries(can_write=True)
        postGree.connect  

        id_campanha = int(input("Informe o ID da Campanha que irá excluir: "))

        if self.verifica_existencia_campanha(postGree, id_campanha):
            df_campanha = postGree.sqlToDataFrame(f"select id_campanha, id_pessoa, nome, descricao, data_inicio, data_fim, formaPagamento from campanha where id_campanha = '{id_campanha}'")
            
            id_pessoa = df_campanha.id_pessoa.values[0]
            sql_cpf = f"select cpf from Pessoa where id_pessoa = '{id_pessoa}'"
            df_pessoa = postGree.sqlToDataFrame(sql_cpf)

            cpf_pessoa = df_pessoa.cpf.values[0]
            pessoa = self.validar_pessoa(postGree, cpf_pessoa)

            opcao_excluir = input(f"Tem certeza que deseja excluir a campanha {id_campanha} [S ou N]:")
            if opcao_excluir.lower() == "s":
                postGree.write(f"delete from campanha where id_campanha = '{id_campanha}'")
                campanha_excluida = Campanha(df_campanha.id[0], pessoa, df_campanha.nome[0], df_campanha.descricao[0], df_campanha.data_inicio[0], df_campanha.data_fim[0], df_campanha.formaPagamento[0])

                print("Campanha removida com Sucesso!")
                print(campanha_excluida.toString())


        else:
            print(f"A campanha de ID {id_campanha} não existe.")
            return None
        

    def verifica_existencia_campanha(self, postGree= PostgresQueries, id: int=None) -> bool:
        df_campanha = postGree.sqlToDataFrame(f"select id_campanha, id_pessoa, nome, descricao, data_inicio, data_fim, formaPagamento from campanha where id_campanha = '{id}'")
        return df_campanha.empty
    

    def listar_pessoas(self, postGree= PostgresQueries, need_connect:bool=False):
        query = """
                select id_campanha,
                c.nome as nome_campanha,
                c.data_inicio,
                c.data_fim
                c.status
                d.id_doacao,
                p.nome as nome_doador
                d.valor as valor_doacao,
                fp.formaPagamento as forma_pagamento_campanha
                from Campanha c
                inner join Doacao d ON c.id_campanha = d.id_campanha
                inner join pessoa p ON d.id_pessoa = p.id_pessoa
                left join FormaPagamento fp ON c.id_campanha = fp.id_campanha
                order by c.data_inicio DESC, nome_campanha, d.data_doacao;
                """
        if need_connect:
            postGree.connect()
        print(postGree.sqlToDataFrame(query))
    

    def validar_pessoa(self, postGree, cpf_pessoa: str=None) -> Pessoa:
        if not self.control_pessoa.verifica_existencia_pessoa(postGree, cpf_pessoa):
            print(f"A pessoa de CPF: {cpf_pessoa} informado não existe.")
            return None

        postGree.connect()
        df_pessoa = postGree.sqlToDataFrame(f"select id_pessoa, nome, cpf, email, senha, perfil from Pessoa where cpf = '{cpf_pessoa}'")

        if df_pessoa.empty:
            print("Erro interno: Pessoa encontrada, mas dados não recuperados.")
            return None
        
        pessoa = Pessoa(df_pessoa.id_pessoa.values[0], df_pessoa.nome.values[0], df_pessoa.cpf.values[0], df_pessoa.email.values[0], df_pessoa.senha.values[0], df_pessoa.perfil.values[0])

        return pessoa

        
    