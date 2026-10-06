# Catatan perubahan: seri 205 batch 1 (12 SWI tanpa padanan Martabe) ke format Heritage

SWI: 205-003, 004, 005, 007, 008, 009, 010, 011, 014, 016, 018, 019. Tidak ada padanan Martabe, jadi isi SWI dipertahankan dan hanya formatnya yang diubah. Tujuh SWI lain (001, 002, 006, 012, 013, 015, 017) punya tambahan Martabe dan dibahas dulu sebelum dikonversi.

## Perubahan umum
- Area: "205 Met Lab - Chemical and Leach Testwork". Parent procedure: HM-PRC-VXX-PRO209 - Metallurgical Laboratory Chemical and Leach Testwork.
- APD sama dengan seri 206: satu baris "Chemical resistant suit, acid-resistant and nitrile rubber gloves, and apron", face shield di baris goggles, monitor HCN dan gas mask.
- Pre-start dan Completion memakai kalimat baku seri lab: induksi site, kompetensi cyanide awareness, JSEA, dan pencatatan nilai di data sheet, register atau logbook.
- SWI safety-critical (003, 007, 008, 009) diberi pernyataan safety-critical dan bullet Pre-start "Cyanide work is not done alone."
- Baris Hazard/Control disalin apa adanya dari SWI lama. Hazard a), b), c), CAUTION dan tabel emergency ditulis dari hazard tersebut.
- Referensi dipindah ke tabel Referenced documents, dengan nomor dan judul di kolom terpisah.

## Per SWI
| SWI | Judul | Step (setelah Pre-start) | Catatan |
|---|---|---|---|
| 205-003 | Sulphuric Acid Strength Titration | Sampling and Dilution; Titration; Calculation and Reporting | Safety-critical. CAUTION: asam ke air, jangan sampling tangki pekat |
| 205-004 | Sodium Chloride (Chloride) Titration | Sample Preparation; Titration; ISE Channel and Standards | - |
| 205-005 | Lime Availability Test | Sampling; Slaking and Titration; Calculation and Reporting | CAUTION: quicklime panas saat slaking |
| 205-007 | Bottle Roll Leach Test - As-Received and Pulverised | Set-up and Charging; pH and Cyanide Addition; Rolling, Sampling and Results | Safety-critical. CAUTION: jangan tambah sianida di bawah pH 10,5; botol dibuka hanya di fume cupboard (7 halaman) |
| 205-008 | Extended and Diagnostic Leach Test | Extended Leach; Diagnostic Sequence; Assay and Deportment | Safety-critical. CAUTION: asam pada residu bersianida melepas HCN (7 halaman) |
| 205-009 | CIL/CIP Sequential Triple Contact Testwork | Pulp Preparation and First Contact; Second and Third Contacts; Assay and Calculation | Safety-critical. CAUTION: pulp pH 10,5 atau lebih sebelum dibuka |
| 205-010 | Carbon Adsorption Capacity and Isotherm Test | Solutions and Charging; Rolling to Equilibrium; Isotherm and Reporting | - |
| 205-011 | Carbon Activity and Ball-Pan Hardness Test | Carbon Activity; Ball-Pan Hardness; Calculation and Reporting | Pelindung telinga ditambahkan (hazard hearing damage, Ro-Tap dan ball-pan) |
| 205-014 | Resin Fouling, Osmotic Shock and Bead Integrity Assessment | Sampling and Washing; Bead Size and Integrity; Fouling Check and Reporting | Pelindung telinga ditambahkan (Ro-Tap). CAUTION: resin dicuci bebas sianida sebelum acid wash |
| 205-016 | Precipitate and Platelet Content Determination | Subsample and Drying; Platelet Content; Assay and Reporting | CAUTION H2S (dari hazard sodium hydrosulphide); emergency H2S |
| 205-018 | Automatic Titrator Operation and Method Set-Up | Electrode and Titrant Set-up; Method Entry and Proving; Method Control | - |
| 205-019 | Automatic Titrator Electrode Care, Standardisation and Verification | Daily Standardisation; Electrode Care; Verification and Records | Kalibrasi 3 titik (pH 4, 7, 10) dengan slope dan offset, sama dengan 206-004 |

Pelindung telinga di 205-011 dan 205-014 mengikuti aturan yang sudah disetujui di seri 204: APD ditambah pelindung telinga bila hazard memuat "hearing damage".

Semua lolos validasi docx dan kotak emergency ada di halaman 1. Hasil render LibreOffice 6 halaman, kecuali 007 dan 008 yang 7 halaman.

## Audit
Diaudit terhadap SWI sebelum konversi (commit 3159ee8). Yang tidak cocok utuh hanya kalimat baku lama (otorisasi Shift Supervisor, baris sarung tangan yang digabung) dan referensi yang dipecah ke dua kolom. Semua langkah lama ada di file baru.

Register seri: `docs/Register-SWI-205.xlsx`. Mohon dicek HSE untuk hazard a), b), c), CAUTION, dan emergency.
