import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import gspread
from datetime import datetime

CREDENTIALS_PATH = Path(__file__).parent / "credentials.json"
SHEET_NAME = "Work Log"

def save_to_sheets(tasks, blockers, tomorrow):
    try:
        gc = gspread.service_account(filename=str(CREDENTIALS_PATH))
        sh = gc.open(SHEET_NAME).sheet1

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sh.append_row([timestamp, tasks, blockers, tomorrow])

        messagebox.showinfo("Success", "Daily work log saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save log: {e}")

def submit():
    tasks = tasks_entry.get("1.0", tk.END).strip()
    blockers = blockers_entry.get("1.0", tk.END).strip()
    tomorrow = notes_entry.get("1.0", tk.END).strip()

    if not tasks or not blockers or not tomorrow:
        messagebox.showwarning("Input Error", "All fields must be filled out.")
        return
    
    save_to_sheets(tasks, blockers, tomorrow)

root = tk.Tk()
root.title("Daily Work Log")

tk.Label(root, text="Tasks Completed:").pack(anchor="w", padx=8, pady=(8,0))
tasks_entry = tk.Text(root, height=5, width=60)
tasks_entry.pack(padx=8, pady=4)

tk.Label(root, text="Blockers:").pack(anchor="w", padx=8, pady=(8,0))
blockers_entry = tk.Text(root, height=3, width=60)
blockers_entry.pack(padx=8, pady=4)

tk.Label(root, text="Tomorrow's Plan / Notes:").pack(anchor="w", padx=8, pady=(8,0))
notes_entry = tk.Text(root, height=3, width=60)
notes_entry.pack(padx=8, pady=4)

tk.Button(root, text="Submit", command=submit).pack(pady=12)

root.mainloop()
