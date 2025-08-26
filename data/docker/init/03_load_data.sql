COPY bronze.empresas(
  clientes_ativos, faturamento_mensal, faturamento_acumulado,
  anos_empresa, tipo_servico, ticket_medio, mix_receita,
  canais_vendas, churn, parcerias, investimento_externo,
  branding_reputacao, network_time, uso_tecnologia,
  roadmap_produto, nps, eficiencia_operacional,
  escala_tecnologica, financas_unidade, headcount,
  experiencia_lideranca, treinamento, rotatividade_time,
  governanca_financeira, score_total
)
FROM '/csv/base_maturidade_final2.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',', ENCODING 'UTF8', QUOTE '"');
