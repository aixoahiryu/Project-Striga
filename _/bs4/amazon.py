from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
 "Accept-Encoding": "gzip, deflate, br",
 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
 "DNT": "1",
 "Connection": "close",
 "Upgrade-Insecure-Requests": "1",
}
for page in range(1, 20):
 cookies = {'session': '137-3358925-0294258'}
 r = requests.get("https://www.amazon.com/s?k=science+fiction&i=movies-tv&crid=BN7SA6H20KD7&sprefix=science%2Caps%2C166&ref=nb_sb_ss_ts-doa-p_3_7".format(
 page=page
 ),
 headers=headers,
 cookies=cookies
 )
 soup = BeautifulSoup(r.content, "html.parser")
 for d in soup.select("span.a-size-medium.a-color-base.a-text-normal"):
 
 print(d.text)