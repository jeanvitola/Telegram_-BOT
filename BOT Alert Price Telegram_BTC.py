#!/usr/bin/env python
# coding: utf-8

# ### BOT de Telegram

# In[112]:


#--------------importamos las librerias/Módulos---------------->

import requests
from bs4 import  BeautifulSoup
import time
import webbrowser
import math
import time
import schedule

while True:
    
    #-------------------- Configuramos el token y el chat Id de TL--------->


    def telegram_bot_sendtext(bot_message):
        bot_token = ''   #inserte su token de Telegram
        bot_chatID = ''  # inserte su Id de Telegram
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        return response.json()

    #-------------------Petición Requests al Navegador---------------->

    url =("https://es.investing.com/indices/investing.com-btc-usd")
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    price=soup.find("span",{"class":"instrument-price_last__KQzyA"})
    price_coin=price.text

    #--------------------Párametros en el cual queremos avisos---------->
    precio_buy= "51.000"

    if price_coin <= precio_buy:
        test = telegram_bot_sendtext("Hola Jean Carlos, ¡Hay oferta de BTC! su precio actual es    " + str(price_coin )+ "  USD   \nEnlace:https://es.investing.com/indices/investing.com-btc-usd  " )

    else:
        pass 
   
    #-------------------- Reportes periodicos para no acceder a la nube--------->

    
    def report():
        my_balance = 20  ## Replace this number with an API call to fetch your account balance
        my_message = "Actualmente el BOT de BTC esta en funcionamiento, su balance es : {}".format(my_balance)   ## Customize your message
        telegram_bot_sendtext(my_message)


    #Configuración de la hora para que nos de aviso de funcionamiento
    schedule.every().day.at("17:00").do(report)

    while True:
        schedule.run_pending()
        time.sleep(1)  
    
    
    
    
    


# In[ ]:





# In[81]:




