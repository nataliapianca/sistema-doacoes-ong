SELECT
    c.id_campanha,
    c.nome AS nome_campanha,
    c.data_inicio,
    c.data_fim,
    COUNT(d.id_doacao) AS total_de_doacoes,      -- Função Agregada: Conta o número de doações
    SUM(d.valor) AS valor_total_arrecadado       -- Função Agregada: Soma o valor das doações
FROM
    Campanha c
INNER JOIN
    Doacao d ON c.id_campanha = d.id_campanha
WHERE
    c.status = TRUE -- Filtra apenas campanhas ativas
GROUP BY
    c.id_campanha, c.nome, c.data_inicio, c.data_fim -- Agrupa por Campanha para sumarizar
ORDER BY
    valor_total_arrecadado DESC;