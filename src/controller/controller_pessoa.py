from model.pessoa import Pessoa
from conexion.connection import PostgresQueries

class Controller_Pessoa:
    def __init__(self):
        pass

#insert
    def inserir_pessoa(self) -> Pessoa:
        postgres = PostgresQueries(can_write=True)
        postgres.connect()
        cpf = input("CPF (Novo): ").strip()
        if self.verifica_existencia_pessoa(postgres, cpf):
            print(f"O CPF {cpf} já está cadastrado.")
            postgres.close()
            return None
        if len(cpf) != 11 or not cpf.isdigit():
            print("CPF inválido. Deve conter exatamente 11 números.")
            postgres.close()
            return None

        nome = input("Nome: ").strip()
        email = input("Email: ").strip()
        senha = input("Senha: ").strip()
        tipo_pessoa = input("Tipo (doador/usuario): ").strip().lower()

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

        print("\nPessoa cadastrada com sucesso!")
        print(nova_pessoa.to_string())

        postgres.close()
        return nova_pessoa

#update REFEITO
    def atualizar_pessoa(self) -> Pessoa:
        postgres = PostgresQueries(can_write=True)
        postgres.connect()

        cpf = input("CPF da pessoa para atualizar: ").strip()

        if not self.verifica_existencia_pessoa(postgres, cpf):
            print(f"O CPF {cpf} não existe.")
            postgres.close()
            return None

        print("\nQual dado deseja alterar?")
        print("1 - Nome")
        print("2 - Email")
        print("3 - Senha")
        print("4 - Tipo de pessoa (doador/usuario)")
        try:
            op = int(input("Opção: ").strip())
        except ValueError:
            print("Opção inválida.")
            postgres.close()
            return None

        campos = {
            1: "nome",
            2: "email",
            3: "senha",
            4: "tipo_pessoa"
        }

        if op not in campos:
            print("Opção inválida.")
            postgres.close()
            return None
        campo = campos[op]
        novo_valor = input(f"Novo valor para {campo}: ").strip()
        if campo == "tipo_pessoa" and novo_valor.lower() not in ("doador", "usuario"):
            print("Tipo inválido. Deve ser 'doador' ou 'usuario'.")
            postgres.close()
            return None
        sql = f"""
            UPDATE pessoa
            SET {campo} = '{novo_valor}'
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
        print("\nPessoa atualizada com sucesso!")
        print(pessoa_atualizada.to_string())

        postgres.close()
        return pessoa_atualizada

#delete refiz caso a pessoa esteja associada a uma campanha!!! NAO PODE EXCLUIR regra de negocio
    def excluir_pessoa(self):
        postgres = PostgresQueries(can_write=True)
        postgres.connect()

        cpf = input("CPF da pessoa que deseja excluir: ").strip()

        if not self.verifica_existencia_pessoa(postgres, cpf):
            print(f"CPF {cpf} não existe.")
            postgres.close()
            return None

       #saber se esta em camoanha
        df_campanha = postgres.sqlToDataFrame(f"""
            SELECT id_campanha FROM campanha
            WHERE id_pessoa = (SELECT id_pessoa FROM pessoa WHERE cpf = '{cpf}');
        """)
        if not df_campanha.empty:
            print("ssa pessoa está associada a uma ou mais campanhas e por isso não pode ser excluída.")
            postgres.close()
            return None

        #caso nao tenha campanha ai tira
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

        print("\nPessoa foi removida")
        print(pessoa_excluida.to_string())

        postgres.close()
        return pessoa_excluida




    def verifica_existencia_pessoa(self, postgres: PostgresQueries, cpf: str) -> bool:
        df_pessoa = postgres.sqlToDataFrame(f"SELECT cpf FROM pessoa WHERE cpf = '{cpf}';")
        return not df_pessoa.empty
