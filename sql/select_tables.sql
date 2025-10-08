-- SELECTS DE CONSULTA

-- Listar campanhas com total de doações
SELECT * FROM vw_total_doacoes_por_campanha;

-- Listar doadores e quanto já doaram
SELECT * FROM vw_total_doacoes_por_pessoa;

-- Listar doações com informações completas
SELECT 
    d.id_doacao,
    p.nome AS nome_doador,
    c.nome AS campanha,
    d.valor,
    d.data_doacao,
    r.codigo_validacao
FROM Doacao d
JOIN Pessoa p ON d.id_pessoa = p.id_pessoa
JOIN Campanha c ON d.id_campanha = c.id_campanha
LEFT JOIN Recibo r ON d.id_doacao = r.id_doacao
ORDER BY d.data_doacao DESC;

-- Campanhas ativas com período e organizador
SELECT 
    c.nome AS campanha,
    c.data_inicio,
    c.data_fim,
    CASE WHEN c.status THEN 'Ativa' ELSE 'Encerrada' END AS status,
    p.nome AS organizador
FROM Campanha c
JOIN Pessoa p ON c.id_pessoa = p.id_pessoa;

-- Formas de pagamento por campanha
SELECT 
    f.descricao AS forma_pagamento,
    c.nome AS campanha
FROM FormaPagamento f
JOIN Campanha c ON f.id_campanha = c.id_campanha;
