
-- LIMPAR TODAS AS TABELAS


-- Remover todos os dados da tabela Recibo
TRUNCATE TABLE Recibo RESTART IDENTITY CASCADE;

-- Remover todos os dados da tabela Doacao
TRUNCATE TABLE Doacao RESTART IDENTITY CASCADE;

-- Remover todos os dados da tabela FormaPagamento
TRUNCATE TABLE FormaPagamento RESTART IDENTITY CASCADE;

-- Remover todos os dados da tabela Campanha
TRUNCATE TABLE Campanha RESTART IDENTITY CASCADE;

-- Remover todos os dados da tabela Pessoa
TRUNCATE TABLE Pessoa RESTART IDENTITY CASCADE;

-- deletar forma de pagamento ao pagar campanha
WITH delete_formas AS (
    DELETE FROM formaPagamento
    WHERE id_campanha = 1
    RETURNING id_campanha
)
DELETE FROM campanha
WHERE id_campanha IN (SELECT id_campanha FROM delete_formas);
