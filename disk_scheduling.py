import tkinter as tk
from tkinter import messagebox

def disk_window():
    window = tk.Toplevel()
    window.title("Disk Scheduling (FCFS Example)")
    window.geometry("600x400")

    tk.Label(window, text="Enter Disk Request Sequence (comma-separated):").pack(pady=10)
    requests_entry = tk.Entry(window, width=40)
    requests_entry.pack()

    tk.Label(window, text="Enter Initial Head Position:").pack(pady=10)
    head_entry = tk.Entry(window, width=20)
    head_entry.pack()

    result_label = tk.Label(window, text="", font=("Helvetica", 12))
    result_label.pack(pady=20)

    def run_disk():
        try:
            requests = list(map(int, requests_entry.get().split(',')))
            head = int(head_entry.get())
            seek_count = 0
            current_head = head

            for req in requests:
                seek_count += abs(req - current_head)
                current_head = req

            result = f"Total Seek Operations: {seek_count}"
            result_label.config(text=result)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(window, text="Run Disk Scheduling", command=run_disk).pack(pady=10)
