
# Laporan Praktikum Minggu [14]
Topik: [ Penyusunan Laporan Praktikum Format IMRAD]

---

## Identitas
- **Nama**  : [Nisa'ul Hidayah]  
- **NIM**   : [250202981]  
- **Kelas** : [1IKRB]

---

## Pendahuluan
## Latar Belakang
Penjadwalan CPU merupakan salah satu fungsi utama sistem operasi yang bertujuan untuk mengatur urutan eksekusi proses agar penggunaan prosesor menjadi efisien dan adil. Setiap proses memiliki waktu kedatangan (arrival time) dan waktu eksekusi (burst time) yang harus dikelola oleh sistem operasi agar tidak etrjadi penumpukan proses. Dua algoritma penjadwalan yang paling dasar adalah First Come First Served (FCFS) dan Shortest Job First (SJF). FCFS mengeksekusi proses berdasarkan urutan kedatangan, sedangkan SJF memprioritaskan proses dengan waktu eksekusi paling pendek.
## Tujuan
Praktikum ini bertujuan untuk:
- Mengimplementasikan dan menganalisis algoritma penjadwalan FCFS dan SJF
- Menghitung dan membandingkan nilai Average Waiting Time dan Average Turnaround Time pada kedua algoritma
- Mengidentifikasi kondisi optimal penggunaan masing-masing algoritma


---

## Metode
## A. Data Proses
Tabel proses yang digunakan:

| Proses | Burst Time | Arrival Time |
|:--:|:--:|:--:|
| P1 | 6 | 0 |
| P2 | 8 | 1 |
| P3 | 7 | 2 |
| P4 | 3 | 3 |

## Langkah Eksperimen
#### Eksperimen 1 – FCFS
1. Mengurutkan proses berdasarkan *arrival time*.  
2. Menghitung:
   - Waiting Time (WT) = Start Time – Arrival Time  
   - Turnaround Time (TAT) = WT + Burst Time  
3. Membuat Gantt Chart.

#### Eksperimen 2 – SJF
1. Mengurutkan proses berdasarkan *burst time* terpendek.  
2. Menghitung WT dan TAT seperti pada FCFS.  
3. Membandingkan hasil dengan FCFS.

---

## Hasil Eksekusi
### A. Hasil FCFS
![Screenshot hasil](screenshots/fcfs.png)
```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
```
### B. Hasil SJF
![Screenshot hasil](screenshots/sjf.png)
```
     | P1 | P2 | P3 | P4 |
     0    6    9   16   24
```
### C. Perbandingan FCFS dan SJF
| Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
|------------|------------------|----------------------|------------|-------------|
| FCFS | 8,75 | 14,75 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
| SJF | 6,25 | 12,25 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

---

## Pembahasan
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?]  
   **Jawaban:**  
   Karena IMRAD menyusun laporan dengan sistematis yang terdiri dari pendahuluan yang memberikan konteks dan tujuan, metode memungkinkan replikasi ilmiah, hasill memyajikan data yang objektif, dan pembahasan menginterpertasikan temuan. Struktur ini memudahkan pembaca memahami alur penelitian. 
2. [Apa perbedaan antara bagian **Hasil** dan **Pembahasan**?]  
   **Jawaban:**  
   Hasil hanya menyajikan data dan temuan, sedangkan pembahasan menginterpretasikan dan analisis dari hasil tersebut.
3. [Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?]  
   **Jawaban:** 
   Karena sitasi menunjukan bahwa anilisis didukung teori ilmiah dan mencegah plagiarisme. 

---

## Daftar Pustaka


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
