import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext
import os

class TextFileEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text File Reader and Writer")
        self.root.geometry("600x400")

        self.file_path = None

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Text area for displaying file content
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=60, height=20)
        self.text_area.grid(column=0, row=0, padx=10, pady=10)

        # Button to open a file
        self.open_button = tk.Button(self.root, text="Open File", command=self.open_file)
        self.open_button.grid(column=0, row=1, sticky=tk.W, padx=10, pady=5)

        # Button to save changes to a file
        self.save_button = tk.Button(self.root, text="Save File", command=self.save_file)
        self.save_button.grid(column=0, row=1, padx=100, pady=5)

        # Button to check the file pointer position
        self.tell_button = tk.Button(self.root, text="Check File Pointer", command=self.check_file_pointer)
        self.tell_button.grid(column=0, row=1, padx=200, pady=5)

        # Label to show file pointer position
        self.pointer_label = tk.Label(self.root, text="File Pointer Position: -")
        self.pointer_label.grid(column=0, row=2, padx=10, pady=5)

    def open_file(self):
        # Open a file dialog to select a text file
        self.file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if self.file_path:
            try:
                with open(self.file_path, "r") as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)  # Clear existing content
                    self.text_area.insert(tk.INSERT, content)  # Insert new content
                self.pointer_label.config(text="File Pointer Position: 0")
            except Exception as e:
                messagebox.showerror("Error", f"Error opening file: {e}")

    def save_file(self):
        # Save the current text area content to the file
        if self.file_path:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(self.file_path, "w") as file:
                    file.write(content)
                messagebox.showinfo("Success", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving file: {e}")
        else:
            messagebox.showwarning("Warning", "No file is open.")

    def check_file_pointer(self):
        # Show the current file pointer position
        if self.file_path:
            try:
                with open(self.file_path, "r") as file:
                    # Move the file pointer to the end and use tell() to get its position
                    file.seek(0, os.SEEK_END)
                    position = file.tell()
                    self.pointer_label.config(text=f"File Pointer Position: {position}")
            except Exception as e:
                messagebox.showerror("Error", f"Error checking file pointer: {e}")
        else:
            messagebox.showwarning("Warning", "No file is open.")

# Create the Tkinter window and run the application
root = tk.Tk()
app = TextFileEditor(root)
root.mainloop()
