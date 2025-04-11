import tkinter as tk
import sqlite3
def create_database():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            due_date TEXT,
            priority INTEGER,
            completed BOOLEAN
        )
    ''')
    conn.commit()
    conn.close()
    
    def create_gui():
        root = tk.Tk()
        root.title("To-Do List")

        # ... (Add widgets for task input, display, and buttons)

        root.mainloop()
def add_task():
    # ... (Get task details from input fields)
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, description, due_date, priority, completed)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, description, due_date, priority, False))
    conn.commit()
    conn.close()
    # ... (Update the task list display)

def edit_task():
    # ... (Get task ID and new details)
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tasks SET title=?, description=?, due_date=?, priority=?
        WHERE id=?
    ''', (new_title, new_description, new_due_date, new_priority, task_id))
    conn.commit()
    conn.close()
    # ... (Update the task list display)

# ... (Similar functions for deleting, marking as completed, and searching tasks)

def display_tasks():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()

    # ... (Populate a listbox or table widget with tasks)