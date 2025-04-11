


import tkinter as tk
def greet():
    print("Hello, welcome to Tkinter!")
root = tk.Tk()
# Label Widget
label = tk.Label(root, text="Welcome to Tkinter")
label.pack()
# Button Widget
button = tk.Button(root, text="Greet", command=greet)
button.pack()
root.mainloop()
