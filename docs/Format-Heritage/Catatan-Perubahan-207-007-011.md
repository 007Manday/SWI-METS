# Catatan perubahan: SWI-PRO-MET-207-007 sampai 207-011 (cyanide analyser online) ke format Heritage

## Fakta plant (dari pengguna, 2026-10-06)
- Mt. Morgan **punya cyanide analyser online** (Molycop Cynoprobe, 032-CA-001 dan 051-CA-002) yang membaca **pH, free cyanide, dan WAD cyanide**.
- **Tidak ada analyser lain.** Selain cyanide analyser, yang ada hanya density meter.
- **Tidak ada sirkuit detox.** Setelah CIL langsung sirkuit ReCYN.

## Keputusan per SWI
| SWI | Judul | Status | Halaman |
|---|---|---|---|
| 207-007 | Daily Operation and Check | Operasi harian NOT FOR USE; ganti filter sock (Martabe) DRAFT | 7 |
| 207-008 | Calibration and Standardisation | DRAFT - kalibrasi leach analyser Martabe untuk kedua analyser; kalibrasi detox dibuang | 8 |
| 207-009 | Electrode Replacement and Conditioning | NOT FOR USE (manual Cynoprobe) | 6 |
| 207-010 | Sample and Booster Pump Service | NOT FOR USE (manual Vender Dura 10) | 6 |
| 207-011 | Leak Detector and High Level Alarm | NOT FOR USE (dokumen vendor); respons sementara dipertahankan | 6 |

## 207-007
- Step: Pre-start (Take 5, siapkan filter sock dan alat), Status - Not for Use (operasi harian), Filter Sock Replacement (Martabe, 8 bullet), Completion.
- CAUTION: kerja hanya tanpa alarm HCN (alarm 5 ppm, high-high 10 ppm; sumber Martabe memakai di bawah 10 ppm), monitor HCN menyala, tidak sendirian di enclosure.
- Open items: filter probe dan suku cadang yang setara, ada tidaknya dosing HCl di analyser Mt. Morgan, susunan jalur flush (foto sumber tidak ada), frekuensi.

## 207-008
- Step: Pre-start (Take 5, elektrolit KCl per SOP-0053), Standards and Titration, Calibration Wizard, Acceptance and Verification, Standards Clean-up, Completion.
- Dibuang: Part B Detox Analyser Calibration, hazard "[JSEA to confirm] tangan terjepit di tutup analyser detox", standar detox 30/250/500 ppm, rujukan WI Martabe 00117.
- Diubah: "latex gloves" saat memegang standar sianida diganti sarung tangan tahan bahan kimia (standar APD SWI). Lab ITS diganti Mt. Morgan laboratory.
- CAUTION: larutan sianida di bawah pH 10,5 melepas HCN; laporkan pembacaan pH analyser di bawah 10,5.
- Open items (5): kalibrasi WAD (sumber tidak mencentang WAD, padahal analyser Mt. Morgan membaca WAD; data kalibrasi Cynoprobe v3 WAD belum ada), nilai standar (250/500/700 vs 30/250/500 ppm) dan rentang untuk 051-CA-002 di ReCYN, rentang pH 9-11 di bawah batas 10,5, panduan troubleshooting belum diterima, titik buang standar dan folder catatan.

## 207-009, 010, 011
Tetap NOT FOR USE. Banner menyebut blocker spesifik (bukan "see the folder README"). 207-011 mempertahankan instruksi sementara: perlakukan alarm bocor atau level tinggi sebagai pelepasan sianida, jangan buka enclosure, evakuasi, laporkan ke control room (juga CAUTION).

## Audit
Diaudit terhadap SWI sebelum konversi. Yang hilang hanya Part B detox (keputusan) dan kalimat "see the folder README" (diganti blocker spesifik).

Hazard a), b), c), CAUTION, dan emergency ditulis baru dari hazard dokumen. Mohon dicek HSE.
