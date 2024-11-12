-- Incluindo chave primária associada à tabela de produtos
ALTER TABLE tb_produtos 
ADD PRIMARY KEY (produto);

INSERT INTO tb_produtos (produto, nome, embalagem, tamanho, sabor, preco_lista)
VALUES ('1078680', 'Frescor do Verão - 470ml - Manga', 'Garrafa', '470ml', 'Manga', 5.18);

SELECT * FROM tb_produtos;