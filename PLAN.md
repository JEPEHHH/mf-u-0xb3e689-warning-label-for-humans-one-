# Rencana Kerja: Warning Label for Humans

## Tujuan
Menghasilkan program `program/v1` yang menulis satu baris label peringatan keselamatan paling lucu untuk manusia (1–160 karakter UTF-8) ke `/output/entry.txt`, memenuhi gate validasi, kriteria juri, dan transcript gate.

## Kriteria Utama Juri
1. Benar-benar label peringatan keselamatan untuk setiap manusia dan mengundang tawa.
2. Punchline mendarat dalam satu bacaan dengan belokan di beberapa kata terakhir.
3. Terasa nyata tentang perilaku manusia sehari-hari (bukan absurditas acak).
4. Meniru gaya bahasa dan ritme label tercetak resmi.
5. Pas dalam <= 160 karakter tanpa basa-basi, ide ganda, atau pengulangan.

## Tahapan Kerja & Milestone
1. **Inisialisasi & Lisensi**: Tambah `LICENSE` (MIT / OSI) dan struktur dasar repo, lalu commit milestone 1.
2. **Eksplorasi & Iterasi Kandidat**: Buat daftar kandidat label peringatan satu baris, evaluasi terhadap 5 kriteria juri secara berpasangan (simulasi A vs B), lalu seleksi kandidat terbaik ke `candidates.md`.
3. **Implementasi Entrypoint**: Tulis `main.py` (runtime `python3.13`, tanpa jaringan) untuk menulis label terpilih secara deterministik ke `/output/entry.txt` (memastikan direktori `/output` ada dan encoding UTF-8), lalu commit milestone 2.
4. **Revisi & Pemolesan**: Tajamkan ritme, diksi label resmi, dan punchline akhir pada `main.py` dalam iterasi terpisah (memenuhi syarat `thinking_revised` dan `thinking_reproduces`), lalu commit milestone 3.
5. **Validasi Lokal**: Jalankan `test_entry.py` untuk verifikasi: file `/output/entry.txt` ada, valid UTF-8, satu baris tanpa newline berlebih, bukan spasi kosong, panjang 1–160 karakter, dan deterministik di 2x eksekusi.
6. **Finalisasi**: Cek `git status`, pastikan semua berkas ditulis lewat file tool, dan commit final siap untuk `check`/submit.

## Daftar Berkas yang Akan Dibuat
- `PLAN.md` — Rencana kerja dan daftar berkas (berkas ini).
- `LICENSE` — Lisensi OSI-approved (`SPDX-License-Identifier: MIT`).
- `candidates.md` — Catatan eksplorasi kandidat label dan hasil seleksi kriteria juri.
- `main.py` — Entrypoint `program/v1` yang menulis label pemenang ke `/output/entry.txt`.
- `test_entry.py` — Skrip uji lokal untuk memverifikasi gate (UTF-8, 1–160 karakter, satu baris, deterministik).

## Aturan Teknis
- Semua berkas ditulis menggunakan file tool (tanpa heredoc/tee/sed/cp).
- Commit terpisah di setiap milestone; tidak menyalin teks referensi/kompetitor.
- Runtime hemat sumber daya (batas sandbox: 1 CPU, 512 MB RAM, 60 detik, offline).
