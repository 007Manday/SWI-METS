# Catatan perubahan: seri 206 batch 1 (11 SWI tanpa padanan Martabe) ke format Heritage

SWI: 206-001, 003, 005, 006, 007, 008, 009, 010, 011, 013, 014. Semuanya tidak punya padanan Martabe, jadi isi SWI dipertahankan dan hanya formatnya yang diubah. 206-002 dan 206-004 punya tambahan Martabe; keduanya dibahas dulu sebelum dikonversi. 206-012 belum ada.

## Perubahan umum
- Area: "206 Met Lab - Facility, Safety and Quality". Parent procedure: HM-PRC-VXX-PRO210 - Metallurgical Laboratory Facility, Safety and Quality.
- APD standar lab untuk seri ini memakai satu baris "Chemical resistant suit, acid-resistant and nitrile rubber gloves, and apron" (menggantikan "Gloves appropriate to the task" dan "Acid-resistant gloves, apron and face shield" yang terpisah). Face shield tetap ada di baris goggles. Monitor HCN dan gas mask ikut dicantumkan karena di ruangan ada sianida.
- Pre-start, Completion dan catatan (Records) memakai kalimat baku seri lab (sama dengan 204): induksi site dan kompetensi cyanide awareness, Take 5, JSEA, serta pencatatan nilai di data sheet, register atau logbook.
- SWI safety-critical (001, 005, 006, 007, 010, 011, 013): ada pernyataan safety-critical di Description of work, dan Pre-start ditambah "Confirm a second person is in the laboratory for any cyanide work. Cyanide work is not done alone."
- Hazard a), b), c), CAUTION, dan tabel emergency ditulis dari hazard dokumen asli. Baris Hazard/Control disalin apa adanya dari SWI lama.
- Referensi (KBK-MIR-LAB SOP, ILS quotation Q0023979) dipindah ke tabel Referenced documents, dengan nomor dan judul di kolom terpisah.

## Per SWI
| SWI | Judul | Step (setelah Pre-start) | Catatan |
|---|---|---|---|
| 206-001 | Met Lab Chemical Receipt, Storage and Decanting | Receipt and Register; Segregated Storage; Decanting | Safety-critical. CAUTION: asam yang mengenai sianida melepas HCN |
| 206-003 | Balance Verification and Calibration Check | Balance Set-up; Verification with Certified Weights; Out of Tolerance and Records | - |
| 206-005 | Cyanide Solution Handling and Spill Response | Cyanide Handling at the Bench; Spill Response; Exposure Response and Reporting | Safety-critical. 2 CAUTION |
| 206-006 | Acid Spill Response and Neutralisation | Containment; Neutralisation and Clean-up; Exposure Response and Reporting | Safety-critical |
| 206-007 | Met Lab Waste, Residue and Effluent Disposal | Segregation at the Bench; Neutralisation and Routing; Labelling, Register and Removal | Safety-critical |
| 206-008 | Glassware Cleaning and Drying | Rinsing and Washing; Acid Wash and Final Rinse; Inspection, Drying and Storage | - |
| 206-009 | Bottle Roller, Bench Mill and Agitator Operation | Bottle Roller; Bench Mill; Magnetic Stirrers and Clean-up | Proteksi telinga ditambahkan ke APD (bench mill), sesuai persetujuan proteksi telinga di seri 204 |
| 206-010 | Drying Oven and Muffle Furnace Operation | Set Temperature and Loading; Handling Hot Items; Ashing and Muffle Furnaces and Records | Safety-critical. Heat-resistant gloves tetap dicantumkan |
| 206-011 | Met Lab Emergency Response - Power Failure and Evacuation | Immediate Actions on Power Loss; Evacuation and Muster; Re-entry | Safety-critical |
| 206-013 | Ductless Fume Cabinet Filter Change and Breakthrough Check | Airflow and Breakthrough Check; Filter Change; Use Limits | Safety-critical |
| 206-014 | Met Lab Equipment Receipt, Installation and Commissioning Handover | Receipt and Services Check; Pressure Vessel and Installation; Calibration, Commissioning and Handover | - |

Semua file 6 halaman (render LibreOffice), kotak emergency di halaman 1, dan lolos validasi docx.

## Audit
Diaudit terhadap SWI sebelum konversi (commit 3159ee8). Kalimat yang tidak cocok utuh hanya kalimat baku lama: "Authorised by the Shift Supervisor before the task starts", "Any control in Section 3 found not in place…", judul "3 HAZARDS SPECIFIC TO THIS TASK", dan baris APD sarung tangan yang digabung. Referensi lain hanya dipecah ke dua kolom. Isinya tetap ada di Pre-start, Completion dan tabel APD. Tidak ada langkah yang hilang.

Register seri: `docs/Register-SWI-206.xlsx`. Mohon dicek HSE untuk hazard a), b), c), CAUTION, dan emergency.
