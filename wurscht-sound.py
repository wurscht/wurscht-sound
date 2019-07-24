import os
import tkinter as tk
import vlc
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3


class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master


root = tk.Tk()
root.minsize(1000, 500)
app = Window(root)

songs = []

realnames = []

v = tk.StringVar()
songlabel = tk.Label(root, textvariable=v, width=35)

index = 0


def choose_directory():
    directory = askdirectory()
    os.chdir(directory)

    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            realdir = os.path.realpath(file)
            audio = ID3(realdir)
            realnames.append(audio["TIT2"].text[0])
            songs.append(file)
    # song = vlc.MediaPlayer(songs[0])
    return songs


def play_song(songs):
    actual_song = vlc.MediaPlayer(songs[0])
    actual_song.play()
    return actual_song


def stop_song(song):
    song.stop()
    v.set("")


def update_label():
    global index
    global songname
    v.set(realnames[index])


def next_song(song, index):
    song = vlc.MediaPlayer(songs[0])
    song.stop()
    index += 1
    song = vlc.MediaPlayer(songs[index])
    song.play()
    update_label()


def prev_song(song, index):
    index -= 1
    song = vlc.MediaPlayer(songs[index])
    song.play()
    update_label()


def print_shit():
    print("wuuuuuuuurscht")


actual_song = play_song(choose_directory())


label = tk.Label(root, text="Wurscht-Sounds")
label.pack()

listbox = tk.Listbox(root)
listbox.pack()

realnames.reverse()

for items in realnames:
    listbox.insert(0, items)

realnames.reverse()

nextbutton = tk.Button(root, text="Next Song")
nextbutton.pack()

previousbutton = tk.Button(root, text="Previous Song")
previousbutton.pack()

stopbutton = tk.Button(root, text="Stop Music")
stopbutton.pack()

nextbutton.bind("<Button-1>", next_song(songs[index], index))
previousbutton.bind("<Button-1>", prev_song(songs[index], index))
stopbutton.bind("<Button-1>", print_shit())

songlabel.pack()

root.mainloop()
