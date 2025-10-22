import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Tabbed Interface Example")
root.geometry("400x300")

# Create a Notebook (tab container)
notebook = ttk.Notebook(root)

# Create frames for each tab
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# Add tabs to the notebook
notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.add(tab3, text='Tab 3')

# Pack the notebook to make it visible
notebook.pack(expand=True, fill='both')

# Add content to Tab 1
label1 = ttk.Label(tab1, text="Welcome to Tab 1!")
label1.pack(pady=20)

# Add content to Tab 2
label2 = ttk.Label(tab2, text="This is Tab 2.")
label2.pack(pady=20)

# Add content to Tab 3
label3 = ttk.Label(tab3, text="You're now in Tab 3.")
label3.pack(pady=20)

# Run the application
root.mainloop()
