import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
label1 = tk.Label(frame, text="Hello")
label2 = tk.Label(frame, text="World!")
button = tk.Button(frame, text="Click me", command=lambda: print("Button clicked"))

# Set up tag for label1
label1.tag_config("my_tag", background="#ff0000")

# Use tag to change background color of label1
label1["background"] = "#ffff00"

# Add button with tag
button.pack()

root.mainloop()