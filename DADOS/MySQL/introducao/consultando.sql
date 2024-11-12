SELECT * FROM tbcliente;
SELECT cpf, nome, endereco01, endereco02 FROM tbcliente LIMIT 5;

-- Usando nome fantasia para uma determinada coluna
SELECT CPF AS cpf_cliente FROM tbcliente;
SELECT CPF AS cpf_cliente, nome AS nome_cliente FROM tbcliente;