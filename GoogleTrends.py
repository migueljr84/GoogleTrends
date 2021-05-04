# Imports
import os
import pytrends
import datetime
import more_itertools
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.pyplot as plotter
from datetime import date
from pytrends.request import TrendReq
from pandas.io.json import json_normalize
from more_itertools import chunked

# Versões dos pacotes usados neste jupyter notebook
%reload_ext watermark
%watermark -a "Miguel Lima" --iversions

# Keyword 1
keyword_1 = "Bolsonaro"

# Keyword 2
keyword_2 = "Lula"

# Keyword 3
keyword_3 = "Ciro Gomes"


# Gravando a primeira keyword na lista
lista_palavras_chave = [keyword_1]


# Se mais de um termo foi digitado, fazemos append à lista
if keyword_2:
    lista_palavras_chave.append(keyword_2)
if keyword_3:
    lista_palavras_chave.append(keyword_3)
    

# Lista de keywords
lista_palavras_chave

# Variável para definição do timeframe (período) de análise
user_timeframe = '' 

# Timeframe
timeframe_list = ('\nAqui está a lista dos timeframes disponíveis: \n\n Para Todos: Todos \n Últimos 5 Anos: 5 anos \n Últimos 4 Anos: 4 anos \n Últimos 3 Anos: 3 anos \n Últimos 2 Anos: 2 anos \n Últimos 1 Ano: 1 ano')
print(timeframe_list)

# Solicita que o usuário digite o timeframe que usaremos para buscar as tendências
user_timeframe = "3 anos"


# Convertemos a escolha do usuário em um valor numérico
if user_timeframe == "5 anos":
    num_anos = 5
elif user_timeframe == "4 anos":
    num_anos = 4
elif user_timeframe == "3 anos":
    num_anos = 3
elif user_timeframe == "2 anos":
    num_anos = 2
else:
    num_anos = 1
    
# Variáveis de controle para definição do range total
num_dias = 7
num_semanas = 52
total_time_range = num_dias * num_semanas * num_anos


# Data final e data atual
data_final = date.today()
data_atual = date.today()


# Data final recebe data atual
data_final = data_atual

# Data de início
data_inicio = data_final - datetime.timedelta(days = total_time_range)

# Agora definimos o timeframe de pesquisa de tendências com a data de início e final
user_timeframe = data_inicio.strftime('%Y-%m-%d') + ' ' + data_final.strftime('%Y-%m-%d')

print(user_timeframe)


# Variável para a localidade
user_geo = ''

# Obtendo input do usuário
# Indique o País Para Análise dos Dados. Exemplo: Brasil é BR. 
user_geo = 'BR'

print(user_geo)

# Categoria
user_cat = 0 

# Cria o objeto para busca no Google Trends
pytrend = TrendReq()

# Extraindo os dados do Google Trends
# A mágica ocorre aqui
pytrend.build_payload(kw_list = lista_palavras_chave, 
                      cat = user_cat, 
                      timeframe = user_timeframe, 
                      geo = user_geo)
                      
# Vamos colocar os dados do interesse ao longo do tempo em um dataframe para começarmos a análise
df_interesse = pytrend.interest_over_time()

# Shape
df_interesse.shape

# Visualiza os dados
df_interesse.head(10)

# Vamos salvar os dados em disco para o caso de não conseguir conectar ao Google Trends
df_interesse.to_csv("dados/df_interesse.csv", index = True)

# Variáveis para o gráfico
num_dias = 7
num_semanas = 52
lista_datas = [data_inicio]

# Preparamos a lista de datas
for index in range (0, num_semanas * num_anos - 2):
    lista_datas.append(lista_datas[index] + datetime.timedelta(days = num_dias)) 
    
# Lista de datas para o plot
lista_datas[1:10]

# Plot
x_axis = lista_datas
plt.figure(figsize = (16,10))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(0,40 * num_anos))
plt.gcf().autofmt_xdate()
plt.plot (x_axis, df_interesse.iloc[:,0], label = '{}'.format(keyword_1))
if keyword_2:
    plt.plot (x_axis, df_interesse.iloc[:,1], label = '{}'.format(keyword_2))
if keyword_3:
    plt.plot (x_axis, df_interesse.iloc[:,2], label = '{}'.format(keyword_3))
plt.xticks(rotation = 1)
plt.xlabel('\nTempo\n')
plt.ylabel('\nNível de Interesse\n')
plt.title('\nInteresse ao Longo do Tempo\n')
plt.legend()
plt.show()


