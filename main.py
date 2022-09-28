import pandas as pd
import openpyxl as pyxl
import twilio as tw

#Lógica do código passo a passo:

#1 Abrir os 6 arquivos em Excel;
#2 Verificar nos 6 arquivos se alguma linha da coluna Vendas é maior que 55.000;
#3 Se for maior que 55.000 = Envie um SMS com o nome, mês e valor de vendas do vendedor;
#4 Caso seja menor que 55.000 = Não faça nada.

from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC97a25e9ee7fad24ddc0525dea4582b44"
# Your Auth Token from twilio.com/console
auth_token  = "067ecfcb9ecb6eb19c2fc4fba27c08ca"
client = Client(account_sid, auth_token)

FILE_PATH = "/c/Users/Lucas/Desktop/Projetos/Github/Projeto-Análise_Viagem_Bônus/Base_de_Dados"

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        valor_vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} um vendedor(a) atingiu a meta! Vendedor(a) {vendedor}, valor de vendas: {valor_vendas}')
        message = client.messages.create(
            to="+NÚMERODAPESSOAAQUI", 
            from_="+SEUNÚMEROAQUI",
            body= f'No mês {mes} um vendedor(a) atingiu a meta! Vendedor(a) {vendedor}, valor de vendas: {valor_vendas}')
        print(message.sid)






