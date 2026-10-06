# Audit: SWI Heritage vs SWI sebelum konversi (yang memuat update Martabe)

Tanggal audit: 2026-10-06. Pembanding: setiap file SWI pada commit `3159ee8` (sebelum konversi pertama, sudah memuat semua update hasil perbandingan Martabe) dicocokkan per paragraf dengan file Heritage saat ini. Skrip: `build/audit_vs_source.py`.

Catatan sumber: file WI Martabe asli tidak disimpan di repo. Update Martabe yang dibahas sudah ditulis ke file SWI (Part B/C/D bertanda [M]) sebelum konversi, jadi file SWI itulah pembandingnya.

## Metode

- Setiap paragraf SWI lama (langkah, bullet, baris hazard, referensi) dicari di file Heritage. Paragraf dianggap "tidak ditemukan utuh" bila kurang dari 75 persen kata pentingnya ada dalam satu paragraf Heritage.
- Setiap paragraf yang tidak ditemukan utuh ditinjau manual dan digolongkan: (a) dipecah atau ditulis ulang (kata-katanya ada di dokumen, misalnya satu langkah menjadi beberapa bullet, satu referensi menjadi kolom ID dan judul, tanda [M]/[CONFIRM] menjadi paragraf Draft dan Open items); (b) boilerplate yang diganti wording Heritage; (c) dibuang sesuai keputusan review; (d) hilang tanpa keputusan - harus diperbaiki.

## Temuan golongan (d) dan perbaikannya

| Temuan | File | Perbaikan |
|---|---|---|
| "Site inducted, with current cyanide awareness and gas detection competency" (Section 2 lama) tidak terbawa | Semua 37 | Ditambahkan ke bullet pertama Pre-start Check |
| "Field or bench data sheet" dan "Register or logbook entry" (Section 8 Records) tidak terbawa | 12 file seri 203, dan 201-025 | Ditambahkan ke step Completion |
| Catatan "(not received)" pada larutan asam sulfat Martabe hilang | 201-020 | Dikembalikan di Equipment Required |
| Kotak emergency tidak muat di halaman 1 (PPE 9 butir) | 201-007 | Heat-resistant gloves digabung ke baris suit dan sarung tangan |

Setelah perbaikan, audit ulang: ketiga temuan isi = 0. Perbedaan file sebelum dan sesudah perbaikan hanya baris-baris di atas.

## Hasil per SWI

| SWI | Paragraf lama | Tidak ditemukan utuh | Hasil tinjauan | Halaman |
|---|---|---|---|---|
| 201-001 | 123 | 9 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 201-002 | 120 | 7 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 8 |
| 201-003 | 146 | 11 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 9 |
| 201-004 | 146 | 10 | OK - dipecah/ditulis ulang; tambahan Martabe ada sebagai step DRAFT, [CONFIRM] jadi Open items | 8 |
| 201-005 | 164 | 45 | OK - Part B dan C Martabe (C2 check dan kalibrasi) dibuang - plant tidak punya analyser C2 | 7 |
| 201-006 | 110 | 4 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 201-007 | 112 | 4 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 201-008 | 120 | 5 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 8 |
| 201-009 | 120 | 5 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 201-010 | 120 | 6 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 201-011 | 112 | 7 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 201-012 | 113 | 6 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 201-013 | 168 | 17 | OK - dipecah/ditulis ulang; tambahan Martabe ada sebagai step DRAFT, [CONFIRM] jadi Open items | 11 |
| 201-014 | 133 | 6 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 8 |
| 201-015 | 114 | 6 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 201-016 | 128 | 7 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 8 |
| 201-017 | 135 | 18 | OK - Part B Martabe (flocculant solution sampling) dipindah ke 201-020 - langkah 8-12 ada utuh di 020 | 7 |
| 201-018 | 114 | 4 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 201-019 | 107 | 14 | OK - Banner NOT FOR USE dan Part A kosong diganti catatan "titik sampling perlu diupdate"; teknik Martabe jadi Step 2-3 | 7 |
| 201-020 | 168 | 11 | OK - dipecah/ditulis ulang; tambahan Martabe ada sebagai step DRAFT, [CONFIRM] jadi Open items | 11 |
| 201-021 | 107 | 6 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 6 |
| 201-022 | 145 | 15 | OK - dipecah/ditulis ulang; tambahan Martabe ada sebagai step DRAFT, [CONFIRM] jadi Open items | 9 |
| 201-023 | 114 | 8 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 201-024 | 113 | 6 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 201-025 | 105 | 11 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 6 |
| 203-001 | 109 | 5 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 203-002 | 135 | 23 | OK - Part B Martabe (density gauge, sampling manual) dibuang - SWI memakai cutter dengan pompa | 7 |
| 203-003 | 135 | 25 | OK - Part B Martabe (cyclone manual di ketinggian) dibuang - SWI memakai cutter dengan pompa | 7 |
| 203-004 | 109 | 5 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 203-005 | 113 | 5 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 203-006 | 113 | 5 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 203-007 | 112 | 5 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 203-008 | 101 | 5 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 6 |
| 203-009 | 108 | 5 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 203-010 | 131 | 20 | OK - Part B Martabe (intertank screen, saat shutdown) dibuang - cek karbon di launder rutin per jam di 201-004 | 7 |
| 203-011 | 110 | 4 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 7 |
| 203-012 | 107 | 5 | OK - dipecah/ditulis ulang dan boilerplate Heritage | 6 |

## Boilerplate lama yang sengaja diganti (golongan b)

- "Authorised by the Shift Supervisor before the task starts" - digabung ke bullet pertama Pre-start.
- "Gloves appropriate to the task" - tercakup baris "Chemical resistant suit, nitrile rubber gloves and apron".
- "Any control in Section 3 found not in place" - menjadi "any control in Part 2 found not in place".
- 201-024 dan 201-025: bullet "plant dalam steady state" tidak dipakai karena SWI ini untuk kondisi tidak steady dan alarm. 201-025: penutup tanpa "tutup valve", "cuci titik", dan "kirim sampel" karena bertentangan dengan larangan masuk kembali.
- 201-023: "tutup valve" dan "cuci titik" di penutup tidak diulang karena sudah ada di langkah 7 dan 9.

## Register

Register dipisah per seri: `docs/Register-SWI-201.xlsx` dan `docs/Register-SWI-203.xlsx`, dibuat ulang dari file setelah perbaikan (`build/build_register.py`). Jumlah halaman beberapa file berubah karena bullet Pre-start lebih panjang.
