class Neon():
	def __init__(self, color2='', color=7):
		self._color = ['#000000', '#FF0C12', '#FDAE32', '#FDFB00', '#5CFF00', '#00CFFB', '#8F00F2', '#ffffff']
		self._name1 = {'black': ['#000000', '#ffffff', '#333333'], 'white': ['#ffffff', '#000000', '#cccccc']}
		self._name1['red'] = ['#fa5a5a', '#471a1a', '#5c2121']
		self._name1['orange'] = ['#FF5F1F', '#401808', '#5c220b']
		self._name1['yellow'] = ['#FFCC00', '#362b00', '#4f3f00']
		self._name1['green'] = ['#6effbe', '#253B34', '#335247']
		self._name1['blue'] = ['#00FFFF', '#014040', '#015c5c']
		self._name1['purple'] = ['#bc13fe', '#2a0538', '#3f0854']
		self.hex = self._color[color]
		if color2 != '':
			self.hex = self._name1[color2][0]
			self.hue = self._name1[color2][1]
			self.hue2 = self._name1[color2][2]

class Gradient():
	def __init__(self, color=7, color2=''):
		self._index = ['black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'white']
		index = self._index[color]
		self._color = {'pink': ['#ffafbd', '#ffc3a0']}
		self._color['red'] = ['#ff512f', '#dd2476']
		self._color['orange'] = ['#eb3349', '#f45c43']
		self._color['yellow'] = ['#ff5f6d', '#ffc371']
		self._color['green'] = ['#56ab2f', '#a8e063']
		self._color['blue'] = ['#2193b0', '#6dd5ed']
		self._color['purple'] = ['#cc2b5e', '#753a88']
		self._color['black'] = ['#141e30', '#243b55']
		self._color['white'] = ['#bdc3c7', '#2c3e50']
		if color2 != '': index = color2
		self.array = self._color[index]

class Smoke():
	def __init__(self):
		self.background = '#D4D4D4'
		self.foregroundb = '#474747'
		self.foregroundw = '#d8d8d8'

class Nier():
	def __init__(self):
		self.background = '#CCC8AF'
		self.foreground = '#555753'
		self.tint = '#B4AF9B'
		self.orange = '#B55B47'
		self.blue = '#3C9794'
