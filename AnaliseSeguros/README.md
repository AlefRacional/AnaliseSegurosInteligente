# **AnaliseSegurosInteligente**


**Ferramenta de análise inteligente para consolidar e visualizar dados financeiros de contratos de seguros.**  
Este programa permite consolidar dados de várias empresas, realizar limpeza e padronização de informações, e gerar gráficos estáticos e interativos para análise detalhada. É uma excelente opção para estudantes, novos usuários e profissionais do setor de seguros que desejam extrair insights estratégicos de seus dados.

---

### **Funcionalidades**
- **Carregamento de Dados:** Lê arquivos CSV de diferentes empresas e os combina em um único conjunto de dados.
- **Limpeza e Padronização:** Remove duplicatas, lida com valores ausentes e renomeia colunas para consistência.
- **Visualização de Dados:**
  - **Gráficos Estáticos:** Receita total por produto e empresa.
  - **Gráficos Interativos:** Lucro total por região e empresa.
- **Mensagens de Erro:** Identifica e notifica problemas relacionados à falta de arquivos ou colunas.

---

### **Pré-requisitos**
Antes de usar este programa, certifique-se de ter instalado:
- **Python** (versão 3.8 ou superior)
- Bibliotecas:
  - `pandas`
  - `matplotlib`
  - `plotly`

Para instalar as bibliotecas, use:
```bash
pip install pandas matplotlib plotly
