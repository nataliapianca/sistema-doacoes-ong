<h1 align="center">🌟 Sistema de Doações para ONG 🌟</h1> <p align="center"> <i>Um sistema simples e organizado pra gerenciar doações, doadores e relatórios, com CRUD completo e interface amigável.</i> </p>

conexão da tabela 
Service URI
postgres://
CLICK_TO:REVEAL_PASSWORD
@pg-1a036a7c-ong.j.aivencloud.com:12001/defaultdb?sslmode=require

Database name
defaultdb

Host
pg-1a036a7c-ong.j.aivencloud.com

Port
12001

User
avnadmin

Password
AVNS_GYnUX8x5-5Puwpe5tJh


SSL mode
require

CA certificate

Show

Connection limit
20




condxão com o vs 

biblioteca: 
python3 -m pip install psycopg2

python: 
import psycopg2



codigo vs

def main():
    conn = psycopg2.connect('postgres://avnadmin:AVNS_GYnUX8x5-5Puwpe5tJh@pg-1a036a7c-ong.j.aivencloud.com:12001/defaultdb?sslmode=require')

    query_sql = 'SELECT VERSION()'

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    print(version)


if __name__ == "__main__":
    main()

[sistema-doacoes-ong-nat-branch.zip](https://github.com/user-attachments/files/22636852/sistema-doacoes-ong-nat-branch.zip)
