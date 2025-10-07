-- View de doações completas
CREATE OR REPLACE VIEW vw_doacoes AS
SELECT 
    d.id_doacao,
    p.nome AS doador,
    c.nome AS campanha,
    d.valor,
    d.data_doacao,
    r.codigo_validacao AS recibo
FROM Doacao d
JOIN Pessoa p ON d.id_pessoa = p.id_pessoa
JOIN Campanha c ON d.id_campanha = c.id_campanha
LEFT JOIN Recibo r ON d.id_doacao = r.id_doacao;

-- View de campanhas com status e tipos de doação
CREATE OR REPLACE VIEW vw_campanhas AS
SELECT 
    c.id_campanha,
    c.nome AS campanha,
    s.descricao AS status,
    STRING_AGG(td.descricao, ', ') AS tipos_doacao
FROM Campanha c
LEFT JOIN Status s ON c.id_status = s.id_statuscampanha
LEFT JOIN CampanhaTipoDoacao ctd ON c.id_campanha = ctd.id_campanha
LEFT JOIN TipoDoacao td ON ctd.id_tipo = td.id_tipo
GROUP BY c.id_campanha, c.nome, s.descricao;

CREATE OR REPLACE VIEW vw_doacoes_completas AS
SELECT
    p.nome AS nome_pessoa,
    td.descricao AS tipo_doacao,
    d.valor,
    c.nome AS campanha
FROM Doacao d
JOIN Pessoa p ON d.id_pessoa = p.id_pessoa
JOIN TipoDoacao td ON d.id_tipo = td.id_tipo
JOIN Campanha c ON d.id_campanha = c.id_campanha;
