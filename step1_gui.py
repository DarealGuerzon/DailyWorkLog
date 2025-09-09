import tkinter as tk
from tkinter import messagebox

def on_save():
    tasks = txt_tasks.get("1.0", tk.END).strip()
    blockers = txt_blockers.get("1.0", tk.END).strip()
    tomorrow = txt_tomorrow.get("1.0", tk.END).strip()

    if not tasks or not blockers or not tomorrow:
        messagebox.showwarning("Input Error", "All fields must be filled out.")
        return
    
    messagebox.showinfo("Success", "Daily work log saved successfully!")
    root.destroy()

root = tk.Tk()
root.title("Daily Work Log")

tk.Label(root, text="Tasks Completed: ").pack(anchor='w',padx=8,pady=(8,0))
txt_tasks = tk.Text(root, height=5, width=50)
txt_tasks.pack(padx=8,pady=(0,8))

tk.Label(root, text="Blockers: ").pack(anchor='w',padx=8,pady=(8,0))
txt_blockers = tk.Text(root, height=5, width=50)
txt_blockers.pack(padx=8,pady=(0,8))

tk.Label(root, text="Plans for Tomorrow: ").pack(anchor='w',padx=8,pady=(8,0))
txt_tomorrow = tk.Text(root, height=5, width=50)    
txt_tomorrow.pack(padx=8,pady=(0,8))

btn_save = tk.Button(root, text="Save Log", command=on_save)
btn_save.pack(pady=8)

root.mainloop()