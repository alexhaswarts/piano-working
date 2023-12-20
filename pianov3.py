import tkinter as tk
import pygame

pygame.init()

def play_sound(note):
    pygame.mixer.music.load(f"piano_sounds/{note}.wav")
    pygame.mixer.music.play(0)

def keyplays(note, key):
    app.bind(key, lambda event, n=note: play_sound(n))

def bindedkeys():
    key_mapping = {
        "C": "a",
        "C#": "s",
        "D": "d",
        "D#": "f",
        "E": "g",
        "F": "h",
        "F#": "j",
        "G": "k",
        "G#": "l",
        "A": ";",
        "A#": "'",
        "B": "Enter"
    }

    for note, key in key_mapping.items():
        keyplays(note, key)

app = tk.Tk()
app.title("Piano")

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

for note in notes:
    if "#" in note:
        button = tk.Button(app, text=note, width=10, height=25, bg="black", fg="white", command=lambda n=note: play_sound(n))
    else:
        button = tk.Button(app, text=note, width=20, height=30, bg="white", fg="black", command=lambda n=note: play_sound(n))
    button.grid(row=0, column=notes.index(note))

bindedkeys()

pygame.mixer.music.set_volume(1)

app.mainloop()
