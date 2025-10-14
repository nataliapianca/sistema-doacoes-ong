import psycopg2
import pandas as pd
import json

class PostgresQueries:
    def __init__(self, can_write: bool = False):
        self.can_write = can_write
        self.host = "bdong-nhui.j.aivencloud.com"
        self.port = 15697
        self.database = "sistema_doacoes"

        with open("src/conexion/passphrase/authentication.pg", "r") as f:
          self.user, self.password = f.read().strip().split(",")

        self.conn = None
        self.cur = None

    def connect(self):
        """cconecta ao banco Postgre"""
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )
        self.cur = self.conn.cursor()
        return self.cur

    def sqlToDataFrame(self, query: str) -> pd.DataFrame:
        """executa SELECT e vem um dataFrame pandas"""
        self.cur.execute(query)
        rows = self.cur.fetchall()
        cols = [desc[0] for desc in self.cur.description]
        return pd.DataFrame(rows, columns=cols)

    def sqlToJson(self, query: str):
        """executa SELECT e volta JSON"""
        self.cur.execute(query)
        cols = [desc[0] for desc in self.cur.description]
        data = [dict(zip(cols, row)) for row in self.cur.fetchall()]
        return json.dumps(data, default=str, ensure_ascii=False, indent=2)

    def write(self, query: str):
        """executa os INSERT, UPDATE, DELETE"""
        if not self.can_write:
            raise Exception("Conexão não permite escrita.")
        self.cur.execute(query)
        self.conn.commit()

    def close(self):
        """fecha cursor e a conexão"""
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()


''' exemplo pra vcs urarem  primeiro chhama assim--
from conexion.postgres import PostgresQueries

ai vc cria a funcao
def atualizar_nome_pessoa():
    query = PostgresQueries(can_write=True)
    query.connect()  --precisa sempre chamar pra conetar com o banco

    ai vc poe a query que deseja, aqui é pra update --

    sql = """
    UPDATE pessoa
    SET nome = 'Natt'
    WHERE id_pessoa = 1;
    """

    query.write(sql)  -- o write escreve ela no banco
    query.close()    --SEMPRE FECHEMM
    print("Nome atualizado com sucesso!")'''


"""GNT NAO IA POR NADA ESSA MERDAA"""
if __name__ == "__main__":
    db = PostgresQueries()
    try:
        db.connect()
        print("FOIIII!!!!<:")
    except Exception as e:
        print("Erro ao conectar:   :( ", e)
    finally:
        db.close()