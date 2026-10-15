# SWI-METS: Safe Work Instruction Metallurgy (Mt. Morgan, 4034-033)

99 SWI Rev A, dikelompokkan per seri di folder `SWI/`.

| Seri | Folder | Jumlah | Nomor |
|---|---|---|---|
| 201 | `SWI/201-Plant-Sampling` | 25 | 001-025 |
| 203 | `SWI/203-Plant-Survey` | 12 | 001-012 |
| 204 | `SWI/204-Physical-Testwork` | 19 | 001-019 |
| 205 | `SWI/205-Chemical-Testwork` | 19 | 001-019 |
| 206 | `SWI/206-Met-Lab-Operations-and-Safety` | 13 | 001-011, 013, 014 (**012 belum ada**) |
| 207 | `SWI/207-Automatic-Samplers-and-Analysers` | 11 | 001-011 |

Seri 202 belum ada di repositori.

`docs/Tabel-SWI-vs-Martabe.xlsx` membandingkan tiap SWI dengan WI Martabe yang cocok dan memuat daftar WI Martabe tanpa SWI. `docs/Matriks-Rujukan-Martabe.xlsx` berisi indeks SWI, pemetaan SOP Martabe ke SWI yang merujuknya, dan daftar SWI tanpa rujukan Martabe.

Status perbandingan dengan Martabe: dokumen SOP Martabe (`KBK-MIR-...`, `KBK SOP-PROC-CNREC-...`) belum ada di repositori, jadi isi SWI belum dilengkapi.

## Format Heritage

Seri 201 (001-025), 203 (001-012), 204 (001-019) dan 207 (001-011) sudah diubah ke format Heritage, begitu juga 206 (001-011, 013, 014) dan 205 (001-019); semua seri sudah dalam format Heritage. Template dan catatan perubahan ada di `docs/Format-Heritage/`, skrip pembuat di `docs/Format-Heritage/build/`. Register per seri (data dibaca dari dokumen) ada di `docs/Register-SWI-201.xlsx`, `-203`, `-204`, `-205`, `-206` dan `-207`. Hasil audit file Heritage terhadap SWI sebelum konversi ada di `docs/Format-Heritage/Audit-Heritage-vs-SWI-201-203.md`. Status per SWI untuk semua seri ada di kolom "Format Heritage" pada `docs/Tabel-SWI-vs-Martabe.xlsx`. SWP HM-PRC-VXX-PRO206, PRO208 dan PRO212 sampai PRO217 ada di folder `SWP/` dalam format Safe Work Procedure Heritage (template `docs/Format-Heritage/SWP-PRO-000_000_Sodium_Hydrosulphide_Management_Plan.docx`, catatan `docs/Format-Heritage/Catatan-Perubahan-SWP.md`).
