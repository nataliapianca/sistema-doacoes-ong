from conexion.connection import PostgresQueries
from pathlib import Path


def create_tables(query: str):
    """Executa um script de criação de tabelas. Usa o método write (commit por comando).
    Caso o script contenha múltiplos comandos separados por ';', divide e executa cada um.
    """
    list_of_commands = [c.strip() for c in query.split(";") if c.strip()]

    postgres = PostgresQueries(can_write=True)
    postgres.connect()

    for command in list_of_commands:
        print(command)
        try:
            # usa write para executar DDL também (commit interno)
            postgres.write(command + (";" if not command.endswith(";") else ""))
            print("Successfully executed")
        except Exception as e:
            print(f"Error executing command: {e}")

def generate_records(query: str, split: bool = True):
    """Insere registros. Por padrão divide por ';' e executa cada comando.
    Se split for False, envia todo o script de uma vez (útil para DO $$ blocks).
    """
    postgres = PostgresQueries(can_write=True)
    postgres.connect()

    if not split:
        try:
            print(query)
            postgres.write(query)
            print("Successfully executed")
        except Exception as e:
            print(f"Error executing command: {e}")
        return

    list_of_commands = [c.strip() for c in query.split(";") if c.strip()]
    for command in list_of_commands:
        print(command)
        try:
            postgres.write(command + (";" if not command.endswith(";") else ""))
            print("Successfully executed")
        except Exception as e:
            print(f"Error executing command: {e}")

def run():
    # Cria tabelas
    base = Path(__file__).resolve().parent
    sql_dir = (base / ".." / "sql").resolve()
    with open(sql_dir / "create_tables_ong.sql", encoding="utf-8") as f:
        query_create = f.read()

    print("Creating tables...")
    create_tables(query=query_create)
    print("Tables successfully created!")

    # Insere registros básicos
    with open(sql_dir / "inserting_samples_records.sql", encoding="utf-8") as f:
        query_generate_records = f.read()

    print("Generating records...")
    generate_records(query=query_generate_records, split=True)
    print("Records successfully generated!")

    # Insere registros relacionados
    with open(sql_dir / "inserting_samples_related_records.sql", encoding="utf-8") as f:
        query_generate_related_records = f.read()

    print("Generating related records...")
    # o arquivo relacionado usa blocos DO $$ ... END $$; não dividir por ';'
    generate_records(query=query_generate_related_records, split=False)
    print("Records successfully generated!")

if __name__ == "__main__":
    run()
