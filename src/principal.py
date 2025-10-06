from conexion import conectar

conexao = conectar()


def main():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT NOW();")
        print("Conexão estabelecida com sucesso!")
        print("Banco respondeu:", cursor.fetchone())
        cursor.close()
        conexao.close()
    else:
        print("Não foi possível conectar ao banco.")

if __name__ == "__main__":
    main()
