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










diarama de relacionamentos@startuml
title Diagrama de Classes - Sistema de Doações

' ======= Classes principais =======

class Pessoa {
  +id_pessoa : int
  +nome : string
  +cpf : string
  +email : string
  +senha : string
  +perfil : string = "doador"
  +tipo_pessoa : string <<{doador, usuario}>>
}

class Endereco {
  +id_endereco : int
  +logradouro : string
  +numero : string
  +complemento : string
  +bairro : string
  +cidade : string
  +estado : string
  +cep : string
}

class StatusCampanha {
  +id_status : int
  +descricao : string
}

class Campanha {
  +id_campanha : int
  +nome : string
  +descricao : text
  +data_inicio : date
  +data_fim : date
}

class FormaPagamento {
  +id_forma : int
  +descricao : string
}

class TipoDoacao {
  +id_tipo : int
  +descricao : string
}

class Doacao {
  +id_doacao : int
  +valor : decimal
  +data_doacao : timestamp
}

class Recibo {
  +id_recibo : int
  +data_emissao : timestamp
  +codigo_validacao : uuid
}

class CampanhaTipoDoacao {
}

class CampanhaFormaPagamento {
}

class FavoritoCampanha {
  +data_favorito : timestamp
}

class VoluntarioCampanha {
  +funcao : string
  +data_entrada : timestamp
}

' ======= Relacionamentos =======

Pessoa "1" -- "0..*" Endereco : possui >
Pessoa "1" -- "0..*" Campanha : cria >
Pessoa "1" -- "0..*" Doacao : realiza >
Pessoa "1" -- "0..*" FavoritoCampanha
Pessoa "1" -- "0..*" VoluntarioCampanha

Campanha "1" -- "0..*" Doacao : recebe >
Campanha "1" -- "0..*" CampanhaTipoDoacao
Campanha "1" -- "0..*" CampanhaFormaPagamento
Campanha "1" -- "0..*" FavoritoCampanha
Campanha "1" -- "0..*" VoluntarioCampanha

StatusCampanha "1" -- "0..*" Campanha : classifica >

Doacao "1" -- "1" Recibo : gera >

FormaPagamento "1" -- "0..*" Doacao
TipoDoacao "1" -- "0..*" Doacao
TipoDoacao "1" -- "0..*" CampanhaTipoDoacao
FormaPagamento "1" -- "0..*" CampanhaFormaPagamento

@enduml



