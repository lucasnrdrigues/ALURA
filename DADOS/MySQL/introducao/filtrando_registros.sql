-- Filtrando Registros
SELECT * FROM tbproduto WHERE PRODUTO = '544931';

-- Usando Maior 
SELECT * FROM tbcliente WHERE idade > 22;

-- Usando menor 
SELECT * FROM tbcliente WHERE idade < 22;
-- Usando menor ou igual a 22
SELECT * FROM tbcliente WHERE idade <= 22;

-- Usando AND e OR
SELECT * FROM tbproduto WHERE EMBALAGEM = 'Garrafa' AND SABOR = 'Manga';
SELECT * FROM tbproduto WHERE EMBALAGEM = 'Garrafa' OR SABOR = 'Manga';

-- OBS
-- Se usar o igual e o diferente ( =, <> ) como condição para achar valores do tipo FLOAT ele não trará nada como resultado!
-- Se for usar uso, use o tipo do valor como DECIMAL!
-- Exemplo do código que dará erro:
SELECT * FROM tbproduto WHERE preco_lista = 16.008;

-- Se for pegar exatamente o número que for 16.008 devemos fazer:
SELECT * FROM tbproduto WHERE preco_lista BETWEEN 16.007 AND 16.009;

-- Filtrando datas
-- Poderiamos usar qualquer outro operador ou ate mesmo o between, and e or como nas consulta
SELECT * FROM tbcliente WHERE data_nascimento = '1995-01-13';

-- usando uma função para saber os anos
SELECT * FROM tb_vendedores WHERE YEAR(data_admissao) >= 2016;
