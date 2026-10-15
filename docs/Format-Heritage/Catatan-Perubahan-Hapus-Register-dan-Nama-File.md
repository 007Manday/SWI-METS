# Catatan perubahan: hapus rujukan prosedur induk dan register; nama file dipersingkat

Permintaan pengguna (setelah PR #1 di-merge): nomor HM-PRC-VXX-PRO2xx dan register SWI/SWMS tidak ada, jadi kalimat rujukan ke keduanya dihapus dari semua SWI dan SWP. Nama file dipersingkat dengan menghapus awalan "MM-4034-033-OR-03-".

## SWI (99 dokumen)
- Dihapus dari Description of work, termasuk baris kosong di bawahnya:
  - "This instruction sits under Standard Work Procedure HM-PRC-VXX-PRO2xx - … Read that procedure before carrying out this task for the first time."
  - "Register line: SWI-PRO-MET-xxx-xxx in HM-MMM-WHS-REG-XXX-R00-SWI-SWMS, tab SWI-MET. The matching hazard analysis is JSEA-PRO-MET-xxx-xxx." Nomor JSEA tetap ada di Part 1 (JSEA ID) dan di tabel Referenced Documents.
- Dihapus dari tabel Referenced Documents: baris prosedur induk (HM-PRC-VXX-PRO2xx) dan baris register (HM-MMM-WHS-REG-XXX-R00-SWI-SWMS).
- Tidak ada perubahan lain. Pada setiap file hanya 8 paragraf yang hilang: 2 kalimat, 2 baris kosong, dan 2 baris tabel. Ini sudah dicek otomatis.
- Semua lolos validasi docx, dan kotak emergency tetap di halaman 1. Beberapa SWI menjadi satu halaman lebih pendek; jumlah halaman di register sudah diperbarui.

## SWP (8 dokumen)
- Purpose and Scope:
  - Kalimat "It is the procedure that the N hazard analyses and N work instructions in register area NNN sit under." dihapus.
  - Bullet "Register area: …" dihapus.
- Bab 8 "Register Traceability" menjadi **"Document Traceability"**:
  - Paragraf "Registers: HM-MMM-WHS-REG-… tab …" dihapus.
  - Kalimat sufiks diubah menjadi "shared between the hazard analysis and the work instruction".
  - Baris tabel "Register lines in area NNN" menjadi "Tasks in area NNN".
- Bab 10.2: kalimat "Register lines are on tabs … (Section 8)." dihapus.
- Daftar isi dibangun ulang dengan nomor halaman yang baru. Semua lolos validasi docx.
- **Belum diubah:** nomor dokumen SWP sendiri (HM-PRC-VXX-PRO206, PRO208, PRO212 sampai PRO217) di sampul, header dan tabel Document History. Menunggu keputusan pengguna.

## Nama file
- `SWI/…/MM-4034-033-OR-03-SWI-PRO-MET-…docx` menjadi `SWI/…/SWI-PRO-MET-…docx`.
- `SWP/MM-4034-033-OR-03-SWP-…docx` menjadi `SWP/SWP-…docx`.
- Kolom "Nama file" di `docs/Register-SWI-*.xlsx` sudah diperbarui. Baris "Referensi register" di sheet Keterangan dihapus.

## Skrip
- `swi_common.py`: `desc()` dan semua `refs*()` tidak lagi menulis rujukan prosedur induk dan register. Konten 201-001 sampai 201-005 ikut disesuaikan. Hasil build ulang sudah dicek sama persis dengan file yang diedit.
- `swp/build_swp.py` dan `run_swp.sh`: perubahan SWP di atas, dan nama output tanpa awalan.
- `audit_vs_source.py`: membaca file lama dengan nama lama di commit dasar.
