from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"
response = requests.get(url)
html = response.text

soup=BeautifulSoup(html, 'html.parser')

text = soup.find_all("span", class_="text")
print(text)

author = soup.find_all("small", class_="author")
print(author)

#С помощью функции range(len) определим общее количество цитат
for i in range(len(text)):
#Присвоим номер каждой цитате так, чтобы нумерация шла с 1
    print(f"Цитата номер - {i + 1}")
#Выводим саму цитату, указывая её id
    print(text[i].text)
#Выводим автора цитаты
    print(f"Автор цитаты - {author[i].text}\n")

