import csv

process = []
allocation = {}
request = {}

# Membaca dataset
with open("dataset_deadlock.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        p = row["Process"]
        process.append(p)
        allocation[p] = row["Allocation"]
        request[p] = row["Request"]

deadlock_process = []

# Deteksi daedlock
for p1 in process:
    p2 = None
    p3 = None

    for x in process:
        if allocation[x] == request[p1]:
            p2 = x

    if p2:
        for y in process:
            if allocation[y] == request[p2] and request[y] == allocation[p1]:
                p3 = y

    if p2 and p3:
        deadlock_process.extend([p1, p2, p3])

deadlock_process = list(set(deadlock_process))

# Output hasil
print("=== HASIL DETEKSI DEADLOCK ===")
if deadlock_process:
    for p in process:
        if p in deadlock_process:
            print("-", p)
else:
    print("Tidak terjadi deadlock")