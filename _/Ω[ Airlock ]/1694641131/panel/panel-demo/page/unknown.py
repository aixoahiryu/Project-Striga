#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Jul 22, 2023 07:00:06 PM +07  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import unknown_support

title = 'test'

_bgcolor = '#ffffff'  # X11 color: 'white'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

class Toplevel1:
    def __init__(self, top=None):
        global title
        title = 'test2'

        top.geometry("600x450+144+139")
        top.attributes('-topmost', True)
        top.minsize(112, 1)
        top.maxsize(1366, 746)
        top.resizable(1,  1)
        top.title(title)
        top.configure(background="#ffffff")

        top2 = tk.Toplevel()
        top2.geometry("200x450+144+139")
        #top2.overrideredirect(1)
        #top2.attributes('-topmost', True)
        top2.title('transient')
        top2.transient(top)

        self.top = top

def start_up():
    unknown_support.main()

if __name__ == '__main__':
    unknown_support.main()




