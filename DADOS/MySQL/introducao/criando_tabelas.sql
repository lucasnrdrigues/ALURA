-- Criando tabelas 
CREATE TABLE tb_cliente3 (
	cpf VARCHAR(11),
    nome VARCHAR(100),
    endereco01 VARCHAR(150),
    endereco02 VARCHAR(150),
    bairro VARCHAR(150),
    cidade VARCHAR(150),
    estado VARCHAR(150),
    cep VARCHAR(8),
    idade SMALLINT,
    sexo VARCHAR(1),
    limite_credito FLOAT,
    volume_compra FLOAT,
    primeira_compra BIT(1)
    );
    
    CREATE TABLE tb_vendedores (
			matricula VARCHAR(5),
            nome VARCHAR(100),
            percentual_comissao FLOAT
    );
    
    
