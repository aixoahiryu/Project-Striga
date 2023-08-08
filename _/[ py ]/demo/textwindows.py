# File: textwindows.py
# 
#    http://infohost.nmt.edu/tcc/help/pubs/tkinter//text.html
#    http://infohost.nmt.edu/tcc/help/pubs/tkinter//panedwindow.html
#    http://www.tcl.tk/man/tcl8.5/TkCmd/text.htm
#    http://www.tcl.tk/man/tcl8.5/TkCmd/panedwindow.htm
    
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb

from demopanels import MsgPanel, SeeDismissPanel

class TextWindowsDemo(ttk.Frame):
    
    def __init__(self, isapp=True, name='textwindowsdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Text Embedded Windows and other features Demo')
        self.isapp = isapp
        self._create_widgets()
        
    def _create_widgets(self):
        if self.isapp:
            # don't need message panel
            SeeDismissPanel(self)
        
        self._create_demo_panel()
        
    def _create_demo_panel(self):
        demoPanel = Frame(self, highlightthickness=1, 
                          borderwidth=1, relief=SUNKEN,
                          name='demo')
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)

        text = self._create_text_widget(demoPanel)
        self._add_content(text)

    def _create_text_widget(self, parent):
                
        # create scrolled text widget
        text = Text(parent, height=30, setgrid=True, wrap=WORD, 
                    width=70, highlightthickness=0, 
                    borderwidth=0, pady=5, padx=8)        
        
        # setup scrollbar
        yscroll = ttk.Scrollbar(parent, orient=VERTICAL,
                                command=text.yview)
        text.configure(yscrollcommand=yscroll.set)
        
        # prevent edit of text
        text.bind('<KeyPress>', lambda e: 'break')
        
        # position in frame and set resize constraints
        # Note: if pack() is used, vertical scrollbar
        #       is 'clipped' when window size is reduced
        #       and disappears
        yscroll.grid(row=0, column=1, sticky=N+S)
        text.grid(row=0, column=0, sticky=N+S+E+W)
        
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
                                
        return text
            
    def _add_content(self, text):
        # configure tags
        text.tag_config('center', justify=CENTER,
                        spacing1='5m', spacing3='5m')
        text.tag_config('buttons', lmargin1='1c', lmargin2='1c',
                        rmargin='1c', spacing1='3m',
                        spacing2=0, spacing3=0)
        
        # insert text
        text.insert(END, ''.join(
                         ["A text widget can contain many different kinds of items, ",
                          "both active and passive.  It can lay these out in various ",
                          "ways, with wrapping, tabs, centering, etc.  In addition, ",
                          "when the contents are too big for the window, smooth ",
                          "scrolling in all directions is provided.\n\n",        
                          "A text widget can contain other widgets embedded ",
                          'in it.  These are called "embedded windows" ',
                          "and they can consist of arbitrary widgets.  ",
                          "For example, here are two embedded button ",
                          "widgets.  You can click on the first button to "]))
        
        # create and add buttons to turn the horizontal scroll on/off
        self._create_hscroll_btns(text)
        text.window_create(END, window=text.__on) # insert button
        
        text.insert(END, ''.join([" horizontal scrolling, which also turns off ",
                                  "word wrapping.  Or, you can click on the second ",
                                  "button to "]))         
                   
        text.window_create(END, window=text.__off) # insert button        
        text.insert(END, " horizontal scrolling and turn word wrapping back on.\n\n")
        
        # create and add buttons to display/remove a simple plot
        self._create_plot_btns(text)
        text.insert(END, "Or, here is another example.  If you ")
        text.window_create(END, window=text.__click)        
        text.insert(END, " a canvas displaying an x-y plot will appear right here.")
        
        # marks for plot insertion
        text.mark_set('plot', INSERT)
        text.mark_gravity('plot', LEFT)
        
        text.insert(END, "  You can drag the data points around with the mouse, ")
        text.insert(END, "or you can click here to ")
        text.window_create(END, window=text.__delete)
        text.insert(END, " the plot again.\n\n")
        
        # create and add 'peer window' buttons
        self._create_peer_btns(text)
        text.insert(END, "You can also create multiple text widgets each of which ")
        text.insert(END, "display the same underlying text. Click this button to ")
        text.window_create(END, window=text.__peer, padx=3, pady=2)  
        text.insert(END, " widget.  Notice how peer widgets can have different ")
        text.insert(END, "font settings, and by default contain all the images ")
        text.insert(END, "of the 'parent', but many of the embedded windows, ")
        text.insert(END, "such as buttons will not be there.  The easiest way ")
        text.insert(END, "to ensure they are in all peers is to use '-create' ")
        text.insert(END, "embedded window creation scripts ")
        text.insert(END, "(the plot above and the 'Make A Peer' button are ")
        text.insert(END, "designed to show up in all peers).  A good use of ")
        text.insert(END, "peers is for ")
        text.window_create(END, window=text.__split, padx=3, pady=2)
        text.insert(END, " \n\n")

        text.insert(END, "Users of previous versions of Tk will also be interested ")
        text.insert(END, "to note that now cursor movement is now by visual line by ")
        text.insert(END, "default, and that all scrolling of this widget is by pixel.\n\n")
        
        text.insert(END, "You may also find it useful to put embedded windows in ")
        text.insert(END, "a text without any actual text.  In this case the ")
        text.insert(END, "text widget acts like a geometry manager.  For ")
        text.insert(END, "example, here is a collection of buttons laid out ")
        text.insert(END, "neatly into rows by the text widget.  These buttons ")
        text.insert(END, "can be used to change the background color of the ")
        text.insert(END, "text widget (\"Default\" restores the color to ")
        text.insert(END, "its default).  If you click on the button labeled ")
        text.insert(END, "\"Short\", it changes to a longer string so that ")
        text.insert(END, "you can see how the text widget automatically ")
        text.insert(END, "changes the layout.  Click on the button again ")
        text.insert(END, "to restore the short string.\n")
        
        # add short, default and color buttons
        text.window_create(END, window=self._create_short_btn(text), padx=3, pady=2)
        text.window_create(END, window=self._create_default_btn(text), padx=3, pady=2)
        self._add_color_btns(text)
        
        # applies the 'buttons' tag to the default, short and color buttons
        text.tag_add('buttons', text.__short, END)
        
        # mark end of color button tagging
        btnEnd = text.tag_ranges('buttons')[1]
        text.insert(END, "\n\nYou can also change the usual border width, ")
        text.insert(END, "highlightthickness and padding.\n")
        
        # remove tag (if not removed will apply to all remaining text)
        text.tag_remove('buttons', btnEnd, END)
        
        # add buttons to control border, highlight and padding
        self._add_border_btns(text)
        text.insert(END, '\n')
        text.tag_add('buttons', text.__borderBtn, END)
        btnEnd = text.tag_ranges('buttons')[-1] # save last pos of all the tag's ranges
        
        # add an image
        text.insert(END, "\nFinally, images fit comfortably in text widgets too:\n")
        text.tag_remove('buttons', btnEnd, END)
        
        # must save a permanent link to the image, otherwise
        # it will be garbage collected
        self.__im = BitmapImage(file='images/letters.xbm')
        text.image_create(END, image=self.__im)
        
        # note that 'btnEnd' is a Tcl_obj, use it's string method
        # to convert it's value to a float
        text.tag_add('center', float(str(btnEnd))+1, END)
                
        
    # ===========================================================================
    # Button Creation 
    #   - methods to create all the buttons used in the text content
    #   - all buttons are created as children of the 'text' widget
    # ===========================================================================
    def _create_hscroll_btns(self, txt):
        txt.__on = ttk.Button(txt, text='Turn On', cursor='top_left_arrow',
                              style='Demo.TButton',
                              command=lambda t=txt: self._text_wnd_on(t))
        txt.__off = ttk.Button(txt, text='Turn Off', cursor='top_left_arrow',
                               style='Demo.TButton',
                               command=lambda t=txt: self._text_wnd_off(t))
        
    def _create_plot_btns(self, txt):
        txt.__click = ttk.Button(txt, text='Click Here', cursor='top_left_arrow',
                                 style='Demo.TButton',
                                 command=lambda t=txt: self._text_wnd_plot(t))
        txt.__delete = ttk.Button(txt, text='Delete', cursor='top_left_arrow',
                                  style='Demo.TButton',
                                  command=lambda t=txt: self._text_wnd_del(t))
        
    def _create_peer_btns(self, txt):
        txt.__peer = ttk.Button(txt, text='Make a Peer', cursor='top_left_arrow',
                                style='Demo.TButton',
                                command=lambda t=txt: self._text_make_peer(t))
        txt.__split = ttk.Button(txt, text='Split Windows', cursor='top_left_arrow',
                                 style='Demo.TButton', state='disabled',
                                 command=lambda t=txt: self._text_split_wnd(t))        
        
    def _create_short_btn(self, txt):
        # button changes size based on text display
        # clicking on it demonstrates the text widget's ability to re-flow the
        # color buttons that follow; much as a grid manager can reflow content
        # the callback changes its text and reconfigures it to act as 
        # a 'Toolbutton' when clicked
        ttk.Style().configure('Demo.Toolbutton', anchor='center', padding=(5,5))
        btn = ttk.Checkbutton( txt, 
                               style='Demo.TButton',
                               offvalue='Short',
                               onvalue='A much longer string',
                               cursor='top_left_arrow')
        
        btn['command'] = lambda b=btn: self._cb_value_changed(b)
        btn['text'] = 'Short'
        txt.__short = btn  # save to use as start of button tag area
        
        return btn

    def _create_default_btn(self, txt):
        # create the 'Default' button to allow colour reset
        bgc = txt['background']
        btn = ttk.Button(txt, text='Default', cursor='top_left_arrow',
                         style='Demo.TButton', width=15,
                         command=lambda c=bgc, t=txt: self._set_bgcolor(t, c))
        return btn
        
    def _add_color_btns(self, txt):
        # add a number of colour buttons that will change the text
        # background colour when clicked 
        colors = ( 'AntiqueWhite3', 'Bisque1', 'Bisque2', 'Bisque3', 'Bisque4',
                   'SlateBlue3', 'RoyalBlue1', 'SteelBlue2', 'DeepSkyBlue3', 'LightBlue1',
                   'DarkSlateGray1', 'Aquamarine2', 'DarkSeaGreen2', 'SeaGreen1',
                   'Yellow1', 'IndianRed1', 'IndianRed2', 'Tan1', 'Tan4' )
        
        for c in colors:
            btn = ttk.Button(txt, text=c, cursor='top_left_arrow',
                             style='Demo.TButton', width=15,
                             command=lambda c=c, t=txt: self._set_bgcolor(t,c))
            txt.window_create(END, window=btn, padx=3, pady=2)

    def _add_border_btns(self, txt):
        # save existing style settings
        norm = {'bw': {'borderwidth': txt.cget('borderwidth')},
                'hi': {'highlightthickness': txt.cget('highlightthickness')},
                'pad': {'padx': txt.cget('padx'),
                        'pady': txt.cget('pady')}}
        
        # create buttons to control the text border and highlight
        btn = ttk.Button(txt, text='Big Borders', 
                         width=15, cursor='top_left_arrow',
                         command=lambda t=txt: t.configure({'borderwidth': 15}))
        txt.window_create(END, window=btn)
        txt.__borderBtn = btn     # save for tag marking
        
        btn = ttk.Button(txt, text='Small borders', 
                         width=15, cursor='top_left_arrow',
                         command=lambda t=txt, n=norm: t.configure(n['bw']))
        txt.window_create(END, window=btn)
        
        # create buttons to control the text highlightthickness
        btn = ttk.Button(txt, text='Big highlight',
                         width=15, cursor='top_left_arrow',
                         command=lambda t=txt: t.configure({'highlightthickness': 15}))
        txt.window_create(END, window=btn)

        btn = ttk.Button(txt, text='Small highlight',
                         width=15, cursor='top_left_arrow',
                         command=lambda t=txt, n=norm: t.configure(n['hi']))
        txt.window_create(END, window=btn)
        
        # create buttons to control the text's padding
        btn = ttk.Button(txt, text='Big pad',
                         width=15, cursor='top_left_arrow',
                         command=lambda t=txt: t.configure({'padx': 30, 'pady': 15}))
        txt.window_create(END, window=btn)

        btn = ttk.Button(txt, text='Small pad',
                         width=15, cursor='top_left_arrow',
                         command=lambda t=txt, n=norm: t.configure(n['pad']))
        txt.window_create(END, window=btn)        

    # ===========================================================================
    # Button Commands
    # ===========================================================================
    def _text_wnd_on(self, txt):
        # add a horizontal scrollbar to the window
        # and turn off word wrap
        hscroll = ttk.Scrollbar(txt.master, orient=HORIZONTAL,
                                command=txt.xview, name='hscroll')
        hscroll.grid(row=1, column=0, sticky=E+W)
        txt['xscrollcommand'] = hscroll.set
        txt['wrap'] = NONE
        
    def _text_wnd_off(self, txt):
        # turn word wrap back on and destroy the horizontal scrollbar
        txt.master.nametowidget('hscroll').destroy()
        txt['xscrollcommand'] = ''
        txt['wrap'] = WORD

        
    def _text_wnd_plot(self, txt):
        if hasattr(txt, 'plot'):
            return  # already showing the plot
        
        # create and insert the plot
        txt.insert('plot', '\n')
        
        # Note: if the 'create' option is used
        #       the plot won't display, even if
        #       a permanent reference is kept to
        #       the canvas object
        txt.window_create('plot', window=self._create_plot(txt))
        txt.tag_add('center', 'plot')
        txt.insert('plot', '\n')    
    
    def _text_wnd_del(self, txt):
        # remove the plot
        if txt.plot:
            c = txt.plot.destroy()
        
        # remove extra space inserted
        # around the plot
        s = txt.get('plot') + ' \t\n'
        for _ in s:
            txt.delete('plot')
        txt.insert('plot', ' ')
            
    def _text_make_peer(self, txt):
        mb.showinfo('Text Peers',
                    'Text.peer_create() is not available in Python 3.2.3')
    
    def _text_split_wnd(self, txt):
        # not implemented
        pass
    
    def _cb_value_changed(self, cb):
        # called when the 'Short' button is clicked
        # if selected, use the 'Toolbutton' 
        # style to make it appear 'sunken'
        if cb.instate(('selected',)):
            cb['style'] = 'Demo.Toolbutton'
            if cb.cget('text'):
                cb['text'] = cb['onvalue']
        else:
            cb['style'] = 'Demo.TButton'
            if cb.cget('text'):
                cb['text'] = cb['offvalue']    
                
    def _set_bgcolor(self, text, color):
        # called when the default or colour buttons are clicked
        text['background'] = color
        ttk.Style().configure('Demo.TButton', background=color)
                
    # ===================================================================
    # Create a simple plot
    # ===================================================================            
    def _create_plot(self, txt):
        c = Canvas(txt, relief=SUNKEN, width=450,
                   height=300, cursor='top_left_arrow')
                
        c.create_text(225, 20, text='A simple plot',
                      font='helvetica 18', fill='brown' )
                
        # draw the x and y  axis
        c.create_line(100, 250, 400, 250, width=2 )
        c.create_line(100,250, 100, 50, width=2 )

        for i in range(1,11):
            x = 100+i*30
            c.create_line(x, 250, x, 245, width=2)
            c.create_text(x, 254, text=str(i*10), anchor='n',
                          font='helvetica 16' )
        
        for i in range(0,6):
            y = 250-i*40
            c.create_line(100, y, 105, y, width=2)
            c.create_text(96, y, text=str(i)+'.0', anchor='e',
                          font='helvetica 16' )
            
        # draw the points
        points = [(12, 56), (20, 94), (33, 98), (32, 120),
                  (61, 180), (75, 160), (98, 223) ]
        
        c.items=[]
        for p0, p1 in points:
            x = 100 + 3*p0
            y = 250 - 4*p1/5

            itm = c.create_oval(x-6,y-6,x+6, y+6,
                                width=1, outline='black',
                                fill='SkyBlue2')
            c.addtag_withtag('points', itm )
            c.items.append(itm)

        # collectively bind the points, using the tag
        c.tag_bind('points', '<Any-Enter>', lambda e, p=c: self._plot_enter(e, p) )
        c.tag_bind('points', '<Any-Leave>', lambda e, p=c: self._plot_leave(e, p))
        c.tag_bind('points', '<B1-Motion>', lambda e, p=c: self._plot_move(e, p) )

        txt.plot = c    # save a reference to the plot
    
        return c

    def _plot_enter( self, evt, plot ):
        plot.itemconfigure('current', fill='red' )
        plot.oldx, plot.oldy = plot.canvasx(evt.x), plot.canvasy(evt.y)

    def _plot_leave( self, evt, plot ):
        plot.itemconfigure('current', fill='SkyBlue2' )

    def _plot_move( self, evt, plot ):
        x,y = plot.canvasx(evt.x), plot.canvasy(evt.y)
        plot.move('current', x-plot.oldx, y-plot.oldy )
        plot.oldx, plot.oldy = x, y

                    
if __name__ == '__main__':
    TextWindowsDemo().mainloop()