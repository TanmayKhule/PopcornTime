import tkinter as tk
import requests
from bs4 import BeautifulSoup as Soup
import sys
import os
from webscrapper import *

root = tk.Tk()

canvas1 = tk.Canvas(root, width=1500, height=650, relief="raised")
canvas1.pack()
canvas1.configure(bg="peachpuff")

label1 = tk.Label(root, text="Popcorn Time")
label1.config(font=("helvetica", 14))
canvas1.create_window(600, 425, window=label1)
label1.configure(bg="peachpuff")

label2 = tk.Label(root, text="Movie Name:")
label2.config(font=("helvetica", 10))
canvas1.create_window(600, 450, window=label2)
label2.configure(bg="peachpuff")
entry1 = tk.Entry(root)
canvas1.create_window(600, 500, window=entry1)


def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def getReviews():
    movie_name_raw = entry1.get()
    # summary = ""
    summary_imdb = IMDB(movie_name_raw)

    summary_rt = rottenTomatoe(movie_name_raw)

    textbox_rt = tk.Text(root, font=("helvetica", 10))
    textbox_rt.insert(tk.END, summary_rt)
    textbox_rt.pack(fill=tk.BOTH, expand=True)
    canvas1.create_window(100, 100, window=textbox_rt)
    textbox_rt.place(x=20, y=10)

    textbox_imdb = tk.Text(root, font=("helvetica", 10))
    textbox_imdb.insert(tk.END, summary_imdb)
    textbox_imdb.pack(fill=tk.BOTH, expand=True)
    canvas1.create_window(100, 100, window=textbox_imdb)
    textbox_imdb.place(x=640, y=10)


button1 = tk.Button(
    text="Get the Reviews",
    command=getReviews,
    bg="mediumpurple3",
    fg="white",
    font=("helvetica", 9, "bold"),
)
canvas1.create_window(600, 540, window=button1)

button2 = tk.Button(text="Reload", command=restart, bg="mediumpurple3", fg="white")
canvas1.create_window(600, 580, window=button2)

root.mainloop()