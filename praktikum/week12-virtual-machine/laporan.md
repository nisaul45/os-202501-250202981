
# Laporan Praktikum Minggu [12]
Topik: [Virtualisasi Menggunakan Virtual Machine]

---

## Identitas 
- **Nama**  : [Nisa'ul Hidayah]  [Latifah Risti Anggraeni]
- **NIM**   : [250202981]  [250202945]
- **Kelas** : [1IKRB]

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).  
2. Membuat dan menjalankan sistem operasi guest di dalam VM.  
3. Mengatur konfigurasi resource VM (CPU, RAM, storage).  
4. Menjelaskan mekanisme proteksi OS melalui virtualisasi.  
5. Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.

---

## Dasar Teori
**Pengertian Virtual Machine**
Virtual Machine adalah mesin virtual berbasis perangkat lunak yang dapat menjalankan sistem operasi layaknya komputer fisik dengan memanfaatkan sumber daya dari host. 

**Konsep Virtualisasi**
Virtualisasi memungkinkan satu perangkat keras fisik menjalankan beberapa sistem operasi secara bersamaan melalui proses abstraksi sumber daya seperti CPU, memori, dan storage. 

**Host OS dan Guest OS**
Host OS adalah sistem operasi utama pada komputer fisik, sedangkan Guest OS adalah sistem operasi yang berjalan di dalam VM. 

**Isolasi dan Keamanan Sistem**
Virtual Machine (VM) menyediakan isolasi antar sistem sehingga gangguan, kesalahan, atau serangan pada satu VM tidak memengaruhi sistem lain maupun host, mendukung konsep sandboxing dan keamanan OS.

---

## Langkah Praktikum
1. **Instalasi Virtual Machine**
   - Instal VirtualBox atau VMware pada komputer host.  
   - Pastikan fitur virtualisasi (VT-x / AMD-V) aktif di BIOS.

2. **Pembuatan OS Guest**
   - Buat VM baru dan pilih OS guest (misal: Ubuntu Linux).  
   - Atur resource awal:
     - CPU: 1–2 core  
     - RAM: 2–4 GB  
     - Storage: ≥ 20 GB

3. **Instalasi Sistem Operasi**
   - Jalankan proses instalasi OS guest sampai selesai.  
   - Pastikan OS guest dapat login dan berjalan normal.

4. **Konfigurasi Resource**
   - Ubah konfigurasi CPU dan RAM.  
   - Amati perbedaan performa sebelum dan sesudah perubahan resource.

5. **Analisis Proteksi OS**
   - Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.  
   - Kaitkan dengan konsep *sandboxing* dan *hardening* OS.

6. **Dokumentasi**
   - Ambil screenshot setiap tahap penting.  
   - Simpan di folder `screenshots/`.

7. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 12 - Virtual Machine"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```
praktikum/week12-virtual-machine/
├─ code/
│  └─ catatan_konfigurasi.txt (opsional)
├─ screenshots/
│  ├─ instalasi_vm.png
│  ├─ konfigurasi_resource.png
│  └─ os_guest_running.png
└─ laporan.md
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
1. Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.
Virtual Machine menjalankan sistem operasi guest (Ubuntu Linux) di atas host (Windows 10) melalui hypervisor VirtualBox. Guest OS tidak memiliki akses langsung ke perangkat keras fisik, melainkan menggunakan resource virtual (CPU, RAM, dan disk) yang dialokasikan oleh hypervisor. Hal ini terbukti dari hasil pengujian free -h, lscpu, dan top, di mana perubahan resource hanya memengaruhi kinerja VM tanpa berdampak pada sistem host. Dengan demikian, jika terjadi error, lag, atau gangguan pada guest OS, sistem host tetap berjalan normal karena keduanya terisolasi.
2. Kaitkan dengan konsep sandboxing dan hardening OS.
Isolasi yang diterapkan oleh VM merupakan bentuk sandboxing, yaitu menjalankan sistem dalam lingkungan terbatas dan terpisah. Pada praktikum, Ubuntu Linux berjalan di dalam sandbox VM sehingga aktivitas seperti instalasi aplikasi dan pengujian performa tidak memengaruhi host. Selain itu, VM mendukung hardening OS karena sistem guest dapat diuji, dikonfigurasi, atau diamankan (misalnya pengaturan resource dan user) tanpa risiko terhadap sistem utama. Hal ini membuat virtualisasi aman digunakan untuk pembelajaran dan eksperimen sistem operasi.  

---

## Kesimpulan
1. **Virtual Machine memungkinkan isolasi sistem operasi**
Sistem operasi guest dapat berjalan secara terpisah dari host melalui hypervisor, sehingga gangguan atau kesalahan pada guest OS tidak memengaruhi sistem host.
2. **Konfigurasi resource memengaruhi kinerja VM**
Hasil praktikum menunjukkan bahwa penambahan CPU dan RAM meningkatkan performa OS guest, sedangkan resource yang rendah menyebabkan sistem berjalan lebih lambat.
3. **Virtualisasi meningkatkan keamanan dan fleksibilitas**
VM mendukung konsep sandboxing dan hardening OS, sehingga aman digunakan untuk pembelajaran, pengujian sistem, dan eksperimen tanpa risiko terhadap sistem utama.

---

## Quiz
1. [Apa perbedaan antara host OS dan guest OS?]  
   **Jawaban:** 
   Host os adalah sistem operasi utama yang berjalan di perangkat keras fisik komputer (RAM, disk, jaringan). Sedangkan Guest os adalah sistem operasi tamu yang berjalan di mesin virtual (VM). 
2. [Apa peran hypervisor dalam virtualisasi?]  
   **Jawaban:**  
   Peran hypervisor dalam virtualisasi adalah sebagai pengelola Virtual Machine (VM) yang mengatur pembagian dan penggunaan sumber daya hardware agar setiap VM dapat berjalan secara efisien.
3. [Mengapa virtualisasi meningkatkan keamanan sistem?]  
   **Jawaban:**  
   Karena pada virtualisasi menyediakan isolasi anatara sistem. Isolasi ini membuat aktivitas di dalam satu Virtual Machine (VM) tidak secara langsung memengaruhi sistem lain maupun sistem utama (host). Dengan begitu, risiko kerusakan sistem menjadi lebih kecil dan lebih aman.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
