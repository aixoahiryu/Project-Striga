import Zeta

x1 = Zeta.Panel.Window(mode='basic', color2='green')
x2 = Zeta.Panel.Window(mode='basic', color2='red')
Zeta.System.WM.toggle_bind(x1, x2)
#x1.toggle[0].hide()

x1.mainloop()