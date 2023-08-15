import shodan
from bs4 import BeautifulSoup
import requests

# Shodan API key goes here
API_KEY = "YOUR_SH_API_KEY"

api = shodan.Shodan(API_KEY)

def scrape_gpt4_keys(url):
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Searching for keys usually stored in meta tags or script tags. Actual tag will depend on how it is stored.
keys_meta_tag = soup.find_all('meta', {'name': 'openai-key'})
keys_script_tag = soup.find_all('script', {'type': 'application/ld+json'})

gpt4_keys_list = []

for tag in (keys_meta_tag + keys_script_tag):

key_content= tag.get('content') if tag.has_attr('content') else None
# check if 'openai' exists within the content/key string
if key_content and ('openai' in key_content.lower()):
gpt4_keys_list.append(key_content)

return(gpt4_keys_list)

try:
results= api.search("gpt-4 openAI")

for result in results['matches']:
url= result['http']['location']
print(scrape_gpt4_keys(url))
except shodan.APIError as e:
print(f"Error encountered: {e}")
```