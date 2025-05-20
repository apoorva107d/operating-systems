import tkinter as tk
from tkinter import messagebox

def rr_window():
    window = tk.Toplevel()
    window.title("Round Robin Scheduling")
    window.geometry("600x400")

    tk.Label(window, text="Enter Burst Times (comma-separated):").pack(pady=10)
    burst_entry = tk.Entry(window, width=40)
    burst_entry.pack()

    tk.Label(window, text="Enter Time Quantum:").pack(pady=10)
    quantum_entry = tk.Entry(window, width=20)
    quantum_entry.pack()

    result_label = tk.Label(window, text="", font=("Helvetica", 12))
    result_label.pack(pady=20)

    def run_rr():
        try:
            burst_times = list(map(int, burst_entry.get().split(',')))
            quantum = int(quantum_entry.get())
            n = len(burst_times)
            remaining_bt = burst_times[:]
            waiting_times = [0] * n
            time = 0

            while True:
                done = True
                for i in range(n):
                    if remaining_bt[i] > 0:
                        done = False
                        if remaining_bt[i] > quantum:
                            time += quantum
                            remaining_bt[i] -= quantum
                        else:
                            time += remaining_bt[i]
                            waiting_times[i] = time - burst_times[i]
                            remaining_bt[i] = 0
                if done:
                    break

            turnaround_times = [bt + wt for bt, wt in zip(burst_times, waiting_times)]

            avg_wait = sum(waiting_times) / n
            avg_turnaround = sum(turnaround_times) / n

            result = f"Avg Waiting Time: {avg_wait:.2f}\nAvg Turnaround Time: {avg_turnaround:.2f}"
            result_label.config(text=result)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(window, text="Run Round Robin", command=run_rr).pack(pady=10)
