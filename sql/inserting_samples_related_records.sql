

-- ======================================
-- CAMPANHAS
-- ======================================

INSERT INTO campanha (
    id_pessoa, nome, descricao, data_inicio, data_fim, id_status
)
VALUES 
(
    1, 
    'Campanha Alimento', 
    'Arrecadação de alimentos para famílias carentes', 
    '2025-10-01', 
    '2025-12-31', 
    1
)
RETURNING id_campanha;


INSERT INTO campanha (
    id_pessoa, nome, descricao, data_inicio, data_fim, id_status
)
VALUES 
(
    2, 
    'Campanha Roupas', 
    'Doação de roupas para pessoas em vulnerabilidade', 
    '2025-09-15', 
    '2025-11-30', 
    1
)
RETURNING id_campanha;

-- ======================================
-- DOAÇÕES
-- ======================================


INSERT INTO doacao (
    id_doador, id_campanha, id_forma, id_tipo, valor
)
VALUES 
(3, 1, 1, 1, 100.00),   
(4, 1, 2, 1, 200.00);   


INSERT INTO doacao (
    id_doador, id_campanha, id_forma, id_tipo, valor
)
VALUES 
(5, 2, 1, 3, 0.00),     
(6, 2, 3, 3, 0.00);     

-- ======================================
-- RECIBOS (um para cada doação feita)
-- ======================================
INSERT INTO recibo (id_doacao)
SELECT id_doacao FROM doacao;

COMMIT;