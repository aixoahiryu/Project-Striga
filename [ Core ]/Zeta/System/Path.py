import Zeta
import inspect
import os

class Core():
	def __init__(self):
		self.ZLCORE = r'D:\MEGA\ZL-Core'
		self.ZETA = os.path.split(inspect.getfile(Zeta))[0]
		self.downstream = r'D:\ZL-Core'

		self.Sidebar = r'D:\ZL-Core\Toolbar\_\[ Sidebar ]'
		self.Planner = r'D:\MEGA\ZL-Core\Commit\_'

class Browser():
	def __init__(self):
		self.main = r'C:\Users\Administrator\AppData\Local\Chromium\Application\chrome.exe' # --disk-cache-size=0 --force-dark-mode --media-cache-size=0 --profile-directory="Default" --process-per-site
		self.experiment = r'D:\Tools\Vivaldi\Application\vivaldi.exe' # --disk-cache-size=0 --force-dark-mode --media-cache-size=0 --process-per-site
		self.lite = r'C:\Program Files\Links\links-g.exe'

class Scraps():
	def __init__(self):
		self.path = r'D:\Scraps'

class Resource():
	def __init__(self):
		self.mp3 = r'D:\MP3'
		self.video = r'D:\Temp'

		self.data = r'D:\Data'
		self.politics = r'C:\Users\Administrator\Desktop\P'
		self.shared = r'D:\Shared'

		self.furry = r'D:\Furry\Archive'