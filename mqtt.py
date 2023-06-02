import paho.mqtt.client as mqtt
import time
import requests
import json


def on_connect(client, userdata, flags, return_code):
    if return_code == 0:
        print("connected")
        client.subscribe("Test")
    else:
        print("could not connect, return code:", return_code)


def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    # print("Received message:", payload)

    # Extraer los valores del mensaje JSON
    try:
        data = json.loads(payload)
        esp32 = data['esp32']
        mensaje = data['mensaje']
        fecha = data['fecha']
        hora = data['hora']
        latitud = data['latitud']
        longitud = data['longitud']

        # ... y así sucesivamente con las claves que necesites
        print("mensaje:", mensaje)
        print("fecha:", fecha)
        # Puedes realizar otras operaciones con los valores extraídos
        url = 'http://127.0.0.1:8000/reportes/post/'
        reporte = {
            'esp32': esp32,
            'mensaje': mensaje,
            'fecha': fecha,
            'hora': hora,
            'latitud': latitud,
            'longitud': longitud
            }

        x = requests.post(url, json = reporte)
        # print("reporte en json: "+reporte)
        print(x.text)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)



    # print("Received message: ", str(message.payload.decode("utf-8")))
    



broker_hostname ="localhost"
port = 1883 

client = mqtt.Client("Client2")
# client.username_pw_set(username="user_name", password="password") # uncomment if you use password auth
client.on_connect=on_connect
client.on_message=on_message

client.connect(broker_hostname, port) 
client.loop_start()

try:
    time.sleep(1900)
finally:
    client.loop_stop()



# {"mensaje": "Gas a niveles peligrosos","fecha": "15/05/23","hora": "17:34","latitud": "52.32","long": "-91.02"}

#mosquitto_pub -t Test -m '{"esp32": "chunche3", "mensaje": "Gas a niveles peligrosos","fecha": "15/05/23","hora": "17:34","latitud": 52
#.32,"longitud": -91.02}'

#sudo docker run -it -p 1883:1883 -p 9001:9001 -v /home/diego/api-rest-djando-reportes/mqtt/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto