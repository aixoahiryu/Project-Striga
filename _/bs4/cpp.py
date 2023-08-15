import requests
from bs4 import BeautifulSoup as BS
import html2text as h2t


def main():
 base_url = "https://www.learncpp.com/";
 response = requests.get(base_url)
 soup = BS(response.text, "html.parser")
 h = h2t.HTML2Text()
 h.mark_code = True
 tutorial_urls = []
 for url in soup.findAll("a"):
 try:
 if "learncpp.com/cpp-tutorial"; in url["href"]:
 tutorial_urls.append(url)
 except KeyError:
 continue
 for url in tutorial_urls:
 cur = requests.get(url["href"])
 with open(f"./markdown_files/{url.text}.md", "w") as data:
 data.write(h.handle(cur.text))
 return 0


if __name__ == "__main__":
 exit(main())