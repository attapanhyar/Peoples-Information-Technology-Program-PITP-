import tkinter as tk
import todolist as tl

def create_gui():
    window = tk.Tk()
    window.title("To-Do List")

    # Create frames for different sections
    task_frame = tk.Frame(window)
    task_frame.pack(pady=10)

    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    # Task input fields
    task_label = tk.Label(task_frame, text="Task:")
    task_label.pack(side=tk.LEFT)
    task_entry = tk.Entry(task_frame)
    task_entry.pack(side=tk.LEFT)

    # Buttons
    add_button = tk.Button(button_frame, text="Add Task")
    add_button.pack(side=tk.LEFT, padx=10)
    edit_button = tk.Button(button_frame, text="Edit Task")
    edit_button.pack(side=tk.LEFT, padx=10)
    delete_button = tk.Button(button_frame, text="Delete Task")
    delete_button.pack(side=tk.LEFT, padx=10)

    # Task list
    task_list = tk.Listbox(window)
    task_list.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()