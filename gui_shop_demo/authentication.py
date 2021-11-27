from tkinter import Button, Entry
from Advanced.gui_shop_demo.canvas import tk
from gui_shop_demo.helpers import clean_screen


def login():
    pass

def render_login():
    clean_screen()
    username = Entry(tk)
    username.grid(row=0, column=0)
    password = Entry(tk)
    password.grid(row=1, column=0)
    Button(tk, text="Enter", bg="green").grid(row=2, colum=0)

def render_main_enter_screen():
    Button(tk, text="Login", bg="green", fg="white", command=render_login()).grid(row=0, column=0)
    Button(tk, text="Register", bg="yellow").grid(row=0, column=1)
