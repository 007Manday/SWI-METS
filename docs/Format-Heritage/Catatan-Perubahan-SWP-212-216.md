# Catatan perubahan: SWP laboratorium 212 sampai 216 ke format Heritage

Dokumen: HM-PRC-VXX-PRO212 Laboratory Sample Preparation, PRO213 Laboratory Wet Chemistry and Digestion, PRO214 Laboratory Instrumental Analysis, PRO215 Laboratory Environmental and Cyanide Analysis, dan PRO216 Laboratory Services, Safety and Quality.

Template: contoh SWP Heritage dari pengguna, `docs/Format-Heritage/SWP-PRO-000_000_Sodium_Hydrosulphide_Management_Plan.docx`. File asli (layout GGT) ada di commit sebelumnya dalam riwayat folder `SWP/`.

## Format yang diikuti (dari template)
- **Halaman sampul.** Logo Heritage, judul "Safe Work Procedure", nama dokumen (warna emas) dan nomor dokumen. Di bawahnya tabel **Document History and Status** dan catatan dokumen terkendali.
- **Daftar isi otomatis.** Nomor halamannya diambil dari render dua tahap, dan diperbarui Word saat field di-update.
- **Header dan footer.** Header berisi logo, "Safe Work Procedure", judul dan nomor dokumen. Footer berisi Document, Revision Date, Revision No. dan Page x of y. Bingkai halaman emas.
- **Gaya isi.** Judul bab bernomor (Heading 1 dan 2), bullet kotak emas, tabel dengan baris judul abu-abu dan kolom label berarsir, serta kotak "Warning:" bergaya italic.
- **Penutup.** Bab **Review Criteria** dan **Legislation & References** mengikuti urutan template.

## Pemetaan isi (isi tidak diubah)
| Bab Heritage | Asal (layout lama) |
|---|---|
| 1. Purpose and Scope | 1 Purpose / Scope; ditambah rincian dokumen (register area, jumlah JSEA dan SWI, process owner, document owner, approver) dari tabel judul lama |
| 2. Responsibilities | 2 Responsibilities (tabel Staff/Responsibilities, tiap tanggung jawab jadi bullet) |
| 3. Abbreviations and Definitions | 3 Abbreviations / Definitions |
| 4. Potential Hazards | 4 Potential Hazards |
| 5. Personal Protective Equipment | 5 PPE |
| 6. Procedure: 6.1 Introduction (kotak Warning), 6.2 Procedure and Implementation Steps, 6.3 Schedule, 6.4 Flowchart | 6 Procedure dan 7 Flowchart |
| 7. Training | 8 Training |
| 8. Register Traceability | 11 Register Traceability |
| 9. Review Criteria | 10 Review |
| 10. Legislation & References: 10.1 Legislation, 10.2 Source Documents by Task | 9 Reference |

## Perubahan kecil yang perlu diketahui
1. **Istilah.** Definisi "Standard work procedure" dan "Standard work instruction" diganti "Safe work procedure" dan "Safe work instruction", sesuai judul dokumen Heritage. Singkatan SWP dan SWI tetap sama.
2. **Referensi** disusun ulang menjadi tabel JSEA | Task | Source documents and notes. Baris "Heritage register line JSEA-…, tab JSEA_LAB / SWI-LAB" menjadi kolom JSEA, dan tab register disebut sekali di atas tabel. Tugas tanpa dokumen sumber ditulis "No source document held".
3. **Legislation** menambahkan Queensland Mining and Quarrying Safety and Health Act 1999 dan Regulation 2017. Keduanya bagian baku template SWP Heritage. Mohon dikonfirmasi bila lab tidak berada di bawah regulasi ini.
4. **Review Criteria.** Kalimat lama dipecah menjadi dua bullet (setiap 12 bulan, atau segera setelah insiden atau perubahan) tanpa mengubah isi. Siklus 12 bulan dipertahankan, bukan 2 tahun seperti di template.
5. **Flowchart.** Kalimat "in Section 6" dihapus, karena langkah kerja ada di masing-masing SWI.
6. **Document History.**
   - Versi A, issue date 11/08/2026.
   - Owner Process Operations Superintendent, Authorised by Process Manager.
   - Prepared by GGT (cost code 4034-033).
   - Nama reviewer dan approver dikosongkan.
   - Kolom History berisi process owner dan approver.
7. **Nomor dokumen** tetap HM-PRC-VXX-PRO212 sampai PRO216 (bukan pola SWP-OPR-… dari contoh), karena nomor ini dirujuk oleh semua SWI di bawahnya.

## Hasil
| SWP | Halaman | JSEA / SWI di bawahnya |
|---|---|---|
| PRO212 Laboratory Sample Preparation | 8 | 17 / 17 |
| PRO213 Laboratory Wet Chemistry and Digestion | 10 | 33 / 33 |
| PRO214 Laboratory Instrumental Analysis | 8 | 14 / 13 |
| PRO215 Laboratory Environmental and Cyanide Analysis | 10 | 25 / 25 |
| PRO216 Laboratory Services, Safety and Quality | 8 | 16 / 12 |

Semua lolos validasi docx. Audit teks: setiap paragraf dan sel tabel lama ada di dokumen baru. Yang tidak cocok persis hanya judul bab lama, label tabel judul, baris register line (sekarang kolom JSEA), definisi yang diganti istilahnya, kalimat review yang dipecah, dan format tanggal.

Skrip: `docs/Format-Heritage/build/swp/`. Jalankan dengan `TPL_X=<template SWP yang sudah di-unzip> run_swp.sh <SWP lama> <folder output>`.
