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