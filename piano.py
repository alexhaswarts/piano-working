import tkinter as tk
import pygame


pygame.init()


def play_sound(note):
    pygame.mixer.music.load(f"piano_sounds/{note}.wav")
    pygame.mixer.music.play(0)


app = tk.Tk()
app.title("Piano")


notes = ["C", "D", "E", "F", "G", "A", "B"]


for note in notes:
    button = tk.Button(app, text=note, width=20, height=30, command=lambda n=note: play_sound(n))
    button.grid(row=0, column=notes.index(note))


pygame.mixer.music.set_volume(0.5)


app.mainloop()