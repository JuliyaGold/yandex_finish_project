import configuration
import requests
import data

#Функция для создания заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)
responce = post_new_order(data.order_body)
track = responce.json() ["track"]
#Функция получения заказа
def get_track_order():
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION_TRACK + "?t=" + str(track))
responce = get_track_order()