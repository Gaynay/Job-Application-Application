import tkinter as tk
from tkinter import ttk

def show_window(input_text):
    """Creates a simple tkinter window to display the input text"""
    root = tk.Tk()
    root.title("Display Input")

    label = ttk.Label(root, text=f"You Typed: {input_text}", font=("Arial", 14))
    label.pack(pady=20, padx=20)

    close_btn = ttk.Button(root, text="Close", command=root.destroy)
    close_btn.pack(pady=10)

    root.mainloop()