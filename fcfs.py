import tkinter as tk
from tkinter import messagebox

def fcfs_window():
    window = tk.Toplevel()
    window.title("First Come First Serve Scheduling")
    window.geometry("600x400")

    tk.Label(window, text="Enter Arrival Times (comma-separated):").pack(pady=10)
    arrival_entry = tk.Entry(window, width=40)
    arrival_entry.pack()

    tk.Label(window, text="Enter Burst Times (comma-separated):").pack(pady=10)
    burst_entry = tk.Entry(window, width=40)
    burst_entry.pack()

    result_label = tk.Label(window, text="", font=("Helvetica", 12))
    result_label.pack(pady=20)

    def run_fcfs():
        try:
            arrival_times = list(map(int, arrival_entry.get().split(',')))
            burst_times = list(map(int, burst_entry.get().split(',')))
            
            if len(arrival_times) != len(burst_times):
                raise ValueError("Arrival and Burst times must have same length.")

            waiting_times = [0] * len(burst_times)
            turnaround_times = [0] * len(burst_times)
            start_time = 0

            for i in range(len(burst_times)):
                if start_time < arrival_times[i]:
                    start_time = arrival_times[i]
                waiting_times[i] = start_time - arrival_times[i]
                start_time += burst_times[i]
                turnaround_times[i] = burst_times[i] + waiting_times[i]

            avg_wait = sum(waiting_times) / len(waiting_times)
            avg_turnaround = sum(turnaround_times) / len(turnaround_times)

            result = f"Avg Waiting Time: {avg_wait:.2f}\nAvg Turnaround Time: {avg_turnaround:.2f}"
            result_label.config(text=result)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(window, text="Run FCFS", command=run_fcfs).pack(pady=10)
