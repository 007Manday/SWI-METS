# Perbandingan SWI vs Work Instruction Martabe (batch 1 sampai 14)

Tujuh puluh file work instruction (WI) tim Martabe diterima dan dibandingkan dengan SWI yang sesuai. Isi Martabe ditambahkan ke SWI dengan tanda **[M]**. Hal yang tidak jelas atau bertentangan di sumber ditandai **[CONFIRM]** di dalam dokumen dan harus diselesaikan sebelum SWI disetujui.

SOP `KBK-MIR-...` dan `CNREC-...` yang dirujuk di bagian Reference masih belum diterima (lihat `Matriks-Rujukan-Martabe.xlsx`). WI ini adalah dokumen lain.

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
- Catatan: file `Work_Instruction_Ball_Mill_Cyclone_Profile` yang diterima lebih dulu ternyata salinan identik dari `Work_Instruction_Resin_Activity_Test` (nama file salah).
- Masalah di sumber: sampling 30 mL di teks vs 20 mL di tabel; screen 1.18 dan 1.4 mm vs screen 0.9 mm di SWI Anda; konsentrasi larutan CuSO4 tidak disebut; "Cek % solid" tanpa objek.
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

## Batch 3

### 205-012: versi KCN
`Resin_Activity_Test_KCN` identik dengan versi NaCN, kecuali memakai 4 g KCN sebagai pengganti 2 g NaCN (tanggal tertulis "03/012/2025"; langkah masih menulis NaCN). 4 g KCN setara sekitar 0.061 mol sianida, 1.5 kali 2 g NaCN (sekitar 0.041 mol); setara molar adalah 2.66 g KCN. Saya tambahkan sebagai catatan varian dengan larangan dijalankan sebelum ada konfirmasi mana yang berlaku.

### 205-013: Part 6 (Copper Loading Test, DOC-3-MET-MEL-WIN-00113-IE v1.0)
WI Martabe terkendali pertama yang diterima (14 halaman, ada kontrol dokumen, JSEA, bahaya, dan foto). Metode: elusi 150 mL resin loaded dengan 0.5 M Zn(CN)4 (322.8 g ZnSO4.7H2O + 351 g KCN, total 2.2 L), 2 BV/jam (300 mL/jam) selama 6 jam, eluate tiap jam, lalu drain dan bilas 300 mL, assay Cu, Fe, Zn di ITS.
- Masalah di sumber: teks Indonesia menulis zinc sulphate tetrahydrate, teks Inggris heptahydrate (322.8 g untuk 0.5 M dalam 2.2 L hanya cocok untuk heptahydrate); reagent berganti-ganti antara KCN dan NaCN, serta "larutan" vs "bubuk"; pH 10 di bawah aturan 10.5; tabel kontrol risiko (9.B) adalah untuk penanganan probe DO, salinan dari WI lain, jadi tidak mencakup HCN dan sianida; buangan cair dikirim ke sump pump tailing, perlu dikonfirmasi sebagai aliran bersianida yang disetujui.
- Tabel kontrol risiko Martabe itu tidak saya bawa. Saya tambahkan baris hazard untuk eluant hi-cyanide 2.2 L, ditandai untuk JSEA.
- Sumber juga menunjukkan cara sampling resin di loaded screen dengan kantong plastik; saya merujuk ke SWI-PRO-MET-201-012.

### Belum dimasukkan: Peroxide performance test (V1 10/01/2025, V2 14/01/2025)
Membandingkan H2O2 existing (isotank Evonik) dengan vendor lain (IBC) lewat respons DO pada feed leach, 4 botol E1, E2, R1, R2. V1: 500 mL feed, dosis 0.25 mL dua kali, DO diukur 10 menit setelah tiap dosis. V2 (menggantikan V1): 1 L feed, dosis sampai DO stabil di 15 dan 20 ppm, lalu hitung konsumsi. Tidak ada SWI yang cocok (203-012 adalah survey plant, bukan uji bench). Masalah di sumber: kekuatan H2O2 tidak disebut; kriteria "stabil" tidak didefinisikan; tidak ada bagian bahaya atau APD; peroksida ditambahkan ke feed leach bersianida; ejaan Evonic/Evonix.
Usul: satu SWI baru untuk uji vendor reagen (peroxide), atau digabung dengan uji NaCl vendor yang sekarang ada di 205-013 Part 1 sampai 3.

## Batch 4

| WI Martabe | SWI Anda | Hasil |
|---|---|---|
| Settling Test with Variance %Strength Flocc (22/03/2025) | 204-010 Flocculant Screening | Ditambah Part B |
| Adsorption Test Fresh Resin / "Adsorption Resin - 2 gpl" (09/01/2025) | 205-012 Resin Adsorption | Ditambah uji adsorpsi pada slurry CIL |
| Testwork QC Expired Reagent (28/03/2025) | 205-017 Standard Solutions | Ditambah Part B |
| Se dan Mn Removal dengan FeCl3 dan MnO2 (28/02/2025) | Tidak ada yang cocok | Belum dimasukkan |
| TDS Water vs Scaling Rate (03/03/2025) | Tidak ada yang cocok | Belum dimasukkan |

### 204-010 - Part B
Variasi kekuatan larutan flokulan 0.35, 0.40, 0.45, 0.50 persen, dosis 70, 80, 90, 100 g/t, 1 L tailing per silinder, 4 silinder per set (selisih berat di bawah 4 g), 8 kali pengadukan, level padatan menit 5 sampai 60 dan 24 serta 48 jam. SWI Anda menahan kekuatan tetap (Part A). Masalah di sumber: rumus volume flokulan memakai angka tetap 100 dan 0.5 (dibaca sebagai dosis dan kekuatan); susunan 4 kekuatan dan 4 dosis ke 4 silinder tidak dijelaskan; "60, 24 jam" ambigu; SOP pembuatan flokulan Martabe belum diterima. SWI Anda menulis silinder settling NOT PURCHASED; Martabe memakai gelas ukur biasa.

### 205-012 - adsorpsi resin fresh pada slurry CIL
10 g resin (2 g/L) dalam 5 L slurry, sampling 150 mL menit 2, 5, 10, 20, 40, 60. Masalah di sumber: "CIL 7" adalah titik Martabe (CIL Anda hanya 032-TK-002 sampai 006); tabel catatan mulai dari 4000 mL, bukan 5 L; beberapa baris di sumber diberi stabilo (tampak draft yang belum final). Slurry bersianida: saya rujuk ke SWI 201-004 dan kontrol HCN.

### 205-017 - Part B (QC reagen kedaluwarsa)
Re-kualifikasi phenolphthalein (visual, kelarutan di etanol 96 persen, uji NaOH dan asam; berlaku 1 tahun setelah uji) dan silica gel (oven 2 jam, kembali oranye). Ini bertentangan dengan Part A langkah 2 (hanya reagen dalam masa berlaku). Saya batasi ke indikator dan desikan saja, tidak untuk standar, reagen primer atau sianida, dan memerlukan persetujuan kebijakan. Suhu oven tidak disebut. Sumber merujuk DOC-IV-MET-CHH-SOP-00039 (Metallurgy Reagent Lifetime Management System), belum diterima.

### Belum dimasukkan: dua uji air (WPP)
- Se dan Mn removal: 70 persen air TSF + 30 persen larutan produk detox; Se dengan 16 g FeCl3 per 8 L pada pH 4.5 sampai 5 (sampel menit 5, 15, 30, 60, 120, duplo); Mn dengan 150 g MnO2 per 5 L pada pH 8 dan 9, udara 1.5 L/menit. Masalah di sumber: bagian pH 9 menulis "maintain pH 7.5-8.5" (salinan dari bagian pH 8; targetnya 8.7 sampai 9); "ulangi langkah 7 dan 8" menunjuk langkah yang salah. **Keselamatan:** sumber menurunkan pH ke 4.5 sampai 5 dengan asam sulfat pada campuran yang mengandung air TSF dan produk detox, yang bisa masih mengandung sianida: risiko HCN. Perlu syarat bebas sianida seperti di 205-006 Part B dan C.
- TDS vs scaling rate: 2.5 g "NaCO3" (mungkin Na2CO3) dalam 100 mL, 2 mL ke 300 mL masing-masing air (raw, filter, overflow WPP, permeat RO, permeat RO TDS buruk), aduk 10 menit, ukur turbidity.
Usul: satu SWI baru "WPP water treatment bench tests" untuk keduanya. 201-019 (sampling WTP) hanya sampling di plant dan tidak cocok.

## Catatan umum: nama titik dan lab Martabe
Beberapa WI Martabe memakai titik atau lab milik Martabe: SP09, MHR-1, TSF Toe, WPP, CIL 7, dan ITS sebagai lab eksternal. Di SWI saya mempertahankan nama itu dengan tanda [CONFIRM] di tempat yang penting. Sebelum SWI disetujui, ganti dengan titik sampel dan lab Mt. Morgan yang setara.

## Batch 5 (versi lain dari WI yang sudah ada)

| WI Martabe | SWI Anda | Hasil |
|---|---|---|
| Copper Adsorption / elution | 205-012 dan 205-013 | Varian ditambahkan; bagian elusi identik dengan 205-013 Part 2 |
| MHR1 Quick Lime dan Caustic V1 dan V1.2 | 205-006 | Ditambah Part D |
| Preconditioning Resin with Cu Variance V2 (07/02/2025) | 205-013 Part 1 | Ditambah dosis 70, 100, 125 kg/t |
| Se Mn Removal Jan 25 (27/01/2025) | Tidak ada yang cocok | Versi lebih awal dari WI Feb/Mar |

- **Copper Adsorption:** versi lebih awal dari uji adsorpsi pada slurry CIL: 4 L slurry dan 150 mL resin dari kolom (versi 2 g/L memakai 10 g resin dalam 5 L). Ini menjelaskan tabel catatan yang masih 4000 mL di versi 2 g/L; catatan itu saya perbarui. Bagian elusinya sama persis dengan WI NaCl vendor (NaCN 29.4 g, NaCl 36.2 g, 1 BV/jam, 3 jam), jadi 205-013 Part 2 kini punya dua sumber. H2SO4 5 persen (25.21 mL) dan NaOH 0.5 M (18 g dalam 900 mL) disiapkan tanpa tujuan yang disebut; H2SO4 1 persen tercantum di bahan tanpa langkah.
- **MHR-1 quicklime dan caustic (205-006 Part D):** 2 L per tangki, 0.5 g quicklime per penambahan, catat pH dan TDS, sampai pH 7, lalu ulangi dengan caustic. Data hasil di V1.2 menunjukkan pH awal 2.13 dan TDS sekitar 4800 (satuan tidak disebut), sehingga MHR-1 tampaknya air asam. Satu penambahan 0.5 g melompatkan pH dari 6.2 ke 9.58, jadi saya sarankan dosis lebih kecil mendekati pH 7. Masalah di sumber: V1.2 tidak punya langkah ulang dengan caustic padahal tabelnya ada (Test Kaustik 1 sampai 3); sampel 1 dan 2 saja vs 1, 2, 3; tabel memakai satuan mL/L dan mL/m3 untuk reagen padat; salah ketik di data ("50020", "05632").
- **Preconditioning V2 (205-013 Part 1):** 300 mL resin, Cu 70, 100, 125 kg/t = 136.4, 194.9, 243.6 mL CuSO4.7H2O dan 20.42, 29.17, 36.46 g NaCN per 4 L; resin dibagi dua: 150 mL ke copper loading test (Part 6) dan 150 mL ke lab untuk AAS di site dan ITS Jakarta. **Tidak konsisten dengan WI NaCl vendor:** 70 kg/t di V2 memakai CuSO4 dua kali lipat (136.4 vs 68.2 mL, resin juga dua kali lipat) tetapi NaCN 2.8 kali lipat (20.42 vs 7.29 g), jadi rasio NaCN dan CuSO4 berbeda (0.15 vs 0.107 g/mL). Perlu konfirmasi.
- **Se Mn Removal Jan 25:** versi awal dari WI Feb/Mar: 7 L dengan 35 g FeCl3 (5 g/L) vs 8 L dengan 16 g (2 g/L); Mn 4 L dengan 30 g MnO2 (7.5 g/L) vs 5 L dengan 150 g (30 g/L); versi Jan menjalankan pH 8 lalu pH 9 dalam satu uji (sampel menit 150), versi Feb/Mar memisahkannya. Risiko HCN pada pH 4.5 sampai 5 tetap berlaku. Tetap belum dimasukkan.

## Batch 6 (WI Martabe terkendali, bilingual)

Lima WI ini berformat dokumen terkendali Martabe (nomor DOC-3-..., versi 1.0, diterbitkan 25/12/2024 atau 25/01/2025, ada JSEA, bahaya, dan tabel kontrol risiko).

| WI Martabe | SWI Anda | Hasil |
|---|---|---|
| Carbon Analyser C2 Check (DOC-3-MET-PRS-WIN-00048-IE) | 201-005 Carbon concentration | Ditambah Part B |
| Cyclone Overflow Underflow Sampling (DOC-3-MET-PRS-00049-IE) | 203-003 Screen and cyclone survey | Ditambah Part B |
| Tailing Flocculant Solution Sampling (DOC-3-MET-PRS-WIN-00064-IE) | 201-017 Tails thickener sampling | Ditambah Part B |
| Electrowinning Survey (DOC-3-MET-PRS-WIN-00052-IE) | 201-013 Gold elution and EW sampling | Ditambah Part B |
| CV004 Moisture Sampling and Size Distribution (DOC-3-MET-PRS-00050-IE) | Tidak ada yang cocok | Belum dimasukkan |

### 201-005 - cek analyser karbon C2
Ambil 2 scoop per tangki dengan bucket sampler, ayak, cuci, ukur volume karbon di gelas ukur 100 mL, bandingkan dengan pembacaan analyser C2; di luar toleransi: ambil ulang 3 kali, atur, lalu kalibrasi. Masalah: tidak ada analyser C2 di SWI Anda (perlu dikonfirmasi apakah terpasang). Rumus Martabe volume/(2 x scoop) berbeda dari rumus SWI Anda (SG 0.47 x volume / volume sampel); pembagian 2 tampak seperti densitas sekitar 0.5 g/mL dengan scoop 1 L, tetapi volume scoop tidak disebut. Toleransi 3 g/L (CIL 13 sampai 7) dan 1.5 g/L (CIL 1 dan 2) memakai penomoran tangki Martabe. Kontrol HCN Martabe (monitor tetap, probe pH, pH di atas 10.5) sama dengan SWI Anda.

### 203-003 - sampling siklon
Sampling manual overflow dan underflow siklon ball mill dan VertiMill: bekerja di ketinggian dengan body harness, 5 cuplikan, satu kali tuang untuk Marcy scale, Tyvek untuk VertiMill, saklar mode open atau close pada underflow VertiMill. Masalah: ditulis untuk ball mill dan VertiMill Martabe, sedangkan pabrik Anda memakai IsaMill; titik jangkar harness dan fungsi saklar open atau close tidak dijelaskan. Baris hazard baru untuk kerja di ketinggian.

### 201-017 - sampling larutan flokulan
Tabung sampling di area pencampuran flokulan, buka valve kontrol pada jalur dengan pompa menyala, isi tabung, isi botol, kosongkan dengan menutup valve feed dan kontrol bersamaan. Hazard: kontak flokulan, lantai licin, titik jepit valve, jangan sampling saat ada pengangkatan flokulan. Cocok sebagai pendukung 204-010 (kekuatan larutan flokulan).

### 201-013 - survey electrowinning
Sampel barren eluate tiap jam, tiap train punya titik sampel sendiri, drain sekitar 1 menit, botol 250 mL terang dan gelap, satu kaustik di botol gelap, kirim untuk Au, Ag, Cu dan free cyanide (estimasi NaCN 3000 ppm). Masalah: sumber meletakkan botol plastik di lantai, sedangkan SWI Anda mensyaratkan botol tahan panas dan sampel didinginkan sebelum pH atau titrasi; saya pertahankan kontrol SWI Anda. Jumlah dan tujuan kaustik tidak disebut. Lab tertulis Intertek (WI lain menulis ITS). Mendukung 203-008.

### Belum dimasukkan: CV004 (belt cut conveyor)
Pemotongan belt 3 m di CV004 di bawah kamera Visiorock, 25 ember 20 L, 3 sekop, isolasi dengan gembok dan tag, izin kerja dan izin ruang terbatas, lalu di lab: oven 105 derajat C minimal 24 jam untuk kadar air dan ayakan 25.4 sampai 1.2 cm. Tidak ada SWI conveyor di set Anda. Ini pekerjaan kritis keselamatan (isolasi, tidak sendirian di atas conveyor, ruang terbatas) dan perlu SWI sendiri, misalnya "Feed conveyor belt-cut sampling". Bagian lab bisa memperkaya 204-006 dan 204-002. Pastikan ada conveyor yang setara di pabrik Anda. Sumber membatasi ember maksimal 10 kg dan tidak lebih dari setengah penuh (di bagian lain tertulis 66 persen), jadi angka itu tidak konsisten.

## Batch 7 (WI Martabe terkendali, bilingual)

| WI Martabe | SWI Anda | Hasil |
|---|---|---|
| Operate DO Meter Portable (DOC-3-MET-PRS-WIN-00055-IE) | 206-004 pH, DO and conductivity calibration | Ditambah Part B |
| Elution Survey (DOC-3-MET-PRS-WIN-00053-IE) | 201-013 Gold elution and EW sampling | Ditambah Part C |
| Pebble Crusher Product Sampling and Sizing (DOC-3-MET-PRS-WIN-00056) | Tidak ada yang cocok | Belum dimasukkan |
| Refill Eyewash (DOC-3-MET-PRS-WIN-00057-IE) | Tidak ada yang cocok | Belum dimasukkan |
| Manual Handling by Bucket or Another Container (DOC-3-MET-PRS-WIN-00054-IE) | Baris hazard di banyak SWI | Belum dimasukkan, perlu keputusan |

### 206-004 - DO meter portabel
Kalibrasi di udara (nilai yang diizinkan 6 sampai 8), lalu ukur DO di tangki slurry dan catat di Daily Task Checklist. Masalah: ditulis untuk Oxyguard Handy Polaris, sedangkan SWI Anda mencantumkan Hanna HI9142, jadi langkah menu hanya berlaku untuk Oxyguard; satuan dan dasar nilai 6 sampai 8 (mg/L atau persen jenuh) tidak disebut.

### 201-013 - elution survey (Part C)
Sampel setelah basket strainer, pakai ember Marcy scale supaya tangan jauh dari larutan panas, biarkan dingin, tuang ke botol gelap dan terang; sampel pertama di 65 derajat C, kedua di 100 derajat C, lalu tiap 30 menit atau akhir tahap; bungkus plastik berlabel "sianida tinggi"; assay Au, Ag, Cu, free cyanide (NaCN sekitar 3000 ppm). **Keselamatan:** sumber menyuruh menuang sisa larutan ke lantai. Itu eluate panas bersianida, jadi langkah itu tidak saya bawa; diganti dengan "jangan dibuang ke lantai, kirim ke aliran limbah bersianida", ditandai [CONFIRM]. Lab tertulis ITS, perlu diganti lab Mt. Morgan.

### Belum dimasukkan
- **Pebble crusher:** sampling produk pebble crusher dengan sample cutter di tiga posisi, ayak 0.6 sampai 90 mm, catat jam sampling (untuk daya pebble, kecepatan feeder, TPH CV-003). Tidak ada pebble crusher atau SWI-nya di set Anda; konfirmasi apakah pabrik Anda punya pebble crusher.
- **Refill eyewash:** pengisian ulang eyewash portabel (Honeywell) di Metlab dan RO plant: bilas, kuras, isi air potable, catat di logsheet inspeksi. Hampir semua SWI Anda mensyaratkan eyewash "proven flowing" di bagian Before You Start, tetapi tidak ada SWI untuk inspeksi dan pengisian ulangnya. Saran: SWI baru "Eyewash and safety shower inspection and refill".
- **Manual handling:** Martabe menetapkan batas angka: ember 20 L tidak lebih dari setengah, atau sekitar 10 kg; kontak tiga titik di tangga; sarung tangan 3M atau nitril; pelatihan pengangkatan manual. Sekitar 35 SWI Anda menulis "site manual handling limit" tanpa angka. Usul: tetapkan angka batas site (misalnya 10 kg bila sesuai) lalu saya perbarui baris itu di semua SWI. Catatan: WI CV004 memberi batas berbeda (66 persen), jadi angka Martabe sendiri tidak konsisten.

## Batch 8 (WI Martabe terkendali, bilingual)

| WI Martabe | SWI Anda | Hasil |
|---|---|---|
| Sampling Density Gauge Slurry (DOC-3-MET-PRS-WIN-00060) | 203-002 Flow, density and tonnage verification | Ditambah Part B |
| Sampling Feed, Product and Final Product of Lime Slaker (DOC-3-MET-PRS-WIN-00059-IE) | 201-020 Reagent solution strength sampling | Ditambah Part B |
| Sampling Hydrated Lime (DOC-3-MET-PRS-WIN-00061-IE) | 201-020 | Ditambah Part C |
| Acid Wash Survey (DOC-3-MET-PMC-WIN-00107-IE) | 201-013 Gold elution and EW sampling | Ditambah Part D |
| Sampling Carbon Launder CIL (DOC-3-MET-PRS-WIN-00058-IE) | 201-004 CIL sampling round | Ditambah Part B |

- **203-002 (density gauge):** empat titik Martabe (leach feed box, siklon ball mill, siklon VertiMill, tailing discharge transfer di filtration plant), komposit potongan (15 potongan di 3 ember untuk leach feed, 9 potongan lainnya), pengecekan skala pulp density dengan air (harus 1.00), saring bertekanan, oven, timbang kering, hitung persen padatan; jika pembacaan PCS berbeda lebih dari 3 persen dari hasil lab, kalibrasi oleh Maintenance Electrical (sama dengan prinsip SWI Anda: jangan disetel sendiri). Masalah: untuk sampling leach feed sumber meminta control room mematikan pompa barren 176 dan 177 serta sump pump 178, 179, 038, 108 (sianida), 163 (kaustik) dan 053 tanpa menyebut alasan. Daftar itu milik Martabe, jadi harus dipetakan dan perlu izin Shift Supervisor; rumus persen padatan tidak ada di teks sumber. Sampling di filtration plant dilakukan dua orang.
- **201-020 Part B (lime slaker):** sampel dengan sampler dari hopper umpan, hopper produk dan tangki kapur, ke kantong plastik kering. Sumber tidak menyebut uji untuk sampel dan tidak menyebut seberapa panas lumpur kapur.
- **201-020 Part C (hydrated lime):** sampel dari bag dengan scoop minimal 10 cm di bawah permukaan, ID di kantong, ikat tangan dan kabel tis, dua lapis; kirim ke lab. Masalah: hasil dicatat sebagai "persen padatan" untuk kapur kering, tidak biasa; uji yang dimaksud perlu dikonfirmasi (ketersediaan kapur ada di 205-005). Forklift hanya oleh operator berwenang.
- **201-013 Part D (acid wash):** sampel saat tahap pembilasan dari tiap bucket strainer dan tangki campur HCl, kuras 30 detik, ukur pH. Sumber tidak memberi pH akhir pembilasan atau kekuatan asam; asam dan sianida: pastikan tidak ada sianida di jalur selama pembilasan.
- **201-004 Part B (karbon di launder):** 5 sendokan sampler di strainer karbon, cuci, bungkus kertas saring, oven di rak paling bawah, timbang. Sumber tidak menyebut tujuan, volume sampler, suhu dan lama oven, jadi perhitungan konsentrasi tidak bisa ditulis.

## Batch 9 (WI Martabe terkendali, bilingual)

| WI Martabe | SWI Anda | Hasil |
|---|---|---|
| Check pH Tailing Slurry Solution (DOC-3-MET-PMC-WIN-00106-IE) | 201-022 Online analyser verification | Ditambah Part C |
| Sampling Raw and Filtrat Water (DOC-3-MET-PRS-WIN-00063-IE) | 201-019 Water treatment plant sampling | Ditambah Part B (teknik saja); 201-019 tetap NOT FOR USE |
| Backwash MMF RO Plant (DOC-3-MET-PMS-WIN-00108-IE) | Tidak ada yang cocok | Belum dimasukkan |
| Check Flow Antiscalant Process (DOC-3-MET-PMC-WIN-00112-IE) | Tidak ada yang cocok | Belum dimasukkan |
| Bullion Weighing (DOC-3-MET-PMC-WIN-00110-IE) | Tidak ada yang cocok | Belum dimasukkan |

- **201-022 Part C (pH tailing):** probe pH tailing dibersihkan, dicelup ke buffer pH 7 lalu pH 10 dalam tutup botol, dibaca di panel; harus 7 dan 10 atau pembulatannya (contoh 9.8); jika tidak cocok, probe diperbaiki. Masalah: toleransi hanya lewat contoh (sekitar 0.2 pH), sementara batas keselamatan sianida pH di atas 10.5; buffer hanya 7 dan 10 (SWI 206-004 memakai 4, 7, 10).
- **201-019 Part B (air baku dan filtrat):** teknik sampling di water filter potabel: berdiri tidak di bawah titik, buka keran pelan, tunggu 30 sampai 60 detik, bilas botol, minimal 900 mL, kirim ke lab. 201-019 mensyaratkan feed dan discharge WTP No. 1 dan 2 yang membawa kewajiban izin lingkungan, sedangkan sumber ini hanya filter air potabel; maka hanya saya tambahkan sebagai referensi teknik dan banner NOT FOR USE dipertahankan.
- **Backwash MMF RO plant:** backwash MMF 1 dan 2 masing-masing 30 menit, bilas 30 menit, nomor valve Martabe (9407 sampai 9411 dan 9507 sampai 9511) dioperasikan oleh control room. Nomor valve milik Martabe dan tidak bisa dipakai di pabrik Anda.
- **Cek flow antiscalant:** ukur aliran dari tabung dengan stopwatch 1 menit, bandingkan dengan panel (seharusnya 5.6 L/jam), minta control room menyesuaikan kecepatan pompa; catat di formulir.
- **Penimbangan bullion:** kalibrasi timbangan A&D 3P-30K dan Sartorius dengan anak timbang 20 kg, timbang tiap batang, segel plastik dan kabel logam, shipment maksimal 1000 kg bruto (kotak sekitar 715 g), serah terima sampel dengan tanda tangan kedua pihak (chain of custody) antara goldroom, metalurgis dan lab ITS. Bahaya yang disebut hanya merkuri. Ini pekerjaan kritis keamanan dan akuntansi; tidak ada SWI goldroom di set Anda.
- Usul pengelompokan SWI baru: "RO plant operations" (backwash, antiscalant, eyewash di RO plant) dan "Bullion weighing and chain of custody".

## Batch 10 (WI Martabe terkendali, bilingual)

| WI Martabe | SWI Anda | Hasil |
|---|---|---|
| Effective Treatment Dosage (DOC-3-MET-PMC-WIN-00122-IE) | 204-010 Flocculant screening | Ditambah Part C |
| Dosing Pump Grundfos DDA Calibration (DOC-3-MET-PMC-WIN-00120-IE) | 205-013 Resin elution | Ditambah Part 7 |
| Cyanide Measurement by AgNO3 Titration (DOC-3-MET-PMC-WIN-00115-IE) | 205-001 Free cyanide titration | Hanya catatan perbandingan; SWI Anda lebih lengkap |
| Flocculant Screw Feeder Calibration (DOC-3-MET-PMC-WIN-00123-IE) | Tidak ada yang cocok | Belum dimasukkan |
| SAG Mill Reject Ball Survey (DOC-3-MET-PMC-WIN-00096-IE) | Tidak ada yang cocok | Belum dimasukkan |

- **204-010 Part C (ETD):** 276 g slurry sebanyak 12 sampel diaduk dengan pengaduk besi, uji flokulan, ukur turbiditas air dari penyaringan sieve dengan turbidity meter dan kuvet. Ujinya sendiri ada di "WI Flocculant testwork on tailing using sieve" yang belum diterima; dasar 276 g dan 12 sampel tidak dijelaskan.
- **205-013 Part 7 (pompa DDA):** kalibrasi pompa dosing Grundfos DDA dengan air: 100 persen, menu kalibrasi, tampung volume, samakan dengan panel (contoh 50 mL), ulangi bila beda. Ini menutup rujukan "WI Kalibrasi Pompa DDA" di WI Copper Loading dan Copper Ads. Perlu dikonfirmasi apakah pompa juga diperiksa pada laju uji (150 mL/jam dan 300 mL/jam), karena kalibrasi sumber memakai air.
- **205-001:** titrasi Martabe (buret digital, 10 mL dengan jarum suntik, 3 tetes rhodanine, titik akhir "merah muda") lebih sederhana daripada SWI Anda (fume cupboard, penyaringan, kondisioning buret, titik akhir salmon pink 30 detik, duplikat dan standar). SWI Anda dipertahankan; hanya dua hal diambil: cek buret digital terbaca 0.00 dan cek tanggal kedaluwarsa AgNO3.
- **Flocculant screw feeder (belum dimasukkan):** cek konsentrasi flokulan dengan mengambil bubuk dari screw feeder 10 detik tiga kali, timbang; jika beda dari target, kalibrasi lewat menu "CPS system setup" dengan mode manual, kata sandi, "Enable screw feeder calibration", masukkan laju umpan rata-rata ke Citect. Ini perubahan setpoint sistem kontrol Martabe (CPS dan Citect); pabrik Anda memakai plant flokulan Roytec, jadi layar dan sistemnya harus dipetakan. Bukan sampling; perlu SWI sendiri atau masuk ke operasi flokulan.
- **SAG mill reject ball survey (belum dimasukkan):** ambil dua bola reject dengan cutter di SAG discharge screen, timbang, ukur diameter di sumbu x, y, z dengan kaliper. Pabrik Anda memakai IsaMill dan tidak ada SAG mill di set; hazard bola baja pecah di bunker. Digabung dengan pebble crusher bila Anda punya SAG.

## Batch 11 (WI Martabe terkendali, bilingual)

| WI Martabe | SWI Anda | Hasil |
|---|---|---|
| Leach Analyzer Calibration (DOC-3-MET-PMC-WIN-00126-IE) | 207-008 Cyanide analyser calibration | Placeholder diganti metode (draft) |
| Intertank Screen Inspection (DOC-3-MET-PMC-WIN-00125-IE) | 203-010 Interstage and safety screen check | Ditambah Part B |
| Measure Viscosity Using Brookfield DV2TLV (DOC-3-MET-PMC-WIN-00128-IE) | 204-008 Slurry viscosity | Ditambah Part B |
| Operating Anemometer GM8902 (DOC-3-MET-PMC-WIN-00130-IE) | 206-002 Fume cupboard operation | Ditambah Part B |
| Flocculant Testwork on Tailing Using Sieve (DOC-3-MET-PMC-WIN-00124-IE) | 204-010 Flocculant screening | Ditambah Part D; melengkapi Part C (ETD) |

- **207-008 (kalibrasi analyser sianida):** ini sumber yang mengisi placeholder yang tertahan karena data kalibrasi vendor belum ada. Metode: tiga standar NaCN 2 L, titrasi manual 3 kali tiap standar, kalibrasi 3 titik lewat calibration wizard (WAD tidak dicentang, flush antar standar 4, antar sampel 1, sample times 4), terima jika R kuadrat di atas 0.99 dan catat M dan C, verifikasi selisih otomatis vs manual di bawah plus minus 10 ppm. Masalah di sumber: teks Indonesia menulis standar 250, 500, 700 ppm, teks Inggris 30, 250, 500 ppm, dan "205" muncul sekali; pH analyser 9 sampai 11 melampaui batas 10.5 keselamatan sianida; panduan troubleshooting adalah lampiran yang tidak ada; kalibrasi WAD tidak tercakup, jadi data vendor Cynoprobe v3 WAD tetap kurang. Banner menjadi DRAFT FOR REVIEW. Sumber merujuk probe sianida satu leach hut Martabe; konfirmasi untuk 032-CA-001 dan 051-CA-002.
- **203-010 (intertank screen):** inspeksi bila karbon di launder di atas 0.1 g/L, atau tiap 2 bulan bila screen lebih dari 6 bulan; angkat dengan gantry crane (operator berlisensi), cuci, ukur celah dengan feeler gauge dari atas, tengah, bawah, ganti bila celah di atas 1.4 mm. **Keselamatan:** sumber menyebut bahaya (slurry bersianida, beban di atas badan, feeler gauge, HCN) tetapi tidak memberi kontrol; kontrol saya tambahkan dan ditandai untuk JSEA. Konfirmasi apakah ada intertank screen di dalam tangki di pabrik Anda dan batas 1.4 mm terhadap register aperture. Terhubung ke 201-004 Part B (karbon di launder).
- **204-008 (viskometer Brookfield):** autozero tanpa spindle, spindle dan kecepatan yang sama untuk semua sampel, 20 rpm untuk harian, torsi 10 sampai 90 persen. Sumber hanya satu titik, sedangkan Part A mengharuskan deret shear rate, densitas dan suhu; diterapkan di atasnya.
- **206-002 (anemometer):** ukur kecepatan udara di tengah bukaan sash yang terbuka penuh, 20 bacaan per detik, tanpa pekerjaan di dalam fume cupboard. Tidak ada nilai penerimaan; ambil dari spesifikasi fume cupboard.
- **204-010 Part D (flokulan dengan sieve):** ini uji yang dirujuk Part C (ETD). Rumus dosis dikonfirmasi: mL = dosis (g/t) x massa slurry (g) x persen padatan / (kekuatan persen x 1.000.000); contoh 60 g/t, 400 g, 46 persen, 0.4 persen = 2.76 mL; ini juga menjelaskan angka 100 dan 0.5 di Part B (contoh dosis 100 g/t dan larutan 0.5 persen). Aseton 3 mL ditambah air 97 mL untuk 0.5 g flokulan; sampling bag flokulan dari satu tumpukan; dosis 30, 40, 60, 80, 120 g/t. **Keselamatan:** tailing bersianida tetapi sumber tidak mencantumkan kontrol HCN; saya tambahkan peringatan dan rujukan ke 201-008 dan 201-017. Titik sampel (safety carbon screen distributor) dan pompa sump PU-372 milik Martabe.

## Batch 12 (WI Martabe, sebagian terkendali)

| WI Martabe | SWI Anda | Hasil |
|---|---|---|
| ReCYN Plant Caustic Strength Measurement (DOC-3-MET-PMC-WIN-00088-IE) | 201-020 dan 205-002 | 201-020 Part D (sampling) dan 205-002 Part B (hitungan H2SO4) |
| Replace Filter Sock (DOC-3-MET-PMC-WIN-00091) | 207-007 Cyanide analyser daily operation | Ditambah Part B (draft); 207-007 tetap NOT FOR USE |
| Scale Coupon Measurement (DOC-3-MET-PMC-WIN-00099-IE) | Tidak ada yang cocok | Belum dimasukkan |
| RO Antiscalant Dosage Check (DOC-3-MET-PMC-WIN-00092-IE) | Tidak ada yang cocok | Belum dimasukkan |
| Replace Cartridge RO II 55 M3 (DOC-3-MET-PMC-WIN-00090-IE) | Tidak ada yang cocok | Belum dimasukkan |

- **201-020 Part D dan 205-002 Part B (kaustik ReCYN):** sampel dari pipa drain pompa kaustik ReCYN ke botol 100 mL; titrasi dengan H2SO4 (rasio 2:1): [NaOH] = 2 x [H2SO4] x V(H2SO4) / V(sampel). SWI 205-002 memakai HCl (rasio 1:1). Persiapan asam sulfat dan teknik titrasi ada di dua WI Martabe lain yang belum diterima. Konfirmasi bahwa pipa drain pompa membawa larutan encer (SWI Anda: jangan sampling dari tangki pekat).
- **207-007 Part B (filter sock):** matikan analyser dan pompa HCl, lepas pipa filter probe, cuci dan potong filter sock lama, bilas jalur filtrat dengan memindah jalur pompa ke ember air, pasang filter sock baru dengan silikon dan klem 60 mm, nyalakan analyser. Sumber meminta alarm HCN di bawah 10 ppm; SWI Anda 5 ppm (alarm) dan 10 ppm (high-high), jadi saya terapkan 5 ppm. Langkah mengacu pada foto yang tidak ikut, dan perangkat HCl pada analyser Martabe belum tentu ada di Cynoprobe Anda.
- **Belum dimasukkan:** pengukuran scale coupon (lepas kupon dari pipa dengan dua kunci inggris, rendam HCl 3 persen, timbang 4 desimal), cek dosis antiscalant RO (gelas ukur 100 mL, 1 menit, sesuaikan kecepatan), ganti cartridge RO II 55 m3 (LOTO, valve 112 dan 113). Semua untuk RO plant dan sistem air Martabe; bergabung dengan kelompok "RO plant operations" (backwash, antiscalant, eyewash di RO plant). Catatan: WI cek dosis antiscalant ini berbeda dari WI "Check Flow Antiscalant" (aliran dengan stopwatch dan nilai 5.6 L/jam); keduanya metode berbeda untuk hal yang sama.

## Batch 13

| WI Martabe | SWI Anda | Hasil |
|---|---|---|
| Operating pH Cube Meter / TPS cube (DOC-3-MET-PMC-WIN-00089-IE) | 206-004 pH, DO and conductivity calibration | Ditambah Part C |
| Scale Coupon in Elution, Raw Water, Cooling Water and Process Water Area (DOC-3-MET-PMC-WIN-00098-IE) | Tidak ada yang cocok | Belum dimasukkan |
| SAG Mill Sound Survey (DOC-3-MET-PMC-WIN-00097-IE) | Tidak ada yang cocok | Belum dimasukkan |
| Replace Filter Sock | Sudah ada di batch 12 | Duplikat, teks identik |
| RO Antiscalant Dosage Check | Sudah ada di batch 12 | Duplikat, teks identik |

- **206-004 Part C (TPS cube):** mode pH, pasang sensor pH dan suhu, lepas tutup probe, bilas, celup, tunggu stabil, catat; simpan probe dalam air; sampel ke jeriken limbah B3. Kalibrasinya ada di WI Martabe yang belum diterima (juga dirujuk Acid Wash Survey, 201-013 Part D). Meter TPS cube tidak ada di daftar alat 206-004 Anda.
- **Scale coupon di air elusi, air baku, air pendingin, air proses dan ReCYN:** versi yang lebih luas dari WI scale coupon batch 12. Beda penting: elusi harus berhenti saat kupon diganti (larutan panas, sianida dan kaustik); oven minimal 6 jam pada 80 derajat C (batch 12 hanya 2 jam, suhu tidak disebut); kupon dibersihkan dengan asam asetat 100 mL selama 1 hari (batch 12 memakai HCl 3 persen sampai bersih). Pembersih asam berbeda di dua WI yang sama-sama membahas kupon; konfirmasi mana yang dipakai. Belum dimasukkan karena tidak ada SWI sistem air yang cocok.
- **SAG mill sound survey:** sound level meter B&K 2240 mode LAeq di atas grit mesh mikrofon audio mill, 5 pengukuran tiap 2 menit. Tidak ada SAG mill di set Anda.
- Dua file lain adalah duplikat WI di batch 12 (teks identik), tidak ada isi baru.

## Batch 14

| WI Martabe | SWI Anda | Hasil |
|---|---|---|
| Detox Analyser Calibration (DOC-3-MET-PMC-WIN-00117-IE) | 207-008 Cyanide analyser calibration | Ditambah Part B; leach menjadi Part A |
| A&D MS-70 Moisture Analyzer Calibration (DOC-3-MET-PMC-WIN-00121-IE) | 204-006 Moisture content | Ditambah Part B |
| Weighing Verti Mill and SAG Mill Liner (DOC-3-MET-PMC-WIN-00105-IE) | Tidak ada yang cocok | Belum dimasukkan |
| SAG Mill Inspection (DOC-3-MET-PMC-WIN-00095-IE) | Tidak ada yang cocok | Belum dimasukkan |
| Operation and Maintenance of Sparing System | Tidak ada yang cocok | Belum dimasukkan |

- **207-008 Part B (analyser detox):** metode kalibrasi Cynoprobe yang sama dengan Part A, tetapi standar 30, 250 dan 500 ppm (daftar bahan menulis 30, 125, 250), cek HMI pH 6 sampai 9 (leach 9 sampai 11), pengukuran otomatis dan manual dicatat sebelum kalibrasi. Ini menjelaskan kebingungan standar di Part A: salinan Inggris WI leach (30, 250, 500 ppm) rupanya diambil dari WI detox; standar leach yang benar menurut teks Indonesia adalah 250, 500, 700 ppm. Catatan Part A sudah diperbarui.
- **204-006 Part B (moisture analyser):** verifikasi bobot dengan anak timbangan 50 g (49.995 sampai 50.000), kalibrasi dengan 20 g bila di luar; verifikasi persen kelembapan dengan natrium tartrat dihidrat 5 g, metode MID pada 160 derajat C. Sumber tidak memberi nilai penerimaan; natrium tartrat dihidrat berisi sekitar 15.66 persen air secara teoretis, dipakai sebagai acuan. Oven di Part A tetap metode acuan.
- **Penimbangan liner VertiMill dan SAG mill:** Franna crane, rigger, timbangan 15 ton, rantai, pengangkatan; hazard kendaraan bergerak dan beban menggantung. Tidak ada mill liner di set Anda (IsaMill).
- **SAG mill inspection:** masuk ke dalam mill (ruang terbatas, isolasi, uji gas, sentry): ukur grate dengan kaliper, isi mill dengan alat laser, keluar lewat feed trunnion. Pekerjaan kritis keselamatan tertinggi di antara semua WI Martabe; bila pabrik Anda punya mill besar yang perlu diinspeksi, butuh SWI dan JSEA tersendiri.
- **Sparing system:** pemantauan pH dan TSS efluen WPP secara kontinu untuk regulator (KLHK): pembersihan oleh operasional, verifikasi pH oleh Maintenance Electrical dengan buffer 7.00 dan 10.00, kalibrasi tahunan oleh pihak resmi dan lab yang ditunjuk. Dokumennya masih berkop templat ("[Intranet Code and Numbering]"), jadi draft belum terbit. Terkait dengan 201-019 (discharge WTP) dan kewajiban izin lingkungan pabrik Anda; regulatornya akan berbeda.

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
