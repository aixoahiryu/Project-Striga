import Zeta

def transparent(root):
	if Zeta.System.OS.Windows: root.wm_attributes("-transparentcolor", "white")
	if Zeta.System.OS.Linux: root.configure(bg='')
	if Zeta.System.OS.Mac: (root.wm_attributes("-transparent", True), root.config(bg='systemTransparent'))


def toggle(master):
	if master.on:
		for i in master.toggle: i.hide()
	else:
		for i in master.toggle: i.show()
	
	master.on = not master.on

def toggle_bind(master, child):
	if not hasattr(master, 'toggle'):
		master.toggle = []
		master.on = False
		master.bind('<Button-1>', lambda e: toggle(master), add="+")

	if isinstance(child, list): master.toggle = child
	else: master.toggle.append(child)
	child.protocol( 'WM_DELETE_WINDOW' , lambda: toggle_unbind(master, child))

def toggle_unbind(master, child):
	master.toggle.remove(child)


def hover_show(master):
	for i in master.hover: i.show()

def hover_hide(master):
	for i in master.hover: i.hide()

def hover_stay(master, widget):
	if widget in master.hover:
		for i in master.hover: i.hide()

def hover_bind(master, child, stay=False):
	if not hasattr(master, 'hover'):
		master.hover = []
		master.bind('<Enter>', lambda e: hover_show(master), add="+")
		if stay: child.bind('<Leave>', lambda e: hover_stay(master, e.widget), add="+")
		else: master.bind('<Leave>', lambda e: hover_hide(master), add="+")

	if isinstance(child, list): master.hover = child
	else: master.hover.append(child)
	child.protocol( 'WM_DELETE_WINDOW' , lambda: hover_unbind(master, child))

def hover_unbind(master, child):
	master.hover.remove(child)


class Workspace():
	def __init__(self, panel):
		# Panel = {'System': {'taskbar': '', 'wallpaper': ''}, 'File': {'root': ''}, 'Network': {'root': ''}, 'Lounge': {'root': ''}}
		self.panel = panel
		self.active = ''
		self.hidden = False

		self.toggle = []
		self.hover = []

	def toggle_sidebar(self, group=''):
		if self.hidden:
			if group=='': self.show(self.active)
			else: self.show(group)
			self.show('System')
		else:
			self.hide(self.active)
			self.hide('System')
			for master in self.hover: hover_hide(master)
			for master in self.toggle:
				if master.on: toggle(master)
			
		self.hidden = not self.hidden

	def hide(self, group=''):
		if group=='':
			for g in self.panel.values():
				for w in g.values(): w.hide()
		else:
			for w in self.panel[group].values(): w.hide()

	def show(self, group=''):
		if group=='': group = 'System'
		for w in self.panel[group].values(): w.show()
		if group!='System': self.active = group

	def toggle_bind(self, master, child):
		self.toggle.append(master)
		toggle_bind(master, child)

	def hover_bind(self, master, child, stay=False):
		self.hover.append(master)
		hover_bind(master, child, stay=stay)