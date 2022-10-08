#importando as bibliotecas
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px



st.title('Dados da educação Brasileira')


df1 = pd.read_csv('MICRODADOS_CADASTRO_IES_2019.CSV',sep=';', encoding = 'ISO-8859-1')
regioes = list(df1['NO_REGIAO_IES'].unique())

regioes_selecionadas = st.multiselect('Região',regioes,regioes)

df= df1.query('NO_REGIAO_IES == @regioes_selecionadas')
ies_nomes = list(df['NO_IES'].unique())

ies_selecionadas = st.multiselect('IES',ies_nomes)
if len(ies_selecionadas) > 0:
    df = df.query('NO_IES == @ies_selecionadas')
st.dataframe(df)
#todas as IES com todos os dados
df_regiao_ies= df['NO_REGIAO_IES'].value_counts().rename_axis('REGIÃO').reset_index(name='QTDE DE IES')
fig1 = px.bar(df_regiao_ies, x="REGIÃO", y="QTDE DE IES")
st.plotly_chart(fig1)
#qt total de IES pela região
#st.dataframe(df_regiao_ies)

#gráfico categoria administrativa 
df_categoria_adm = df['TP_CATEGORIA_ADMINISTRATIVA'].value_counts().rename_axis('CATEGORIA ADMINISTRATIVA').reset_index(name='QTDE DE IES')
#trocando os nomes das variaveis que estavam genericas
df_categoria_adm ['CATEGORIA ADMINISTRATIVA'].replace([1], 'Pública Federal', inplace=True)
df_categoria_adm ['CATEGORIA ADMINISTRATIVA'].replace([2], 'Pública Estadual', inplace=True)
df_categoria_adm ['CATEGORIA ADMINISTRATIVA'].replace([3], 'Pública Municipal', inplace=True)
df_categoria_adm ['CATEGORIA ADMINISTRATIVA'].replace([4], 'Particular com fins lucrativos', inplace=True)
df_categoria_adm ['CATEGORIA ADMINISTRATIVA'].replace([5], 'Particular sem fins lucrativos', inplace=True)
df_categoria_adm ['CATEGORIA ADMINISTRATIVA'].replace([6], 'Privada- Particular em sentido estrito', inplace=True)
df_categoria_adm ['CATEGORIA ADMINISTRATIVA'].replace([7], 'Especial', inplace=True)
#plotando o gráfico especifico
fig2 = px.bar(df_categoria_adm, x="QTDE DE IES", y="CATEGORIA ADMINISTRATIVA", orientation='h')
st.plotly_chart(fig2)

#grafico organizacao academica3
df_organizacao_academica = df['TP_ORGANIZACAO_ACADEMICA'].value_counts().rename_axis('ORGANIZAÇÃO ACADÊMICA').reset_index(name='QTDE DE IES')

df_organizacao_academica ['ORGANIZAÇÃO ACADÊMICA'].replace([1], 'Universidade', inplace=True)
df_organizacao_academica ['ORGANIZAÇÃO ACADÊMICA'].replace([2], 'Centro Universitário', inplace=True)
df_organizacao_academica ['ORGANIZAÇÃO ACADÊMICA'].replace([3], 'Faculdade', inplace=True)
df_organizacao_academica ['ORGANIZAÇÃO ACADÊMICA'].replace([4], 'Instituto Federal de Educação, Ciência e Tecnologia', inplace=True)
df_organizacao_academica ['ORGANIZAÇÃO ACADÊMICA'].replace([5], 'Centro Federal de Educação Tecnológica', inplace=True)

fig3 = px.bar(df_organizacao_academica, x="QTDE DE IES", y="ORGANIZAÇÃO ACADÊMICA", orientation='h')
st.plotly_chart(fig3)

#gráfico dos estados

df_uf_ies = df['CO_UF_IES'].value_counts().rename_axis('UNIDADE FEDERATIVA').reset_index(name='QTDE DE IES')
df_uf_ies.sort_values(by=['UNIDADE FEDERATIVA'], inplace=True)

df_uf_ies['UNIDADE FEDERATIVA'].replace([11], 'Rondônia', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([12], 'Acre', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([13], 'Amazonas', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([14], 'Roraima', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([15], 'Pará', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([16], 'Amapá', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([17], 'Tocantins', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([21], 'Maranhão', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([22], 'Piauí', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([23], 'Ceará', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([24], 'Rio Grande do Norte', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([25], 'Paraíba', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([26], 'Pernambuco', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([27], 'Alagoas', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([28], 'Sergipe', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([29], 'Bahia', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([31], 'Minas Gerais', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([32], 'Espírito Santo', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([33], 'Rio de Janeiro', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([35], 'São Paulo', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([41], 'Paraná', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([42], 'Santa Catarina', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([43], 'Rio Grande do Sul', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([50], 'Mato Grosso do Sul', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([51], 'Mato Grosso', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([52], 'Goiás', inplace=True)
df_uf_ies['UNIDADE FEDERATIVA'].replace([53], 'Distrito Federal', inplace=True)
fig4 = px.bar(df_uf_ies, x="QTDE DE IES", y="UNIDADE FEDERATIVA", orientation='h', height=700)
st.plotly_chart(fig4)

#procurar nomes das variaveis