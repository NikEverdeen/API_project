import requests
import json
API_KEY = "40d1649f-0493-4b70-98ba-98533de7710b"

def get_geo_location(city_name):

    # делаем запрос по имени города с ограничением результатов (2)
    geocoder_request_template = \
        "http://geocode-maps.yandex.ru/1.x/?format=json&apikey=" + API_KEY +\
            "&geocode="+ city_name+"&results=2"

    # принимаем ответ от API
    response = requests.get(geocoder_request_template)

    # переводим байтовый ответ в json формат
    result = json.loads(response.content)

    # находим координаты города
    # {'pos':"lng lat"}
    geo_pos = result['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']

    # возвращаем ответ
    return geo_pos
