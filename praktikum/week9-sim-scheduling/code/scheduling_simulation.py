import csv

data_proses = []
with open('dataset.csv', 'r') as file:
    baca = csv.DictReader(file)
    for baris in baca:
        data_proses.append({
            'proses': baris['Process'],
            'arrival_time': int(baris['ArrivalTime']),
            'burst_time': int(baris['BurstTime'])
        })

data_proses.sort(key=lambda x: x['arrival_time'])

waktu_sekarang = 0
total_waiting_time = 0
total_turnaround_time = 0

print("SIMULASI PENJADWALAN FCFS")
print("=" * 70)
print("Proses | Arrival Time | Burst Time | Waiting Time | Turnaround Time")
print("-" * 70)

for p in data_proses:
    if waktu_sekarang < p['arrival_time']:
        waktu_sekarang = p['arrival_time']

    waiting_time = waktu_sekarang - p['arrival_time']
    turnaround_time = waiting_time + p['burst_time']

    total_waiting_time += waiting_time
    total_turnaround_time += turnaround_time

    print(f"{p['proses']:>4}   | {p['arrival_time']:>12} | {p['burst_time']:>10} |"
          f" {waiting_time:>12} | {turnaround_time:>15}")

    waktu_sekarang += p['burst_time']

jumlah_proses = len(data_proses)

print("-" * 70)
print(f"Rata-rata Waiting Time    : {total_waiting_time / jumlah_proses:.2f}")
print(f"Rata-rata Turnaround Time : {total_turnaround_time / jumlah_proses:.2f}")