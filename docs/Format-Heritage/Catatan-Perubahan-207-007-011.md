# Catatan perubahan: SWI-PRO-MET-207-007 sampai 207-011 (cyanide analyser online) ke format Heritage

## Fakta plant (dari pengguna, 2026-10-06)
- Mt. Morgan **punya cyanide analyser online** (Molycop Cynoprobe, 032-CA-001 dan 051-CA-002) yang membaca **pH, free cyanide, dan WAD cyanide**.
- **Tidak ada analyser lain.** Selain cyanide analyser, yang ada hanya density meter.
- **Tidak ada sirkuit detox.** Setelah CIL langsung sirkuit ReCYN.

## Keputusan per SWI
| SWI | Judul | Status | Halaman |
|---|---|---|---|
| 207-007 | Daily Operation and Check | Operasi harian NOT FOR USE; ganti filter sock (Martabe) DRAFT | 7 |
| 207-008 | Calibration and Standardisation | DRAFT - kalibrasi leach analyser Martabe untuk 032-CA-001; kalibrasi detox Martabe untuk analyser ReCYN tailing 051-CA-002 | 9 |
| 207-009 | Electrode Replacement and Conditioning | NOT FOR USE (manual Cynoprobe) | 6 |
| 207-010 | Sample and Booster Pump Service | NOT FOR USE (manual Vender Dura 10) | 6 |
| 207-011 | Leak Detector and High Level Alarm | NOT FOR USE (dokumen vendor); respons sementara dipertahankan | 6 |

## 207-007
- Step: Pre-start (Take 5, siapkan filter sock dan alat), Status - Not for Use (operasi harian), Filter Sock Replacement (Martabe, 8 bullet), Completion.
- CAUTION: kerja hanya tanpa alarm HCN (alarm 5 ppm, high-high 10 ppm; sumber Martabe memakai di bawah 10 ppm), monitor HCN menyala, tidak sendirian di enclosure.
- Open items: filter probe dan suku cadang yang setara, ada tidaknya dosing HCl di analyser Mt. Morgan, susunan jalur flush (foto sumber tidak ada), frekuensi.

## 207-008
**Keputusan (revisi):** "detox analyser" di sumber Martabe dipetakan ke **analyser ReCYN tailing 051-CA-002**. Kalibrasi detox tidak dibuang, tetapi menjadi Step 6 untuk 051-CA-002. Kalibrasi leach analyser (Step 2-5) berlaku untuk 032-CA-001.
- Step: Pre-start (Take 5, elektrolit KCl per SOP-0053), Standards and Titration - 032-CA-001, Calibration Wizard - 032-CA-001, Acceptance and Verification - 032-CA-001, Standards Clean-up - 032-CA-001, ReCYN Tailing Analyser Calibration - 051-CA-002, Completion.
- Hazard "[JSEA to confirm] tangan terjepit di tutup analyser detox" dipertahankan dengan nama alat diganti "ReCYN tailing analyser (051-CA-002)". Nama logsheet dan form Martabe ("Detox Analyzer Calibration") dipertahankan sebagai nama sumber.
- Diubah: "latex gloves" saat memegang standar sianida diganti sarung tangan tahan bahan kimia (standar APD SWI). Lab ITS diganti Mt. Morgan laboratory.
- CAUTION: pH di bawah 10,5 melepas HCN (Step 4 dan 6); jauhi titik jepit tutup analyser (Step 6).
- Open items (6): kalibrasi WAD (data Cynoprobe v3 WAD belum ada), standar 032-CA-001 (250/500/700 vs 30/250/500 ppm), standar 051-CA-002 (30/125/250 vs 30/250/500 ppm), rentang pH verifikasi (9-11 leach, 6-9 detox) di bawah 10,5 terutama untuk ReCYN tailing, panduan troubleshooting belum diterima, titik buang standar dan folder catatan.
- Deskripsi 051-CA-002 di 207-007 sampai 011 diseragamkan menjadi "ReCYN tailing online cyanide analyser (pH, free cyanide and WAD cyanide)".

## 207-009, 010, 011
Tetap NOT FOR USE. Banner menyebut blocker spesifik (bukan "see the folder README"). 207-011 mempertahankan instruksi sementara: perlakukan alarm bocor atau level tinggi sebagai pelepasan sianida, jangan buka enclosure, evakuasi, laporkan ke control room (juga CAUTION).

## Audit
Diaudit terhadap SWI sebelum konversi. Setelah revisi, semua langkah Part B lama ada di Step 6 207-008. Yang tidak cocok utuh hanya tanda [M]/[CONFIRM] yang menjadi Draft dan Open items, referensi yang dipecah, dan kalimat "see the folder README" (diganti blocker spesifik).

Hazard a), b), c), CAUTION, dan emergency ditulis baru dari hazard dokumen. Mohon dicek HSE.
