# File: anilabel.py
#    This deviates from the original Tcl demo; an animated
#    GIF is used rather than a flat GIF whose characters
#    are manipulated.
#    Even with an animated GIF, you still must 'play'
#    the image; rotating through the animation frames.
#
# Source for rotating earth gif
#    http://www.animatedgif.net/earthglobe/earthglobe.shtml

from tkinter import *
from tkinter import ttk
from demopanels import MsgPanel, SeeDismissPanel

class AniLabelDemo(ttk.Frame):
    
    def __init__(self, isapp=True, name='anilabeldemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Animated Label Demo')
        self.isapp = isapp
        self._create_widgets()
        
    def _create_widgets(self):
        if self.isapp:
            MsgPanel(self, 
                     ["Four animated labels are displayed below; each of the labels ",
                      "on the left is animated by making the text message inside it ",
                      "appear to scroll, and the label on the right is an animated ",
                      "GIF, animated by changing the frame being dispalyed."])
            
            SeeDismissPanel(self)
        
        self._create_demo_panel()
        
    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)
        
        left = ttk.LabelFrame(demoPanel, text='Scrolling Text')
        right = ttk.LabelFrame(demoPanel, text='GIF Image')
        left.pack(side=LEFT, expand=True, padx=10, pady=10, fill=BOTH)
        right.pack(side=LEFT, expand=True, padx=10, pady=10, fill=BOTH)
        
        self._fill_panels(left, right)
        
        # start the text animations
        for w, txt, interval in self.__anilabels:
            self._animate_label_text(w, txt, interval)
            
        # start image animation
        self._animate_label_image(self.__lblImg, 150)

    def _fill_panels(self, left, right):
        # This method of scrolling text looks better with a fixed-width font
        lblA = ttk.Label(left, relief=RIDGE, font='fixedFont', width=15, padding=(0,5))
        lblB = ttk.Label(left, relief=GROOVE, font='fixedFont', width=15, padding=(0,5))
        lblC = ttk.Label(left, relief=FLAT, font='fixedFont', width=15)
 
        lblA.pack(side=TOP, expand=Y, padx=10, pady=10, anchor=W)
        lblB.pack(side=TOP, expand=Y, padx=10, pady=10, anchor=W)
        lblC.pack(side=TOP, expand=Y, padx=10, pady=10, anchor=W)
        
        # save the labels, their text and their animation intervals
        self.__anilabels = ((lblA, '* Slow Animation * ', 300),
                            (lblB, '* Fast Animation * ', 80),
                            (lblC, 
                             'This is a longer scrolling text in a widget that will not show the whole message at once. ',
                             150))
        
        # a label to hold the image in the right hand panel
        self.__lblImg = Label(right, bd=0)
        self.__lblImg.pack(side=TOP, expand=Y, padx=10, pady=10)
        
    def _animate_label_text(self, w, txt, interval):
        w.configure(text=txt)
        
        # Schedule the start of the animation loop
        self.after(interval, self._scroll_text, w, interval)
        
    def _scroll_text(self, w, interval):
        # the core animation routine, it continually re-calls
        # itself for each widget after the given time interval
        self.after(interval, self._scroll_text, w, interval)
        
        # do a marquee-like scroll by chopping a character off
        # the front of the label and adding it back on the end
        txt = w.cget('text')
        newTxt = txt[1:] + txt[0]
        w.configure(text=newTxt)
                
    def _animate_label_image(self, w, interval):
        img = PhotoImage(file='apgomoon_e0.gif')
        w.configure(image=img)
        w.image=img
        
        # Schedule the start of the animation loop
        w.frame = 0
        self.after(interval, self._play_gif, w, interval)
           
    def _play_gif(self, w, interval):
        # animates the GIF by rotating through
        # the GIF animation frames
        try:
            opt = "GIF -index {}".format(w.frame)
            w.image.configure(format=opt)
        except TclError:
            w.frame = 0
            self._play_gif(w, interval)
            return
            
        w.frame += 1
            
        self.after(interval, self._play_gif, w, interval)    
    
if __name__ == '__main__':
    AniLabelDemo().mainloop()