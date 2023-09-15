from tkinter import *

class Neon():
	def __init__(self, color=7, color2=''):
		self._color = ['#000000', '#FF0C12', '#FDAE32', '#FDFB00', '#5CFF00', '#00CFFB', '#8F00F2', '#ffffff']
		self._name1 = {'black': ['#000000', '#000000'], 'white': ['#ffffff', '#ffffff']}
		self._name1['red'] = ['#ec5555', '#471a1a']
		self._name1['orange'] = ['#FF5F1F', '#401808']
		self._name1['yellow'] = ['#FFCC00', '#362b00']
		self._name1['green'] = ['#6effbe', '#253B34']
		self._name1['blue'] = ['#00FFFF', '#014040']
		self._name1['purple'] = ['#bc13fe', '#2a0538']

		self.hex = self._color[color]
		if color2 != '':
			self.hex = self._name1[color2][0]
			self.hue = self._name1[color2][1]