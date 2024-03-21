import pandas as pd

# Carregando o arquivo CSV em um DataFrame
file_path = "dados-venda.csv"
df = pd.read_csv(file_path)

# Visualizando as primeiras linhas do DataFrame para verificar os dados
print(df.head())

# Calculando o total de vendas por produto
total_sales_by_product = df.groupby('Produto')['Valor'].sum()

# Extraindo o mês da coluna 'Data'
df['Mes'] = pd.to_datetime(df['Data']).dt.month

# Calculando o total de vendas por mês
total_sales_by_month = df.groupby('Mes')['Valor'].sum()

# Visualizando os resultados das transformações
print("Total de Vendas por Produto:")
print(total_sales_by_product)

print("\nTotal de Vendas por Mês:")
print(total_sales_by_month)

# Salvando os dados transformados em um arquivo CSV
total_sales_by_product.to_csv("total_vendas_por_produto.csv")
total_sales_by_month.to_csv("total_vendas_por_mes.csv")

# Alternativamente, criar uma visualização simples usando Matplotlib
import matplotlib.pyplot as plt

# Criando gráfico de barras para total de vendas por produto
total_sales_by_product.plot(kind='bar')
plt.xlabel('Produto')
plt.ylabel('Total de Vendas')
plt.title('Total de Vendas por Produto')
plt.show()

# Criando gráfico de linha para total de vendas por mês
total_sales_by_month.plot(kind='line', marker='o')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas')
plt.title('Total de Vendas por Mês')
plt.xticks(range(1, 13), ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.show()
