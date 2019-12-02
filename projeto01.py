import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')

arq_base =  "vgsales.csv"
df = pd.read_csv(arq_base)

#-------> resposta da 2
df.columns = ['Ranking', 'Nome', 'Plataforma', 'Ano', 'Gênero', 'Editora', 'Vendas América do Norte', 'Vendas EUA', 'Vendas Japão', 'Outras Vendas', 'Vendas Globais']
df.head()
print(df.dtypes)

#-------> resposta da 3 
#avaliando variaveis  - pré processamento

df=df.drop(['Ranking'], axis=1) #excluindo as features que não serão usadas
df.isnull().sum() #identificando quantidade de registros nulos por features

#features com valores nulos: Ano e Editora

df[df['Ano'].isnull()]['Vendas Globais'].sum() # as vendas com ano nulo serão alocadas na Min(ano)-1 devido a expressividade dos dados
df[df['Editora'].isnull()]['Vendas Globais'].sum()  # as vendas com a Editora nulas serão alocadas numa nova editora [desconhecida]


df['Ano'].fillna(df['Ano'].min()-1,inplace=True) #substituindo os valores nulos para o Ano mínimo -1
df['Editora'].fillna('Desconhecida',inplace=True) #substituindo as Editoras nulas para editora Desconhecida

df['Ano'] = df['Ano'].astype(int) #convertendo ano float para int

df = df.dropna(how='any',axis=0)  #retirando demais valores nulos caso ainda existam

#-------> resposta da 4
#-------> --->  resposta da 4.1

genero = df.groupby("Gênero").size()
genero.sort_values().plot(kind='bar', color='green') #gerando grafico com o genero que mais teve jogos lançados 
plt.show()

genero_vendas = df.groupby("Gênero")['Vendas Globais'].sum()
genero_vendas.sort_values().plot(kind='bar', color='blue')
plt.show()

df.groupby("Plataforma")["Vendas Globais"].sum().sort_values()[:10].plot(kind="bar")
plt.show()

editora_vendas = df.groupby("Editora")['Vendas Globais'].size().sort_values()
editora_vendas.sort_values()
plt.show()




valor_ano = pd.crosstab(df['Ano'],df['Vendas Globais'])
valor_ano.head()



label = ['Min','Max']
valores= [df.Rank.min(),df.Rank.max()]
plt.bar(label, valores)
plt.title('Min-Max - Rank')
#plt.show()

label_min_max = ['Rank','Year','Global_Sales']
ranque = []
ranque.append(df.Rank.min())
ranque.append(df.Rank.max())

ano=[]
ano.append(df.Year.min())
ano.append(df.Year.max())

vendas=[]
vendas.append(df.Global_Sales.min())
vendas.append(df.Global_Sales.max())

df1 = pd.DataFrame([ranque,ano, vendas],['Rank','Year','Vendas'],columns=['Min','Max'])
print(df1.head(3))


#buscando valores nulos nas colunas
#print(df.isnull().sum())
#removendo valores nulos
df = df.dropna(how='any',axis=0) 

#print(df.isnull().sum())









