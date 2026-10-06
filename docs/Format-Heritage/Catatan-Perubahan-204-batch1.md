# Catatan perubahan: seri 204 batch 1 (16 SWI) ke format Heritage

SWI: 204-001, 002, 003, 004, 005, 007, 009, 011, 012, 013, 014, 015, 016, 017, 018, 019. Tanpa padanan Martabe. 204-006, 008, dan 010 (punya tambahan Martabe) dibahas terpisah.

## Pola seri 204
- Parent procedure `HM-PRC-VXX-PRO208 Metallurgical Laboratory Physical Testwork`. Semua berstatus Operating, jadi tanpa pernyataan safety-critical dan tanpa butir "second person".
- Pre-start versi lab (sama di 19 SWI lama): fume cupboard dan scrubber, safety shower dan eyewash, kalibrasi instrumen atau neraca, reagen dalam masa berlaku, inspeksi glassware. Ditambah bullet pelatihan, JSEA, induksi, dan otorisasi dari Section 2 lama.
- Penutup versi lab: bersihkan bench dan fume cupboard, glassware ke rak, residu ke aliran limbah yang benar (efluen sianida tidak ke saluran umum), catat hasil, metode, dan identitas alat, ditambah butir Records (data sheet, logbook, langkah tidak selesai, kontrol tidak ada).
- Wording ada di `build/swi_common.py` (`prestart_lab`, `CLOSE_LAB`, `PPE_LAB`), isi tiap SWI di `build/gen204.py`.
- Setiap SWI: Pre-start Check, dua atau tiga step metode (dikelompokkan dari langkah lama), Completion and Clean Up.

## Perubahan APD yang perlu dikonfirmasi
**204-002, 012, 013, 014, 015, 016, 017** punya hazard "hearing damage" (mill, Ro-Tap, shaker), tetapi APD lamanya tidak memuat pelindung telinga. Pelindung telinga ditambahkan ke baris helmet, dan CAUTION di step shaker atau mill mengingatkannya.

## Hal khusus
- **204-003:** tetap **NOT FOR USE**. Banner jadi paragraf tebal di Description of work dan menyebut blocker-nya langsung (laser particle size analyser belum dibeli, tidak ada di ILS Q0023979), menggantikan rujukan "see the folder README" yang tidak ada isinya.
- **204-011:** CAUTION cek selang dan fitting sebelum diberi tekanan (dari hazard tekanan lama).
- **204-012 dan 013:** CAUTION hentikan dan isolasi mill sebelum dibuka (dari hazard peralatan yang hidup tanpa peringatan).
- **204-018:** CAUTION filtrasi bersianida di fume cupboard.
- **204-019:** CAUTION jangan membuka lid atau menyentuh rotor sebelum berhenti sendiri (dari langkah lama 6).
- Kotak emergency ditambah butir baru "Cuts from Broken Glassware" untuk SWI dengan hazard glassware.

## Audit
Diaudit terhadap SWI sebelum konversi (`build/audit_vs_source.py`): semua paragraf ada. Yang tidak cocok utuh hanya referensi yang dipecah jadi kolom ID dan judul, dan kalimat placeholder 204-003 yang ditulis ulang.

## Berlaku untuk semuanya
Hazard a), b), c), CAUTION, dan emergency ditulis baru dari hazard dokumen. Mohon dicek HSE.
