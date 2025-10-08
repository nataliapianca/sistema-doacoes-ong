-- Active: 1759353781911@@bdong-nhui.j.aivencloud.com@15697@ong
-- Tabela Pessoa
CREATE TABLE Pessoa (
    id_pessoa SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    senha VARCHAR(100) NOT NULL,
    tipo_pessoa VARCHAR(20) CHECK (tipo_pessoa IN ('doador', 'usuario'))
);

-- Tabela Endereco
CREATE TABLE Endereco (
    id_endereco SERIAL PRIMARY KEY,
    id_pessoa INT NOT NULL,
    logradouro VARCHAR(200),
    numero VARCHAR(20),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    estado CHAR(2),
    cep VARCHAR(10),
    FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa)
);

-- Tabela Campanha
CREATE TABLE Campanha (
    id_campanha SERIAL PRIMARY KEY,
    id_pessoa INT NOT NULL,
    nome VARCHAR(150),
    descricao TEXT,
    data_inicio DATE,
    data_fim DATE,
    id_status INT,
    FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa),
    FOREIGN KEY (id_status) REFERENCES Status(id_statuscampanha)
);

-- Tabela Status
CREATE TABLE Status (
    id_statuscampanha SERIAL PRIMARY KEY,
    descricao VARCHAR(100)
);

-- Tabela FormaPagamento
CREATE TABLE FormaPagamento (
    id_forma SERIAL PRIMARY KEY,
    forma_pagamento VARCHAR(50)
);

-- Tabela TipoDoacao
CREATE TABLE TipoDoacao (
    id_tipo SERIAL PRIMARY KEY,
    descricao VARCHAR(100)
);

-- Tabela Doacao
CREATE TABLE Doacao (
    id_doacao SERIAL PRIMARY KEY,
    id_pessoa INT NOT NULL,
    id_campanha INT NOT NULL,
    id_forma INT,
    id_tipo INT,
    valor DECIMAL(12,2),
    data_doacao TIMESTAMP,
    FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa),
    FOREIGN KEY (id_campanha) REFERENCES Campanha(id_campanha),
    FOREIGN KEY (id_forma) REFERENCES FormaPagamento(id_forma),
    FOREIGN KEY (id_tipo) REFERENCES TipoDoacao(id_tipo)
);

-- Tabela Recibo
CREATE TABLE Recibo (
    id_recibo SERIAL PRIMARY KEY,
    id_doacao INT NOT NULL UNIQUE,
    data_emissao TIMESTAMP,
    codigo_validacao UUID,
    FOREIGN KEY (id_doacao) REFERENCES Doacao(id_doacao)
);

-- Tabela CampanhaTipoDoacao (associação)
CREATE TABLE CampanhaTipoDoacao (
    id_campanha INT NOT NULL,
    id_tipo INT NOT NULL,
    PRIMARY KEY (id_campanha, id_tipo),
    FOREIGN KEY (id_campanha) REFERENCES Campanha(id_campanha),
    FOREIGN KEY (id_tipo) REFERENCES TipoDoacao(id_tipo)
);

-- Tabela CampanhaFormaPagamento (associação)
CREATE TABLE CampanhaFormaPagamento (
    id_campanha INT NOT NULL,
    id_forma INT NOT NULL,
    PRIMARY KEY (id_campanha, id_forma),
    FOREIGN KEY (id_campanha) REFERENCES Campanha(id_campanha),
    FOREIGN KEY (id_forma) REFERENCES FormaPagamento(id_forma)
);
