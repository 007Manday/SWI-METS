# Perbandingan SWI vs Work Instruction Martabe (batch 1 dan 2)

Sepuluh work instruction (WI) tim Martabe diterima dan dibandingkan dengan SWI yang sesuai. Isi Martabe ditambahkan ke SWI dengan tanda **[M]**. Hal yang tidak jelas atau bertentangan di sumber ditandai **[CONFIRM]** di dalam dokumen dan harus diselesaikan sebelum SWI disetujui.

SOP `KBK-MIR-...` dan `CNREC-...` yang dirujuk di bagian Reference masih belum diterima (lihat `Matriks-Rujukan-Martabe.xlsx`). Sepuluh WI ini adalah dokumen lain.

## Pemetaan

| WI Martabe | SWI Anda | Hasil |
|---|---|---|
| Dosing NaOH vs Ca(OH)2 (pH 6,7,8,9) | 205-006 Lime Addition and Lime Demand | Ditambah Part B |
| Verifikasi Analyzer Leaching (12/05/2025) | 201-022 Online Analyser Verification | Ditambah Part B |
| Resin activity test (03/03/2025) | 205-012 Resin Adsorption Capacity and Kinetics | Placeholder diganti metode |
| Testing NaCl from New Vendor (11/01/2025) | 205-013 Resin Elution Efficiency | Placeholder diganti metode |
| Stirred Leach with %Solid Variation (26/04/2025) | Tidak ada yang cocok | Belum dimasukkan (lihat bawah) |
| MHR1 - Konsumsi Quick lime, metal removed (file `MHR_1_Liming_vs_Limingair`) | 205-006 Lime | Ditambah Part C |
| TSF Toe to WPP Test | 205-015 Cyanide Destruction Detox | Ditambah Part B (draft); Part A tetap NOT FOR USE |
| Scaling eluant garam dengan sulfamic acid (07/10/2025) | 205-013 Resin Elution | Ditambah Part 4 |
| IPHK mixing NaCN-NaCl | 205-013 Resin Elution | Ditambah Part 5 |
| Leaching with NaNO2 preoxidation V2 (14/02/2025) | Tidak ada yang cocok | Belum dimasukkan (lihat bawah) |

## Per dokumen

### 205-006 (lime) - Part B
- SWI Anda: kebutuhan kapur untuk menahan pH target leach. Martabe: netralisasi sampel SP09 ke pH 6, 7, 8, 9 dengan kapur dan caustic, tiap titik ditahan 5 menit, lalu settling (maks 2 jam), foto, filtrasi, assay base metal. Tujuannya berbeda, jadi Martabe ditambahkan sebagai Part B, bukan menggantikan.
- Ditambah: kode sampel A1-0/1/2 dan B1-0/1/2, daftar assay logam terlarut, catatan foto dan waktu settling.
- Masalah di sumber: SP09 tidak didefinisikan; langkah Run 2 masih tertulis "tambahkan lime"; "ulangi langkah 4 dan 5" merujuk penomoran sumber yang ambigu.
- **Keselamatan:** tes ini membawa sampel ke pH di bawah 10.5. Saya tambahkan syarat STOP: hanya untuk sampel yang terbukti bebas sianida. Baris hazard baru ditandai untuk JSEA.

### 201-022 (analyser) - Part B
- SWI Anda: ambil sampel manual di titik analyser online. Martabe: ambil 3 L slurry dari leach tank 1, 2, 3, press, 200 mL + caustic, baca NaCN dan WAD CN di analyser, titrasi 10 mL, sisa ke ITS (NaCN, WAD CN, Cu).
- Ditambah: tiga tangki, pembacaan WAD CN, assay Cu di lab, botol hitam 250 mL, filter press.
- Masalah di sumber: jumlah caustic atau pH target tidak disebut. Saya tulis [CONFIRM] dan menyarankan pH di atas 10.5 sesuai kontrol HCN di SWI.

### 205-012 (resin kinetics) - placeholder diganti
- Banner NOT FOR USE diubah menjadi DRAFT FOR REVIEW. Target penerimaan GG1200M/GG1200C tetap menunggu data vendor.
- Metode Martabe hanya mengukur kinetika adsorpsi (resin loaded dan Cu-eluted vs resin fresh, 1 L larutan, 5 g resin, sampling menit 5/10/15/20/30). Kapasitas loading tidak tercakup.
- Masalah di sumber: file bernama "Ball_Mill_Cyclone_Profile" tetapi isinya resin activity test; sampling 30 mL di teks vs 20 mL di tabel; screen 1.18 dan 1.4 mm vs screen 0.9 mm di SWI Anda; konsentrasi larutan CuSO4 tidak disebut; "Cek % solid" tanpa objek.
- **Keselamatan:** sumber menahan pH 10 sampai 10.5, sedangkan aturan di SWI 205-007: sianida TIDAK boleh ditambahkan di bawah pH 10.5. Saya tulis pH 10.5 atau lebih sebelum NaCN, dan [CONFIRM].

### 205-013 (elution) - placeholder diganti
- Banner diubah menjadi DRAFT FOR REVIEW. Metode Martabe membandingkan NaCl dari vendor lewat tes elusi tembaga: preconditioning 70 kg/t Cu(CN)4 pada 150 mL resin, elusi 3 jam pada 1 BV/jam, sampling tiap 30 menit, serta uji pelarutan NaCl 1 M (30.15 g) dan 3 M (90.46 g) per 500 mL.
- Barren resin loading tidak tercakup oleh sumber.
- Masalah di sumber: titrasi AgNO3 0.1 M di satu tempat, 0.01 M di tempat lain; 29.4 g NaCN dalam 600 mL setara sekitar 49 g/L (sekitar 1 M), mohon konfirmasi kekuatan ini disengaja; pH eluant 10 sampai 11 di bawah aturan pH 10.5; kekuatan CuSO4 tidak disebut; jenis CuSO4 berbeda (7H2O di tabel, "plant" di daftar bahan); empat resin tidak dijelaskan mewakili vendor mana.
- **Keselamatan:** baris hazard baru untuk penimbangan NaCN padat dan eluant pekat, ditandai untuk JSEA.

## Batch 2

### 205-006 - Part C (MHR-1 quicklime)
Quicklime ke pH 4, 7, 9, 10 pada sampel MHR-1 (1 L), tiga run: A kapur saja, B dengan plant air, C dengan plant air dan 0.5 mL H2O2. Assay base metal di pH 7 dan 10. Masalah di sumber: MHR-1 tidak didefinisikan; aliran udara, kekuatan H2O2 dan volume yang dimaksud 0.5 mL tidak disebut. Sumber hanya mencantumkan kacamata dan sarung tangan karet, di bawah standar SWI. STOP condition bebas-sianida dari Part B berlaku juga di sini (pH 4 dan di bawah 10.5).

### 205-015 - Part B (TSF Toe)
Hydrated lime ke pH 7 pada air TSF Toe, dengan assay lengkap di ITS (logam, TSS, TDS, free/WAD/total CN, nitrit, ammonia bebas, COD, fluorida, BOD). Part A (uji rute destruksi sianida) tetap NOT FOR USE karena keputusan OR-07 belum ada. Masalah di sumber: tujuan menyebut peroxide atau hydrated lime, tetapi langkah hanya lime (dosis peroxide dan tangki mana yang menerima apa tidak disebut); pH awal sampel tidak diketahui padahal sampel mengandung sianida; 2 L sampel untuk tangki 1 dan 2 ambigu. Saya perlakukan sampel sebagai bersianida.

### 205-013 - Part 4 (sulfamic acid) dan Part 5 (IPHK)
- Part 4: 7.5 g asam sulfamat dalam 300 mL air proses atau air mentah, 5 g scale, tanpa pengadukan, foto sampai 240 menit, STOP dan evakuasi jika HCN di atas 5 ppm (sama dengan alarm 5 ppm di SWI). Risiko: asam pada scale bersianida melepas HCN. Baris hazard baru.
- Part 5: campuran 85 mL NaCl plant + 15 mL NaCN plant untuk melihat endapan; selalu NaCN ke NaCl. Masalah di sumber: kekuatan larutan plant tidak disebut (target 1.0 M NaCN dan 0.9 M NaCl berarti sekitar 6.7 M NaCN dan 1.06 M NaCl); pH tidak disebut; arti "IPHK" tidak disebut.
- Catatan: 205-013 sekarang berisi lima bagian yang semuanya tentang sistem eluant garam. Pertimbangkan memindahkan Part 3 sampai 5 ke SWI terpisah, misalnya "Eluant salt compatibility and scaling tests".

## Belum dimasukkan: dua uji stirred leach
Keduanya uji leach teraduk 20 jam pada pH 10.5 sampai 11, NaCN 1500 ppm, DO 15 sampai 25 ppm, cek pada jam ke 2, 4, 6, assay Au/Ag/Cu/S di ITS. SWI Anda hanya punya bottle roll (205-007) dan extended/diagnostic leach (205-008), yang bukan uji yang sama. Usul: satu SWI baru, misalnya 205-020 "Stirred Leach Testwork".
- Variasi persen padatan: 50, 52, 55, 57 persen, dengan sampel leach feed.
- Preoksidasi NaNO2: 3 botol feed (A 19 jam, B 5 jam, C tanpa) pada 40 persen padatan, dan tailing (D tanpa, E 19 jam). Masalah di sumber: "3 x 1061 kg solid dengan 1592 kg air" untuk 40 persen padatan cocok bila satuannya gram, bukan kg; dosis NaNO2 124.2 satuannya tidak jelas (tabel menulis g) dan terlihat sangat besar untuk 1061 g padatan; penomoran langkah loncat dari 12 ke 20.
Menunggu keputusan Anda.

## Yang perlu Anda lakukan
1. Selesaikan semua [CONFIRM] di keempat SWI.
2. Perbarui JSEA untuk baris hazard bertanda [JSEA to confirm] (205-006, 201-022, 205-012, 205-013, 205-015).
3. Reviewer dan approver mengisi tanda tangan. Revisi tetap Rev A; ubah sesuai aturan kontrol dokumen Anda.
4. Kirim SOP `KBK-MIR-...` dan `CNREC-...` yang masih kurang.
