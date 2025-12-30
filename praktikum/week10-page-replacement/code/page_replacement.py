def print_header(title):
    print("\n" + "=" * 60)
    print(f"{title:^60}")
    print("=" * 60)
    print(f"| {'Page':^6} | {'Status':^8} | {'Isi Frame (Memori)':^33} |")
    print("-" * 60)

def fifo(pages, frame_size):
    frame = []
    page_fault = 0

    print_header("SIMULASI FIFO (First-In First-Out)")

    for page in pages:
        if page in frame:
            status = "HIT"
        else:
            status = "MISS"
            page_fault += 1
            if len(frame) < frame_size:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)

        tampilan = frame + ["-"] * (frame_size - len(frame))
        print(f"| {page:^6} | {status:^8} | {str(tampilan):^33} |")

    print("-" * 60)
    print(f"Total Page Fault FIFO : {page_fault}")
    return page_fault

def lru(pages, frame_size):
    frame = []
    page_fault = 0

    print_header("SIMULASI LRU (Least Recently Used)")

    for page in pages:
        if page in frame:
            status = "HIT"
            frame.remove(page)
            frame.append(page)
        else:
            status = "MISS"
            page_fault += 1
            if len(frame) < frame_size:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)

        tampilan = frame + ["-"] * (frame_size - len(frame))
        print(f"| {page:^6} | {status:^8} | {str(tampilan):^33} |")

    print("-" * 60)
    print(f"Total Page Fault LRU  : {page_fault}")
    return page_fault

# ===================== MAIN PROGRAM =====================
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3

print("Dataset Loaded :", pages)
print("Jumlah Frame   :", frame_size)

fifo_fault = fifo(pages, frame_size)
lru_fault = lru(pages, frame_size)

print("\n=== PERBANDINGAN ===")
print(f"FIFO Page Faults : {fifo_fault}")
print(f"LRU  Page Faults : {lru_fault}")

if lru_fault < fifo_fault:
    print(">> Algoritma LRU lebih efisien pada dataset ini.")
elif fifo_fault < lru_fault:
    print(">> Algoritma FIFO lebih efisien pada dataset ini.")
else:
    print(">> Kedua algoritma memiliki performa yang sama.")