CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    DATA DATE,
    REG_ANS VARCHAR(10),
    CD_CONTA_CONTABIL INTEGER,
    DESCRICAO TEXT,
    VL_SALDO_INICIAL NUMERIC,
    VL_SALDO_FINAL NUMERIC
);

CREATE TABLE IF NOT EXISTS op_plano_de_saude (
    Registro_ANS VARCHAR(10),
    CNPJ BIGINT,
    Razao_Social TEXT,
    Nome_Fantasia TEXT,
    Modalidade TEXT,
    Logradouro TEXT,
    Numero INTEGER,
    Complemento TEXT,
    Bairro TEXT,
    Cidade TEXT,
    UF VARCHAR(2),
    CEP VARCHAR(8),
    DDD VARCHAR(2),
    Telefone VARCHAR(8),
    Fax VARCHAR(8),
    Endereco_eletronico TEXT,
    Representante TEXT,
    Cargo_Representante TEXT,
    Regiao_de_Comercializacao INTEGER,
    Data_Registro_ANS DATE
);

