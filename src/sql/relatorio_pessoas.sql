SELECT
    p.id_pessoa,
    p.nome,
    p.cpf,
    p.tipo_pessoa
FROM
    Pessoa p
ORDER BY
    p.nome;