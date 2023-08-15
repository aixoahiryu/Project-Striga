import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin # Import the urljoin function

def download_images(url, save_folder):
 try:
 # Send an HTTP GET request to the URL
 response = requests.get(url)

 # Check if the request was successful
 response.raise_for_status()

 # Parse the HTML content using BeautifulSoup
 soup = BeautifulSoup(response.content, 'html.parser')

 # Find all image tags in the page
 img_tags = soup.find_all('img')

 # Create the save folder if it doesn't exist
 if not os.path.exists(save_folder):
 os.makedirs(save_folder)

 # Download and save each image
 for img_tag in img_tags:
 img_url = img_tag['src']

 # Check if the image URL is relative and convert it into an absolute URL
 if not img_url.startswith('http'):
 img_url = urljoin(url, img_url)

 img_name = img_url.split('/')[-1]

 img_response = requests.get(img_url)
 img_response.raise_for_status()

 img_path = os.path.join(save_folder, img_name)
 with open(img_path, 'wb') as f:
 f.write(img_response.content)

 print(f"Downloaded: {img_name}")

 except requests.exceptions.RequestException as e:
 print("Error:", e)

if __name__ == "__main__":
 url_to_scrape = "https://boards.4channel.org/int/thread/185330089"; # Replace this with the URL of the page containing images
 # Replace this with the folder name where images will be saved

 download_images(url_to_scrape, "your_download_directory_here")