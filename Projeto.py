# %%
import requests
import pandas as pd
from bs4 import BeautifulSoup
import schedule
import time
import datetime
from twilio.rest import Client
def informacoes_gupy():
    url = 'https://tecnologiamartins.gupy.io/'
    response = requests.get(url)

    #criação do objeto que representa o HTML da pg
    soup = BeautifulSoup(response.text, 'html.parser')
    vagas = soup.find_all('div', class_= "sc-f5007364-4 gPLESq")
    complemento = f"*VAGAS DE EMPREGO DO DIA*\n"
    for vaga in vagas:
        complemento += vaga.text + "\n"
    return complemento
def envia_mensagens():
   
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=informacoes_gupy(),
    to='whatsapp:+553484345667'
    )


envia_mensagens()


