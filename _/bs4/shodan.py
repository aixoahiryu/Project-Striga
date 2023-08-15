import requests
from bs4 import BeautifulSoup

# Define search URL
url = 'https://www.shodan.io/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all UUIDs starting with "sk-"
keys = [uuid.get('href') for uuid in soup.find_all(href=True) if uuid['href'].startswith('sk-')]

print(keys)