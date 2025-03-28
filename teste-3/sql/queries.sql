-- Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?

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


