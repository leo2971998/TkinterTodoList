import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        # create a listbox to display the tasks
        self.tasks = tk.Listbox(master)
        self.tasks.pack()

        # create a text entry box for adding tasks
        self.task_entry = tk.Entry(master)
        self.task_entry.pack()

        # create a button to add tasks to the list
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        # create a button to delete the selected task
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        self.tasks.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_task = self.tasks.curselection()
        if selected_task:
            self.tasks.delete(selected_task)
        else:
            messagebox.showerror("Error", "No task selected.")

root = tk.Tk()
app = ToDoApp(root)
root.mainloop()
