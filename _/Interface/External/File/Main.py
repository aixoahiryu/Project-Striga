import Zeta
from Zeta.Panel import *

class File(Window):
	def __init__(self, controller, *args, **kwargs):
		Window.__init__(self, mode='border', color2='white', *args, **kwargs)
		home = r'D:\MEGA\ZL-Core\Commit\╬'
		self.attributes('-topmost', True)
		self.attributes('-alpha', 0.77)
		height = Zeta.System.Size.Screen.height - 25 -Zeta.System.Size.taskbar
		self.geometry(f"333x{height}+1+25")
		self.overrideredirect(1)

		self.File1 = FileBox(self.frame, home=home, darkmode=True, controller=controller)

		self.hide()
		self.theme(self.frame, bg='#000000', fg='#ffffff')