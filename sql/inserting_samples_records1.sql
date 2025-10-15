<<<<<<< HEAD
-- TABELA Pessoa
INSERT INTO Pessoa (nome, cpf, email, senha, tipo_pessoa)
VALUES
('João Gabriel', '01234567891', 'joao.gabriel@email.com', '123', 'doador'),
('Maria Clara', '20123456789', 'maria.clara@email.com', '123', 'usuario'),
('José Carlos', '32012345678', 'jose.carlos@email.com', '123', 'doador'),
('Antônio Marcos', '43201234567', 'antonio.marcos@email.com', '123', 'usuario'),
('Carla Souza', '54320123456', 'carla.souza@email.com', '123', 'doador');


-- TABELA Campanha
INSERT INTO Campanha (nome, descricao, data_inicio, data_fim, status, id_pessoa, formaPagamento)
VALUES
('Ajuda ao Lar dos Idosos', 'Campanha de arrecadação de alimentos e roupas.', '2025-09-01', '2025-12-31', TRUE, (SELECT id_pessoa FROM Pessoa WHERE nome='Maria Clara'), 'PIX'),
('Doe Esperança', 'Campanha de arrecadação para crianças carentes.', '2025-08-01', '2025-11-30', TRUE, (SELECT id_pessoa FROM Pessoa WHERE nome='Antônio Marcos'), 'Cartão de Crédito'),
('Natal Solidário', 'Arrecadação de brinquedos para o Natal.', '2025-10-01', '2025-12-20', TRUE, (SELECT id_pessoa FROM Pessoa WHERE nome='Maria Clara'), 'Dinheiro');


-- TABELA FormaPagamento
INSERT INTO FormaPagamento (descricao, id_campanha, id_pessoa)
VALUES
('PIX', (SELECT id_campanha FROM Campanha WHERE nome='Ajuda ao Lar dos Idosos'), (SELECT id_pessoa FROM Pessoa WHERE nome='Maria Clara')),
('Cartão de Crédito', (SELECT id_campanha FROM Campanha WHERE nome='Ajuda ao Lar dos Idosos'), (SELECT id_pessoa FROM Pessoa WHERE nome='Maria Clara')),
('Transferência Bancária', (SELECT id_campanha FROM Campanha WHERE nome='Doe Esperança'), (SELECT id_pessoa FROM Pessoa WHERE nome='Antônio Marcos')),
('Dinheiro', (SELECT id_campanha FROM Campanha WHERE nome='Natal Solidário'), (SELECT id_pessoa FROM Pessoa WHERE nome='Maria Clara'));


-- TABELA Doacao
INSERT INTO Doacao (id_pessoa, id_campanha, valor)
VALUES
((SELECT id_pessoa FROM Pessoa WHERE nome='João Gabriel'), (SELECT id_campanha FROM Campanha WHERE nome='Ajuda ao Lar dos Idosos'), 150.00),
((SELECT id_pessoa FROM Pessoa WHERE nome='José Carlos'), (SELECT id_campanha FROM Campanha WHERE nome='Doe Esperança'), 200.00),
((SELECT id_pessoa FROM Pessoa WHERE nome='Carla Souza'), (SELECT id_campanha FROM Campanha WHERE nome='Natal Solidário'), 100.00),
((SELECT id_pessoa FROM Pessoa WHERE nome='João Gabriel'), (SELECT id_campanha FROM Campanha WHERE nome='Doe Esperança'), 50.00);


-- TABELA Recibo
INSERT INTO Recibo (id_doacao, id_pessoa, id_campanha, codigo_validacao)
VALUES (
    (SELECT id_doacao FROM Doacao WHERE id_pessoa=(SELECT id_pessoa FROM Pessoa WHERE nome='João Gabriel') AND id_campanha=(SELECT id_campanha FROM Campanha WHERE nome='Ajuda ao Lar dos Idosos')),
    (SELECT id_pessoa FROM Doacao WHERE id_pessoa=(SELECT id_pessoa FROM Pessoa WHERE nome='João Gabriel') AND id_campanha=(SELECT id_campanha FROM Campanha WHERE nome='Ajuda ao Lar dos Idosos')),
    (SELECT id_campanha FROM Doacao WHERE id_pessoa=(SELECT id_pessoa FROM Pessoa WHERE nome='João Gabriel') AND id_campanha=(SELECT id_campanha FROM Campanha WHERE nome='Ajuda ao Lar dos Idosos')),
    gen_random_uuid()
);
=======
-- ======================================
-- INSERE PESSOAS
-- ======================================
INSERT INTO pessoa (nome, cpf, email, senha, perfil, tipo_pessoa) VALUES 
('JOÃO GABRIEL', '01234567891', 'joao.gabriel@email.com', 'senha123', 'admin', 'usuario'),
('JOÃO GUILHERME', '20123456789', 'joao.guilherme@email.com', 'senha123', 'usuario', 'usuario'),
('JOÃO JOSÉ', '32012345678', 'joao.jose@email.com', 'senha123', 'doador', 'doador'),
('JOSÉ ANTÔNIO', '43201234567', 'jose.antonio@email.com', 'senha123', 'doador', 'doador'),
('JOSÉ CARLOS', '54320123456', 'jose.carlos@email.com', 'senha123', 'doador', 'doador'),
('ANTÔNIO CARLOS', '65432012345', 'antonio.carlos@email.com', 'senha123', 'doador', 'doador'),
('CARLOS ANTÔNIO', '76543201234', 'carlos.antonio@email.com', 'senha123', 'doador', 'doador'),
('MARCO ANTÔNIO', '87654320123', 'marco.antonio@email.com', 'senha123', 'doador', 'doador');

-- ======================================
-- INSERE STATUS DE CAMPANHA
-- ======================================
INSERT INTO status_campanha (descricao) VALUES 
('ativa'), 
('finalizada'), 
('cancelada');

-- ======================================
-- INSERE FORMAS DE PAGAMENTO
-- ======================================
INSERT INTO forma_pagamento (descricao) VALUES 
('pix'), 
('cartão'), 
('boleto');

-- ======================================
-- INSERE TIPOS DE DOAÇÃO
-- ======================================
INSERT INTO tipo_doacao (descricao) VALUES 
('dinheiro'), 
('alimento'), 
('roupa');

-- ======================================
-- INSERE CAMPANHAS
-- Apenas pessoas com tipo_pessoa = 'usuario' devem criar campanhas (id 1 e 2)
-- ======================================
INSERT INTO campanha (id_pessoa, nome, descricao, data_inicio, data_fim, id_status) VALUES
(1, 'Campanha Alimento', 'Arrecadação de alimentos para famílias carentes', '2025-10-01', '2025-12-31', 1),
(2, 'Campanha Roupas', 'Doação de roupas para pessoas em situação de vulnerabilidade', '2025-09-15', '2025-11-30', 1);

-- ======================================
-- INSERE DOAÇÕES
-- Apenas pessoas com tipo_pessoa = 'doador' devem doar (id 3 a 8)
-- ======================================
INSERT INTO doacao (id_doador, id_campanha, id_forma, id_tipo, valor, data_doacao) VALUES
(3, 1, 1, 1, 100.00, CURRENT_TIMESTAMP),
(4, 1, 2, 1, 200.00, CURRENT_TIMESTAMP),
(5, 2, 1, 3, 0.00, CURRENT_TIMESTAMP),
(6, 2, 3, 3, 0.00, CURRENT_TIMESTAMP);

-- ======================================
-- INSERE RECIBOS
-- ======================================
INSERT INTO recibo (id_doacao) VALUES
(1),
(2),
(3),
(4);
>>>>>>> bfe45d602936e22027711c96504d38cbfbf142e1

COMMIT;
