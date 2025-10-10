from controller.controller_campanha import Controller_Campanha
from controller.controller_pessoa import Controller_Pessoa
from model.formaPagamento import FormaPagamento
from conexion.connection import PostgresQueries
from model.pessoa import Pessoa
from model.campanha import Campanha

class Controller_FormaPagamento:
    def __init__(self):
        self.control_pessoa = Controller_Pessoa
        self.control_campanha = Controller_Campanha

    def inserir_formaPagamento(self) -> FormaPagamento:
        postGree = PostgresQueries()

        self.listar_campanhas(postGree, need_connect= True)
        id_campanha = str(input("Digite o ID da Campanha: "))
        campanha = self.validar_campanha(postGree, id_campanha)
        if campanha == None:
            return None
        
        self.listar_pessoas(postGree, need_connect= True)
        id_pessoa = str(input("Digite o ID da Pessoa: "))
        

        formaPagamento = str(input("Informa a forma de Pagamento(obs* Apenas uma): "))

        cursor = postGree.connect()
        output_value = cursor.var(int)

        dado = dict(id=output_value, formaPagamento=formaPagamento)
        cursor.execute("""
        begin
            :codigo := CAMPANHA_ID_CAMPANHA_SEQ.NEXTVAL;
            insert into campanha values(:ID, :formaPagamento);
        end;          
        """, dado)

        id = output_value.getvalue()
        postGree.conn.commit()
        df_formaPagamento = postGree.sqlToDataFrame(f"select id, formaPagamento from campanha where id = {id}")

        nova_formaPagamento = FormaPagamento(df_formaPagamento.id[0], df_formaPagamento.formaPagamento[0], campanha, pessoa)

        print(nova_formaPagamento.toString())

        return nova_formaPagamento


    def listar_pessoas(self, postGree= PostgresQueries, need_connect:bool=False):
        query = """
               select id_campanha,
               c.nome as nome_campanha,
               c.data_inicio,
               c.data_fim,
               c.status,
               d.id_doacao,
               p.nome as nome_doador,
               d.valor as valor_doacao,
               d.data_doacao,
               fp.formaPagamento as forma_pagamento_campanha,
               from Campanha c
               inner join Doacao d ON c.id_campanha = d.id_campanha
               inner join pessoa p ON d.id_pessoa = p.id_pessoa
               left join FormaPagamento fp ON d.id_campanha = fp.id_campanha AND d.id_pessoa = fp.id_pessoa
               order by c.data_inicio DESC, nome_campanha, d.data_doacao;
               """
        if need_connect:
           postGree.connect()
        print(postGree.sqlToDataFrame(query))


    def listar_campanhas(self, postGree= PostgresQueries, need_connect:bool=False):
            query = """
                    select fp.id_forma,
                    fp.formapagamento AS forma_de_pagamento,
                    fp.id_campanha,
                    c.nome AS nome_campanha,
                    c.data_inicio,
                    c.status
                    from FormaPagamento fp
                    inner join Campanha c ON fp.id_campanha = c.id_campanha
                    order by c.nome, fp.formaPagamento;
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
        


    def validar_campanha(self, postGree= PostgresQueries, id_campanha: int=None) -> Campanha:
        if self.control_campanha.verifica_existencia_campanha(postGree, id_campanha):
            print(f"A Campanha {id_campanha} informada não existe.")
            return None
        else:
            postGree.connect()
            df_campanha = postGree.sqlToDataFrame(f"select id, cpf_pessoa, data_inicio, data_fim, formaPagamento from campanha where id = {id_campanha}")
            campanha = Campanha(df_campanha.id[0], df_campanha.nome[0], df_campanha.cpf_pessoa[0], df_campanha.data_inicio[0], df_campanha.data_fim[0], df_campanha.formaPagamento[0])
            return campanha
        

    """
    def atualizar_formaPagamento(self) -> FormaPagamento:

    def excluir_formaPagamento(self):
    def verificar_existencia_formaPagamento(self, postGree: PostgresQueries, id_forma: int=None) -> bool:

"""