# Sistema de Doações para ONG 🌟

Um sistema simples e organizado para gerenciar doações, doadores e relatórios, com CRUD completo e interface amigável.

O sistema é composto por cinco tabelas principais: `pessoa`, `doacao`, `campanha`, `formadepagamento` e `recibo`.

---

## Inicialização do Sistema

Antes de executar o sistema, certifique-se de criar as tabelas e inserir os dados de exemplo usando o script abaixo:

```bash
~$ pensa isso aqui
```

Para executar o sistema e acessar a interface principal:

```bash
~$ python principal.py
```

Para testar a conexão com o banco de dados PostgreSQL via módulo de conexão desenvolvido para este projeto:

```bash
~$ python test.py
```

> **Observação:** A conexão com o banco de dados utiliza PostgreSQL hospedado no **Aiven**, podendo ser acessado via **VSCode** com a extensão **PostgreSQL**.

---

## Organização do Projeto

```

Sistema de Doações para ONG 🌟
│
├── diagrams/
│   └── diagrama_relacional.png        # Diagrama lógico das tabelas: pessoa, doacao, campanha, formaPagamento, recibo
│
├── sql/
│   ├── create_tables_doacoes.sql      # Criação das tabelas e tipos ENUM
│   ├── insert_sample_records.sql      # Inserção de dados fictícios para testes
│   └── insert_sample_related_records.sql # Inserção de registros relacionados (opcional)
│
├── src/
│   ├── conexion/
│   │   └── postgres_queries.py        # Módulo de conexão com PostgreSQL (CRUD e consultas)
│   │
│   ├── controller/
│   │   ├── pessoa_controller.py       # Inserção, atualização e exclusão de pessoas
│   │   ├── doacao_controller.py       # Inserção, atualização e exclusão de doações
│   │   ├── campanha_controller.py     # Inserção, atualização e exclusão de campanhas
│   │   ├── formadepagamento_controller.py
│   │   └── recibo_controller.py
│   │
│   ├── model/
│   │   ├── pessoa.py                  # Classe Pessoa
│   │   ├── doacao.py                  # Classe Doacao
│   │   ├── campanha.py                # Classe Campanha
│   │   ├── formadepagamento.py
│   │   └── recibo.py
│   │
│   ├── reports/
│   │   └── relatorios.py              # Geração de relatórios do sistema
│   │
│   ├── utils/
│   │   └── helpers.py                 # Funções auxiliares
│   │
│   ├── create_tables_and_records_postgres.py # Script para criar tabelas e inserir registros
│   ├── principal.py                   # Script principal do sistema (interface com o usuário)
│   └── test.py                        # Teste de conexão e funcionalidades do módulo de conexão
│
└── requirements.txt                   # Bibliotecas necessárias

```

### diretórios principais

* `diagrams`:
  Contém o diagrama relacional (lógico) do sistema.
  O sistema possui cinco entidades: `pessoa`, `doacao`, `campanha`, `formadepagamento` e `recibo`.

<img width="1157" height="697" alt="image" src="https://github.com/user-attachments/assets/764e0367-8a3c-4913-91b5-67aa238fbdd8" />



* `sql`:
  Scripts para criação das tabelas e inserção de dados fictícios para testes do sistema.
  Certifique-se de que o usuário do banco possui privilégios suficientes antes de executar os scripts.

  * `create_tables.sql`: Criação das tabelas, relacionamentos e permissões necessárias.
  * `insert_sample_records.sql`: Inserção de registros fictícios para testes do sistema.

* `src`:
  Contém os scripts do sistema.

  * `conexion`:
    Módulo de conexão com o banco de dados PostgreSQL. Possui funcionalidades úteis para execução de consultas e alterações (DML e DDL), com suporte a saída em JSON, Pandas DataFrame ou lista.

    **Exemplo de utilização para consultas simples:**

    ```python
    def listar_pessoas(self, postgres: PostgresQueries, need_connect: bool = False):
        query = """
                SELECT id, nome, email
                FROM pessoa
                ORDER BY nome
                """
        if need_connect:
            postgres.connect()
        print(postgres.sqlToDataFrame(query))
    ```

    **Exemplo de inserção de registro:**

    ```python
    from conexion.postgres_queries import PostgresQueries

    def inserir_pessoa(self):
        postgres = PostgresQueries(can_write=True)
        postgres.connect()

        nome = input("Nome: ")
        email = input("Email: ")

        postgres.write(f"INSERT INTO pessoa (nome, email) VALUES ('{nome}', '{email}')")
        df_pessoa = postgres.sqlToDataFrame(f"SELECT * FROM pessoa WHERE email = '{email}'")
        print(df_pessoa)
    ```

* `controller`:
  Classes controladoras responsáveis por realizar inserção, alteração e exclusão de registros nas tabelas.

* `model`:
  Classes das entidades do sistema conforme o diagrama relacional.

* `reports`:
  Classe responsável por gerar relatórios a partir dos dados do sistema.

* `utils`:
  Scripts de configuração e automação de tarefas auxiliares do sistema.

---

## Scripts Principais

* `create_tables_and_records.py`: Cria as tabelas e registros fictícios. Deve ser executado **antes** do script `principal.py`.
* `principal.py`: Interface principal do sistema entre o usuário e os módulos de acesso ao banco de dados.
* `test.py`: Testa a conexão e funcionalidades do módulo de conexão.

---

## Bibliotecas Utilizadas

Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## Observações de Configuração

Caso esteja utilizando VSCode com PostgreSQL no **Aiven**, configure as credenciais do banco e host no módulo de conexão (`conexion/postgres_queries.py`).

> Não é necessário instalar o Oracle InstantClient, pois o sistema utiliza PostgreSQL.

---

