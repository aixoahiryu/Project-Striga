import os
import subprocess
import sys

def open(fullpath):
	if os.path.isfile(fullpath): path = os.path.split(fullpath)[0]
	else: path = fullpath
	os.startfile(path)

def edit(fullpath):
	subprocess.Popen(['C:\Program Files\Sublime Text 3\sublime_text.exe', fullpath], start_new_session=True)

def terminal(fullpath):
	if os.path.isfile(fullpath): path = os.path.split(fullpath)[0]
	else: path = fullpath
	subprocess.Popen(r'cmd /k cd /d '+path)
