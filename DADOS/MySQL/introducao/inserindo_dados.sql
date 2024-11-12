USE sucos;

-- Primeira forma de inserir dados:  
-- String: aspas simples ou duplas!
-- Numeros quebrados utilza-se ponto! 
INSERT INTO tb_produtos (
	produto, 
    nome, 
    embalagem, 
	tamanho, 
    sabor, 
    preco_lista
    ) VALUES (
	'1040107',
    'Light - 350ml - Melância',
    'Lata',
    '350ml',
    'Melância',
    4.56);

-- Inserindo Vários registros
-- Tabela de Produtos
INSERT INTO tb_produtos (produto, nome, embalagem, tamanho, sabor, preco_lista)
VALUES ('1037797', 'Clean - 2 Litros - Laranja', 'PET', '2 Litros', 'Laranja', 16.01);

INSERT INTO tb_produtos (produto, nome, embalagem, tamanho, sabor, preco_lista)
VALUES ('1000889', 'Sabor da Montanha - 700ml - Uva', 'Garrafa', '700ml', 'Uva', 6.31);

INSERT INTO tb_produtos (produto, nome, embalagem, tamanho, sabor, preco_lista)
VALUES ('1004327', 'Videira do Campo', 'PET', '1,5 Litros', 'Melância', 19.51);

INSERT INTO tb_produtos (produto,  nome, embalagem, tamanho, sabor, preco_lista) 
VALUES ('544931', 'Frescor do Verão - 350 ml - Limão', 'PET', '350 ml','Limão',3.20);

INSERT INTO tb_produtos (produto,  nome, embalagem, tamanho, sabor, preco_lista) 
VALUES ('1078680', 'Frescor do Verão - 470 ml - Manga', 'Lata', '470 ml','Manga',5.18);


-- Tabela de vendedores
INSERT INTO tb_vendedores (matricula, nome, percentual_comissao)
VALUES ('00233', 'João Geraldo da Fonseca', 0.10);

INSERT INTO tb_vendedores (matricula, nome, percentual_comissao)
VALUES ('00235', 'Márcio Almeida Silva', 0.08);

INSERT INTO tb_vendedores (matricula, nome, percentual_comissao)
VALUES ('00236', 'Cláudia Morais', 0.08);

SELECT * FROM tb_produtos;
SELECT * FROM tb_vendedores;

    

    