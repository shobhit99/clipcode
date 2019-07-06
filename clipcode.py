#!/usr/bin/env python3.7
from pynput import keyboard
import pyperclip
import time
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import requests
from sys import exit
#languages to be listed
# add your own keycodes https://www.lucidar.me/en/web-dev/list-of-supported-languages-by-prism/
OPTIONS = [
    "None",
    "c",
    "python",
    "html",
    "php",
    "java",
    "javascript",
    "css",
    "markup",
    "bash",
    "cpp",
    "csharp",
    "go",
    "perl",
    "sql"
] 
# Hotkey for execute()
COMBINATIONS = [
    {keyboard.Key.scroll_lock}
]

current = set()

ui_theme = "vista" if sys.platform == "win32" else "alt"

def upload(code, lang):
    d = {
        'code' : code,
        'language' : lang
    }
    h = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }
    resp = requests.post("https://clipco.de/upload.php", data = d, headers=h)
    return resp.text

def execute():
    root = Tk()
    style = ttk.Style()
    style.theme_use(ui_theme)
    root.title("ClipCode")
    root.lift()
    topframe = Frame(root)
    topframe.pack( padx=10, pady=10)
    bottomframe = Frame(root)
    bottomframe.pack(side=BOTTOM, padx=10, pady=5)
    title = Label(topframe, text="Syntax Highlighting")
    title.pack(side=LEFT)
    variable = StringVar(root)
    variable.set(OPTIONS[0]) # default value
    w = OptionMenu(topframe, variable, *OPTIONS)
    w.pack(side=LEFT)
    button = Button(topframe, text="Upload", command=lambda: E1.insert(0,"https://clipco.de/"+upload(pyperclip.paste(), variable.get())))
    button.pack(side=LEFT)
    E1 = Entry(bottomframe, width=25)
    E1.pack(side = LEFT, padx=5, pady=5)
    def copyurl(urltext):
        pyperclip.copy(urltext)
        time.sleep(0.01)
        root.destroy()
    button = Button(bottomframe, text="Copy", command=lambda: copyurl(E1.get()))
    button.pack(side=LEFT)
    root.mainloop()
def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
