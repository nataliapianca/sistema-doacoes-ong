INSERT INTO Status (descricao) VALUES
('Ativa'),
('Encerrada'),
('Pausada');

INSERT INTO Pessoa (nome, cpf, email, senha, tipo_pessoa) VALUES
('João Silva', '123.456.789-00', 'joao@email.com', 'senha123', 'doador'),
('Maria Souza', '987.654.321-00', 'maria@email.com', 'senha456', 'usuario'),
('Carlos Lima', '111.222.333-44', 'carlos@email.com', 'senha789', 'doador');

INSERT INTO Endereco (id_pessoa, logradouro, numero, complemento, bairro, cidade, estado, cep) VALUES
(1, 'Rua A', '123', 'Apto 101', 'Centro', 'São Paulo', 'SP', '01000-000'),
(2, 'Av. B', '456', '', 'Jardins', 'Rio de Janeiro', 'RJ', '20000-000'),
(3, 'Rua C', '789', 'Casa', 'Mooca', 'São Paulo', 'SP', '03100-000');

INSERT INTO Campanha (id_pessoa, nome, descricao, data_inicio, data_fim, id_status) VALUES
(2, 'Campanha do Agasalho', 'Arrecadação de roupas para pessoas carentes.', '2025-06-01', '2025-07-31', 1),
(2, 'Campanha Alimentar', 'Distribuição de cestas básicas.', '2025-08-01', '2025-09-30', 1);

INSERT INTO FormaPagamento (forma_pagamento) VALUES
('Cartão de Crédito'),
('Pix'),
('Boleto Bancário');

INSERT INTO TipoDoacao (descricao) VALUES
('Dinheiro'),
('Roupas'),
('Alimentos');

INSERT INTO Doacao (id_pessoa, id_campanha, id_forma, id_tipo, valor, data_doacao) VALUES
(1, 1, 2, 1, 150.00, '2025-06-15 10:30:00'),
(3, 2, 1, 3, 0, '2025-08-05 15:45:00');  -- 0 no valor porque é doação de alimento

INSERT INTO Recibo (id_doacao, data_emissao, codigo_validacao) VALUES
(1, '2025-06-15 11:00:00', gen_random_uuid()),
(2, '2025-08-05 16:00:00', gen_random_uuid());

INSERT INTO CampanhaTipoDoacao (id_campanha, id_tipo) VALUES
(1, 1),
(1, 2),
(2, 3);

INSERT INTO CampanhaFormaPagamento (id_campanha, id_forma) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 3);
