processes = [
    ("P1", 0, 6),
    ("P2", 1, 8),
    ("P3", 2, 7),
    ("P4", 3, 3),
]

def sjf(processes):
    processes = processes.copy()
    time = 0
    completed = []
    total_wt = 0
    total_tat = 0

    print("=== SJF Scheduling ===")
    print("Proses | AT | BT | ST | WT | TAT | FT")
    print("-" * 45)

    while processes:
        ready_queue = [p for p in processes if p[1] <= time]

        if not ready_queue:
            time += 1
            continue

        # pilih proses dengan burst time terpendek
        name, at, bt = min(ready_queue, key=lambda x: x[2])
        processes.remove((name, at, bt))

        start_time = time
        waiting_time = start_time - at
        turnaround_time = waiting_time + bt
        finish_time = start_time + bt

        total_wt += waiting_time
        total_tat += turnaround_time
        time = finish_time

        completed.append(name)

        print(f"{name:^6} | {at:^2} | {bt:^2} | {start_time:^2} | {waiting_time:^2} | {turnaround_time:^3} | {finish_time:^2}")

    n = len(completed)
    print("\nAverage Waiting Time     :", round(total_wt / n, 2))
    print("Average Turnaround Time :", round(total_tat / n, 2))

    print("\nGantt Chart SJF:")
    print("| " + " | ".join(completed) + " |")

sjf(processes)