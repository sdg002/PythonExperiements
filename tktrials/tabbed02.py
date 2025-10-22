import tkinter as tk
from tkinter import ttk


class TabOne(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ttk.Label(self, text="This is Tab One")
        label.pack(pady=20)
        button = ttk.Button(self, text="Click Me", command=self.say_hello)
        button.pack()

    def say_hello(self):
        print("Hello from Tab One!")


class TabTwo(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ttk.Label(self, text="This is Tab Two")
        label.pack(pady=20)
        self.my_entry = ttk.Entry(self)
        self.my_entry.pack()
        self.my_entry.bind("<KeyRelease>", self.on_key_release)

    def on_key_release(self, event):
        print(f"Entry changed: {self.my_entry.get()}")


class TabThree(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ttk.Label(self, text="This is Tab Three")
        label.pack(pady=20)
        checkbox = ttk.Checkbutton(self, text="Check me")
        checkbox.pack()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tabbed Interface with Classes")
        self.geometry("400x300")

        self._notebook = ttk.Notebook(self)
        self._notebook.pack(expand=True, fill='both')

        # Add tabs
        self._notebook.add(TabOne(self._notebook), text="Tab 1")
        self._notebook.add(TabTwo(self._notebook), text="Tab 2")
        self._notebook.add(TabThree(self._notebook), text="Tab 3")

        self.tab_loaded = [False, False, False]
        self._notebook.bind("<<NotebookTabChanged>>", self.on_tab_changed)

    def on_tab_changed(self, event):
        #
        # We are using this event to keep track when a tab becomes active
        #
        idx = self._notebook.index(self._notebook.select())
        if not self.tab_loaded[idx]:
            print(f"Tab {idx+1} loaded for the first time")
            self.tab_loaded[idx] = True


if __name__ == "__main__":
    app = App()
    app.mainloop()
