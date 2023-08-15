import requests
from tkinter import messagebox

def get_public_ip_address():
 try:
 response = requests.get('https://api.ipify.org?format=json')
 ip_address = response.json()['ip']
 except requests.RequestException:
 ip_address = "Unknown"
 return ip_address

ip_address = get_public_ip_address()
messagebox.showinfo("IP Address", "Public IP Address: " + ip_address)