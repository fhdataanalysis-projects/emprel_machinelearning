# crie uma interface basica no streamlit
import streamlit as st


st.set_page_config(layout="wide")

st.title("Desafio CORETO - Cientista de Dados")
st.write("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

'### Previsão de Score'
'___'


# Criação de selectboxes para cada coluna
import streamlit as st
import pandas as pd
from joblib import load

# Carregar o pipeline salvo
modelo_carregado = load('notebooks/modelo_startup.pkl')

# expander com o formulário

with st.expander("Formulário de Avaliação da Startup", expanded=True):
    with st.form("formulario_startup"):
        startup_name = st.text_input("**Nome da Startup**")
        '####  Métricas Financeiras'
        col1, col2 = st.columns(2)
        with col1:
            faturamento_mensal = st.number_input("Faturamento Mensal", min_value=0.0, step=0.01, format="%.2f")
            faturamento_acumulado = st.number_input("Faturamento Acumulado", min_value=0.0, step=0.01, format="%.2f")
            ticket_medio = st.number_input("Ticket Médio", min_value=0.0, step=0.01, format="%.2f")
            mix_receita = st.selectbox("Mix de Receita", ['3–5 clientes >50%', 'Receita diversificada', '1–2 clientes >50%'])
        with col2:
            investimento_externo = st.selectbox("Investimento Externo", ['Série A+', 'Aceleradora/Anjo', 'Não', 'Seed/Pré-Série A'])
            governanca_financeira = st.selectbox("Governança Financeira", ['Não existem controles', 'DRE e auditoria', 'Controles básicos'])
            financas_unidade = st.selectbox("Finanças por Unidade", ['Algumas', 'Não', 'Sim, regularmente'])
        '---'
        "#### Clientes & Mercado"
        col1, col2 = st.columns(2)
        with col1:
            clientes_ativos = st.number_input("Clientes Ativos", min_value=0, step=1)
            churn = st.number_input("Percentual de Churn (%)", min_value=0.0, max_value=50.0, step=0.01, format="%.2f") / 100
            nps = st.number_input("NPS (Net Promoter Score)", min_value=-100.0, max_value=100.0, step=0.01, format="%.2f")
            canais_vendas = st.number_input("Número de Canais de Vendas", min_value=0, max_value=5, step=1)

        with col2:
            tipo_servico = st.selectbox("Tipo de Serviço", options=['Serviço', 'Produto'])
            branding_reputacao = st.selectbox("Branding e Reputação", ['Reconhecimento forte', 'Não reconhecida', 'Algum reconhecimento'])
            parcerias = st.selectbox("Parcerias", ['Algumas', 'Poucas', 'Muitas', 'Nenhuma'])
            network_time = st.selectbox("Network Time", ['Sim, forte', 'Ocasionalmente', 'Não'])
        '---'
        "#### Operacional & Produto"
        col1, col2 = st.columns(2)
        with col1:
            anos_empresa = st.number_input("Anos de Empresa", min_value=0, step=1)
            uso_tecnologia = st.selectbox("Uso de Tecnologia", ['Alto', 'Médio', 'Baixo'])
            roadmap_produto = st.selectbox("Roadmap do Produto", ['Parcial', 'Não existe', 'Claro e executado'])
        with col2:
            eficiencia_operacional = st.selectbox("Eficiência Operacional", ['Parcialmente', 'Quase tudo', 'Quase nada'])
            escala_tecnologica = st.selectbox("Escala Tecnológica", ['Parcialmente', 'Não', 'Sim'])
        '---'
        "#### Pessoas & Gestão"
        col1, col2 = st.columns(2)
        with col1:
            headcount = st.number_input("Headcount", min_value=0, step=1)
            rotatividade_time = st.number_input("Rotatividade do Time (%)", min_value=0.0, max_value=100.0, step=0.01, format="%.1f") / 100
        with col2:
            experiencia_lideranca = st.selectbox("Experiência de Liderança", ['Experiência forte', 'Sem experiência', 'Experiência parcial'])
            treinamento = st.selectbox("Frequência de Treinamentos", ['Às vezes', 'Regularmente', 'Nunca'])
        '---'
        # Botão de submissão

        submit = st.form_submit_button(" Enviar Respostas ")

        if submit:
            # Monta DataFrame com os dados do formulário
            dados_teste = pd.DataFrame([{
                'clientes_ativos': clientes_ativos,
                'faturamento_mensal': faturamento_mensal,
                'faturamento_acumulado': faturamento_acumulado,
                'anos_empresa': anos_empresa,
                'tipo_servico': tipo_servico,
                'ticket_medio': ticket_medio,
                'mix_receita': mix_receita,
                'canais_vendas': canais_vendas,
                'churn': churn,
                'parcerias': parcerias,
                'investimento_externo': investimento_externo,
                'branding_reputacao': branding_reputacao,
                'network_time': network_time,
                'uso_tecnologia': uso_tecnologia,
                'roadmap_produto': roadmap_produto,
                'nps': nps,
                'eficiencia_operacional': eficiencia_operacional,
                'escala_tecnologica': escala_tecnologica,
                'financas_unidade': financas_unidade,
                'headcount': headcount,
                'experiencia_lideranca': experiencia_lideranca,
                'treinamento': treinamento,
                'rotatividade_time': rotatividade_time,
                'governanca_financeira': governanca_financeira
            }])

            # Fazer previsão
            y_pred_novo = modelo_carregado.predict(dados_teste)

            st.success(f"✅ O Score previsto da Startup {startup_name}: {y_pred_novo[0]:.2f}")






