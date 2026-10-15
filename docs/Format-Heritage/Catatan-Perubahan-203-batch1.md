# Catatan perubahan: seri 203 batch 1 (203-001, 004, 005, 006, 007, 008, 009, 011, 012) ke format Heritage

Aturan umum sama dengan seri 201. Seri 203 memakai parent procedure `HM-PRC-VXX-PRO207 Plant Surveys and Circuit Performance Assessment` dan wording Pre-start dan Completion sendiri (sama di semua 12 SWI 203): control room diberi tahu "task is starting, and where you will be", cek monitor gas, shower dan eyewash, area layak (tanpa akses terbatas, alarm gas, atau respons tumpahan), dan penutup membersihkan area, mengembalikan alat, mencatat hasil, memberi tahu control room. Wording ini ada di `build/swi_common.py` (`prestart203`, `CLOSE203`).

Sembilan SWI ini tidak punya padanan Martabe. 203-002, 003, dan 010 punya padanan Martabe dan dibahas terpisah.

| SWI | Judul | Halaman | Step |
|---|---|---|---|
| 203-001 | Plant Survey Planning, Permitting and Execution | 7 | Pre-start, Survey Plan and Window, Permits Briefing and Labelling, Running the Survey, Debrief, Completion |
| 203-004 | Residence Time and Tracer Test | 6 | Pre-start (tracer disetujui, steady state), Tracer Injection, Outlet and Intermediate Sampling, Analysis and Report, Completion |
| 203-005 | Leach and CIL Profile Survey | 7 | Pre-start, Profile Sampling, Filtration and Assay, Profile and Report, Completion |
| 203-006 | Adsorption Profile Survey | 7 | Pre-start, Profile Sampling, Field Determinations and Submission, Profile Isotherm and Bead Size, Completion |
| 203-007 | Thickener Performance Survey | 7 | Pre-start, Steady-State Record and Sampling, Solids Flux, Settling and Flocculant Dose Tests, Survey Report, Completion |
| 203-008 | Elution and EW Batch Performance | 6 | Pre-start (ventilasi merkuri), Batch Record and Assays, Efficiency Calculation, Comparison and Report, Completion |
| 203-009 | Reagent Dosing Verification | 7 | Pre-start, Dose Check, Out of Tolerance and Restoration, Completion |
| 203-011 | Carbon and Resin Loss | 7 | Pre-start, Stream Sampling, Recovery and Weighing, Attrition and Loss Accounting, Survey Report, Completion |
| 203-012 | Oxygen Utilisation and Sparger | 6 | Pre-start (catat tekanan dan flow oksigen), Dissolved Oxygen Measurement, Utilisation and Sparger Check, Survey Report, Completion |

## Perubahan APD yang perlu dicek
- **203-008:** daftar APD lama hanya hard hat, kacamata, hi-vis, sepatu, sarung tangan, sarung tangan tahan panas, dan face shield, padahal hazard-nya memuat HCN dan percikan larutan sianida. Saya samakan dengan APD standar (monitor HCN, goggles, sarung nitrile, apron, masker A2B2E2K2P3) ditambah sarung tangan tahan panas.
- **203-009:** daftar APD lama memuat sarung tangan tahan asam, apron, face shield, goggles, dan monitor multi-gas H2S, tetapi tidak monitor HCN dan masker, padahal hazard HCN ada. Saya tambahkan keduanya.

## Hal khusus
- **203-005:** CAUTION "tidak boleh masuk" dari hazard confined space; kotak emergency ditambah butir "person down at tank top".
- **203-008:** kontrol hazard panas (sarung tangan panas, face shield, tidak sampling kolom bertekanan atau saat pemanasan) jadi CAUTION; ventilasi gold room dari hazard merkuri jadi bullet Pre-start.
- **203-009:** CAUTION "jangan putus jalur dosing yang hidup" dari langkah lama 3.

## Berlaku untuk semuanya
Hazard a), b), c), CAUTION, dan emergency ditulis baru dari hazard dokumen. Classification dibuang; Area ke Description of work. Mohon dicek HSE.

## Persetujuan
Perubahan APD di 203-008 dan 203-009 (lihat atas) disetujui.
