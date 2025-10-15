from .controller_campanha import Controller_Campanha
from controller.controller_pessoa import Controller_Pessoa
from model.formaPagamento import FormaPagamento
from conexion.connection import PostgresQueries
from model.pessoa import Pessoa
from model.campanha import Campanha

class Controller_FormaPagamento:
    def __init__(self):
        self.control_pessoa = Controller_Pessoa
        self.control_campanha = Controller_Campanha


    def inserir_formaPagamento(self, postGree, id_campanha: int, id_pessoa:int, nome_forma:str) -> FormaPagamento:
        self.listar_campanhas(postGree, need_connect= True) 
        """aqui ele lista as campanhas, não sei se é necessário"""
        campanha = self.validar_campanha(postGree, id_campanha)
        if campanha is None:
            return None
        
        self.listar_pessoas(postGree, need_connect= True) 
        """aqui ele lista as pessoas, não sei se é necessário"""

        df_pessoa = postGree.sqlToDataFrame(f"select cpf from Pessoa where id_pessoa = '{id_pessoa}'")
        cpf_pessoa = df_pessoa.cpf[0]

        pessoa = self.validar_pessoa(postGree, cpf_pessoa)
        if pessoa is None:
            return None

        cursor = postGree.connect()
        output_value = cursor.var(int)

        dado = dict(id_forma=output_value, id_campanha=id_campanha, id_pessoa=id_pessoa, nome_forma=nome_forma)

        try: 
            cursor.execute("""
            begin
                :id_forma := FORMAPAGAMENTO_ID_FORMAPAGAMENTO_SEQ.NEXTVAL;
                insert into formaPagamento values(:id_forma, :id_campanha, :id_pessoa, :formaPagamento);
            end;          
            """, dado)

            id_forma = output_value.getvalue()
            postGree.conn.commit()

            nova_formaPagamento = FormaPagamento(id_forma, campanha, pessoa, nome_forma)

            print(nova_formaPagamento.toString())
            return nova_formaPagamento
        except Exception as e:
            print(f"Erro ao inserir forma de Pagamento: {e}.")
            return None


    def atualizar_formaPagamento(self, id_campanha: int, id_pessoa_respon: int, nome_forma: str) -> bool:
        postGree = PostgresQueries(can_write=True)
        postGree.connect()
        
        try:
            postGree.write(f"update FormaPagamento set formaPagamento = '{nome_forma}' where id_campanha = '{id_campanha}' and id_pessoa = '{id_pessoa_respon}';")
            return True
        except Exception as e:
            print(f"Erro ao salvar a forma de Pagamento: {e}")
            return False


    def executar_atualizar_formaPagamento(self, postGree)-> bool:
        try:
            id_campanha_alvo = int(input("Informe o ID da Campanha: "))
            cpf_pessoa_respon = str(input("Informe o CPF da Pessoa Responsável (para identificação):"))

            pessoa = self.control_pessoa.verifica_existencia_pessoa(postGree, cpf_pessoa_respon)
            if pessoa is None:
                print("Pessoa Responsável não encontrada.")
                return False
            
            id_pessoa_respon = pessoa.get_id_pessoa()

            novo_nome_forma = str(input("Informe a nova Forma de Pagamento: "))
            sucesso = self.atualizar_formaPagamento(id_campanha_alvo, id_pessoa_respon, novo_nome_forma)

            if sucesso:
                print(f"A Forma de Pagamento da Campanha {id_campanha_alvo} foi atualizada para {novo_nome_forma}!")
                return True
            
            print(f"Falha na atualização da Forma de Pagamento no Banco de dados.")
            return False
        except ValueError:
            print("Entrada inválida.Certifique-se de usar números para os IDs.")
            return False


    def listar_pessoas(self, postGree: PostgresQueries, need_connect:bool=False):
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


    def listar_campanhas(self, postGree: PostgresQueries, need_connect:bool=False):
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
    

    def validar_pessoa(self, postGree: PostgresQueries, cpf_pessoa: int=None) -> Pessoa:
        if self.control_pessoa.verifica_existencia_pessoa(postGree, cpf_pessoa):
            print(f"A pessoa de CPF: {cpf_pessoa} informado não existe.")
            return None
        else:
            postGree.connect()
            df_pessoa = postGree.sqlToDataFrame(f"select id_pessoa, nome, cpf, email, senha, tipo_pessoa from Pessoa where cpf = '{cpf_pessoa}'")

            if df_pessoa.empty:
                print(f"Erro ao recuperar dados da Pessoa {cpf_pessoa}.")
                return None
            
            pessoa = Pessoa(df_pessoa.id_pessoa.values[0], df_pessoa.nome.values[0], df_pessoa.cpf.values[0], df_pessoa.email.values[0], df_pessoa.senha.values[0], df_pessoa.tipo_pessoa.values[0])
            return pessoa
        

    def validar_campanha(self, postGree: PostgresQueries, id_campanha: int=None) -> Campanha:
        if not self.control_campanha.verifica_existencia_campanha(postGree, id_campanha):
            print(f"A Campanha {id_campanha} informada não existe.")
            return None
    
        postGree.connect()
        df_campanha = postGree.sqlToDataFrame(f"select id_campanha, id_pessoa, nome, descricao, data_inicio, data_fim, formaPagamento from campanha where id_campanha = '{id_campanha}'")

        if df_campanha.empty:
            print("Campanha encontrada, porém não foi possível recuperar os dados.")
            return None
        
        id_pessoa = df_campanha.id_pessoa.values[0]
        sql_cpf = f"select cpf from Pessoa where id_pessoa = '{id_pessoa}'"
        df_pessoa = postGree.sqlToDataFrame(sql_cpf)

        if df_pessoa.empty:
            print("Erro: Pessoa responsável pela Campanha não encontrada.")
            return None

        cpf_pessoa = df_pessoa.cpf.values[0]
        pessoa = self.validar_pessoa(postGree, cpf_pessoa)

        if pessoa is None:
            print("A Pessoa informada não é válida.")
            return None

        campanha = Campanha(df_campanha.id_campanha[0], pessoa, df_campanha.nome[0], df_campanha.descricao[0], df_campanha.data_inicio[0], df_campanha.data_fim[0], df_campanha.formaPagament[0])
        return campanha
    

    def verificar_existencia_formaPagamento(self, postGree: PostgresQueries, id_forma: int) -> bool:
        df_formaPagamento = postGree.sqlToDataFrame(f"select id_forma from formaPagamento where id_forma = '{id_forma}'")
        return df_formaPagamento.empty