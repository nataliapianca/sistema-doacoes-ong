import psycopg2
import pandas as pd
import json
import os

class PostgresQueries:
    def __init__(self, can_write: bool = False):
        self.can_write = can_write

        # Configuração do banco via .env
        self.host = os.getenv("DB_HOST")
        self.port = int(os.getenv("DB_PORT", "5432"))
        self.database = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")

        # Validação mínima (falha rápido e claro)
        missing = [
            name for name, value in {
                "DB_HOST": self.host,
                "DB_PORT": self.port,
                "DB_NAME": self.database,
                "DB_USER": self.user,
                "DB_PASSWORD": self.password,
            }.items() if not value
        ]

        if missing:
            raise RuntimeError(
                "Variáveis de ambiente ausentes: " + ", ".join(missing)
            )

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


if __name__ == "__main__":
    db = PostgresQueries()
    try:
        db.connect()
        print("FOIIII!!!!<:")
    except Exception as e:
        print("Erro ao conectar:   :( ", e)
    finally:
        db.close()