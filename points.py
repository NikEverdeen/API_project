import requests, distance

url = 'https://geocode-maps.yandex.ru/1.x/?apikey=46baa895-6d77-4b6b-8fe6-a88c43a5f388&format=json&geocode='

print('Расстояние от двух точек.')

first_adress = input('Адрес первой точки: ')
second_adress = input('Адрес второй точки: ')

s_resp = requests.get(url + first_adress)
s_point = s_resp.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')
s_point[0], s_point[1] = float(s_point[0]), float(s_point[1])

h_resp = requests.get(url + second_adress)
h_point = h_resp.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')
h_point[0], h_point[1] = float(h_point[0]), float(h_point[1])

print(s_point, h_point)
print(round(distance.lonlat_distance(s_point, h_point)), 'Метров')
