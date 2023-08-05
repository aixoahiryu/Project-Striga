import tkinter as tk

class GradientFrame(tk.Canvas):
    '''A gradient frame which uses a canvas to draw the background'''
    def __init__(self, parent, borderwidth=1, relief="sunken", color=4, color2=''):
        tk.Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief)
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
        self._color1 = self._color[index][0]
        self._color2 = self._color[index][1]
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i,0,i,height, tags=("gradient",), fill=color)
        self.lower("gradient")

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_overrideredirect(True)
        gradient_frame = GradientFrame(self)
        gradient_frame.pack(side="top", fill="both", expand=True)
        inner_frame = tk.Frame(gradient_frame)
        inner_frame.pack(side="top", fill="both", expand=True, padx=8, pady=(16,8))

        b1 = tk.Button(inner_frame, text="Close",command=self.destroy)
        t1 = tk.Text(inner_frame, width=40, height=10)
        b1.pack(side="top")
        t1.pack(side="top", fill="both", expand=True)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()