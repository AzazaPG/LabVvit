import requests
city = "Podolsk, RU"
appid = "ce932ff1ff291fa7c13815272d1a071a"
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город: ", city)
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <", i['weather'][0]['description'], ">" "Скорость ветра <", i['wind']['speed'], ">" "Видимость <", i['visibility'], ">")
    print("____________________________")