-- Fazendo alterações

-- Adicionando uma chave primária
ALTER TABLE tb_clientes
ADD PRIMARY KEY(cpf);

-- Adicionando nova coluna
ALTER TABLE tb_clientes
ADD COLUMN (data_nascimento DATE);

-- Inserindo alguns dados
INSERT INTO tb_clientes (cpf, nome, endereco01, endereco02, bairro, 
cidade, estado, cep, idade, sexo, limite_credito, volume_compra, 
primeira_compra, data_nascimento) 
VALUES ('00388934505', 'João da Silva', 'Rua projetada A número 10', 
'', 'Vila Roman', 'Caratinga', 'Amazonas', '2222222', 30, 'M', 10000.00,
2000, 0, '1989-10-05');
-- Representação no MySQL para representar data, nos a tratamos como string, por isso colocamos entre aspas!

 
CREATE TABLE tb_vendedores(
	matricula VARCHAR(5),
	nome VARCHAR(100),
	percentual_comissao FLOAT,
	data_admissao DATE,
	de_ferias BIT,

	PRIMARY KEY(matricula)
);
 
INSERT INTO tb_vendedores(matricula, nome, percentual_comissao, data_admissao, de_ferias)
VALUES ('00235', 'Márcio Almeida Silva', 0.08 ,'2014-08-15', 0),
	('00236', 'Cláudia Morais', 0.08, '2013-09-17', 1),
    ('00237', 'Roberta Martins', 0.11, '2017-03-18', 1),
    ('00238', 'Pericles Alves', 0.11, '2016-08-21', 0);
 
SELECT * FROM tb_vendedores;
SELECT * FROM tb_clientes;

