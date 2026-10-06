# Catatan perubahan: SWI-PRO-MET-206-002 dan 206-004 (tambahan Martabe) ke format Heritage

Semua saran pembahasan disetujui pengguna (2026-10-06). Kedua SWI berstatus DRAFT FOR REVIEW sampai JSEA diperbarui.

## 206-002 Fume Cupboard Operation, Scrubber Check and Cleaning (safety-critical, 7 halaman)
Step: Pre-start Check; Fume Cupboard and Scrubber Start-up; Working in the Fume Cupboard; Face Velocity Measurement - GM8902 Anemometer (Martabe); Acceptance and Records; Completion and Clean Up.

Keputusan:
1. **Nilai penerimaan:** kecepatan udara di bukaan sash diambil dari spesifikasi Safetyflow (ILS Q0023979), atau dari AS/NZS 2243.8 bila spesifikasi tidak memuatnya. Angka sekitar 0,5 m/s hanya disebut sebagai nilai umum di Open items dan tidak ditulis sebagai batas di langkah kerja.
2. **Cara merata-ratakan:** catat rata-rata dan bacaan terendah dari 20 bacaan (1 bacaan per detik). Bila rata-rata di bawah batas, fume cupboard di-tag out, tidak dipakai, dan dilaporkan ke Met Lab supervisor (CAUTION Step 5).
3. **Posisi sash:** pengukuran di tinggi sash kerja yang ditandai, bukan sash terbuka penuh seperti di Martabe.
4. **Frekuensi:** bulanan dan setelah perbaikan fan, ducting atau scrubber.
- Hazard dari sumber Martabe (titik jepit sash dan menghirup fume saat mengukur) menjadi hazard Step 4 dan CAUTION.
- Open items: nilai penerimaan, bacaan tunggal terendah yang diizinkan, frekuensi bulanan, serta keberadaan anemometer GM8902 dan sertifikat kalibrasinya.

## 206-004 pH, DO and Conductivity Meter Calibration (operating, 9 halaman)
Step: Pre-start Check; pH Meter Calibration - Three Point; TPS Cube pH Calibration (Martabe); Measuring pH with the TPS Cube (Martabe); DO Meter Calibration in Air - HI9142 (Martabe); DO Measurement in Slurry (Martabe); Electrode Storage and Meter Log; Completion and Clean Up.

Keputusan:
1. **DO meter:** alur Martabe (kalibrasi di udara, cek, ukur di tangki, catat) dipakai untuk Hanna HI9142. Langkah menu Oxyguard Handy Polaris dihapus; menu mengikuti manual HI9142.
2. **Nilai "6 sampai 8":** tidak dipakai karena tidak ada satuannya. Batas penerimaan kalibrasi di udara diambil dari manual HI9142 (open item).
3. **TPS cube pH meter:** dipakai seperti di Martabe dan masuk daftar alat. Keberadaan alat di site atau pengadaannya dicatat sebagai open item.
4. **Kalibrasi pH:** tetap 3 titik (pH 4, 7, 10) dengan slope dan offset dicatat, termasuk untuk TPS cube. Kalibrasi 2 titik Martabe tidak dipakai. Martabe menulis "pH 4: sama seperti pH 7"; kontrol untuk pH 4 dikonfirmasi dari manual TPS cube (open item).
5. **Sarung tangan:** "Latex gloves" pada dua baris hazard Martabe ([JSEA to confirm]) diganti "Chemical-resistant gloves". Limbah "B3" diganti aliran limbah site, dan sampel bersianida masuk aliran sianida, tidak ke saluran umum.
6. **DO di tangki slurry:** tetap dipakai, dengan kontrol sianida dari SWI-PRO-MET-201-003 (monitor HCN, datang dari arah angin, orang kedua terlihat) sebagai bullet dan CAUTION Step 6.
- Path folder G: dan nomor form Martabe tidak dipakai sebagai catatan Mt. Morgan; dicatat sebagai open item.
- Open items (6): TPS cube di site, batas DO dari manual HI9142, kontrol pH 4 di TPS cube, rentang slope elektroda, catatan DO dan logsheet kalibrasi pH Mt. Morgan, standar konduktivitas yang belum ada.

## Perubahan terkait
- 201-013: rujukan "SWI-PRO-MET-206-004 Part C" diganti "Step 3" (di bullet dan tabel referensi). Selain itu tidak ada perubahan; teks dokumen lain identik.

## Audit
Diaudit terhadap SWI sebelum konversi (commit 3159ee8). Bagian yang tidak cocok utuh hanya bagian yang sengaja diubah sesuai keputusan di atas:
- tanda [M]/[CONFIRM], yang menjadi Draft dan Open items;
- menu Oxyguard;
- nilai 6-8;
- kalibrasi 2 titik;
- sash terbuka penuh;
- path folder G:;
- kalimat baku lama.

Lolos validasi docx, dan kotak emergency ada di halaman 1. Mohon dicek HSE untuk hazard a), b), c), CAUTION, dan emergency.
