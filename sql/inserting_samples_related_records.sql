
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
