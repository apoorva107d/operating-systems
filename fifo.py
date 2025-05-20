import tkinter as tk
from tkinter import messagebox

def fifo_window():
    window = tk.Toplevel()
    window.title("FIFO Page Replacement")
    window.geometry("600x400")

    tk.Label(window, text="Enter Page Reference String (comma-separated):").pack(pady=10)
    pages_entry = tk.Entry(window, width=40)
    pages_entry.pack()

    tk.Label(window, text="Enter Number of Frames:").pack(pady=10)
    frames_entry = tk.Entry(window, width=20)
    frames_entry.pack()

    result_label = tk.Label(window, text="", font=("Helvetica", 12))
    result_label.pack(pady=20)

    def run_fifo():
        try:
            pages = list(map(int, pages_entry.get().split(',')))
            frame_count = int(frames_entry.get())
            frames = []
            page_faults = 0

            for page in pages:
                if page not in frames:
                    if len(frames) < frame_count:
                        frames.append(page)
                    else:
                        frames.pop(0)
                        frames.append(page)
                    page_faults += 1

            result = f"Total Page Faults: {page_faults}"
            result_label.config(text=result)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(window, text="Run FIFO", command=run_fifo).pack(pady=10)
