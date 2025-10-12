"""
In this exampel we are using a ComboBox with data binding to a StringVar.

You can get the index of the selected item using the `current()` method of the ComboBox.
"""
import tkinter as tk
from tkinter import ttk

class ComboBoxDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ComboBox Data Binding Demo")
        self.geometry("300x150")

        # StringVar for data binding
        self.selected_option = tk.StringVar()

        # Label
        ttk.Label(self, text="Choose a fruit:").grid(row=0, column=0, padx=10, pady=10, sticky="e")

        # ComboBox with data binding
        self.combobox = ttk.Combobox(
            self,
            textvariable=self.selected_option,  # Data binding
            values=["Apple", "Banana", "Cherry", "Date", "Elderberry"]
        )
        self.combobox.grid(row=0, column=1, padx=10, pady=10)
        self.combobox.state(["readonly"])  # Make it readonly

        # Label to display the selected value
        self.display_label = ttk.Label(self, text="")
        self.display_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Trace the StringVar for changes (data binding demonstration)
        self.selected_option.trace_add("write", self.on_selection_change)

    def on_selection_change(self, *args):
        selected = self.selected_option.get()
        selected_index = self.combobox.current()
        self.display_label.config(text=f"You selected: {selected} , index: {selected_index}")

if __name__ == "__main__":
    app = ComboBoxDemo()
    app.mainloop()