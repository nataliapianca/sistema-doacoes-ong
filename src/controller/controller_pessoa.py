from model.pessoa import Pessoa
from conexion.connection import PostgresQueries
from model.doacao import Doacao
from model.recibo import Recibo
from typing import List

class Controller_Pessoa:
    def __init__(self):
        pass

    def inserir_pessoa(self) -> Pessoa:
        postgres = PostgresQueries(can_write=True)
        postgres.connect()

        cpf = input("CPF (Novo): ")
        if self.verifica_existencia_pessoa(postgres, cpf):
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            tipo_pessoa = input("Tipo (doador/usuario): ").lower()

            if tipo_pessoa not in ("doador", "usuario"):
                print("Tipo inválido. Deve ser 'doador' ou 'usuario'.")
                postgres.close()
                return None

            sql = f"""
                INSERT INTO pessoa (nome, cpf, email, senha, tipo_pessoa)
                VALUES ('{nome}', '{cpf}', '{email}', '{senha}', '{tipo_pessoa}');
            """
            postgres.write(sql)

            df_pessoa = postgres.sqlToDataFrame(f"""
                SELECT id_pessoa, nome, cpf, email, senha, tipo_pessoa
                FROM pessoa
                WHERE cpf = '{cpf}';
            """)

            nova_pessoa = Pessoa(
                id_pessoa=df_pessoa.id_pessoa.values[0],
                nome=df_pessoa.nome.values[0],
                cpf=df_pessoa.cpf.values[0],
                email=df_pessoa.email.values[0],
                senha=df_pessoa.senha.values[0],
                tipo_pessoa=df_pessoa.tipo_pessoa.values[0]
            )

            print("\nPessoa cadastrada ")
            print(nova_pessoa.to_string())

            postgres.close()
            return nova_pessoa

        else:
            print(f"O CPF {cpf} já está cadastrado.")
            postgres.close()
            return None

    def atualizar_pessoa(self) -> Pessoa:
        postgres = PostgresQueries(can_write=True)
        postgres.connect()

        cpf = input("CPF da pessoa para atualizar: ")

        if not self.verifica_existencia_pessoa(postgres, cpf):
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            senha = input("Nova senha: ")
            tipo_pessoa = input("Novo tipo (doador/usuario): ").lower()
            
            if tipo_pessoa not in ("doador", "usuario"):
                print("Tipo inválido. Deve ser 'doador' ou 'usuario'.")
                postgres.close()
                return None

            sql = f"""
                UPDATE pessoa
                SET nome = '{nome}',
                    email = '{email}',
                    senha = '{senha}',
                    tipo_pessoa = '{tipo_pessoa}'
                WHERE cpf = '{cpf}';
            """
            postgres.write(sql)

            pessoa_atualizada = self.validar_pessoa(postgres, cpf)

            print("\nPessoa atualizada")
            if pessoa_atualizada:
                print(pessoa_atualizada.to_string())
                if pessoa_atualizada.get_tipo_pessoa() == 'doador':
                    print(f"Total de doações carregadas: {len(pessoa_atualizada.get_doacoes())}")

            postgres.close()
            return pessoa_atualizada
        else:
            print(f"O CPF {cpf} não existe.")
            postgres.close()
            return None

    def excluir_pessoa(self):
        postgres = PostgresQueries(can_write=True)
        postgres.connect()

        cpf = input("CPF da pessoa que deseja excluir: ")

        if not self.verifica_existencia_pessoa(postgres, cpf):
            
            pessoa_excluida = self.validar_pessoa(postgres, cpf)
            
            if pessoa_excluida and pessoa_excluida.get_tipo_pessoa() == 'doador' and len(pessoa_excluida.get_doacoes()) > 0:
                print(f"Erro: Não é possível excluir o doador {pessoa_excluida.get_nome()} pois ele possui {len(pessoa_excluida.get_doacoes())} doação(ões) registradas.")
                print("Para excluir, remova as doações desta pessoa primeiro.")
                postgres.close()
                return

            postgres.write(f"DELETE FROM pessoa WHERE cpf = '{cpf}';")

            print("\nPessoa removida !")
            if pessoa_excluida:
                print(pessoa_excluida.to_string())
        else:
            print(f"CPF {cpf} não existe.")

        postgres.close()

    def verifica_existencia_pessoa(self, postgres: PostgresQueries, cpf: str) -> bool:
        df_pessoa = postgres.sqlToDataFrame(f"SELECT cpf FROM pessoa WHERE cpf = '{cpf}';")
        return df_pessoa.empty

    def _carregar_doacoes(self, postgres: PostgresQueries, id_pessoa: int) -> List[Doacao]:
        
        df_doacoes = postgres.sqlToDataFrame(
            f"SELECT * FROM doacao WHERE id_pessoa = {id_pessoa} ORDER BY data_doacao DESC"
        )
        
        lista_doacoes = []
        if df_doacoes.empty:
            return lista_doacoes

        for _, row in df_doacoes.iterrows():
            id_doacao_atual = row['id_doacao']
            
            df_recibo = postgres.sqlToDataFrame(
                f"SELECT * FROM recibo WHERE id_doacao = {id_doacao_atual}"
            )
            
            recibo_obj = None
            if not df_recibo.empty:
                recibo_row = df_recibo.iloc[0]
                recibo_obj = Recibo(
                    id_recibo=recibo_row['id_recibo'],
                    data_emissao=recibo_row['data_emissao'],
                    codigo_validacao=recibo_row['codigo_validacao']
                )

            doacao_obj = Doacao(
                id_doacao=id_doacao_atual,
                id_pessoa=row['id_pessoa'],
                id_campanha=row['id_campanha'],
                valor=row['valor'],
                data_doacao=row['data_doacao'],
                recibo=recibo_obj
            )
            
            if recibo_obj:
                recibo_obj.set_doacao(doacao_obj)
                
            lista_doacoes.append(doacao_obj)
            
        return lista_doacoes

    def validar_pessoa(self, postGree: PostgresQueries, cpf_pessoa: str=None) -> Pessoa:
        if self.verifica_existencia_pessoa(postGree, cpf_pessoa):
            print(f"A pessoa de CPF: {cpf_pessoa} informado não existe.")
            return None

        if not postGree.conn:
            postGree.connect()
            
        df_pessoa = postGree.sqlToDataFrame(f"select id_pessoa, nome, cpf, email, senha, tipo_pessoa from Pessoa where cpf = '{cpf_pessoa}'")

        if df_pessoa.empty:
            print("Erro interno: Pessoa encontrada, mas dados não recuperados.")
            return None
        
        pessoa_row = df_pessoa.iloc[0]

        pessoa = Pessoa(
            id_pessoa=pessoa_row['id_pessoa'],
            nome=pessoa_row['nome'],
            cpf=pessoa_row['cpf'],
            email=pessoa_row['email'],
            senha=pessoa_row['senha'],
            tipo_pessoa=pessoa_row['tipo_pessoa']
        )

        if pessoa.get_tipo_pessoa() == 'doador':
            doacoes = self._carregar_doacoes(postGree, pessoa.get_id_pessoa())
            pessoa.set_doacoes(doacoes)
            print(f"Doador {pessoa.get_nome()} validado. {len(doacoes)} doações carregadas.")

        return pessoa