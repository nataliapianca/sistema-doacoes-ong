from model.pessoa import Pessoa
from conexion.connection import PostgresQueries

class Controller_Pessoa:
    def __init__(self):
        pass
#insert
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
#update
    def atualizar_pessoa(self) -> Pessoa:
        postgres = PostgresQueries(can_write=True)
        postgres.connect()

        cpf = input("CPF da pessoa para atualizar: ")

        if not self.verifica_existencia_pessoa(postgres, cpf):
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            senha = input("Nova senha: ")
            tipo_pessoa = input("Novo tipo (doador/usuario): ").lower()

            sql = f"""
                UPDATE pessoa
                SET nome = '{nome}',
                    email = '{email}',
                    senha = '{senha}',
                    tipo_pessoa = '{tipo_pessoa}'
                WHERE cpf = '{cpf}';
            """
            postgres.write(sql)

            df_pessoa = postgres.sqlToDataFrame(f"""
                SELECT id_pessoa, nome, cpf, email, senha, tipo_pessoa
                FROM pessoa
                WHERE cpf = '{cpf}';
            """)

            pessoa_atualizada = Pessoa(
                id_pessoa=df_pessoa.id_pessoa.values[0],
                nome=df_pessoa.nome.values[0],
                cpf=df_pessoa.cpf.values[0],
                email=df_pessoa.email.values[0],
                senha=df_pessoa.senha.values[0],
                tipo_pessoa=df_pessoa.tipo_pessoa.values[0]
            )

            print("\nPessoa atualizada")
            print(pessoa_atualizada.to_string())

            postgres.close()
            return pessoa_atualizada
        else:
            print(f"O CPF {cpf} não existe.")
            postgres.close()
            return None
#delete
    def excluir_pessoa(self):
        postgres = PostgresQueries(can_write=True)
        postgres.connect()

        cpf = input("CPF da pessoa que deseja excluir: ")

        if not self.verifica_existencia_pessoa(postgres, cpf):
            df_pessoa = postgres.sqlToDataFrame(f"""
                SELECT id_pessoa, nome, cpf, email, senha, tipo_pessoa
                FROM pessoa
                WHERE cpf = '{cpf}';
            """)
            postgres.write(f"DELETE FROM pessoa WHERE cpf = '{cpf}';")
            pessoa_excluida = Pessoa(
                id_pessoa=df_pessoa.id_pessoa.values[0],
                nome=df_pessoa.nome.values[0],
                cpf=df_pessoa.cpf.values[0],
                email=df_pessoa.email.values[0],
                senha=df_pessoa.senha.values[0],
                tipo_pessoa=df_pessoa.tipo_pessoa.values[0]
            )

            print("\nPessoa removida !")
            print(pessoa_excluida.to_string())
        else:
            print(f"CPF {cpf} não existe.")

        postgres.close()

 

    def verifica_existencia_pessoa(self, postgres: PostgresQueries, cpf: str) -> bool:
        df_pessoa = postgres.sqlToDataFrame(f"SELECT cpf FROM pessoa WHERE cpf = '{cpf}';")
        return df_pessoa.empty