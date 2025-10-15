
# Laporan Praktikum Minggu [1]
Topik: [Arsitektur Sistem Operasi dan Kernel]

---

## Identitas
- **Nama**  : [Nisa'ul hidayah]  
- **NIM**   : [250202981]  
- **Kelas** : [1IKRB]

---

## Tujuan
> Menjelaskan peran sistem operasi dalam arsitektur komputer.
> Mengidentifikasi komponen utama OS (kernel, system call, device driver, file system).
> Membandingkan model arsitektur OS (monolithic, layered, microkernel).
> Menggambarkan diagram sederhana arsitektur OS menggunakan alat bantu digital (draw.io / mermaid).
---

## Dasar Teori
Perbedaan mode eksekusi kernel mode dan user mode.
Mekanisme system call (panggilan sistem).
Perbandingan model arsitektur OS seperti monolithic kernel, layered approach, dan microkernel.

---

## Langkah Praktikum
1. Setup Environment
Pastikan Linux (Ubuntu/WSL) sudah terinstal.
Pastikan Git sudah dikonfigurasi dengan benar:  
2. Diskusi Konsep
Baca materi pengantar tentang komponen OS.
Identifikasi komponen yang ada pada Linux/Windows/Android.
3. Eksperimen Dasar Jalankan perintah berikut di terminal:
4. Membuat Diagram Arsitektur

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
whoami
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/diagramarsitekturos.png)

---

## Analisis
- Hasil percobaan menunjukan bahwa arsitektur sistem operasi bekerja secara berlapis.Setiap tindakan pengguna,seperti membuka browser atau menjalankan game, melewati lapisan aplikasi lalu diterjemahkan menjadi system call yang diproses oleh kerneluntuk mengakses sumber daya perangkat keras seperti disk,cpu,ram dan I/O.
- Application system yang berisi program yang dijalankan  penguna.Kernel merupakan inti os yang mengatur proses,memori,sistem file,perangkat keras,dan operasi I/O.System call interface berfungsi sebagai jembatan antar aplikasi dan kernel,menerjemahkan perintah aplikasi menjadi intruksi sistem.Hardware merupakan lapisan fisik tempat seluruh proses yang dijalankan melalui pengaturan kernel.
- Perbedaannya yaitu linux menggunakan kernel monolitik modular yang fleksibel,sedangkan pada windows menggunakan kernel hybrid.Pada mekanisme keamanan dan penjadwalan proses juga berbeda,sehingga sehingga respon sistem terhadap beban kerja berbeda.  

---

## Kesimpulan
- Diagram arsitektur sistem operasi mununjukan bahwa setiap interaksi pengguna dengan hardware harus melalui lapisan application system,system call,dan kernel.
- Kernel memiliki peran penting dalamm mengelola seluruh sumber daya sistem agar aplikasi dapat berjalan dengan aman dan efisien.

---

## Quiz
1. [Sebutkan tiga fungsi utama sistem operasi.]  
   **Manajemen proses, Manajemen memori, Manajemen I/O**  
2. [Jelaskan perbedaan antara kernel mode dan user mode]  
   **Kernel mode memiliki akses penuh ke seluruh sumber daya komputer dan digunakan oleh sistem operasi sedangkan pada user mode akses yang terbatas dan digunakan oleh program atau aplikasi pengguna**  
3. [Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.]  
   **Monolithic: Linux,Unix,Windows Microkernel:QNX,Symbian,Minix3**

---

## Refleksi Diri
Tuliskan secara singkat:
- Memahami hubungan antar komponen sistem operasi, terutama cara kerja pada kernel,system call,dan lapisan aplikasi dalam mengakses hardware.  
- Mempelajari kembali teori arsitektur sistem operasi.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
