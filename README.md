# Analisis Komentar YouTube tentang PP Tunas

Proyek mata kuliah Sosial Media (Bisnis Digital, UNM).

## Latar belakang
PP Tunas (PP Nomor 17 Tahun 2025) mewajibkan platform digital membatasi
akses anak sesuai usia. Sejak 28 Maret 2026, akun anak di bawah 16 tahun
mulai dinonaktifkan di sejumlah platform besar. Kebijakan ini memengaruhi
cara kerja platform dan memunculkan beragam tanggapan publik di media sosial.

## Tujuan
Melihat apa yang dibicarakan warganet pada video YouTube tentang PP Tunas,
dengan menghitung seberapa sering kata-kata tertentu muncul di kolom komentar.

## Sumber data
- Platform: YouTube (video Shorts, tayang 6 Maret 2026)
- Tautan: https://youtube.com/shorts/hzDavp3DQo4
- Jumlah komentar yang diambil: maksimal 300
- Nama pengguna tidak disimpan

## Alat yang dipakai
- Python
- `youtube-comment-downloader` untuk mengambil komentar
- `pandas` untuk merapikan data dan menyimpannya

## Menjalankan program
pip install -r requirements.txt
python pptunas.py


## Hasil
- Ringkasan di terminal: jumlah komentar, rentang waktu, hitungan kata kunci,
  dan lima komentar dengan like terbanyak
- File `komentar_pptunas.csv` berisi kolom waktu, tanggal, like, dan komentar

## Catatan
Keterangan waktu dari YouTube berbentuk perkiraan (misalnya "3 bulan yang lalu"),
sehingga kolom tanggal pada CSV bersifat kasar.

## Kelompok
- Mutiah Anwar (240907500007)
- Nadyah Fakhriyah Izzah FS (240907501005)
- Shofiyah Jihan Aulia Anwar (240907502006)
- Siti Nadhifa Fadhilah (240907502011)