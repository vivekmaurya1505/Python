import tkinter as tk
from tkinter import messagebox
from functools import partial
root = tk.Tk()

def on_closing(x):
    if messagebox.askyesno("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", partial(on_closing,3))
root.mainloop()


