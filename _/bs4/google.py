import requests
import sys
from bs4 import BeautifulSoup

def prod(a,b):
 html = requests.get("https://google.com/search?q=%d times %d" % (a,b), headers={'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/1488.1.1.1 Safari/525.13'}).text;

 soup = BeautifulSoup(html, 'html.parser');
 
 calc = soup.select_one(".card-section");
 result = calc.find("div").find("div").find("div").find("div").find_next_sibling("div").find_all("span")[-1].text.strip()
 
 return result
 
 
print(prod(int(sys.argv[1]),int(sys.argv[2])));