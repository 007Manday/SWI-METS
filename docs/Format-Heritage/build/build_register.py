"""Build a per-series register from the Heritage-format SWIs.
Usage: python build_register.py <series> <pdf_dir> <out.xlsx>
<pdf_dir> holds PDF renders of the series files (same basename), used for the page count."""
import glob, os, re, subprocess, sys, zipfile
from collections import Counter
from lxml import etree
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

SERIES, PDF_DIR, OUT = sys.argv[1:4]
FOLDERS = {'201': 'SWI/201-Plant-Sampling', '203': 'SWI/203-Plant-Survey', '204': 'SWI/204-Physical-Testwork',
           '205': 'SWI/205-Chemical-Testwork', '206': 'SWI/206-Met-Lab-Operations-and-Safety', '207': 'SWI/207-Automatic-Samplers-and-Analysers'}
NAMES = {'201': 'Plant Sampling', '203': 'Plant Survey', '204': 'Physical Testwork', '205': 'Chemical Testwork',
         '206': 'Met Lab Operations and Safety', '207': 'Automatic Samplers and Analysers'}
OVERRIDES = {  # decisions taken in the review, shown instead of the raw comparison text
    '201-005': 'Carbon Analyser C2 Check dan C2 Meter Calibration - tidak dipakai (plant tidak punya analyser C2)',
    '201-017': 'Tailing Flocculant Solution Sampling - dipindah ke 201-020 (area reagent)',
    '201-020': 'Lime slaker, hydrated lime, ReCYN caustic strength, dan Tailing Flocculant Solution Sampling (dari 201-017) - Step 4-7',
    '203-002': 'Sampling Density Gauge Slurry - tidak dipakai (SWI memakai cutter dengan pompa, Martabe sampling manual)',
    '203-003': 'Cyclone Overflow Underflow Sampling - tidak dipakai (SWI memakai cutter dengan pompa, Martabe sampling manual)',
    '204-006': 'A&D MS-70 Moisture Analyzer Calibration - tidak dipakai (Mt. Morgan tidak punya moisture analyser)',
    '204-008': 'Brookfield DV2TLV Viscometer dan Marsh Funnel - cara Martabe dipakai dengan alat yang sama',
    '204-010': 'Settling Test Strength Variance; Effective Treatment Dosage; Flocculant Testwork on Tailing Using Sieve - Step 4-8',
    '207-007': 'Replace Filter Sock - Step 3, DRAFT (operasi harian tetap NOT FOR USE)',
    '207-008': 'Leach Analyzer Calibration - dipakai untuk kedua analyser; Detox Analyser Calibration tidak dipakai (tidak ada sirkuit detox)',
    '203-010': 'Intertank Screen Inspection - tidak dipakai (inspeksi saat shutdown; cek karbon di launder rutin per jam di 201-004)',
}
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
ns = {'w': W}
txt = lambda e: ''.join(e.itertext()).strip()

idx = {r[0]: r for r in openpyxl.load_workbook('docs/Matriks-Rujukan-Martabe.xlsx')['Indeks SWI'].iter_rows(min_row=2, values_only=True)}
reg = {r[1]: r for r in openpyxl.load_workbook('docs/Tabel-SWI-vs-Martabe.xlsx')['SWI vs Martabe'].iter_rows(min_row=2, values_only=True)}

rows, items = [], []
for f in sorted(glob.glob(os.path.join(FOLDERS[SERIES], '*.docx'))):
    code = re.search(r'MET-(%s-\d{3})' % SERIES, f).group(1)
    doc = 'SWI-PRO-MET-' + code
    if reg[code][5] != 'Sudah':
        continue
    root = etree.fromstring(zipfile.ZipFile(f).read('word/document.xml'))
    tbl = [t for t in root.iter('{%s}tbl' % W) if 'Part 1: Information' in txt(t)][0]
    trs = tbl.findall('w:tr', ns)
    cell = lambda r, i: txt(trs[r].findall('w:tc', ns)[i])
    title = cell(1, 1).split(' - ', 1)[1]
    paras = [txt(p) for p in trs[5].findall('w:tc', ns)[1].findall('w:p', ns) if txt(p)]
    area = [p[6:].rstrip('.') for p in paras if p.startswith('Area: ')][0]
    freq = [p[11:] for p in paras if p.startswith('Frequency: ')][0]
    draft = [p for p in paras if p.startswith('Draft for review')]
    note = [p for p in paras if p.startswith('Note:') or p.startswith('Safety-critical finding') or p.startswith('ISSUED BUT NOT FOR USE')]
    openi = [p for p in paras if p.startswith('Open items')]
    status = 'Final (isi tanpa tambahan)'
    if [p for p in paras if p.startswith('ISSUED BUT NOT FOR USE')]:
        status = 'NOT FOR USE (menunggu input)'
    elif draft:
        status = 'DRAFT FOR REVIEW (tambahan Martabe)'
    elif [p for p in paras if p.startswith('Note:')]:
        status = 'Catatan: titik sampling perlu diupdate'
    pdf = os.path.join(PDF_DIR, os.path.basename(f)[:-5] + '.pdf')
    pages = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
    r = reg[code]
    if code in OVERRIDES:
        mart = OVERRIDES[code]
    elif r[3] == 'Tidak ada yang cocok':
        mart = 'Tidak ada padanan'
    else:
        mart = re.sub(r'\s*\[[^\]]*\]', '', r[3])
        mart = re.sub(r'(^|\s)\d\.\s', '; ', mart).strip('; ').strip()
    rows.append([code, doc, title, area, idx[doc][3], cell(3, 3), 'A', cell(2, 1), cell(2, 3), cell(3, 1), freq,
                 len(trs) - 11, pages, mart, status, 'Sudah', os.path.basename(f)])
    for p in draft + note + openi:
        kind = 'Draft' if p.startswith('Draft') else ('Open items' if p.startswith('Open') else 'Catatan')
        items.append([doc, title, kind, p])

wb = openpyxl.Workbook()
ws = wb.active
ws.title = 'Register ' + SERIES
hdr = ['Kode', 'No. dokumen', 'Judul', 'Area', 'Klasifikasi', 'JSEA ID', 'Rev', 'Tanggal terbit', 'Review berikutnya', 'Document owner',
       'Frekuensi', 'Jumlah step', 'Halaman', 'Padanan Martabe', 'Status isi', 'Format Heritage', 'Nama file']
thin = Side(style='thin', color='BBBBBB')
ws.append(hdr)
for r in rows:
    ws.append(r)
for i, w in enumerate([9, 22, 58, 34, 16, 24, 6, 13, 16, 14, 52, 11, 10, 48, 34, 15, 95], 1):
    ws.column_dimensions[get_column_letter(i)].width = w
for c in ws[1]:
    c.font = Font(bold=True, color='FFFFFF'); c.fill = PatternFill('solid', fgColor='1F3864')
    c.alignment = Alignment(wrap_text=True, vertical='center', horizontal='center')
for row in ws.iter_rows(min_row=2):
    for c in row:
        c.alignment = Alignment(wrap_text=True, vertical='top', horizontal='center' if c.column in (1, 7, 8, 9, 10, 12, 13, 16) else 'left')
        c.border = Border(top=thin, bottom=thin, left=thin, right=thin)
    if row[14].value.startswith('NOT FOR USE'):
        row[14].fill = PatternFill('solid', fgColor='F8CBAD')
    elif row[14].value.startswith('DRAFT'):
        row[14].fill = PatternFill('solid', fgColor='FFF2CC')
    elif row[14].value.startswith('Catatan'):
        row[14].fill = PatternFill('solid', fgColor='FCE4D6')
ws.freeze_panes = 'D2'; ws.auto_filter.ref = 'A1:Q%d' % ws.max_row; ws.row_dimensions[1].height = 32

w2 = wb.create_sheet('Draft dan open items')
w2.append(['No. dokumen', 'Judul', 'Jenis', 'Isi catatan'])
for it in items:
    w2.append(it)
if not items:
    w2.append(['-', '-', '-', 'Tidak ada draft, catatan, atau open items di seri ini.'])
for i, w in enumerate([22, 58, 12, 150], 1):
    w2.column_dimensions[get_column_letter(i)].width = w
for c in w2[1]:
    c.font = Font(bold=True, color='FFFFFF'); c.fill = PatternFill('solid', fgColor='7A4B00'); c.alignment = Alignment(horizontal='center', vertical='center')
for row in w2.iter_rows(min_row=2):
    for c in row:
        c.alignment = Alignment(wrap_text=True, vertical='top')
w2.freeze_panes = 'A2'; w2.auto_filter.ref = 'A1:D%d' % w2.max_row

w3 = wb.create_sheet('Keterangan')
for l in ['Register seri %s %s (%d dokumen dalam format Heritage).' % (SERIES, NAMES[SERIES], len(rows)),
          'Data dibaca langsung dari Part 1 dan Part 2 tiap dokumen (judul, tanggal, owner, JSEA ID, area, frekuensi).',
          'Klasifikasi dan padanan Martabe diambil dari docs/Matriks-Rujukan-Martabe.xlsx dan docs/Tabel-SWI-vs-Martabe.xlsx, ditimpa oleh keputusan review bila ada. Format Heritage tidak memuat kolom klasifikasi, jadi klasifikasi hanya ada di register.',
          'Jumlah step dan halaman dihitung dari render dokumen (LibreOffice); halaman bisa sedikit berbeda di Microsoft Word.',
          'Status isi: Final = tanpa tambahan Martabe terbuka; DRAFT FOR REVIEW = ada tambahan Martabe yang menunggu JSEA; Catatan = ada catatan yang perlu ditindaklanjuti.',
          'Sheet "Draft dan open items" memuat paragraf draft, catatan, temuan safety-critical, dan open items di Description of work.',
          'Referensi register: HM-MMM-WHS-REG-XXX-R00-SWI-SWMS, tab SWI-MET.']:
    w3.append([l])
w3.column_dimensions['A'].width = 160
for row in w3.iter_rows():
    for c in row:
        c.alignment = Alignment(wrap_text=True, vertical='top')
wb.save(OUT)
print(len(rows), 'rows,', len(items), 'items')
print(Counter(r[14] for r in rows))
