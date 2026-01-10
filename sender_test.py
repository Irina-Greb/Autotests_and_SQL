#Ирина Гребенникова, 39 когорта - Финальный проект. Инженер по тестированию плюс.
#импорт библиотек
import configuration
import data
import requests 	

# Создание заказа
def create_order(body):
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, 
					     json = data.body,
						 headers = data.headers)

# Получение заказа по его трекеру
def get_order(track):
	return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK + str(track),
	                    headers = data.headers)

# Получение статуса созданного заказа по его треку.
def get_code():
	order = create_order(data.body)
	track = order.json()["track"]
	return get_order(track).status_code
		
# Проверка, что код ответа для созданного заказа равен 200.
def test_code():
	assert get_code() == 200