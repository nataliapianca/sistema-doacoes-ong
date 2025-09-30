-- ======================================
-- INSERE PESSOAS
-- ======================================
INSERT INTO pessoa (nome, cpf, email) VALUES 
('JOÃO GABRIEL', '01234567891', 'joao.gabriel@email.com'),
('JOÃO GUILHERME', '20123456789', 'joao.guilherme@email.com'),
('JOÃO JOSÉ', '32012345678', 'joao.jose@email.com'),
('JOSÉ ANTÔNIO', '43201234567', 'jose.antonio@email.com'),
('JOSÉ CARLOS', '54320123456', 'jose.carlos@email.com'),
('ANTÔNIO CARLOS', '65432012345', 'antonio.carlos@email.com'),
('CARLOS ANTÔNIO', '76543201234', 'carlos.antonio@email.com'),
('MARCO ANTÔNIO', '87654320123', 'marco.antonio@email.com');

-- ======================================
-- INSERE DOADORES (todas as pessoas são doadores)
-- ======================================
INSERT INTO doador (id_pessoa) VALUES (1),(2),(3),(4),(5),(6),(7),(8);

-- ======================================
-- INSERE USUÁRIOS (quem pode criar campanhas)
-- ======================================
INSERT INTO usuario (id_pessoa, senha, perfil) VALUES 
(1, 'senha123', 'admin'),
(2, 'senha123', 'usuario');

-- ======================================
-- INSERE STATUS DE CAMPANHA
-- ======================================
INSERT INTO status_campanha (descricao) VALUES 
('ativa'), ('finalizada'), ('cancelada');

-- ======================================
-- INSERE FORMAS DE PAGAMENTO
-- ======================================
INSERT INTO forma_pagamento (descricao) VALUES 
('pix'), ('cartão'), ('boleto');

-- ======================================
-- INSERE TIPOS DE DOAÇÃO
-- ======================================
INSERT INTO tipo_doacao (descricao) VALUES 
('dinheiro'), ('alimento'), ('roupa');

-- ======================================
-- INSERE CAMPANHAS
-- ======================================
INSERT INTO campanha (id_usuario, nome, descricao, data_inicio, data_fim, id_status) VALUES
(1, 'Campanha Alimento', 'Arrecadação de alimentos para famílias carentes', '2025-10-01', '2025-12-31', 1),
(2, 'Campanha Roupas', 'Doação de roupas para pessoas em situação de vulnerabilidade', '2025-09-15', '2025-11-30', 1);

-- ======================================
-- INSERE DOAÇÕES
-- ======================================
INSERT INTO doacao (id_doador, id_campanha, id_forma, id_tipo, valor, data_doacao) VALUES
(1, 1, 1, 1, 100.00, CURRENT_TIMESTAMP),
(2, 1, 2, 1, 200.00, CURRENT_TIMESTAMP),
(3, 2, 1, 3, 0.00, CURRENT_TIMESTAMP),
(4, 2, 3, 3, 0.00, CURRENT_TIMESTAMP);

-- ======================================
-- INSERE RECIBOS
-- ======================================
INSERT INTO recibo (id_doacao) VALUES
(1),
(2),
(3),
(4);

COMMIT;