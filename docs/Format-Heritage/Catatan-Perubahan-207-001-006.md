# Catatan perubahan: SWI-PRO-MET-207-001 sampai 207-006 (automatic sampler) ke format Heritage

## Pola seri 207
- Parent procedure `HM-PRC-VXX-PRO211 Automatic Sampling and Online Analyser Operation`. Semua Safety-critical.
- Wording Pre-start dan penutup di SWI lama sama persis dengan seri 203 (control room diberi tahu task dan lokasi, monitor gas, shower dan eyewash, area layak; bersihkan area, kembalikan alat, catat, beri tahu control room), jadi memakai `prestart203` dan `CLOSE203` di `build/swi_common.py`, ditambah butir Records.
- Isi tiap SWI di `build/gen207a.py`. Tidak ada padanan Martabe untuk 001-006.

| SWI | Judul | Status | Halaman |
|---|---|---|---|
| 207-001 | IsaMill Feed 022-XM-011 / 017 | NOT FOR USE | 6 |
| 207-002 | CIL Tails 032-XM-012 | NOT FOR USE | 6 |
| 207-003 | Metal Adsorption Tails 041-XM-013 | NOT FOR USE | 6 |
| 207-004 | Final Tails 051-XM-014 | NOT FOR USE | 6 |
| 207-005 | Sampler Cleaning, Unblocking, Cutter Wear | NOT FOR USE | 6 |
| 207-006 | Auto vs Manual Bias Check | Aktif | 6 |

## 207-001 sampai 005 (tetap NOT FOR USE)
- Banner jadi paragraf tebal di Description of work dan menyebut blocker-nya langsung, menggantikan "see the folder README" yang tidak ada isinya: desain sampler dan cutter belum ada (vendor TBA), status NEW versus FUTURE yang bertentangan di equipment list (001, 002), tanpa referensi P&ID (004).
- Step: Pre-start Check, Status - Not for Use, Completion.

## 207-006 (aktif)
- Step: Pre-start (atur dengan control room dan lab agar dianalisis dalam batch yang sama), Paired Sampling, Bias Test, Report and Correction, Completion.
- CAUTION Paired Sampling: sampling manual mengikuti SWI Area 201 untuk titik itu; jauhi cutter sampler.
- Catatan: 006 aktif di SWI lama, tetapi samplernya (001-005) belum terpasang atau desainnya belum ada. Dalam praktik cek bias baru bisa jalan setelah sampler terpasang.

## Audit
Diaudit terhadap SWI sebelum konversi: semua paragraf ada. Yang beda hanya kalimat "see the folder README" yang diganti blocker spesifik.

Hazard a), b), c), CAUTION, dan emergency ditulis baru dari hazard dokumen. Mohon dicek HSE.
