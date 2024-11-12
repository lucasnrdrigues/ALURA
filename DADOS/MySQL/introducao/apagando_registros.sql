-- Apagando registros 

-- DELETE FROM tb_produtos : isso apagara todos os registros da tabela!

-- Use o WHERE para apagar um registro específico!
DELETE FROM tb_produtos WHERE produto = '1078680';

DELETE FROM tb_vendedores WHERE matricula = '00233';

SELECT * FROM tb_produtos;
SELECT * FROM tb_vendedores;