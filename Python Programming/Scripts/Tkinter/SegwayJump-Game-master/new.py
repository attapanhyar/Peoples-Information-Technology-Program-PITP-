import tkinter as tk

root = tk.Tk("300x400")
root.title('PITP Python')

tk.Label(root, text="Enter Amount: ").grid(row=0)
tk.Entry(root).grid(row=0, column=1)
tk.Button(root, text="Deposit").grid(row=1, column=0)
tk.Button(root, text="Withdraw").grid(row=1, column=1)


root.mainloop()


