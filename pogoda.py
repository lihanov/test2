import requests
#Почтовый индекс желаемого места 
index = 350000
#Страна
cont = 'RU'
#Api ключ доступа к сайту
api = '715bde72ec94436195cd3fc6c18ac62a'

res = requests.get("https://api.weatherbit.io/v2.0/current",
                 params={'postal_code': index, 'country': cont, 'key': api, 'lang': 'ru'})

data =  res.json()
print('Гидрометеоцентр транслирует следующие погодные условия в городе', data["data"][0]["city_name"],':' '\n'
'Температура воздуха', data["data"][0]["temp"], 'град. по Цельсию, ощущается как', data["data"][0]["app_temp"], 'град.,',data["data"][0]["weather"]["description"], '\n'
'Ветер:', data["data"][0]["wind_cdir_full"], '\n'
'Скорость ветра:', data["data"][0]["wind_spd"],'м/с' '\n'
'Относительная влажность:', data["data"][0]["rh"], '%''\n'
'Давление:', data["data"][0]["pres"], 'мб' '\n'
'Время восхода солнца:', data["data"][0]["sunrise"], '\n'
'Время захода солнца:', data["data"][0]["sunset"], '\n'
'\n'
'Дата составления прогноза:', data["data"][0]["ob_time"], '\n'
'Спасибо, что воспользовались нашим сервисом, приходите к нам ещё ))'
)