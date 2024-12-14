import tkinter as tk
from random import randint
from tkinter import font


def roll_dice():
    result = randint(1, 6)
    label.config(text=str(result))


def center_window(root, width=300, height=200):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    root.geometry(f'{width}x{height}+{x}+{y}')


root = tk.Tk()
root.title("Symulator rzutu kostką")

center_window(root, 300, 200)

root.columnconfigure(0, weight=1)
custom_font = font.Font(family="Helvetica", size=16, weight="bold")

label = tk.Label(root, text="Kliknij, aby rzucić kostką", font=custom_font)
label.grid(row=0, column=0, pady=20)

button = tk.Button(root, text="Rzuć kostką", command=roll_dice)
button.grid(row=1, column=0, pady=80)

root.mainloop()
