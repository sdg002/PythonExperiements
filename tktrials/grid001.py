import tkinter as tk
from tkinter import ttk


class GridDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Grid System Demo")
        self.geometry("300x150")

        # Create labels and entries using grid
        ttk.Label(self, text="Name:").grid(
            row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = ttk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self, text="Email:", foreground="blue", background="yellow").grid(
            row=1, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = ttk.Entry(self)
        self.email_entry.grid(row=1, column=1, padx=10, pady=5)

        submit_btn = ttk.Button(self, text="Submit", command=self.on_submit)
        submit_btn.grid(row=2, column=0, columnspan=2, pady=10)

    def on_submit(self):
        print(f"Name: {self.name_entry.get()}, Email: {self.email_entry.get()}")


if __name__ == "__main__":
    app = GridDemo()
    app.mainloop()
