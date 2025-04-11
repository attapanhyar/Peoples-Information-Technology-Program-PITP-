import tkinter as tk


root = tk.Tk()
file = open('example.txt','w')
tk.Label(root, text="Enter Text").grid(row=0)

entry1  = tk.Entry()
entry1.grid(row=0, column = 3)
def savetofile():
    text = entry1.get()
    file.write(text)
    
tk.Button(root, text="SAVE", command = savetofile).grid(row=2, column=1)

