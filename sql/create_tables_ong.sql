-- Active: 1759353781911@@bdong-nhui.j.aivencloud.com@15697@sistema_doacoes
-- Extensão para UUID
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Tipo ENUM
CREATE TYPE tipo_pessoa_enum AS ENUM ('doador', 'usuario');

-- TABELA: Pessoa
CREATE TABLE Pessoa (
    id_pessoa SERIAL PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    email VARCHAR(50) NOT NULL,
    senha VARCHAR(60) NOT NULL,
    tipo_pessoa tipo_pessoa_enum NOT NULL
);

-- TABELA: Campanha
CREATE TABLE Campanha (
    id_campanha SERIAL PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    descricao TEXT NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    statos BOOLEAN DEFAULT TRUE NOT NULL,
    id_pessoa INT NOT NULL REFERENCES Pessoa(id_pessoa),
    formaPagamento VARCHAR(30) NOT NULL
);

-- TABELA: FormaPagamento
CREATE TABLE FormaPagamento (
    id_forma_pagamento SERIAL PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL,
    id_campanha INT NOT NULL REFERENCES Campanha(id_campanha),
    id_pessoa INT NOT NULL REFERENCES Pessoa(id_pessoa)
);

-- TABELA: Doacao
CREATE TABLE Doacao (
    id_doacao SERIAL PRIMARY KEY,
    id_pessoa INT NOT NULL REFERENCES Pessoa(id_pessoa),
    id_campanha INT NOT NULL REFERENCES Campanha(id_campanha),
    valor NUMERIC(10,2) NOT NULL,
    data_doacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- TABELA: Recibo
CREATE TABLE Recibo (
    id_recibo SERIAL PRIMARY KEY,
    id_doacao INT NOT NULL REFERENCES Doacao(id_doacao),
    id_pessoa INT NOT NULL REFERENCES Pessoa(id_pessoa),
    id_campanha INT NOT NULL REFERENCES Campanha(id_campanha),
    data_emissao TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    codigo_validacao UUID DEFAULT gen_random_uuid() NOT NULL
);
