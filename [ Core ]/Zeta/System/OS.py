import os
import subprocess
import platform

Windows = True if platform.system() == 'Windows' else False
Linux = True if platform.system() == 'Linux' else False
Mac = True if platform.system() == 'Darwin' else False

def open(fullpath):
	if os.path.isfile(fullpath): path = os.path.split(fullpath)[0]
	else: path = fullpath
	os.startfile(path)
	#subprocess.Popen(r'explorer /select,"C:\xampp"')

def edit(fullpath):
	subprocess.Popen(['C:\Program Files\Sublime Text 3\sublime_text.exe', fullpath], start_new_session=True)
	#os.startfile(r'C:\Program Files\Sublime Text 3\sublime_text.exe '+fullpath)

def terminal(fullpath):
	if os.path.isfile(fullpath): path = os.path.split(fullpath)[0]
	else: path = fullpath
	
	if Windows: subprocess.Popen(r'cmd /k cd /d '+path)
