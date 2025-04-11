from tkinter import *
import customtkinter as ctk
ctk.set_appearance_mode("System") # dark, light
root = ctk.CTk()
root.geometry("300x400")
root.title("PITP Custom APPs")

button = ctk.CTkButton(master = root, text="Hello world!")
button.place(relx = 0.5, rely = 0.5, anchor=CENTER)

root.mainloop()