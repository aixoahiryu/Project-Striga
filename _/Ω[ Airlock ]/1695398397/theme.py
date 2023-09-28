import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create a ttk.Style instance
style = ttk.Style()

# Get the current theme
current_theme = style.theme_use()

# Print the current theme
print(current_theme)