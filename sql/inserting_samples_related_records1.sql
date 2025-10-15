
<<<<<<< HEAD
-- INSERE DADOS NAS TABELAS PRINCIPAIS

DO $$
DECLARE
    v_id_pessoa INT;
    v_id_campanha INT;
    v_id_doacao INT;
BEGIN

    -- DOAÇÃO 1
    v_id_pessoa := (SELECT id_pessoa FROM Pessoa WHERE cpf='01234567891');  -- João Gabriel
    v_id_campanha := (SELECT id_campanha FROM Campanha WHERE nome='Ajuda ao Lar dos Idosos');

    INSERT INTO Doacao (id_pessoa, id_campanha, valor)
    VALUES (v_id_pessoa, v_id_campanha, 150.00)
    RETURNING id_doacao INTO v_id_doacao;

    INSERT INTO Recibo (id_doacao, id_pessoa, id_campanha, codigo_validacao)
    VALUES (v_id_doacao, v_id_pessoa, v_id_campanha, gen_random_uuid());


    -- DOAÇÃO 2
    v_id_pessoa := (SELECT id_pessoa FROM Pessoa WHERE cpf='32012345678');  -- José Carlos
    v_id_campanha := (SELECT id_campanha FROM Campanha WHERE nome='Doe Esperança');

    INSERT INTO Doacao (id_pessoa, id_campanha, valor)
    VALUES (v_id_pessoa, v_id_campanha, 200.00)
    RETURNING id_doacao INTO v_id_doacao;

    INSERT INTO Recibo (id_doacao, id_pessoa, id_campanha, codigo_validacao)
    VALUES (v_id_doacao, v_id_pessoa, v_id_campanha, gen_random_uuid());


    -- DOAÇÃO 3
    v_id_pessoa := (SELECT id_pessoa FROM Pessoa WHERE cpf='54320123456');  -- Carla Souza
    v_id_campanha := (SELECT id_campanha FROM Campanha WHERE nome='Natal Solidário');

    INSERT INTO Doacao (id_pessoa, id_campanha, valor)
    VALUES (v_id_pessoa, v_id_campanha, 100.00)
    RETURNING id_doacao INTO v_id_doacao;

    INSERT INTO Recibo (id_doacao, id_pessoa, id_campanha, codigo_validacao)
    VALUES (v_id_doacao, v_id_pessoa, v_id_campanha, gen_random_uuid());


    -- DOAÇÃO 4
    v_id_pessoa := (SELECT id_pessoa FROM Pessoa WHERE cpf='01234567891');  -- João Gabriel
    v_id_campanha := (SELECT id_campanha FROM Campanha WHERE nome='Doe Esperança');

    INSERT INTO Doacao (id_pessoa, id_campanha, valor)
    VALUES (v_id_pessoa, v_id_campanha, 50.00)
    RETURNING id_doacao INTO v_id_doacao;

    INSERT INTO Recibo (id_doacao, id_pessoa, id_campanha, codigo_validacao)
    VALUES (v_id_doacao, v_id_pessoa, v_id_campanha, gen_random_uuid());

END
$$;
=======

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
>>>>>>> bfe45d602936e22027711c96504d38cbfbf142e1
