SELECT
    c.id_campanha,
    c.nome AS nome_campanha,
    c.descricao,
    p.nome AS pessoa_responsavel, -- Nome do criador/responsável único
    c.data_inicio,
    c.data_fim,
    c.status,
    -- Métricas de Doação
    COUNT(d.id_doacao) AS total_de_doacoes,
    COALESCE(SUM(d.valor), 0.00) AS valor_total_arrecadado
FROM
    Campanha c
-- 1. JOIN para obter o NOME da Pessoa Responsável (criador da campanha)
LEFT JOIN
    Pessoa p ON c.id_pessoa = p.id_pessoa -- ASSUME que 'id_pessoa' está na tabela Campanha
-- 2. LEFT JOIN para obter as Doações e agregá-las
LEFT JOIN
    Doacao d ON c.id_campanha = d.id_campanha
WHERE
    c.status = TRUE -- Filtra apenas campanhas ativas
GROUP BY
    c.id_campanha, c.nome, c.descricao, p.nome, c.data_inicio, c.data_fim, c.status
ORDER BY
    valor_total_arrecadado DESC, c.nome;