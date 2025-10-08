-- Lista de doações com dados de pessoa, campanha e recibo
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

-- Campanhas com tipos de doação aceitos
SELECT 
    c.nome AS campanha,
    td.descricao AS tipo_doacao
FROM Campanha c
JOIN CampanhaTipoDoacao ctd ON c.id_campanha = ctd.id_campanha
JOIN TipoDoacao td ON ctd.id_tipo = td.id_tipo;

-- Campanhas com formas de pagamento aceitas
SELECT 
    c.nome AS campanha,
    fp.forma_pagamento
FROM Campanha c
JOIN CampanhaFormaPagamento cfp ON c.id_campanha = cfp.id_campanha
JOIN FormaPagamento fp ON cfp.id_forma = fp.id_forma;
