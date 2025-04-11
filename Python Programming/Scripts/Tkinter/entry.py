import tkinter as tk
root = tk.Tk()

def Action():
    print('Button Clicked!')
tk.Label(root, text="Username").grid(row=0)
tk.Label(root, text="Password").grid(row=1)
tk.Button(root, text = "Submit", command=Action).grid(row=3)
# Entry Widgets
username = tk.Entry(root)
password = tk.Entry(root, show="*")
# Bind User name to Grid
username.grid(row=0, column=1)
password.grid(row=1, column=1)

root.mainloop()
