import Zeta
import os
import inspect
from tkinter import *

class Load():
	def __init__(self, icon='', icontype='', iconformat='png'):
		root = os.path.split(inspect.getfile(Zeta))[0]
		path = f"{root}/Image/{icontype}/{icon}.{iconformat}"
		status = os.path.isfile(path)
		if status: self.image = PhotoImage(file=path)
		else: self.image = PhotoImage(file=f"{root}/Image/bw/geminiw.png")