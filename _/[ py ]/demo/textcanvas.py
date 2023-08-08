# File: textcanvas.py
# References:
#    http://infohost.nmt.edu/tcc/help/pubs/tkinter//canvas.html
#    http://tkinter.unpythonic.net/wiki/A_tour_of_Tkinter_widgets 

from tkinter import *
from tkinter import ttk
from demopanels import MsgPanel, SeeDismissPanel

class TextCanvasDemo(ttk.Frame):
    
    def __init__(self, isapp=True, name='textcanvasdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Text Canvas Demo')
        self.isapp = isapp
        self._create_widgets()
        
    def _create_widgets(self):
        if self.isapp:
            MsgPanel(self, 
                     ["This window displays a string of text to demonstrate ",
                      "the text facilities of canvas widgets.\n",
                      "Click in the 'Text Position' grid to adjust the position of ",
                      "the text relative to its anchor (red square).\n",
                      "Click in the 'Justification' grid to change the text's justification.\n",
                      "The text also supports the following simple bindings for editing: \n\n",
                      " 1. You can point, click, and type in the text area.\n",
                      " 2. You can select text with the left mouse button.\n",
                      " 3. You can copy the selection to the mouse position with \n",
                      "     the right mouse button (must be within text).\n",
                      " 4. Backspace deletes the selection if there is one;\n",
                      "     otherwise it deletes the character just before the insertion cursor.\n",
                      " 5. 'Delete' deletes the selection if there is one; otherwise it deletes \n",
                      "     the character just after the insertion cursor.\n",
                      " 6. Use left and right arrow keys to position icursor within text."])
            
        spd = SeeDismissPanel(self)
        # prevent 'Return' event in text object from
        # propagating to the 'See Code' button event
        spd.winfo_toplevel().unbind('<Return>') 
        
        self._create_demo_panel()
        
    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP)
        
        self.canvas = self._create_canvas(demoPanel)
        self._create_text()
        self._text_pos_grid()
        self._text_justify_grid()
        self._add_canvas_bindings()

    # ==============================================================================
    # Canvas and objects
    # ==============================================================================
        
    def _create_canvas(self, parent):    
        canvas = Canvas(relief=FLAT, borderwidth=0,
                        width=500, height=350)
        
        # grid fill colours
        canvas.posBoxFill = 'LightSkyBlue1'
        canvas.justifyBoxFill = 'SeaGreen2'
        canvas.selBoxFill = 'black'
        canvas.anchorBoxFill = 'red'
        
        canvas.pack(in_=parent, side=TOP, expand=Y, fill=BOTH)

        return canvas
        
    def _create_text(self):
        # create editable text, red square shows text anchor position
        rect = self.canvas.create_rectangle(245, 195, 255, 205,
                                            outline='black', 
                                            fill=self.canvas.anchorBoxFill)
        
        txtStr = "This is just a string of text to demonstrate the text " \
                 "facilities of canvas widgets. Bindings have been been " \
                 "defined to support editing (see above)."
        
        txt = self.canvas.create_text(250, 200, text=txtStr, width=440,
                                      anchor=N, font=('Helv', 18), justify=LEFT,
                                      tag=('text', ) )
        
        self.canvas.etext = txt  # save id of editable text item        
        
    def _text_pos_grid(self):
        
        # set up text position control grid
        # the posTags are the reverse of the 'row' placements
        # as they refer to the position of the ANCHOR; the text
        # is moved to place the anchor in the chosen position
        posTags = (('se', 's', 'sw'), ('e','c','w'), ('ne','n','nw'))
        x0, y0 = 50, 50          # start position
        size = 30                # size of square
        
        # draw grid
        for r in range(3):
            y = y0 + r * size
            tags = posTags[r]
            for c in range(3):
                x = x0 + c * size
                item = self.canvas.create_rectangle(x, y, x+size, y+size,
                                                    outline='black',
                                                    fill=self.canvas.posBoxFill,
                                                    tag=('posBox', tags[c], ))
        
        # add small red rect to represent the text anchor
        rect = self.canvas.create_rectangle(x0+40, y0+40, x0+50, y0+50,
                                       outline='black', 
                                       fill=self.canvas.anchorBoxFill,
                                       tag=('anchorBox', 'c'))

        # label for text position control grid
        self.canvas.create_text(x0+45, y0-5, text='Text Position',
                                anchor=S, font=('Times', 18), fill='brown')

                
    def _text_justify_grid(self):
        # set up text justification grid
        jtags = ('left', 'center', 'right')
        x0, y0 = 350, 50    # start position
        size = 30           # size of square
                
        # draw the grid
        for c in range(3):        
            x = x0 + c * size
            item = self.canvas.create_rectangle(x, y0, x+size, y0+size,
                                           outline='black',
                                           fill=self.canvas.justifyBoxFill,
                                           tag=('jbox', jtags[c] ))

        # add label for grid
        self.canvas.create_text(x0+45, y0-5, text='Justification',
                           anchor=S, font=('Times', 18), fill='brown')


    # ==============================================================================
    # Canvas Bindings
    # ==============================================================================
    def _add_canvas_bindings(self):
        self.canvas.tag_bind('posBox', '<Any-Enter>', self._enter_box)
        self.canvas.tag_bind('posBox','<Any-Leave>',
                             lambda evt: self._leave_box(evt, self.canvas.posBoxFill))
        self.canvas.tag_bind('posBox', '<1>',
                             lambda evt: self._position_etext(evt, 'anchor'))

        self.canvas.tag_bind('anchorBox','<Any-Leave>',
                              lambda evt: self._leave_box(evt, self.canvas.anchorBoxFill))
        self.canvas.tag_bind('anchorBox', '<1>',
                        lambda evt: self._position_etext(evt,'anchor'))

        self.canvas.tag_bind('jbox', '<Any-Enter>', self._enter_box)
        self.canvas.tag_bind('jbox','<Any-Leave>',
                        lambda evt: self._leave_box(evt, self.canvas.justifyBoxFill))
        self.canvas.tag_bind('jbox', '<1>',
                        lambda evt: self._position_etext(evt, 'justify'))
        
        # following bindings handle 'text' edits
        self.canvas.tag_bind('text', '<1>', self._text_set_cursor)
        self.canvas.tag_bind('text', '<B1-Motion>', self._text_sel)
        self.canvas.tag_bind('text', '<Delete>', self._text_delete)
        self.canvas.tag_bind('text', '<KeyPress>', self._text_insert)
        self.canvas.tag_bind('text', '<BackSpace>', self._text_bs)
        self.canvas.tag_bind('text', '<Left>', self._text_left)
        self.canvas.tag_bind('text', '<Right>', self._text_right)
        self.canvas.tag_bind('text', '<3>', self._text_paste)
        
    # ==============================================================================
    # Bound methods
    # ==============================================================================
    def _enter_box(self, evt):
        self.canvas.itemconfigure(CURRENT, fill=self.canvas.selBoxFill)
        
    def _leave_box(self, evt, color):
        self.canvas.itemconfigure(CURRENT, fill=color)

    def _position_etext(self, evt, option):
        tags = self.canvas.gettags(CURRENT)
        for t in tags:
            if t not in ('posBox', 'jbox', 'anchorBox', 'current'): 
                d = {option: t}  # option can be 'justify' or 'anchor'
                self.canvas.itemconfigure(self.canvas.etext, d)                          
    
    # following methods handle text edits
    def _text_set_cursor(self, evt):
        pos = '@{},{}'.format(evt.x, evt.y)
        self.canvas.icursor(CURRENT, pos)
        self.canvas.focus(CURRENT)
        self.canvas.focus_set()
        self.canvas.select_clear()
        self.canvas.select_from(CURRENT, pos )
        
    def _text_sel(self, evt):
        self.canvas.select_to(CURRENT, '@{},{}'.format(evt.x, evt.y))
            
    def _text_delete(self, evt):        
        if self.canvas.select_item():
            self.canvas.dchars(CURRENT, 'sel.first', 'sel.last')
        else:
            self.canvas.dchars(CURRENT, 'insert')
            
    def _text_insert(self, evt):
        self.canvas.insert(CURRENT, 'insert', evt.char)
        
    def _text_bs(self, evt):
        if self.canvas.select_item():
            self.canvas.dchars(CURRENT, 'sel.first', 'sel.last')
        else:
            self.canvas.dchars(CURRENT, 
                               self.canvas.index(CURRENT, 'insert' )-1 )
                        
    def _text_left(self, evt):
        self.canvas.icursor(CURRENT, 
                            self.canvas.index(CURRENT, 'insert') - 1)
        self.canvas.selection_clear()
                        
    def _text_right(self, evt):
        self.canvas.icursor(CURRENT, 
                            self.canvas.index(CURRENT, 'insert') + 1)
        self.canvas.selection_clear()
                        
    def _text_paste(self, evt):
        pos = '@{},{}'.format(evt.x, evt.y)
        try:
            self.canvas.insert(CURRENT, 
                               pos, 
                               self.canvas.selection_get())
        except TclError:
            # ignore, no selection to paste
            pass
                        
if __name__ == '__main__':
    TextCanvasDemo().mainloop()