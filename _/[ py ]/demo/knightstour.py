# File: knightstour.py
#    http://infohost.nmt.edu/tcc/help/pubs/tkinter//canvas.html
#    http://www.fileformat.info/info/unicode/char/265e/index.htm
#    http://opensource.apple.com/source/tcl/tcl-87/tk/tk/library/demos/knightstour.tcl

import random

from tkinter import *
from tkinter import ttk
from tkinter.font import Font

from demopanels import MsgPanel, SeeDismissPanel

class KnightsTourDemo(ttk.Frame):
    
    def __init__(self, isapp=True, name='knightstourdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Knights Tour Canvas Demo')
        self.isapp = isapp
        self._create_widgets()
        
    def _create_widgets(self):
        if self.isapp:
            # message panel not required          
            SeeDismissPanel(self)
        
        self._create_demo_panel()
        
    def _create_demo_panel(self):
        demoPanel = Frame(self, name='demo')
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)
        
        board = self._create_tour(demoPanel)
        self._add_bindings(board)
        
    def _create_tour(self, parent):
        c = Canvas(parent, width=240, height=240, name='board')
        self._draw_board(c)
        
        txt = Text(parent, width=10, height=1, name='dlg',
                   background='white', font=('Arial', 8))
        vscroll = ttk.Scrollbar(parent, orient=VERTICAL,
                                command=txt.yview)
        txt['yscrollcommand'] = vscroll.set
        controls = self._create_controls(parent, c)

        # position and configure resize behaviour
        c.grid(row=0, column=0, sticky='news')
        txt.grid(row=0, column=1, sticky='news')
        vscroll.grid(row=0, column=2, sticky='news')
        controls.grid(row=1, column=0, columnspan=3,
                      sticky=N+E)
        
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(1, weight=1)
        
        return c                

    def _draw_board(self, canvas):   
        # draw checkerboard
        for r in range(7, -1, -1):
            for c in range(8):
                if c&1 ^ r&1:
                    fill = 'tan3'
                    dfill = 'tan4'
                else:
                    fill = 'bisque'
                    dfill= 'bisque3'
                coords = (c*30+4, r*30+4, c*30+30, r*30+30)
                canvas.create_rectangle(coords,
                                        fill=fill,
                                        disabledfill=dfill,
                                        width=2,
                                        state='disabled')
                
        # create knight
        canvas.create_text(0, 0, font=('Courier 20'), text='\u265e',
                           anchor='nw', tags='knight',
                           fill='black', activefill='#600000')
        
        # randomly place him on the board
        self._put_random_knight(canvas)
                
    def _create_controls(self, parent, canvas):
        # board controls
        delay = IntVar()
        continuous = BooleanVar()
        
        frame = ttk.Frame(parent, name='controls')
        ttk.Label(frame, text='Speed').pack(side=RIGHT, padx=(4,24), pady=12)
        ttk.Scale(frame, from_=8, to=2000,
                  variable=delay).pack(side=RIGHT, padx=4, pady=12)
        ttk.Checkbutton(frame, text='Repeat',
                        variable=continuous).pack(side=RIGHT, padx=4, pady=12)
        btn = ttk.Button(frame, text='Start', name='start')
        btn['command'] = self._start_tour
        btn.pack(side=RIGHT, padx=(16,4), pady=12)        

        # set variable values and safe a reference to them        
        delay.set(600)
        continuous.set(False)
        canvas.__delay = delay
        canvas.__continuous = continuous
        
        return frame
                                
    # ========================================================================
    # Bindings
    # ========================================================================
    def _add_bindings(self, board):
        board.tag_bind('knight', '<1>', 
                       lambda e, b=board: self._start_drag(e, b))
        board.tag_bind('knight', '<B1-Motion>', 
                       lambda e, b=board: self._drag(e,b))
        board.tag_bind('knight', '<ButtonRelease-1>', 
                       lambda e, b=board: self._end_drag(e,b))    
                
    # ========================================================================
    # Bound methods
    # ========================================================================
                                
    def _start_drag(self, evt, board):
        # save drag start coords
        board.__lastX = board.canvasx(evt.x)
        board.__lastY = board.canvasy(evt.y)
    
    def _drag(self, evt, board):
        # move the knight with the mouse
        x = board.canvasx(evt.x)
        y = board.canvasy(evt.y)
        board.move(CURRENT, x-board.__lastX, y-board.__lastY)
        board.__lastX = x
        board.__lastY = y
        
    def _end_drag(self, evt, board):
        # place the knight in the square closest to
        # the mouse position
        square = board.find_closest(evt.x, evt.y, 0, 65)
        coords = board.coords(square)        
        board.coords(CURRENT, (coords[0], coords[1]))

    # ========================================================================
    # Commands
    # ========================================================================

    def _start_tour(self, square=None):        
        # start a new Knight's Tour
        self._toggle_start_btn('disabled')    
    
        b = self.nametowidget('demo.board')     # board
        t = self.nametowidget('demo.dlg')       # text 
        
        t.delete(1.0, END)    # clear text
        visited = []          # squares visited in this tour
        
        for n in range(64):
            b.itemconfigure(n, {'state': 'disabled',
                                'outline': 'black'})
        
        if not square:
            # get start position from current placement of knight
            coords = b.coords('knight')
            square = b.find_closest(coords[0], coords[1], 0, 65)

        if square[0] > 64:
            # knight is off the board
            self._put_random_knight(b)
            coords = b.coords('knight')
            square = b.find_closest(coords[0], coords[1], 0, 65)
                
        square = (square[0]-1, )
        b.__initial = square    # save starting square
        
        self._move_piece(b, t, square, square, visited)


    # ========================================================================
    # Chessboard methods
    # ========================================================================
    def _toggle_start_btn(self, newState):
        sbtn = self.nametowidget('demo.controls.start')
        sbtn.configure(state=newState)
        
    def _put_random_knight(self, board):
        # randomly choose a board square and position
        # the knight
        sqr = int( 1 + random.random() * 64)
        coords = board.coords((sqr, ))
        board.coords('knight', (coords[0], coords[1]))
        
    def _move_piece(self, b, txt, last, square, visited):
        # b - chess board (canvas)
        # txt - text console 
        # last - last square visited
        # square - current square    
        
        # display the square moves using standard
        # chess nomenclature
        chessSqr = '{}. {} .. {}\n'.format(len(visited),
                                    self._chess_sqr(last),
                                    self._chess_sqr(square) )
        txt.insert(END, chessSqr )
        txt.see(END)
        
        # configure squares, move the knight and update visited squares
        b.itemconfigure(1+last[0], state='normal', outline='black')
        b.itemconfigure(1+square[0], state='normal', outline='red')
        coords = b.coords(1+square[0])
        b.coords('knight', (coords[0], coords[1]))
        visited.append(square[0])
        
        # get the next move
        next = self._next_square(square[0], visited)
        if next != -1:
            # new legal move, pause and then move the knight
            self.after(b.__delay.get(), self._move_piece, b, txt, square, (next,), visited)           
        else:
            # no legal moves left
            if len(visited) == 64:
                if b.__initial == square:
                    txt.insert(END, 'Closed tour!\n')
                    self._toggle_start_btn('normal')
                else:
                    txt.insert(END, 'Success\n')
                    self._toggle_start_btn('normal')
                    if b.__continuous.get():
                        self.after(b.__delay.get() * 2,
                                   self._start_tour,
                                   self._put_random_knight(b))
            else:
                txt.insert(END, 'Failed!\n')
                self._toggle_start_btn('normal')
                
        return    
                
    def _chess_sqr(self, square):
        # Display a square number as a standard chess square notation.
        return '{}{}'.format(chr(97 + square[0]%8), square[0]//8 + 1)
                
    def _valid_moves(self, square):
        # Return a list of squares accessible from the given square
        moves = []
        pairs = [(-1,-2), (-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2)]
        for p in pairs :
            col = (square % 8) + p[0]
            row = (square // 8) + p[1]
            if (-1 < row < 8) and (-1 < col < 8):
                moves.append(row * 8 + col)
         
        return moves        
    
    def _check_squares(self, square, visited):
        # Return the number of available moves for this square
        moves = 0
        for test in self._valid_moves(square):
            if test not in visited:
                moves += 1
                
        return moves        

    def _next_square(self, square, visited):
        # Select the next square to move to. 
        # Returns -1 if no valid moves left
        minimum = 9
        nextSqr = -1
        for t in self._valid_moves(square):
            if t not in visited:
                count = self._check_squares(t, visited)
                if count < minimum:
                    minimum = count
                    nextSqr = t
                elif count == minimum:
                    nextSqr = self._edgemost(nextSqr, t)
                    
        return nextSqr

    def _edgemost(self, a, b):
        # Select the square nearest the edge of the board        
        colA = 3 - int(abs(3.5 - (a % 8)))
        colB = 3 - int(abs(3.5 - (b % 8)))
        rowA = 3 - int(abs(3.5 - (a // 8)))
        rowB = 3 - int(abs(3.5 - (b // 8)))
        
        if (colA * rowA) < (colB * rowB):
            return a
        else:
            return b
    
if __name__ == '__main__':
    KnightsTourDemo().mainloop()