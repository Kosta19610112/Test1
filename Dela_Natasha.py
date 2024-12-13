import tkinter as tk


def add_task():
    ftask = open('task.txt', 'a') #
    task = task_entry.get()       #
    ftask.write(task+'\n')        #
    ftask.close()                 #

    if task:
        tasks_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)


def delete_task():
    selected_task_index = tasks_listBox.curselection()
    if selected_task_index:
        tasks_listBox.delete(selected_task_index)

def mark_task_done():
    selected_task_index = tasks_listBox.curselection()
    if selected_task_index:
        current_task = tasks_listBox.get(selected_task_index)
        tasks_listBox.delete(selected_task_index)
        tasks_listBox.insert(tk.END, f"{current_task} (done)")

root = tk.Tk()
root.title("My Tasks")
root.configure(background="khaki3")

text1 = tk.Label(root, text="Enter your deals:", bg="khaki3")
text1.pack(pady=10)

task_entry = tk.Entry(root, width=40, bg="goldenrod4", fg="black")
task_entry.pack(pady=15)


add_tasks_button = tk.Button(root, text="Add new deals", command=add_task)
add_tasks_button.pack(pady=15)


delete_button = tk.Button(root, text="Remove deals", command=delete_task)
delete_button.pack(pady=15)


mark_button = tk.Button(root, text="Mark if it was done", command=mark_task_done)
mark_button.pack(pady=15)


text2 = tk.Label(root, text="My deals:", bg="khaki3")
text2.pack(pady=10)


tasks_listBox = tk.Listbox(root, height=15, width=50, bg="linen")
f= open('task.txt')
ts = f.readlines()
for t in ts:
    tasks_listBox.insert(tk.END, t)
f.close()
tasks_listBox.pack(pady=10)


root.mainloop()


