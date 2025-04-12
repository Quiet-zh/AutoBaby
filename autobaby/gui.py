# autobaby/gui.py
import tkinter as tk
from .core import start_scheduler

def create_window():
    root = tk.Tk()
    root.title("AutoBaby")
    start_btn = tk.Button(root, text="开始定时任务", command=start_scheduler)
    start_btn.pack()
    root.mainloop()