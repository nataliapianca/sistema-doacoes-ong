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

COMMIT;
