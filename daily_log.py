import tkinter as tk
from tkinter import messagebox, scrolledtext
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

        # Clear inputs
        tasks_entry.delete("1.0", tk.END)
        blockers_entry.delete("1.0", tk.END)
        tomorrow_entry.delete("1.0", tk.END)
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save log: {e}")

def submit():
    tasks = tasks_entry.get("1.0", tk.END).strip()
    blockers = blockers_entry.get("1.0", tk.END).strip()
    tomorrow = tomorrow_entry.get("1.0", tk.END).strip()

    if not tasks or not blockers or not tomorrow:
        messagebox.showwarning("Input Error", "All fields must be filled out.")
        return
    
    save_to_sheets(tasks, blockers, tomorrow)

root = tk.Tk()
root.title("Daily Work Log")
root.geometry("600x500")
root.configure(bg="#f8f9fa")

title_label = tk.Label(root, text="Daily Work Log", font=("Segoe UI", 18, "bold"), bg="#f8f9fa", fg="#333")
title_label.pack(pady=12)

# Tasks
tk.Label(root, text="✅ Tasks Completed:", font=("Segoe UI", 12), bg="#f8f9fa").pack(anchor="w", padx=12)
tasks_entry = scrolledtext.ScrolledText(root, height=6, width=70, font=("Segoe UI", 10))
tasks_entry.pack(padx=12, pady=6)

# Blockers
tk.Label(root, text="🚧 Blockers:", font=("Segoe UI", 12), bg="#f8f9fa").pack(anchor="w", padx=12)
blockers_entry = scrolledtext.ScrolledText(root, height=4, width=70, font=("Segoe UI", 10))
blockers_entry.pack(padx=12, pady=6)

# Tomorrow's Plan
tk.Label(root, text="📌 Tomorrow's Plan / Notes:", font=("Segoe UI", 12), bg="#f8f9fa").pack(anchor="w", padx=12)
tomorrow_entry = scrolledtext.ScrolledText(root, height=4, width=70, font=("Segoe UI", 10))
tomorrow_entry.pack(padx=12, pady=6)

# Submit button
submit_btn = tk.Button(root, text="💾 Save Log", font=("Segoe UI", 12, "bold"),
                       bg="#0078d7", fg="white", padx=20, pady=6, command=submit)
submit_btn.pack(pady=20)

root.mainloop()
