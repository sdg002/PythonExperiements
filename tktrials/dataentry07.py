"""
Remember the screen position of the window when it is closed and restore it when reopened.
"""

import tkinter as tk
import os
import json

# File to store window position
POSITION_FILE = "window_position.json"

def save_position(root):
    current_geometry = root.geometry()
    with open(POSITION_FILE, "w") as f:
        json.dump({"geometry": current_geometry}, f)

def load_position():
    if os.path.exists(POSITION_FILE):
        with open(POSITION_FILE, "r") as f:
            data = json.load(f)
            return data.get("geometry")
    return None

def on_closing():
    save_position(root)
    root.destroy()

root = tk.Tk()

# Load and set previous position
geometry = load_position()
if geometry:
    root.geometry(geometry)

root.title("Remember Window Position")
root.geometry("400x200")  # Default size if no saved position

# Handle window close
root.protocol("WM_DELETE_WINDOW", on_closing)

tk.Label(root, text="Move me around!").pack(pady=50)

root.mainloop()
