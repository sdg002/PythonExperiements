"""
Binding the fields of a data entry form to variables
"""
import tkinter as tk
from tkinter import messagebox


class DataEntryForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Entry Form")

        # Variables to bind to entry widgets
        self.name_var = tk.StringVar()
        self.age_var = tk.IntVar()
        self.email_var = tk.StringVar()
        self.subscribe_var = tk.BooleanVar()

        # Build the form
        self.create_widgets()

    def create_widgets(self):
        # Name
        tk.Label(self.root, text="Name:").grid(
            row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.name_var).grid(
            row=0, column=1, padx=5, pady=5)

        # Age
        tk.Label(self.root, text="Age:").grid(
            row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.age_var).grid(
            row=1, column=1, padx=5, pady=5)

        # Email
        tk.Label(self.root, text="Email:").grid(
            row=2, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.email_var).grid(
            row=2, column=1, padx=5, pady=5)

        # Subscribe checkbox
        tk.Checkbutton(self.root, text="Subscribe to newsletter",
                       variable=self.subscribe_var).grid(row=3, columnspan=2, pady=5)

        # Submit button
        tk.Button(self.root, text="Submit", command=self.submit_form).grid(
            row=4, columnspan=2, pady=10)

    def submit_form(self):
        # Collect data
        name = self.name_var.get()
        age = self.age_var.get()
        email = self.email_var.get()
        subscribed = self.subscribe_var.get()

        # Display the data
        message = f"Name: {name}\nAge: {age}\nEmail: {email}\nSubscribed: {'Yes' if subscribed else 'No'}"
        messagebox.showinfo("Form Submitted", message)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DataEntryForm(root)
    root.mainloop()
