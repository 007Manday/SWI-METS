# Catatan perubahan: SWI-PRO-MET-201-006 sampai 201-012 ke format Heritage

Aturan umum sama dengan catatan sebelumnya. Teks tabel hazard disalin otomatis dari file lama. Wording umum (Pre-start, Completion, PPE, emergency) ada di `build/swi_common.py`. Tidak ada bagian Martabe di tujuh SWI ini, jadi tidak ada yang dibuang atau ditambah dari Martabe.

| SWI | Judul | Halaman | Step |
|---|---|---|---|
| 201-006 | Loaded Carbon at 032-SC-002 | 7 | Pre-start, Sample Collection, Washing and Submission, Completion |
| 201-007 | Barren Carbon at 061-SC-013 | 8 | sama, plus bahaya panas |
| 201-008 | CIL Tail at 032-SC-003 | 7 | Pre-start, Sample Collection, Carbon Check, Per Cent Solids and Assay, Completion |
| 201-009 | Metal Adsorption 041-TK-007/008 | 7 | Pre-start, Sample Collection, pH and Free Cyanide, Filtration and Profile Sheet, Completion |
| 201-010 | Cyanide Adsorption 051-TK-009/010 | 7 | sama dengan 009 |
| 201-011 | Resin Concentration | 7 | Pre-start, Sampling and Resin Volume, Resin Profile, Completion |
| 201-012 | Loaded and Barren Resin | 7 | Pre-start, Sample Collection, Washing and Submission, Completion |

## Hal khusus per SWI
- **006:** langkah lama 1 (konfirmasi transfer karbon) ke Pre-start. Langkah 2-3 ke Sample Collection, 4-6 ke Washing and Submission.
- **007:** PPE ditambah "Heat-resistant gloves" (dari daftar PPE lama). Kontrol hazard panas (tidak sedang heating cycle, kolom tidak bertekanan) diulang di Pre-start dan CAUTION Sample Collection. Kotak emergency ditambah butir burns (diadaptasi dari 304-008).
- **008:** banner SAFETY-CRITICAL FINDING dipindah ke Description of work (paragraf tebal, isi tidak diubah) dan diulang ringkas di CAUTION step Carbon Check. Cek posisi valve 032-XV-003/004 jadi bullet Pre-start. Kotak emergency ditambah butir "carbon in the undersize" (dari kontrol lama: lapor segera ke Shift Supervisor).
- **009 dan 010:** langkah lama 4 (pH dan free cyanide) jadi step sendiri; rujukan SOP Martabe tetap sebagai Referenced Documents.
- **010:** langkah lama 6 merujuk "online cyanide analyser". Dibiarkan seperti SWI asli. Perlu dikonfirmasi apakah analyser itu ada di plant ini (lihat pertanyaan di bawah).
- **011:** langkah lama 1-2 digabung ke Pre-start; 3-7 jadi Sampling and Resin Volume; 8 jadi Resin Profile.
- **012:** langkah lama 1 ke Pre-start; 2 ke Sample Collection; 3-5 ke Washing and Submission. Rujukan SOP KBK dan site procedure 9 dipertahankan.

## Berlaku untuk semuanya
- Hazard a), b), c) per step, kotak CAUTION, dan kotak emergency ditulis baru dari hazard tiap dokumen (butir "fall" hanya bila ada hazard fall, dst.). Mohon dicek HSE.
- Butir "second person in the area" ditambahkan ke Pre-start (dari pernyataan safety-critical dan kontrol HCN lama).
- Section 2 (Who may do this) digabung ke Step 1. Classification dibuang; Area ke Description of work.
- PPE digabung jadi 8-9 butir agar kotak emergency muat di halaman 1.
- Ikon PPE tetap 10 ikon heritage; Visual Reference kosong; Document Owner "Processing".
