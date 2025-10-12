"""
Binding the fields of a data entry form to variables encapsulated in a class
This is an attempt to emulate MVVM (Model-View-ViewModel) pattern
"""
import tkinter as tk
from tkinter import messagebox


class ViewModel:
    def __init__(self):
        self.name = tk.StringVar()
        self.age = tk.IntVar(value=13)
        self.email = tk.StringVar()
        self.subscribe = tk.BooleanVar(value=True)

    def clear_data(self):
        self.name.set("")
        self.age.set(0)
        self.email.set("")
        self.subscribe.set(False)


class DataEntryForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Entry Form")

        self.view_model = ViewModel()

        # Build the form
        self.create_widgets()

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
        tk.Entry(self.root, textvariable=self.view_model.email).grid(
            row=2, column=1, padx=5, pady=5)

        # Subscribe checkbox
        tk.Checkbutton(self.root, text="Subscribe to newsletter",
                       variable=self.view_model.subscribe).grid(row=3, columnspan=2, pady=5)

        # Submit button
        tk.Button(self.root, text="Submit", command=self.submit_form).grid(
            row=4, columnspan=2, pady=10)

    def submit_form(self):
        # Collect data
        name = self.view_model.name.get()
        age = self.view_model.age.get()
        email = self.view_model.email.get()
        subscribed = self.view_model.subscribe.get()

        # Display the data
        message = f"Name: {name}\nAge: {age}\nEmail: {email}\nSubscribed: {'Yes' if subscribed else 'No'}"
        messagebox.showinfo("Form Submitted", message)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DataEntryForm(root)
    root.mainloop()
