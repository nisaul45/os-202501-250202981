# Data proses: (Nama, Arrival Time, Burst Time)
processes = [
    ("P1", 0, 6),
    ("P2", 1, 8),
    ("P3", 2, 7),
    ("P4", 3, 3),
]

def fcfs(processes):
    processes = sorted(processes, key=lambda x: x[1])
    time = 0
    total_wt = 0
    total_tat = 0

    print("=== FCFS Scheduling ===")
    print("Proses | AT | BT | ST | WT | TAT | FT")
    print("-" * 45)

    for name, at, bt in processes:
        start_time = max(time, at)
        waiting_time = start_time - at
        turnaround_time = waiting_time + bt
        finish_time = start_time + bt

        total_wt += waiting_time
        total_tat += turnaround_time
        time = finish_time

        print(f"{name:^6} | {at:^2} | {bt:^2} | {start_time:^2} | {waiting_time:^2} | {turnaround_time:^3} | {finish_time:^2}")

    n = len(processes)
    print("\nAverage Waiting Time     :", round(total_wt / n, 2))
    print("Average Turnaround Time :", round(total_tat / n, 2))

    print("\nGantt Chart FCFS:")
    print("| " + " | ".join(p[0] for p in processes) + " |")

fcfs(processes)