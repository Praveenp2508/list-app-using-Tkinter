import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("List App")
root.geometry("800x400")

def add_task():
    task_name=task_entry.get()
    Category=category_combobox.get()
    Priority=priority_var.get()
    duration=duration_spinbox.get()
    Completed='yes' if completedvar.get() else 'no'

    if not task_name:
        messagebox.showwarning('input error.please enter the task name')
        return

    taskdetails=(f'{task_name}\t{Category}\t{Priority}\t{duration}mins\t{Completed}')
    listbox.insert(tk.END,taskdetails)

    task_entry.delete(0,tk.END)
    category_combobox.set('')
    priority_var.set('normal')
    duration_spinbox.delete(0, tk.END)
    duration_spinbox.insert(0, "30")
    completedvar.set(False)


def remove_task():
    try:
        selected_task_index=listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning('selection error,please select a task to remove')
            return

        listbox.delete(selected_task_index)
    except Exception as e:
        messagebox.showerror('error',str(e))




tk.Label(root, text="task_name:").grid(row=0, column=0)
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=1)



tk.Label(root, text="Category:").grid(row=1, column=0)
category_var = tk.StringVar(value="Work")
category_combobox = ttk.Combobox(root, textvariable=category_var, values=["Work", "Personal", "Shopping", "Others"])
category_combobox.grid(row=1, column=1)



tk.Label(root, text="Priority:").grid(row=2, column=0)
priority_var = tk.StringVar(value="Normal")
tk.Radiobutton(root, text="Low", variable=priority_var, value="Low").grid(row=2, column=1)
tk.Radiobutton(root, text="Normal", variable=priority_var, value="Normal").grid(row=2, column=2)
tk.Radiobutton(root, text="High", variable=priority_var, value="High").grid(row=2, column=3)



durationlabel=tk.Label(root, text="Duration (mins):")
durationlabel.grid(row=3, column=0)
duration_spinbox = tk.Spinbox(root, from_=5, to=300)
duration_spinbox.grid(row=3, column=1)


completedvar = tk.BooleanVar()
completed_checkbox = tk.Checkbutton(root, text="Completed", variable=completedvar)
completed_checkbox.grid(row=4, column=1)


add_task_button = tk.Button(root, text="Add Task", width=15, bg="green", fg="white",command=add_task)
add_task_button.grid(row=5, column=1)

remove_task_button = tk.Button(root, text="Remove Task",width=15, bg="red", fg="white",command=remove_task)
remove_task_button.grid(row=5, column=2)

listbox=tk.Listbox(root,height=10,width=60)
listbox.grid(row=6,column=0,columnspan=5)
scrollbar=tk.Scrollbar(root,orient=tk.VERTICAL,command=listbox.yview)
scrollbar.grid(row=6,column=3,sticky='ns')
listbox.config(yscrollcommand=scrollbar.set)


root.mainloop()




