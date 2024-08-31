import requests   # type: ignore
import tkinter as ttk
import ttkbootstrap as ttk  

url = "http://api.quotable.io/random"


def fetch_quote():
    response = requests.get(url)
    data = response.json
    quote = data["content"]
    author = data["author"]
    return quote, author


def update_quote():
    quote, author = fetch_quote()
    qoute_label.config(text=quote)
    author_label.config(text=f"~{author}")


root = ttk.window(themename="pulse")
root.title("quotes generator")
root.geometry("700x250")

frame = ttk.frame(root)
frame.pack(padx=30, pady=40)

qoute_label = ttk.label(frame, text="", font=("helvetica", 16), wraplength=650)
qoute_label.pack()

author_label = ttk.label(frame, text="", font=("helvetica", 12))
author_label.pack(pady=10)

ttk.button(frame, text="get quote", command=update_quote).pack(pady=20)
root.mainloop()
