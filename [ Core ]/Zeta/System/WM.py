import Zeta

def transparent(root):
	if Zeta.System.OS.Windows: root.wm_attributes("-transparentcolor", "white")
	if Zeta.System.OS.Linux: root.configure(bg='')
	if Zeta.System.OS.Mac: (root.wm_attributes("-transparent", True), root.config(bg='systemTransparent'))
