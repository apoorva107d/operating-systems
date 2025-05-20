import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def visualize_gantt(processes_result):
    fig, ax = plt.subplots(figsize=(10, 3))
    y = 1
    for p in processes_result:
        ax.broken_barh([(p['completion_time'] - p['turnaround_time'], p['burst_time'])],
                       (y, 0.5), facecolors='tab:blue')
        ax.text(p['completion_time'] - p['turnaround_time'] + p['burst_time']/2, y + 0.25,
                f"P{p['pid']}", ha='center', va='center', color='white')
    
    ax.set_ylim(0, 2)
    ax.set_xlim(0, max(p['completion_time'] for p in processes_result) + 2)
    ax.set_xlabel('Time')
    ax.set_yticks([])
    ax.set_title('CPU Scheduling Gantt Chart')
    plt.show()
