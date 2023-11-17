import tkinter as tk
from tkinter import messagebox

def function_one():
    messagebox.showinfo("Function One", "You clicked Function One!")

def function_two():
    messagebox.showinfo("Function Two", "You clicked Function Two!")

# Create the main application window
app = tk.Tk()
app.title("Command Line UI")

# Create buttons to access functions
button1 = tk.Button(app, text="Function One", command=function_one)
button2 = tk.Button(app, text="Function Two", command=function_two)

# Arrange the buttons in the window
button1.pack(pady=10)
button2.pack(pady=10)

# Run the application
app.mainloop()
