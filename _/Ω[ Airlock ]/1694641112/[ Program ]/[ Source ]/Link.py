import subprocess
import webbrowser
import os

#import win32clipboard
import tkinter
import tkinter.messagebox


# win32clipboard.OpenClipboard()
# data = win32clipboard.GetClipboardData()
# win32clipboard.CloseClipboard()
root = tkinter.Tk()
root.withdraw()
data = root.clipboard_get()
os.chdir('C:\\Users\\Administrator\\Desktop')


data = data.rstrip()
if data.startswith('http'):
    if data.startswith('https://boards.4chan.org/pol/thread/'):
        data = data.replace('https://boards.4chan.org/pol/thread/', 'https://archive.4plebs.org/pol/thread/')
        subprocess.Popen(["C:\Program Files\Links\links-g.exe", data], start_new_session=True)
    elif data.startswith('https://boards.4channel.org/g/thread/'):
        data = data.replace('https://boards.4channel.org/g/thread/', 'https://desuarchive.org/g/thread/')
        subprocess.Popen(["C:\Program Files\Links\links-g.exe", data], start_new_session=True)
    elif data.startswith('https://boards.4channel.org/x/thread/'):
        data = data.replace('https://boards.4channel.org/x/thread/', 'https://archive.4plebs.org/x/thread/')
        subprocess.Popen(["C:\Program Files\Links\links-g.exe", data], start_new_session=True)
    elif data.endswith(('.mp4','.webm')):
        subprocess.Popen(['D:\Tools\mpv\mpv.exe', data], start_new_session=True)
    elif 'twitch.tv' in data[1:30]:
        subprocess.Popen(['D:\Tools\mpv\mpv.exe', data], start_new_session=True)
    elif 'youtube.com' in data[1:30]:
        os.system('youtube-dl -f 18 '+data)
    elif 'github.com' in data[1:30]:
        data = data.replace('/blob/','/raw/')
        webbrowser.open(data, new=2, autoraise=True)
    else:
        subprocess.Popen(["C:\Program Files\Links\links-g.exe", data], start_new_session=True)
    #subprocess.run(["C:\Program Files\Links\links-g.exe", data])
    #tkinter.messagebox.showinfo(title="URL", message=data)
elif data.startswith('/'):
    if data.startswith('/pol/'):
        data = data.replace('/pol/', 'https://archive.4plebs.org/pol/post/')
    elif data.startswith('/g/'):
        data = data.replace('/g/', 'https://desuarchive.org/g/post/')
    elif data.startswith('/x/'):
        data = data.replace('/x/', 'https://archive.4plebs.org/x/post/')
    subprocess.Popen(["C:\Program Files\Links\links-g.exe", data], start_new_session=True)
elif "\n" in data:
    data2=data.split()
    for i in data2:
        if i.startswith('http'):
            webbrowser.open(i, new=2, autoraise=True)
elif len( data.replace('_480p','').replace('_720p','') )==32:
    webbrowser.open('https://e621.net/posts?tags=md5:'+data.replace('_480p','').replace('_720p',''), new=2, autoraise=True)
elif data.endswith(']'):
    webbrowser.open('https://youtu.be/'+data[data.rfind('[')+1:data.rfind(']')], new=2, autoraise=True)
elif data.startswith('embed/'):
    webbrowser.open('https://youtu.be/'+data.replace('embed/',''), new=2, autoraise=True)
else:
    #subprocess.Popen(["C:\Program Files\Links\links-g.exe", "https://www.google.com/search?hl=en&q="+data], start_new_session=True)
    webbrowser.open("https://archive.4plebs.org/pol/search/text/"+data, new=2, autoraise=True)
    webbrowser.open("https://desuarchive.org/g/search/text/"+data, new=2, autoraise=True)
    webbrowser.open("https://archive.4plebs.org/x/search/text/"+data, new=2, autoraise=True)
    webbrowser.open("https://desuarchive.org/k/search/text/"+data, new=2, autoraise=True)

