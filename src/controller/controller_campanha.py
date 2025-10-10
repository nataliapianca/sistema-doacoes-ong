from datetime import date, datetime
from controller_pessoa import Controller_Pessoa
from model.campanha import Campanha
from conexion.connection import PostgresQueries
from model.pessoa import Pessoa


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
        

        nome = str(input("Informe o nome da Campanha: "))
        decricao = str(input("Descrição da Campanha: "))

        data_i = input("Data de início(dd/mm/aaaa): ")
        data_inicio = datetime.strptime(data_i, "%d/%m/%Y").date()

        data_f = input("Data de término(dd/mm/aaaa): ")
        data_fim = datetime.strptime(data_f, "%d/%m/%Y").date()
        
        formaPagamento = str(input("Informa a forma de Pagamento(obs* Apenas uma): "))

        cursor = postGree.connect()
        output_value = cursor.var(int)

        dado = dict(id=output_value, nome=nome,cpf_pessoa=int(pessoa.get_cpf()), data_inicio=data_inicio, data_fim=data_fim, formaPagamento=formaPagamento)
        cursor.execute("""
        begin
            :codigo := CAMPANHA_ID_CAMPANHA_SEQ.NEXTVAL;
            insert into campanha values(:ID, :nome, :cpf_pessoa, data_inicio, :data_fim, :formaPagamento);
        end;          
        """, dado)

        id = output_value.getvalue()
        postGree.conn.commit()
        df_campanha = postGree.sqlToDataFrame(f"select id, cpf_pessoa, data_inicio, data_fim, formaPagamento from campanha where id = {id}")

        nova_campanha = Campanha(df_campanha.id[0], df_campanha.nome[0], df_campanha.cpf_pessoa[0], df_campanha.data_inicio[0], df_campanha.data_fim[0], df_campanha.formaPagamento[0], pessoa)

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
            
            data_i = input("Data de início(dd/mm/aaaa): ")
            data_inicio = datetime.strptime(data_i, "%d/%m/%Y").date()

            data_f = input("Data de término(dd/mm/aaaa): ")
            data_fim = datetime.strptime(data_f, "%d/%m/%Y").date()

            formaPagamento = str(input("Informe a Forma de Pagamento(obs* Apenas uma): "))

            postGree.write(f"update campanha set cpf_pessoa = {cpf_pessoa}, data_inicio = {data_inicio}, data_fim = {data_fim}, formaPagamento = {formaPagamento}")

            df_campanha = postGree.sqlToDataFrame(f"select id, cpf_pessoa, data_inicio, data_fim, formaPagamento from campanha where id = {cpf_pessoa}")

            campanha_atualizada = Campanha(df_campanha.id[0], df_campanha.nome[0], df_campanha.cpf_pessoa[0], df_campanha.data_inicio[0], df_campanha.data_fim[0], df_campanha.formaPagamento[0], pessoa)
            print(campanha_atualizada.toString())

            return campanha_atualizada
        else:
            print(f"A campanha de ID {id_campanha} não existe.")
            return None
        

    def excluir_campanha(self):
        postGree = PostgresQueries(can_write=True)
        postGree.connect  

        id_campanha = int(input("Informe o ID da Campanha que irá alterar: "))

        if self.verifica_existencia_campanha(postGree, id_campanha):
            df_campanha = postGree.sqlToDataFrame(f"select id, cpf_pessoa, data_inicio, data_fim, formaPagamento from campanha where id = {id}")
            pessoa = self.validar_pessoa(postGree, df_campanha.cpf_pessoa.values[0])

            opcao_excluir = input(f"Tem certeza que deseja excluir a campanha {id_campanha} [S ou N]:")
            if opcao_excluir.lower() == "s":
                postGree.write(f"delete from campanha where id_campanha = {id_campanha}")
                campanha_excluida = Campanha(df_campanha.id[0], df_campanha.nome[0], df_campanha.cpf_pessoa[0], df_campanha.data_inicio[0], df_campanha.data_fim[0], df_campanha.formaPagamento[0], pessoa)

                print("Item do Pedido Removido com Sucesso!")
                print(campanha_excluida.toString())


        else:
            print(f"A campanha de ID {id_campanha} não existe.")
            return None
        

    def verifica_existencia_campanha(self, postGree= PostgresQueries, id: int=None) -> bool:
        df_campanha = postGree.sqlToDataFrame(f"select id, cpf_pessoa, data_inicio, data_fim, formaPagamento from campanha where id = {id}")
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
    

    def validar_pessoa(self, postGree= PostgresQueries, id_pessoa: int=None) -> Pessoa:
        if self.control_pessoa.verifica_existencia_pessoa(postGree, id_pessoa):
            print(f"A pessoa {id_pessoa} informada não existe.")
            return None
        else:
            postGree.connect()
            df_pessoa = postGree.sqlToDataFrame(f"select id_pessoa, nome, cpf, email from Pessoa where id_pessoa = {id_pessoa}")
            pessoa = Pessoa(df_pessoa.id_pessoa.values[0], df_pessoa.nome.values[0], df_pessoa.cpf.values[0], df_pessoa.email.values[0])
            return pessoa
    

        
    