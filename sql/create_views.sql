
-- VIEWS PARA O SISTEMA DE DOAÇÕES

-- Resumo de Doações por Campanha
CREATE OR REPLACE VIEW vw_resumo_campanha AS
SELECT 
    c.id_campanha,
    c.nome AS campanha,
    COUNT(d.id_doacao) AS total_doacoes,
    SUM(d.valor) AS valor_total,
    COUNT(DISTINCT d.id_pessoa) AS total_doadores
FROM Campanha c
LEFT JOIN Doacao d ON c.id_campanha = d.id_campanha
GROUP BY c.id_campanha, c.nome;


-- Extrato de Doações de Cada Pessoa
CREATE OR REPLACE VIEW vw_doacoes_por_pessoa AS
SELECT 
    p.id_pessoa,
    p.nome AS doador,
    c.nome AS campanha,
    d.valor,
    d.data_doacao
FROM Doacao d
JOIN Pessoa p ON d.id_pessoa = p.id_pessoa
JOIN Campanha c ON d.id_campanha = c.id_campanha
ORDER BY p.nome, d.data_doacao;


-- Recibos Emitidos
CREATE OR REPLACE VIEW vw_recibos AS
SELECT 
    r.id_recibo,
    r.codigo_validacao,
    r.data_emissao,
    p.nome AS doador,
    c.nome AS campanha,
    d.valor AS valor_doado
FROM Recibo r
JOIN Doacao d ON r.id_doacao = d.id_doacao
JOIN Pessoa p ON r.id_pessoa = p.id_pessoa
JOIN Campanha c ON r.id_campanha = c.id_campanha;


-- Campanhas Ativas
CREATE OR REPLACE VIEW vw_campanhas_ativas AS
SELECT 
    id_campanha,
    nome,
    data_inicio,
    data_fim,
    status
FROM Campanha
WHERE status = TRUE;


-- Formas de Pagamento por Campanha
CREATE OR REPLACE VIEW vw_forma_pagamento_campanha AS
SELECT 
    f.id_forma_pagamento,
    f.descricao AS forma_pagamento,
    c.nome AS campanha,
    p.nome AS responsavel
FROM FormaPagamento f
JOIN Campanha c ON f.id_campanha = c.id_campanha
JOIN Pessoa p ON f.id_pessoa = p.id_pessoa;


-- Relatório Detalhado de Doações por Pessoa e Campanha
CREATE OR REPLACE VIEW vw_relatorio_doacoes AS
SELECT
    p.id_pessoa,
    p.nome AS doador,
    p.cpf,
    p.email,
    c.id_campanha,
    c.nome AS campanha,
    c.data_inicio,
    c.data_fim,
    COUNT(d.id_doacao) AS total_doacoes,
    SUM(d.valor) AS valor_total_doado,
    MIN(d.data_doacao) AS primeira_doacao,
    MAX(d.data_doacao) AS ultima_doacao,
    COUNT(r.id_recibo) AS total_recibos_emitidos,
    STRING_AGG(r.codigo_validacao::text, ', ') AS codigos_recibos
FROM Pessoa p
LEFT JOIN Doacao d ON p.id_pessoa = d.id_pessoa
LEFT JOIN Campanha c ON d.id_campanha = c.id_campanha
LEFT JOIN Recibo r ON d.id_doacao = r.id_doacao
GROUP BY p.id_pessoa, p.nome, p.cpf, p.email, c.id_campanha, c.nome, c.data_inicio, c.data_fim
ORDER BY p.nome, c.nome;


-- Relatório Completo Integrado (Pessoa, Campanha, Doação, Recibo, Forma de Pagamento)
CREATE OR REPLACE VIEW vw_relatorio_completo AS
SELECT
    p.id_pessoa,
    p.nome AS doador,
    p.cpf,
    p.email,
    c.id_campanha,
    c.nome AS campanha,
    c.descricao AS descricao_campanha,
    c.data_inicio,
    c.data_fim,
    c.status AS campanha_ativa,
    COUNT(DISTINCT d.id_doacao) AS total_doacoes,
    SUM(d.valor) AS valor_total_doado,
    MIN(d.data_doacao) AS primeira_doacao,
    MAX(d.data_doacao) AS ultima_doacao,
    COUNT(DISTINCT r.id_recibo) AS total_recibos_emitidos,
    STRING_AGG(DISTINCT r.codigo_validacao::text, ', ') AS codigos_recibos,
    STRING_AGG(DISTINCT f.descricao, ', ') AS formas_pagamento
FROM Pessoa p
LEFT JOIN Doacao d ON p.id_pessoa = d.id_pessoa
LEFT JOIN Campanha c ON d.id_campanha = c.id_campanha
LEFT JOIN Recibo r ON d.id_doacao = r.id_doacao
LEFT JOIN FormaPagamento f ON f.id_campanha = c.id_campanha
GROUP BY 
    p.id_pessoa, p.nome, p.cpf, p.email,
    c.id_campanha, c.nome, c.descricao, c.data_inicio, c.data_fim, c.status
ORDER BY p.nome, c.nome;
