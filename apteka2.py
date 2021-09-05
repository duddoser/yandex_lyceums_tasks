import sys
import requests
from Show_map import show_map
from Get_delta import get_delta

# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:
toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {"geocode": toponym_to_find, "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    # обработка ошибочной ситуации
    pass

# Преобразуем ответ в json-объект
json_response = response.json()
# Получаем первый топоним из ответа геокодера.
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
# Координаты центра топонима:
toponym_coodrinates = toponym["Point"]["pos"]
# Долгота и широта:
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

address_ll = "{},{}".format(toponym_longitude, toponym_lattitude)

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"
}

response = requests.get(search_api_server, params=search_params)
if not response:
    # ...
    pass

# Преобразуем ответ в json-объект
json_response = response.json()

# Получаем первую найденную организацию.
organization = json_response["features"][0]
print(organization)
# Название организации.
org_name = organization["properties"]["CompanyMetaData"]["name"]
# Адрес организации.
org_address = organization["properties"]["CompanyMetaData"]["address"]
org_hours = organization["properties"]["CompanyMetaData"]['Hours']['text']

# Получаем координаты ответа.
point = organization["geometry"]["coordinates"]
org_point = "{0},{1}".format(point[0], point[1])
org_s = 111144 * (((point[0] - float(toponym_longitude)) ** 2 + (point[1] - float(toponym_lattitude)) ** 2) ** 0.5)

# Собираем параметры для запроса к StaticMapsAPI:
delta = get_delta(toponym_longitude, toponym_lattitude, point[0], point[1])
map_params = {
    # позиционируем карту центром на наш исходный адрес
    "ll": address_ll,
    "spn": delta,
    "l": "map",
    # добавим точку, чтобы указать найденную аптеку
    "pt": "{0},pm2dgl,~{1},pm2pnl".format(org_point, address_ll)
}

map_api_server = "http://static-maps.yandex.ru/1.x/"

response = requests.get(map_api_server, params=map_params)
show_map(response)

snippet = {'Адрес: ': org_address,
           'Название аптеки:': org_name,
           'Время работы:': org_hours,
           'Расстояние до аптеки:': round(org_s)}

for el in snippet:
    print(el, snippet[el])
