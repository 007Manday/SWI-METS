# Catatan perubahan: SWI 205 dengan tambahan Martabe (001, 002, 006, 012, 013, 015, 017) ke format Heritage

Semua saran pembahasan disetujui pengguna (2026-10-06). Untuk 205-006, persetujuan diartikan sebagai jalur "ya": metode netralisasi air asam dipertahankan dalam bentuk DRAFT. Open item (1) meminta nama aliran air asam di Mt. Morgan. Bila ternyata testwork ini tidak dilakukan, Step 4-7 cukup dihapus.

Umum: Area "205 Met Lab - Chemical and Leach Testwork", Parent procedure PRO209. APD dan kalimat baku sama dengan 205 batch 1. Tanda [M]/[CONFIRM] di SWI lama menjadi paragraf Draft dan Open items di Description of work, atau masuk ke langkah kerja sesuai keputusan. Path folder G: dan nomor form Martabe tidak dipakai.

| SWI | Status | Halaman | Ringkasan |
|---|---|---|---|
| 205-001 Free Cyanide Titration | Final | 7 | Isi SWI tetap. Dari Martabe hanya cek buret digital 0.00 dan kedaluwarsa AgNO3. Titik akhir salmon pink tahan 30 detik |
| 205-002 Caustic Soda Strength Titration | DRAFT | 7 | HCl tetap metode utama (Step 3). H2SO4 jadi alternatif (Step 4) dengan faktor 2 dan x40 untuk g/L. Titrant "5%" wajib distandarisasi. Titik akhir pink hilang 30 detik, bukan "soft pink". Limbah B3 diganti aliran limbah site. Sampel caustic ReCYN mengikuti 201-020 |
| 205-006 Lime Addition and Lime Demand | DRAFT | 8 | Part A tetap (Step 2-3). Part B, C, D dan TSF Toe (dari 205-015) digabung menjadi satu metode netralisasi air asam (Step 4-7): reagen lime, quicklime atau caustic, opsi udara atau H2O2, dan pemantauan TDS. Kondisi STOP: hanya sampel bebas sianida. Dosis kecil dipakai setelah pH sekitar 5,5. Nama sampel SP09/MHR-1/TSF Toe dan angka tabel Martabe tidak dipakai |
| 205-012 Resin Adsorption Capacity and Kinetics | DRAFT, NOT FOR USE | 8 | pH >= 10,5 sebelum NaCN, sampel 20 mL, varian KCN dibuang. "CIL tank 7 to detox" dipetakan ke discharge 032-TK-006 ke ReCYN. Slurry 5 L dan logsheet mulai dari 5 L. Ukuran screen, kapasitas loading dan data Goldquip jadi open item. Ditambah bullet "tidak sendirian" |
| 205-013 Resin Elution Efficiency | DRAFT, NOT FOR USE, safety-critical | 11 | Lihat rincian di bawah |
| 205-015 Cyanide Destruction (Detox) Bench Test | NOT FOR USE | 6 | Blocker spesifik: tidak ada sirkuit detox (ReCYN langsung setelah CIL), keputusan OR-07 terbuka. TSF Toe dan baris hazard-nya dipindah ke 205-006 |
| 205-017 Preparation of Standard and Working Solutions | DRAFT | 8 | Re-kualifikasi hanya untuk phenolphthalein dan silica gel, dan perlu persetujuan Metallurgy Superintendent. Langkah lama "hanya reagen in-date" diberi pengecualian. Etanol dipakai di fume cupboard, jauh dari oven. Suhu oven dari SDS (open item) |

## 205-013 rincian
- Step:
  1. Pre-start (semua kerja sianida di fume cupboard, tidak ada asam di area kerja, tidak sendirian)
  2. Preconditioning (V2: 70, 100 dan 125 kg/t, resin 300 mL)
  3. Eluant elution
  4. Column run
  5. NaCl dissolution
  6. Sulfamic acid
  7. NaCN-NaCl mixing
  8. Zn(CN)4 eluant
  9. Column elution
  10. DDA calibration
  11. Completion
- Preconditioning memakai V2. Dosis versi vendor NaCl (150 mL resin, 68,2 mL CuSO4, 7,29 g NaCN) tidak dipakai, dan perbedaan rasionya dicatat sebagai open item.
- Setiap penambahan sianida dilakukan pada pH >= 10,5. Rentang Martabe pH 10-11 dan pH 10 tidak dipakai.
- AgNO3 0,1 M untuk eluate pekat dan 0,01 M untuk larutan encer, mengikuti 205-001.
- Sulfamic acid: dijaga selama 240 menit penuh dengan monitor HCN. Berhenti di 5 ppm, encerkan, lalu evakuasi. Limbahnya masuk aliran sianida.
- Zn(CN)4: zinc sulphate heptahydrate dan KCN, karena hitungan 0,5 M cocok.
- Kalibrasi pompa DDA juga dicek pada laju uji (150 dan 300 mL/jam).
- Hazard "cloth gloves" di titik jepit quick-connect diganti "chemical-resistant gloves", konsisten dengan keputusan sarung tangan latex.
- **Temuan baru (open item 6):** sumber Martabe menambahkan larutan KCN ke larutan zinc sulphate yang agak asam. Ini perlu dicek HSE, karena urutan sebaliknya (zinc sulphate ke KCN basa) menjaga sianida tetap basa. Langkah kerja sekarang hanya mewajibkan pH dipantau dan dihentikan di bawah 10,5.
- Open items (9): data Goldquip, rasio dan kekuatan CuSO4, kekuatan eluant 49 g/L, sumber NaCl untuk 4 resin, kekuatan larutan plant dan arti IPHK, urutan pencampuran Zn(CN)4, aliran limbah hi-cyanide di Mt. Morgan, sambungan selang pompa, dan worksheet catatan.

## Audit
Diaudit terhadap SWI sebelum konversi (commit 3159ee8). Bagian yang tidak cocok utuh hanya bagian yang sengaja diubah sesuai keputusan di atas:
- tanda [M]/[CONFIRM] dan paragraf "Purpose";
- nama sampel dan path Martabe;
- dosis preconditioning versi vendor;
- varian KCN 205-012;
- TSF Toe yang dipindah;
- kalimat baku lama.

Setelah audit, dua hal dipulihkan: alat "Solutions at known metal and cyanide concentration" (012) dan kalimat "semua kerja di fume cupboard" (013).

Semua lolos validasi docx dan kotak emergency ada di halaman 1. Mohon dicek HSE untuk hazard a), b), c), CAUTION, dan emergency.
