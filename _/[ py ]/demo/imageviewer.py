# File: imageviewer.py
# References:
#    http://www.tcl.tk/man/tcl8.5/TkCmd/ttk_labelframe.htm
#    http://www.tcl.tk/man/tcl8.5/TkCmd/listbox.htm
#    http://www.tcl.tk/man/tcl8.5/TkCmd/ttk_label.htm
#    http://www.tcl.tk/man/tcl8.5/TkCmd/bind.htm 
#    http://infohost.nmt.edu/tcc/help/pubs/pil/index.html
#    http://www.pythonware.com/library/pil/handbook/introduction.htm

import os
from os.path import basename
from glob import *
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from demopanels import MsgPanel, SeeDismissPanel

# file formats that can be 'read' by PIL
FILETYPES = ['.bmp', '.dib', '.dcx', '.gif', '.im', '.jpg',
             '.jpe', '.jpeg', '.pcd', '.pcx', '.png', '.pbm',
             '.pgm', '.ppm', '.psd', '.tif', '.tiff', '.xbm', 
             '.xpm']

class ImageViewerDemo(ttk.Frame):
    
    def __init__(self, isapp=True, name='imageviewerdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Image Viewer Demo')
        self.isapp = isapp
        self._create_widgets()
        
    def _create_widgets(self):
        if self.isapp:
            MsgPanel(self, 
                     ["This demonstration allows you to view images using the Python Imaging Library (PIL).\n\n",
                      "To view an image, double-click on its name in the 'Files' list.\n\n",
                      "To view images in another directory, click on the ",
                      "'Directory...' button and select a new directory via a 'File Dialog'."])
            
            SeeDismissPanel(self)
        
        self._create_demo_panel()
        
    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)
        
        dirPanel = self._create_dir_panel(demoPanel)
        filePanel = self._create_file_panel(demoPanel)
        imagePanel = self._create_image_panel(demoPanel)
        
        # position panels        
        dirPanel.grid(in_=demoPanel, sticky='ew', padx='1m', pady='1m', columnspan=2)
        filePanel.grid(in_=demoPanel, sticky='nw', padx='1m', pady='1m', row=1, column=0)
        imagePanel.grid(in_=demoPanel, sticky='nw', padx='1m', pady='1m', row=1, column=1)
        demoPanel.columnconfigure(1, weight=1)
        
        self.entry.focus_set() 

    def _create_dir_panel(self, parent):
        lf = ttk.Labelframe(parent, text='Directory')
        lf.pack(side=TOP, fill=BOTH, expand=Y)
        
        self.curpath = os.path.join(os.getcwd(),'images')  # current path
        self.dirName = StringVar()  # entry control variable
        self.dirName.set(self.curpath)
        
        self.entry = ttk.Entry(lf, width=30, textvariable=self.dirName)
        self.entry.bind('<Return>', self._load_dir)
        
        btn = ttk.Button(lf, text='Directory...',
                         command=self._select_dir)
        
        self.entry.pack(side=LEFT, fill=BOTH, padx='2m', pady='2m', expand=Y)
        btn.pack(side=LEFT, fill=Y, padx=(0, '2m'), pady='2m')

        return lf
    
    def _create_file_panel(self, parent):
        lf = ttk.Labelframe(parent, text='Files')
        lf.pack(side=TOP, fill=BOTH, expand=Y)       
        
        # there is no ttk.Listbox; however, ttk.Scrollbar
        # works fine with the tkinter Listbox
        self.files = Listbox(lf, width=20, height=10)
        sbar = ttk.Scrollbar(lf, command=self.files.yview, orient=VERTICAL)
        self.files.configure(yscrollcommand=sbar.set)
        self._load_dir()
        
        self.files.pack(side=LEFT, fill=Y, expand=Y)
        sbar.pack(side=LEFT, fill=Y, expand=Y)
        
        self.files.bind('<Double-1>', self._load_image)
        
        return lf
    
    def _create_image_panel(self, parent):
        lf = ttk.Labelframe(parent, text='Image')
        
        # image handle to prevent garbage collection
        # of current display image
        self.imh = None    

        self.labelImage = ttk.Label(lf, image=self.imh, relief=SUNKEN, border=2)
        self.labelImage.pack(side=TOP, padx='.5m', pady='.5m')
        
        return lf
    
    def _select_dir(self):
        dir = filedialog.askdirectory(initialdir=self.dirName.get(),
                                      parent=self,
                                      title='Select a new files image directory',
                                      mustexist=True) # only existing dirs
        if dir:
            self.dirName.set(dir)
            self._load_dir()
    
    def _load_dir(self, *args):
        dn = os.path.join(self.dirName.get(), '*')

        self.files.delete(0, END)
        
        # populate files list with filenames from
        # selected directory
        for f in iglob(dn):
            if os.path.splitext(f)[1] in FILETYPES:
                self.files.insert(END, basename(f))
        
        # prevent <Return> event from propagating to
        # windows higher up in the hierarchy
        return 'break'
    
    def _load_image(self, event):
        item = self.files.curselection()
        fn = self.files.get(item)
        
        imagePath = os.path.join(self.dirName.get(), fn)    
            
        try:
            im = Image.open(imagePath)

            if im.mode == '1':
                self.imh = ImageTk.BitmapImage(im)
            else:
                self.imh = ImageTk.PhotoImage(im)
            self.labelImage.configure(image=self.imh)
        
        except Exception:
            # mark non-image selections
            self.files.itemconfig(item, background='red', 
                                  selectbackground='red')
            
        
if __name__ == '__main__':
    ImageViewerDemo().mainloop()