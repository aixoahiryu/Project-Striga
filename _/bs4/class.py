import requests
import bs4

SERVER="https://www.pontosido.com/";

def GetServerTime():
 time = bs4.BeautifulSoup(requests.get(SERVER).text, 'html.parser')
 time = time.find(id="clock").get_text()
 return time

def GetServerDate():
 date = bs4.BeautifulSoup(requests.get(SERVER).text, 'html.parser')
 date = date.find(class_="date").get_text()
 return date

print(GetServerDate() + " " + GetServerTime())