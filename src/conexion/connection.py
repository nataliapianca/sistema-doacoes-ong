import psycopg2

def conectar():
    try:
        conexao = psycopg2.connect(
            host="bdong-nhui.j.aivencloud.com",
            port=15697,
            database="defaultdb",
            user="avnadmin",
            password="AVNS_t_ZAEU766Z1B4pPok5Z"
        )
        print("Conexão estabelecida com sucesso!")
        return conexao
    except Exception as e:
        print("Erro ao conectar ao banco:", e)
        return None
