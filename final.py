import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from pygame import mixer

# Initialize pygame mixer
mixer.init()


window = tk.Tk()
window.title("Gong Player")
window.geometry("450x250")

# Create the playlist frame on the top
playlist_frame = tk.Frame(window, bg="white")
playlist_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create the scrollbar for the playlist
scrollbar = tk.Scrollbar(playlist_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create the listbox for the playlist
playlist = tk.Listbox(playlist_frame, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set, bg="black", fg="white", font=('arial', 12))
playlist.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Link the scrollbar with the playlist
scrollbar.config(command=playlist.yview)

# Add the songs to the playlist
def add_songs():
    songs = filedialog.askopenfilenames(title="Select Songs", filetypes=[("Audio Files", "*.mp3;*.wav")])
    for song in songs:
        playlist.insert(tk.END,song)



buttons_frame = tk.Frame(window)
buttons_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

play_button = tk.Button(buttons_frame, text=" Play  ", font=('arial', 15), bg="green", fg="white", padx=10, pady=5)
play_button.pack(side=tk.LEFT, padx=5, pady=5)

pause_button = tk.Button(buttons_frame, text="Pause", font=('arial', 15), bg="red", fg="white", padx=9, pady=5)
pause_button.pack(side=tk.LEFT, padx=5, pady=5)

stop_button = tk.Button(buttons_frame, text=" Stop  ", font=('arial', 15), bg="red", fg="white", padx=8, pady=5)
stop_button.pack(side=tk.LEFT, padx=5, pady=5)

volume_scale = tk.Scale(buttons_frame, from_=0, to=100, orient=tk.HORIZONTAL, font=('arial', 12), bg="white")
volume_scale.set(80)
volume_scale.pack(side=tk.BOTTOM, padx=4, pady=4)

def play_song():
    try:
        selected_song = playlist.get(playlist.curselection())
        mixer.music.load(selected_song)
        mixer.music.play()
    except:
        messagebox.showerror("Error", "No song selected")


def pause_song():
    mixer.music.pause()


def stop_song():
    mixer.music.stop()

def set_volume(val):
    mixer.music.set_volume(int(val)/100)

play_button.config(command=play_song)
pause_button.config(command=pause_song)
stop_button.config(command=stop_song)
volume_scale.config(command=set_volume)

add_songs_button = tk.Button(window, text="Add Songs", font=('arial', 10), bg="white", fg="black", command=add_songs)
add_songs_button.pack(side=tk.BOTTOM, padx=5, pady=5)

window.mainloop()
