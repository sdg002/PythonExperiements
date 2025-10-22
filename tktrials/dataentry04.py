"""
In this example we are using the trace method to lisen to the "Subscribe" checkbox
and enable/disable the email entry field accordingly.
This is an attempt to emulate MVVM (Model-View-ViewModel) pattern.
See method "toggle_email_entry" for implementation details.

What did we learn from this example?
------------------------------------
- There is no easy enable property in tkinter to enable/disable an entry field.
- You will need to use the config method to change the state of the entry field.
- You will need to setup callbacks to listen to changes in the UI state
"""
import tkinter as tk


class ViewModel:
    def __init__(self):
        self.name = tk.StringVar()
        self.age = tk.IntVar(value=13)
        self.email = tk.StringVar()
        self.subscribe_checkbox = tk.BooleanVar(value=True)
        self.full_name_ronly = tk.StringVar()

        self.name.trace_add("write", self.update_full_name)
        self.age.trace_add("write", self.update_full_name)

    def clear_data(self):
        self.name.set("")
        self.age.set(0)
        self.email.set("")
        self.subscribe_checkbox.set(False)
        self.full_name_ronly.set("")

    def update_full_name(self, *args):
        """
        This call is triggered whenever the name or age changes (via trace_add method).
        """
        print("Updating full name")
        self.full_name_ronly.set(f"{self.name.get()} (Age: {self.age.get()})")

class DataEntryForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Entry Form")

        self.view_model = ViewModel()

        # Build the form
        self.create_widgets()

        # Trace subscribe variable to enable/disable email entry
        self.view_model.subscribe_checkbox.trace_add("write", self.toggle_email_entry)

    def create_widgets(self):
        # Name
        tk.Label(self.root, text="Name:").grid(
            row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.view_model.name).grid(
            row=0, column=1, padx=5, pady=5)

        # Age
        tk.Label(self.root, text="Age:").grid(
            row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.view_model.age).grid(
            row=1, column=1, padx=5, pady=5)

        # Email
        tk.Label(self.root, text="Email:").grid(
            row=2, column=0, sticky="e", padx=5, pady=5)
        self.email_entry = tk.Entry(self.root, textvariable=self.view_model.email)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        # Subscribe checkbox
        tk.Checkbutton(self.root, text="Subscribe to newsletter",
                       variable=self.view_model.subscribe_checkbox).grid(row=3, columnspan=2, pady=5)

        # Read-only field for full name
        tk.Label(self.root, text="Full Name (Read-Only):", textvariable=self.view_model.full_name_ronly).grid(
            row=5, column=0, sticky="e", padx=5, pady=5)

    def toggle_email_entry(self, *args):
        if self.view_model.subscribe_checkbox.get():
            self.email_entry.config(state="normal")
        else:
            self.email_entry.config(state="disabled")
    
    # Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DataEntryForm(root)
    root.mainloop()
