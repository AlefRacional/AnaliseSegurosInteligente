# Importação das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Função para carregar os dados de diferentes empresas
def carregar_dados(caminhos):
    dados_comb = pd.DataFrame()  # DataFrame vazio para combinar os dados
    for nome, caminho in caminhos.items():
        try:
            dados = pd.read_csv(caminho, sep=';', encoding='latin1')  # Lê os arquivos CSV
            dados['Empresa'] = nome  # Adiciona uma coluna para identificar a empresa
            dados_comb = pd.concat([dados_comb, dados], ignore_index=True)  # Combina os dados
        except FileNotFoundError:
            print(f"Erro: O arquivo '{caminho}' não foi encontrado.")
        except UnicodeDecodeError as e:
            print(f"Erro de codificação no arquivo '{caminho}': {e}")
        except Exception as e:
            print(f"Erro ao carregar o arquivo '{caminho}': {e}")
    return dados_comb

# Função para limpar e padronizar os dados
def limpar_dados(dados):
    # Renomeia colunas para garantir consistência
    colunas_renomeadas = {
        'Premium': 'Valor Contrato',  # Renomeia "Premium" para "Valor Contrato"
        'Product': 'Produto',        # Renomeia "Product" para "Produto"
        'Policy Date': 'Data Contrato',  # Renomeia "Policy Date" para "Data Contrato"
        'Profit': 'Lucro',           # Renomeia "Profit" para "Lucro"
        'Region': 'Região'           # Renomeia "Region" para "Região"
    }
    dados.rename(columns=colunas_renomeadas, inplace=True)

    colunas_criticas = ['Valor Contrato', 'Produto', 'Empresa']
    for coluna in colunas_criticas:
        if coluna not in dados.columns:
            print(f"Aviso: A coluna '{coluna}' não foi encontrada nos dados.")

    dados = dados.drop_duplicates()

    if 'Data Contrato' in dados.columns:
        dados['Data Contrato'] = pd.to_datetime(dados['Data Contrato'], dayfirst=True, errors='coerce')

    if 'Valor Contrato' in dados.columns:
        dados['Valor Contrato'] = pd.to_numeric(dados['Valor Contrato'], errors='coerce')

    if all(coluna in dados.columns for coluna in colunas_criticas):
        dados = dados.dropna(subset=colunas_criticas, how='any', axis=0)
    else:
        print("Erro: Algumas colunas críticas estão ausentes. Dados não podem ser processados.")

    return dados

# Função para criar gráfico de receita por produto
def grafico_receita_por_produto(dados):
    if 'Valor Contrato' in dados.columns and 'Produto' in dados.columns:
        receita = dados.groupby(['Empresa', 'Produto'])['Valor Contrato'].sum().unstack()
        receita.plot(kind='bar', figsize=(12, 6))
        plt.title('Receita Total por Produto e Empresa', fontsize=16)  # Título do gráfico em português
        plt.ylabel('Receita Total (CLP)', fontsize=12)  # Rótulo do eixo Y
        plt.xlabel('Empresas', fontsize=12)  # Rótulo do eixo X
        plt.legend(title='Produtos', fontsize=10)  # Título da legenda
        plt.tight_layout()
        plt.show()
    else:
        print("Erro: As colunas necessárias ('Valor Contrato' e 'Produto') não estão presentes nos dados.")

# Função para criar gráfico interativo de lucro por região
def grafico_interativo_lucro_por_regiao(dados):
    if 'Lucro' in dados.columns and 'Região' in dados.columns:
        lucro_regiao = dados.groupby(['Região', 'Empresa'])['Lucro'].sum().reset_index()
        fig = px.bar(
            lucro_regiao,
            x='Região',
            y='Lucro',
            color='Empresa',
            barmode='group',
            title='Lucro Total por Região e Empresa'  # Título do gráfico interativo em português
        )
        fig.update_layout(
            xaxis_title='Regiões',  # Rótulo do eixo X
            yaxis_title='Lucro Total (CLP)',  # Rótulo do eixo Y
            legend_title='Empresas'  # Título da legenda
        )
        fig.show()
    else:
        print("Erro: As colunas necessárias ('Lucro' e 'Região') não estão presentes nos dados.")

# Caminhos dos arquivos CSV
caminhos = {
    'AutoCare': 'dados/autocare_seguros.csv',
    'HealthPro': 'dados/healthpro_seguros.csv',
    'HomeGuard': 'dados/homeguard_seguros.csv'
}

# Carregar e limpar os dados
dados_combinados = carregar_dados(caminhos)

if dados_combinados.empty:
    print("Erro: Nenhum dado foi carregado. Verifique os arquivos CSV.")
else:
    print("Colunas disponíveis após carregar os dados:")
    print(dados_combinados.columns)

    dados_combinados = limpar_dados(dados_combinados)

    print("Colunas disponíveis no DataFrame após limpeza:")
    print(dados_combinados.columns)
    print(dados_combinados.head())

    if not dados_combinados.empty:
        grafico_receita_por_produto(dados_combinados)
        grafico_interativo_lucro_por_regiao(dados_combinados)
