USE sucos;

-- Modificando a tabela tb_produtos, produto num. 544931
-- Alterando o campo "embalagem" que estava com o valor 'GARRAFA'e colocando o valor "LATA"
-- E o campo "preco_lista", pondo valor "2.46"
-- OBSERVAÇÃO: 
	-- Sempre coloque UPDATE, SET e o WHERE!!!
	-- Se você rodar sem o WHERE ele mudará todos os resgistros!
UPDATE tb_produtos 
SET embalagem = 'Lata', preco_lista = 2.46
WHERE produto = '544931';

UPDATE tb_produtos
SET embalagem = 'Garrafa'
WHERE produto = '1078680';

-- Modificando tabela de vendedores
UPDATE tb_vendedores 
SET percentual_comissao = 0.11
WHERE matricula = '00236';

UPDATE tb_vendedores
SET nome = 'José Geraldo da Fonseca Junior'
WHERE matricula = '00233';

SELECT * FROM tb_produtos;
SELECT * FROM tb_vendedores;