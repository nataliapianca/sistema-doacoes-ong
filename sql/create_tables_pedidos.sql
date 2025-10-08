-- ===============================
-- TABELA PESSOA
-- ===============================
CREATE TABLE pessoa (
    id_pessoa SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    senha VARCHAR(200) NOT NULL,
    perfil VARCHAR(50) DEFAULT 'doador', 
    tipo_pessoa VARCHAR(20) NOT NULL CHECK (tipo_pessoa IN ('doador', 'usuario'))
);

-- ===============================
-- TABELA ENDERECO (relacionada a Pessoa)
-- ===============================
CREATE TABLE endereco (
    id_endereco SERIAL PRIMARY KEY,
    id_pessoa INT NOT NULL,
    logradouro VARCHAR(200),
    numero VARCHAR(10),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    estado CHAR(2),
    cep CHAR(8),
    FOREIGN KEY (id_pessoa) REFERENCES pessoa(id_pessoa)
);

-- ===============================
-- TABELA STATUS_CAMPANHA
-- ===============================
CREATE TABLE status_campanha (
    id_status SERIAL PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL 
);

-- ===============================
-- TABELA CAMPANHA (criada por um usuário)
-- ===============================
CREATE TABLE campanha (
    id_campanha SERIAL PRIMARY KEY,
    id_pessoa INT NOT NULL,
    nome VARCHAR(150) NOT NULL,
    descricao TEXT,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    id_status INT NOT NULL,
    FOREIGN KEY (id_pessoa) REFERENCES pessoa(id_pessoa),
    FOREIGN KEY (id_status) REFERENCES status_campanha(id_status)
);

-- ===============================
-- TABELA FORMA_PAGAMENTO
-- ===============================
CREATE TABLE forma_pagamento (
    id_forma SERIAL PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL 
);

-- ===============================
-- TABELA TIPO_DOACAO
-- ===============================
CREATE TABLE tipo_doacao (
    id_tipo SERIAL PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL 
);

-- ===============================
-- TABELA DOACAO
-- ===============================
CREATE TABLE doacao (
    id_doacao SERIAL PRIMARY KEY,
    id_doador INT NOT NULL,     
    id_campanha INT NOT NULL,
    id_forma INT NOT NULL,
    id_tipo INT NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    data_doacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_doador) REFERENCES pessoa(id_pessoa),
    FOREIGN KEY (id_campanha) REFERENCES campanha(id_campanha),
    FOREIGN KEY (id_forma) REFERENCES forma_pagamento(id_forma),
    FOREIGN KEY (id_tipo) REFERENCES tipo_doacao(id_tipo)
);

-- ===============================
-- TABELA RECIBO
-- ===============================
CREATE TABLE recibo (
    id_recibo SERIAL PRIMARY KEY,
    id_doacao INT NOT NULL,
    data_emissao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    codigo_validacao UUID DEFAULT gen_random_uuid(), -- gera código único
    FOREIGN KEY (id_doacao) REFERENCES doacao(id_doacao)
);





