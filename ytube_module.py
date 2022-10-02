from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
import threading
from moviepy.editor import VideoFileClip
import tkinter as tk
# bar = tk.Toplevel()


def get_urls(url):
    urls = []
    if '&list=' not in url:
        return urls
    p = Playlist(url)
    for u in p.video_urls:
        urls.append(u)
    return urls


"""
def onProgress(stream, chunk, remains):
    total = stream.filesize
    percent = (total - remains) / total

    canvas = tk.Canvas(bar, width=465, height=22, bg="white")
    canvas.place(x=110, y=60)
    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
    x = 100  # 未知變量，可更改
    raise_data = 100 / percent  # 465是矩形填充滿的次數
    n = 0
    for i in range(x):
        n = n + raise_data
        canvas.coords(fill_line, (0, 0, n, 60))
        bar.update()
        time.sleep(0.5)

"""
# text = "download.......{0:.2f}".format(percent)


def mp4tomp3(file_name):
    str = 'D:\\downloads\\歌\\name1.mp4'
    mp4_file = str.replace("name1", file_name)
    str2 = 'D:\\downloads\\歌\\name1.mp3'
    mp3_file = str2.replace("name1", file_name)
    videoclip = VideoFileClip(mp4_file)
    audio_clip = videoclip.audio
    audio_clip.write_audiofile(mp3_file)
    audio_clip.close()
    videoclip.close()


lock = threading.Lock()


def start_dload(url, listbox):
    # bar = tk.Toplevel()
    yt = YouTube(url)
    name = yt.title
    # ~~~~~~
    lock.acquire()
    no = listbox.size()
    listbox.insert(tk.END, f'{no:02d}:{name}......下載中')
    f_str = 'download' + str(no)
    print('插入:', no, name)
    lock.release()
    # ~~~~~~~

    yt.streams.first().download(output_path='D:/downloads/歌',
                                filename=f'download{no}')

    # ~~~~~~~
    lock.acquire()
    print('\n\n', '更新:', no, name)
    listbox.delete(no)
    listbox.insert(no, f'{no:02d}:●{name}......下載完成')
    mp4tomp3(f_str)
    lock.release()
    # ~~~~~~~~
