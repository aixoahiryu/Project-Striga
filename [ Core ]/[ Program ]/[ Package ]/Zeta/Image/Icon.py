import Zeta
import os
import inspect
from tkinter import *

class Load():
	def __init__(self, icon='', icontype='', iconformat='png'):
		try:
			root = os.path.split(inspect.getfile(Zeta))[0]
			path = f"{root}/Image/{icontype}/{icon}.{iconformat}"
			self.image = PhotoImage(file=path)
		except: self.image = PhotoImage(file=f"{root}/Image/meta/placeholder.png")