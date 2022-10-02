import ytube_module as m
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from tkinter import filedialog

import pygame
import threading
import time


def click_func():
    url = yt_url.get()

    try:
        YouTube(url)
    except:
        messagebox.showerror('錯誤', 'pytube 不支援此影片或者網址錯誤')
        return

    urls = m.get_urls(url)

    if urls and messagebox.askyesno('確認方塊', '是否下載清單內的所有影片? 選擇 否(N) 則下載單一影片'):
        print('開始下載清單')
        # urls.sort(key=lambda s: int(re.search("index=\d+", s).group()[6:]))
        for u in urls:
            threading.Thread(target=m.start_dload, args=(u, listbox)).start()
            time.sleep(0.5)

    else:
        yt = YouTube(url)
        if messagebox.askyesno('確認方塊', f'是否下載{yt.title}影片?'):
            threading.Thread(target=m.start_dload, args=(url, listbox)).start()
        else:
            print('取消下載')


def play():
    filepath = filedialog.askopenfilename(initialdir='D:/downloads/歌',
                                          filetypes=(("mp3files", "*.mp3"),
                                                     ("all files", "*.*")))
    if not filepath:
        messagebox.showerror('warn', "出錯了")
    else:
        # file = os.path.basename(filepath)
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)
        track = pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()


def click_openfile():
    threading.Thread(target=play).start()


"""
def increment(*args):
    p1.start()
"""
# .................................#

window = tk.Tk()
window.geometry('640x480')
window.resizable(False, False)
window.title('Youtube 下載器')

# ........yturl......#

input_fm = tk.Frame(window, bg='red', width=640, height=120)
input_fm.pack()

lb = tk.Label(input_fm,
              text='請輸入 YouTube 影片網址',
              bg='red',
              fg='white',
              font=('細明體', 12, 'bold'))
lb.place(rely=0.25, relx=0.5, anchor='center')

yt_url = tk.StringVar()
entry = tk.Entry(input_fm, textvariable=yt_url, width=50)
entry.place(rely=0.5, relx=0.5, anchor='center')

btn = tk.Button(input_fm,
                text='下載影片',
                command=click_func,
                bg='#FFD700',
                fg='Black',
                font=('細明體', 10))
btn.place(rely=0.5, relx=0.85, anchor='center')

# ....listbox..........#

dload_fm = tk.Frame(window, width=640, height=360)
dload_fm.pack()

lb = tk.Label(dload_fm, text='下載狀態', fg='black', font=('細明體', 10))
lb.place(rely=0.1, relx=0.5, anchor='center')

listbox = tk.Listbox(dload_fm, width=65, height=15)
listbox.place(rely=0.5, relx=0.5, anchor='center')

sbar = tk.Scrollbar(dload_fm)
sbar.place(rely=0.5, relx=0.87, anchor='center', relheight=0.7)

sbar_x = tk.Scrollbar(dload_fm, orient=tk.HORIZONTAL)
sbar_x.place(rely=0.81, relx=0.14, anchor='w', relheight=0.05, relwidth=0.7)

listbox.config(yscrollcommand=sbar.set)
sbar.config(command=listbox.yview)
listbox.config(xscrollcommand=sbar_x.set)
sbar_x.config(command=listbox.xview)

play_button = tk.Button(dload_fm,
                        text='openfile',
                        command=click_openfile,
                        bg='#FFD700',
                        fg='Black',
                        font=('細明體', 10))

play_button.place(rely=0.9,
                  relx=0.5,
                  anchor='center',
                  relheight=0.1,
                  relwidth=0.1)
"""
p1 = ttk.Progressbar(window,
                     length=200,
                     mode="determine",
                     maximum=200,
                     orient=tk.HORIZONTAL)"""
# .................#

window.mainloop()
