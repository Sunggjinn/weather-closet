from urllib.request import urlopen, Request
import urllib
import bs4
import requests
import html5lib


def get_weather(area):
    url = f"https://search.naver.com/search.naver?ie=utf8&query={area}+날씨"
    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html, 'html5lib')

    temp = soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text
    weather_desc = soup.find('ul', class_='info_list').find('li').find('p', class_='cast_txt').text
    min_temp = soup.find('span', class_='min').find('span', class_='num').text
    max_temp = soup.find('span', class_='max').find('span', class_='num').text

    if '맑음' in weather_desc:
        weather = 'sunny'
    elif '흐림' in weather_desc:
        weather = 'cloudy'
    elif '비' in weather_desc:
        weather = 'rainy'
    else:
        weather = 'cloudful'

    weathers = temp

    return weathers
