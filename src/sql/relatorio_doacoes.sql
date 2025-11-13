SELECT
    d.id_doacao,
    p.nome AS nome_doador,
    p.cpf,
    c.id_campanha,
    c.nome AS nome_campanha,
    d.valor AS valor_doacao,
    d.data_doacao
FROM
    Doacao d
INNER JOIN
    Pessoa p ON d.id_pessoa = p.id_pessoa      -- JOIN com Pessoa para obter o nome do doador
INNER JOIN
    Campanha c ON d.id_campanha = c.id_campanha  -- JOIN com Campanha para obter o nome da campanha
ORDER BY
    d.data_doacao DESC, nome_doador;