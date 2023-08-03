from tkinter import *
from File import Example
from Corner import CornerFrame

class SampleApp(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.wm_overrideredirect(True)
		gradient_frame = CornerFrame(self)
		gradient_frame.pack(side="top", fill="both", expand=True)
		inner_frame = Frame(gradient_frame)
		inner_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

		b1 = Button(inner_frame, text="Ω",command=self.destroy)
		t1 = Text(inner_frame, width=40, height=10)
		b1.pack(side="top")
		t1.pack(side="top", fill="both", expand=True)
		Example(inner_frame).pack(side="top")

if __name__ == "__main__":
	app = SampleApp()
	app.mainloop()