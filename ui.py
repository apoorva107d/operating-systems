
import tkinter as tk
from tkinter import messagebox, ttk

# Color scheme
BG_COLOR = "#ECEFF1"  # Light gray-blue background
HEADER_COLOR = "#37474F"  # Dark slate for header
BTN_COLOR = "#64B5F6"  # Soft blue for buttons
BTN_HOVER = "#42A5F5"  # Brighter blue on hover
TEXT_COLOR = "#263238"  # Dark gray for text
ACCENT_COLOR = "#CFD8DC"  # Light accent for frames

class SchedulerUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OS Scheduler")
        self.geometry("900x700")
        self.configure(bg=BG_COLOR)

        # Header
        header_frame = tk.Frame(self, bg=HEADER_COLOR, height=60)
        header_frame.pack(fill="x")
        header_label = tk.Label(header_frame, text="OS Scheduling Algorithms", font=("Helvetica", 20, "bold"), 
                               fg="white", bg=HEADER_COLOR)
        header_label.pack(pady=15)

        # Main content frame with shadow effect
        main_frame = tk.Frame(self, bg=ACCENT_COLOR, bd=2, relief="raised")
        main_frame.pack(padx=20, pady=(10, 20), fill="both", expand=True)

        self.create_buttons(main_frame)

        # Footer
        footer_frame = tk.Frame(self, bg=HEADER_COLOR, height=40)
        footer_frame.pack(fill="x", side="bottom")
        footer_label = tk.Label(footer_frame, text="© 2025 OS Scheduler Demo", font=("Helvetica", 10), 
                               fg="white", bg=HEADER_COLOR)
        footer_label.pack(pady=10)

    def create_buttons(self, parent):
        button_frame = tk.Frame(parent, bg=ACCENT_COLOR)
        button_frame.pack(pady=30)

        algorithms = {
            "First Come First Serve": self.open_fcfs,
            "Round Robin": self.open_rr,
            "Shortest Job First": self.open_sjf,
            "FIFO (Memory Management)": self.open_fifo,
            "CPU Scheduling Visualization": self.open_gantt,
            "Memory Management Visualization": self.open_memory_viz,
            "Disk Scheduling": self.open_disk_scheduling
        }

        for i, (algo, command) in enumerate(algorithms.items()):
            btn = tk.Button(button_frame, text=algo, font=("Helvetica", 14, "bold"), fg=TEXT_COLOR,
                            bg=BTN_COLOR, width=35, height=2, relief="flat", bd=0,
                            command=command, cursor="hand2")
            btn.grid(row=i, column=0, pady=15, padx=30)
            btn.config(activebackground=BTN_HOVER, activeforeground=TEXT_COLOR)
            btn.bind("<Enter>", lambda event, b=btn: b.config(bg=BTN_HOVER))
            btn.bind("<Leave>", lambda event, b=btn: b.config(bg=BTN_COLOR))

    def open_fcfs(self):
        PlaceholderWindow(self, "First Come First Serve (FCFS)")

    def open_rr(self):
        PlaceholderWindow(self, "Round Robin (RR)")

    def open_sjf(self):
        SJFWindow(self)

    def open_fifo(self):
        PlaceholderWindow(self, "FIFO (Memory Management)")

    def open_gantt(self):
        PlaceholderWindow(self, "CPU Scheduling Visualization")

    def open_memory_viz(self):
        PlaceholderWindow(self, "Memory Management Visualization")

    def open_disk_scheduling(self):
        PlaceholderWindow(self, "Disk Scheduling")

class SJFWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Shortest Job First (SJF) Scheduling")
        self.geometry("600x550")
        self.configure(bg=BG_COLOR)

        # Header
        header_frame = tk.Frame(self, bg=HEADER_COLOR, height=50)
        header_frame.pack(fill="x")
        tk.Label(header_frame, text="Shortest Job First (SJF)", font=("Helvetica", 16, "bold"), 
                 fg="white", bg=HEADER_COLOR).pack(pady=10)

        # Main content frame
        content_frame = tk.Frame(self, bg=ACCENT_COLOR, bd=2, relief="raised")
        content_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Input section
        self.process_inputs(content_frame)

        # Output Frame
        self.result_frame = tk.Frame(content_frame, bg=ACCENT_COLOR)
        self.result_frame.pack(pady=20, fill="both", expand=True)

    def process_inputs(self, parent):
        """Creates input fields for burst times."""
        frame = tk.Frame(parent, bg=ACCENT_COLOR)
        frame.pack(pady=20)

        tk.Label(frame, text="Enter Burst Times (comma-separated):", font=("Helvetica", 12), 
                 bg=ACCENT_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, padx=10, pady=10)
        self.burst_entry = tk.Entry(frame, width=35, font=("Helvetica", 12))
        self.burst_entry.grid(row=0, column=1, padx=10, pady=10)

        btn = tk.Button(frame, text="Calculate SJF", font=("Helvetica", 12, "bold"), 
                        command=self.calculate_sjf, bg=BTN_COLOR, fg=TEXT_COLOR, 
                        relief="flat", width=20, height=2, cursor="hand2")
        btn.grid(row=1, columnspan=2, pady=20)
        btn.config(activebackground=BTN_HOVER, activeforeground=TEXT_COLOR)
        btn.bind("<Enter>", lambda event: btn.config(bg=BTN_HOVER))
        btn.bind("<Leave>", lambda event: btn.config(bg=BTN_COLOR))

    def calculate_sjf(self):
        """Processes SJF scheduling and displays results."""
        try:
            burst_times = list(map(int, self.burst_entry.get().split(",")))
            if not burst_times:
                raise ValueError("Please enter valid burst times.")

            # Sorting burst times (Non-Preemptive SJF)
            burst_times.sort()

            waiting_time = [0] * len(burst_times)
            turnaround_time = [0] * len(burst_times)

            # Calculate Waiting Time
            for i in range(1, len(burst_times)):
                waiting_time[i] = waiting_time[i - 1] + burst_times[i - 1]

            # Calculate Turnaround Time
            for i in range(len(burst_times)):
                turnaround_time[i] = waiting_time[i] + burst_times[i]

            avg_waiting_time = sum(waiting_time) / len(burst_times)
            avg_turnaround_time = sum(turnaround_time) / len(burst_times)

            self.display_results(waiting_time, turnaround_time, avg_waiting_time, avg_turnaround_time)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def display_results(self, waiting_time, turnaround_time, avg_waiting_time, avg_turnaround_time):
        """Displays SJF results in a grid layout."""
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        # Header row
        tk.Label(self.result_frame, text="Process", font=("Helvetica", 12, "bold"), 
                 bg=ACCENT_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.result_frame, text="Waiting Time", font=("Helvetica", 12, "bold"), 
                 bg=ACCENT_COLOR, fg=TEXT_COLOR).grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self.result_frame, text="Turnaround Time", font=("Helvetica", 12, "bold"), 
                 bg=ACCENT_COLOR, fg=TEXT_COLOR).grid(row=0, column=2, padx=5, pady=5)

        # Process rows
        for i in range(len(waiting_time)):
            tk.Label(self.result_frame, text=f"P{i+1}", font=("Helvetica", 12), 
                     bg=ACCENT_COLOR, fg=TEXT_COLOR).grid(row=i+1, column=0, padx=5, pady=5)
            tk.Label(self.result_frame, text=f"{waiting_time[i]}", font=("Helvetica", 12), 
                     bg=ACCENT_COLOR, fg=TEXT_COLOR).grid(row=i+1, column=1, padx=5, pady=5)
            tk.Label(self.result_frame, text=f"{turnaround_time[i]}", font=("Helvetica", 12), 
                     bg=ACCENT_COLOR, fg=TEXT_COLOR).grid(row=i+1, column=2, padx=5, pady=5)

        # Averages
        tk.Label(self.result_frame, text=f"Avg Waiting Time: {avg_waiting_time:.2f}", 
                 font=("Helvetica", 12, "bold"), bg=ACCENT_COLOR, fg=TEXT_COLOR).grid(
                 row=len(waiting_time)+1, column=0, columnspan=3, pady=10)
        tk.Label(self.result_frame, text=f"Avg Turnaround Time: {avg_turnaround_time:.2f}", 
                 font=("Helvetica", 12, "bold"), bg=ACCENT_COLOR, fg=TEXT_COLOR).grid(
                 row=len(waiting_time)+2, column=0, columnspan=3, pady=5)

class PlaceholderWindow(tk.Toplevel):
    def __init__(self, parent, title):
        super().__init__(parent)
        self.title(title)
        self.geometry("600x500")
        self.configure(bg=BG_COLOR)

        # Header
        header_frame = tk.Frame(self, bg=HEADER_COLOR, height=50)
        header_frame.pack(fill="x")
        tk.Label(header_frame, text=title, font=("Helvetica", 16, "bold"), 
                 fg="white", bg=HEADER_COLOR).pack(pady=10)

        # Content frame
        content_frame = tk.Frame(self, bg=ACCENT_COLOR, bd=2, relief="raised")
        content_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Placeholder label
        tk.Label(content_frame, text=f"Placeholder for {title}\n(To be implemented)", 
                 font=("Helvetica", 14), bg=ACCENT_COLOR, fg=TEXT_COLOR).pack(pady=50)

if __name__ == "__main__":
    app = SchedulerUI()
    app.mainloop()
