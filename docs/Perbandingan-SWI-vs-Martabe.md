# Perbandingan SWI vs Work Instruction Martabe (batch 1)

Lima work instruction (WI) tim Martabe diterima dan dibandingkan dengan SWI yang sesuai. Isi Martabe ditambahkan ke SWI dengan tanda **[M]**. Hal yang tidak jelas atau bertentangan di sumber ditandai **[CONFIRM]** di dalam dokumen dan harus diselesaikan sebelum SWI disetujui.

SOP `KBK-MIR-...` dan `CNREC-...` yang dirujuk di bagian Reference masih belum diterima (lihat `Matriks-Rujukan-Martabe.xlsx`). Lima WI ini adalah dokumen lain.

## Pemetaan

| WI Martabe | SWI Anda | Hasil |
|---|---|---|
| Dosing NaOH vs Ca(OH)2 (pH 6,7,8,9) | 205-006 Lime Addition and Lime Demand | Ditambah Part B |
| Verifikasi Analyzer Leaching (12/05/2025) | 201-022 Online Analyser Verification | Ditambah Part B |
| Resin activity test (03/03/2025) | 205-012 Resin Adsorption Capacity and Kinetics | Placeholder diganti metode |
| Testing NaCl from New Vendor (11/01/2025) | 205-013 Resin Elution Efficiency | Placeholder diganti metode |
| Stirred Leach with %Solid Variation (26/04/2025) | Tidak ada yang cocok | Belum dimasukkan (lihat bawah) |

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

## Belum dimasukkan: Stirred Leach with %Solid Variation
Uji leach teraduk 20 jam pada 50, 52, 55 dan 57 persen padatan (pH 10.5 sampai 11 dengan kapur, NaCN 1500 ppm, DO 15 sampai 25 ppm, cek pada jam ke 2, 4, 6, assay Au/Ag/Cu/S di ITS). SWI Anda hanya punya bottle roll (205-007) dan extended/diagnostic leach (205-008), yang bukan uji yang sama. Pilihan: SWI baru (misalnya 205-020) atau lampiran di 205-007. Menunggu keputusan Anda.

## Yang perlu Anda lakukan
1. Selesaikan semua [CONFIRM] di keempat SWI.
2. Perbarui JSEA untuk baris hazard bertanda [JSEA to confirm] (205-006, 201-022, 205-012, 205-013).
3. Reviewer dan approver mengisi tanda tangan. Revisi tetap Rev A; ubah sesuai aturan kontrol dokumen Anda.
4. Kirim SOP `KBK-MIR-...` dan `CNREC-...` yang masih kurang.
