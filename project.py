import requests, distance

url = 'https://geocode-maps.yandex.ru/1.x/?apikey=46baa895-6d77-4b6b-8fe6-a88c43a5f388&format=json&geocode='
school_adress = input('Адрес первой точки: ')
home_adress = input('Адрес второй точки: ')
s_resp = requests.get(url + school_adress)
s_point = s_resp.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')
s_point[0], s_point[1] = float(s_point[1]), float(s_point[0])

h_resp = requests.get(url + home_adress)
h_point = h_resp.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')
h_point[0], h_point[1] = float(h_point[1]), float(h_point[0])

print(h_point, s_point)
print(distance.lonlat_distance(s_point, h_point))
