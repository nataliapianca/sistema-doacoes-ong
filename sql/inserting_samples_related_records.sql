-- ======================================
-- CAMPANHAS
-- ======================================
-- Campanha 1
INSERT INTO campanha (id_usuario, nome, descricao, data_inicio, data_fim, id_status)
VALUES (1, 'Campanha Alimento', 'Arrecadação de alimentos para famílias carentes', '2025-10-01', '2025-12-31', 1)
RETURNING id_campanha;

-- Campanha 2
INSERT INTO campanha (id_usuario, nome, descricao, data_inicio, data_fim, id_status)
VALUES (2, 'Campanha Roupas', 'Doação de roupas para pessoas em vulnerabilidade', '2025-09-15', '2025-11-30', 1)
RETURNING id_campanha;

-- ======================================
-- DOAÇÕES
-- ======================================
-- Doações para Campanha 1
INSERT INTO doacao (id_doador, id_campanha, id_forma, id_tipo, valor)
VALUES 
(1, 1, 1, 1, 100.00),   -- João Gabriel doa dinheiro via pix
(2, 1, 2, 1, 200.00);   -- João Guilherme doa dinheiro via cartão

-- Doações para Campanha 2
INSERT INTO doacao (id_doador, id_campanha, id_forma, id_tipo, valor)
VALUES 
(3, 2, 1, 3, 0.00),    -- João José doa roupas via pix
(4, 2, 3, 3, 0.00);    -- José Antônio doa roupas via boleto

-- ======================================
-- RECIBOS
-- ======================================
-- Gera recibos automaticamente para todas as doações inseridas
INSERT INTO recibo (id_doacao)
SELECT id_doacao FROM doacao;

COMMIT;