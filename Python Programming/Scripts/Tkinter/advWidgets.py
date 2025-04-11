import tkinter as tk
root = tk.Tk()
listbox = tk.Listbox(root)
listbox.pack()

for item in ["Apple", "Banana", "Cherry",1,2,2,3,4,5,6,7,7,7,8,9,7,65,55]:
    listbox.insert(tk.END, item)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
root.mainloop()
