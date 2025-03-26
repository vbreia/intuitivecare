-- Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?

-- Crio um CTE para rodar TRIM na descrição, pois a descrição tem espaços em branco e alguns problemas no texto que poderiam atrapalhar a busca
-- JOIN com a tabela de operadoras para pegar o nome da operadora
-- WHERE para pegar apenas as linhas que tem a descrição da categoria pedida, mas para evitar problemas com acentos e maiúsculas e minúsculas, uso LIKE com % a partir do momento que a descrição difere de outros Eventos/Sinistros
-- uma subquery para pegar as datas dos últimos 3 meses
-- GROUP BY para agrupar por operadora
-- ORDER BY para ordenar por Total_Despesas
-- LIMIT para pegar apenas as 10 primeiras linhas

with cte as (
SELECT trim(dc.descricao) as descricao ,dc.reg_ans , dc.VL_SALDO_FINAL, dc.VL_SALDO_INICIAL, dc.data
FROM demonstracoes_contabeis dc
) 
SELECT op.Razao_Social, SUM(dc.VL_SALDO_FINAL - dc.VL_SALDO_INICIAL) AS Total_Despesas
FROM cte dc
JOIN op_plano_de_saude op ON dc.REG_ANS = op.Registro_ANS
WHERE dc.DESCRICAO like '%DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
AND dc.data in (select distinct data from demonstracoes_contabeis
order by data desc limit 3)
GROUP BY op.Razao_Social
ORDER BY Total_Despesas DESC
limit 10;

-- Quais as 10 operadoras com maiores despesas nessa categoria no último ano?
-- Faço a mesma query anterior, mas na subquery, pego apenas as datas do último ano (datas posteriores a janeiro de 2024)

with cte as (
SELECT trim(dc.descricao) as descricao ,dc.reg_ans , dc.VL_SALDO_FINAL, dc.VL_SALDO_INICIAL, dc.data
FROM demonstracoes_contabeis dc
) 
SELECT op.Razao_Social, SUM(dc.VL_SALDO_FINAL - dc.VL_SALDO_INICIAL) AS Total_Despesas
FROM cte dc
JOIN op_plano_de_saude op ON dc.REG_ANS = op.Registro_ANS
WHERE dc.DESCRICAO like '%DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
AND dc.data >= '2024-01-01'
GROUP BY op.Razao_Social
ORDER BY Total_Despesas DESC
limit 10;


