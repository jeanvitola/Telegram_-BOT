# Como Crear un Bot de Telegram en Tiempo Real, API-WebScraping
Crear un Bot de telegram que nos de aviso del Precio de una criptomoneda


![image](https://user-images.githubusercontent.com/75003188/138358183-76402206-325b-4c17-9b38-4318e9127b23.png)


# Requerimientos

Librerias/Módulos a utilizar :
* BeautifulSoup
* Requests
* Math
* schedule
* webbrowser


# Creación del bot

* En Telegram, buscamos a `@botfather` y le abrimos un privado.
* Escribimos `/newbot`
 * BotFather nos pedirá que le demos un nombre, escribimos un nombre
*Ahora BotFather nos pedirá un username, que debe terminar en “bot”. Lo escribimos.
* Una vez hecho, nos aparecerá un mensaje como este:

![image](https://user-images.githubusercontent.com/75003188/138358567-a219c164-e0a0-4a40-b96c-5fbadd8f0262.png)

* Copiamos y guardamos el número de token que nos aparece en rojo


# Configuración básica

```import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

test = telegram_bot_sendtext("Testing Telegram bot")
print(test)```


![image](https://user-images.githubusercontent.com/75003188/138360033-375c8bb6-d86e-4130-80c0-7913de81a600.png)







