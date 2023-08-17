def transparent(root):
	if Zeta.OS.Window: root.wm_attributes("-transparentcolor", "white")
	elif Zeta.OS.Linux: root.configure(bg='')
	elif Zeta.OS.Mac: (root.wm_attributes("-transparent", True), root.config(bg='systemTransparent'))
