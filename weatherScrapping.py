from urllib.request import urlopen, Request
import urllib
import bs4
import html5lib

location = '서울'
enc_location = urllib.parse.quote(location + '날씨')

url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location

req = Request(url)
page = urlopen(req)
html = page.read()
soup = bs4.BeautifulSoup(html,'html5lib')

today_temperature = soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text
today_weather_desc = soup.find('ul', class_='info_list').find('li').find('p', class_='cast_txt').text
min_temp = soup.find('span', class_='min').find('span', class_='num').text
max_temp = soup.find('span', class_='max').find('span', class_='num').text
windchill = soup.find('span', class_='sensible').find('em').find('span', class_='num').text

print(today_temperature, today_weather_desc, min_temp, max_temp, windchill)
