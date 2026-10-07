"""Build a Heritage-format Safe Work Procedure from an old-format SWP.
Usage: python build_swp.py old_swp.docx heritage_swp_unpacked_dir work_dir out.docx [pages.json]
pages.json (optional) maps TOC bookmark -> page number, from a first render."""
import copy, json, os, re, shutil, subprocess, sys, zipfile
from lxml import etree

SRC, TPL_X, OUT_X, OUT_DOCX = sys.argv[1:5]
PAGES = json.load(open(sys.argv[5])) if len(sys.argv) > 5 else {}
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
q = lambda t: '{%s}%s' % (W, t)
txt = lambda e: ''.join(x.text or '' for x in e.iter(q('t'))).strip()

# ---------- 1. read the old SWP ----------
old = etree.fromstring(zipfile.ZipFile(SRC).read('word/document.xml'))
info, sec, cur = {}, {}, None
for el in old.find(q('body')):
    if el.tag == q('p'):
        st = el.find('.//' + q('pStyle'))
        st = st.get(q('val')) if st is not None else ''
        x = txt(el)
        if not x:
            continue
        if st == 'Heading1':
            cur = re.sub(r'^\d+\s+', '', x); sec[cur] = []
        elif cur:
            sec[cur].append(('li' if st == 'ListParagraph' else 'p', x))
    elif el.tag == q('tbl'):
        rows = [[[txt(p) for p in tc.iter(q('p')) if txt(p)] for tc in tr.findall(q('tc'))] for tr in el.iter(q('tr'))]
        if cur is None:
            for row in rows:
                info[' '.join(row[0])] = ' '.join(row[1])
        else:
            sec[cur].append(('tbl', rows))

DOCNO, TITLE = info['Document number'], info['Title']
d, m, y = info['Date'].split()
MONTHS = 'January February March April May June July August September October November December'.split()
DATE = '%02d/%02d/%s' % (int(d), MONTHS.index(m) + 1, y)
REV = info['Revision'].replace('Rev ', '')

# ---------- 2. copy the template ----------
if os.path.exists(OUT_X):
    shutil.rmtree(OUT_X)
shutil.copytree(TPL_X, OUT_X)

def set_runs(p, text):
    """Put text in the first w:t of paragraph p and empty the rest."""
    ts = list(p.iter(q('t')))
    ts[0].text = text
    ts[0].set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    for t in ts[1:]:
        t.text = ''

def patch_part(name, fn):
    path = os.path.join(OUT_X, 'word', name)
    tree = etree.parse(path)
    fn(tree.getroot())
    tree.write(path, xml_declaration=True, encoding='UTF-8', standalone=True)

def header(root):
    for p in root.iter(q('p')):
        t = txt(p)
        if t.startswith('Sodium Hydrosulphide'):
            set_runs(p, TITLE)
        elif t == 'SWP-OPR-OPR-000-000':
            set_runs(p, DOCNO)
patch_part('header1.xml', header)

def footer(root):
    for p in root.iter(q('p')):
        t = txt(p)
        if t.startswith('SWP-OPR-OPR-000-000_'):
            set_runs(p, '%s_%s' % (DOCNO, TITLE))
        elif t == '29/09/2027':
            set_runs(p, DATE)
        elif t == 'R01':
            set_runs(p, REV)
patch_part('footer1.xml', footer)

core = os.path.join(OUT_X, 'docProps', 'core.xml')
s = open(core, encoding='utf8').read()
s = re.sub(r'<dc:title>.*?</dc:title>', '<dc:title>%s - %s</dc:title>' % (DOCNO, TITLE.replace('&', '&amp;')), s)
open(core, 'w', encoding='utf8').write(s)

tree = etree.parse(os.path.join(OUT_X, 'word', 'document.xml'))
body = tree.getroot().find(q('body'))
ch = list(body)
cover, toc_sdt, sectPr = ch[0], ch[1], ch[-1]
P_BREAK, P_H1, P_NORMAL, P_SPACER, P_RESP, P_WARN, P_H2, P_BULLET = ch[2], ch[3], ch[4], ch[6], ch[8], ch[11], ch[16], ch[32]

# ---------- 3. cover page and document history ----------
cc = cover.find(q('sdtContent'))
for p in cc.findall(q('p')):
    t = txt(p)
    if t.startswith('Sodium Hydrosulphide'):
        set_runs(p, TITLE)
    elif t == 'SWP-OPR-OPR-000-000':
        set_runs(p, DOCNO)
trs = cc.find(q('tbl')).findall(q('tr'))
def cell(r, c, text):
    tc = trs[r].findall(q('tc'))[c]
    p = tc.find(q('p'))
    if p.find('.//' + q('t')) is None:
        run = etree.SubElement(p, q('r'))
        rpr = trs[r].findall(q('tc'))[0].find('.//' + q('rPr'))
        etree.SubElement(run, q('t'))
    set_runs(p, text)
cell(1, 1, '%s Safe Work Procedure' % TITLE); cell(1, 3, REV)
cell(2, 1, DOCNO); cell(2, 3, info['Document owner'])
cell(3, 1, DATE); cell(3, 3, '-')
cell(4, 1, 'Process owner: %s. Document approver: %s.' % (info['Process owner'].replace('  ·  ', ', '), info['Document approver']))
cell(6, 0, DATE); cell(6, 1, REV); cell(6, 2, info['Prepared by']); cell(6, 3, ''); cell(6, 4, '')
cell(9, 0, 'Rev %s - first issue. Converted from the GGT Standard Work Procedure layout to the Heritage Safe Work Procedure format; content unchanged.' % REV)
cell(11, 1, info['Prepared by']); cell(11, 2, 'Document preparer'); cell(11, 3, DATE)
cell(12, 2, info['Document owner']); cell(13, 2, '')
cell(14, 2, info['Document approver'])

# ---------- 4. body builders ----------
for el in ch[2:-1]:
    body.remove(el)
out = []
toc = []
bm = [9000]
counters = [0, 0]

def strip_ids(e):
    for el in e.iter():
        for a in list(el.attrib):
            if a.startswith('{http://schemas.microsoft.com/office/word/2010/wordml}'):
                del el.attrib[a]
    return e

def para(text, proto=None):
    if proto is None:
        p = etree.Element(q('p'))
        r = etree.SubElement(p, q('r'))
        t = etree.SubElement(r, q('t'))
    else:
        p = strip_ids(copy.deepcopy(proto))
        for x in p.findall(q('proofErr')) + p.findall(q('bookmarkStart')) + p.findall(q('bookmarkEnd')):
            p.remove(x)
        rs = p.findall(q('r'))
        for r in rs[1:]:
            p.remove(r)
        t = rs[0].find(q('t'))
        for sub in rs[0].findall(q('rPr')):
            for v in sub.findall(q('vertAlign')):
                sub.remove(v)
    t.text = text
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    return p

def heading(level, text):
    proto = P_H1 if level == 1 else P_H2
    p = strip_ids(copy.deepcopy(proto))
    for x in list(p):
        if x.tag != q('pPr'):
            p.remove(x)
    bm[0] += 1
    name = '_Toc%d' % (159300000 + bm[0])
    s = etree.SubElement(p, q('bookmarkStart')); s.set(q('id'), str(bm[0])); s.set(q('name'), name)
    r = etree.SubElement(p, q('r')); t = etree.SubElement(r, q('t')); t.text = text
    e = etree.SubElement(p, q('bookmarkEnd')); e.set(q('id'), str(bm[0]))
    if level == 1:
        counters[0] += 1; counters[1] = 0; num = '%d.' % counters[0]
    else:
        counters[1] += 1; num = '%d.%d' % tuple(counters)
    toc.append((level, num, text, name))
    if level == 1:
        out.append(strip_ids(copy.deepcopy(P_SPACER)))
    out.append(p)

def normal(text):
    out.append(para(text, P_NORMAL))

def bullet(text):
    out.append(para(text, P_BULLET))

def warning(text):
    t = strip_ids(copy.deepcopy(P_WARN))
    p = t.findall('.//' + q('tc'))[1].find(q('p'))
    for x in p.findall(q('proofErr')):
        p.remove(x)
    rs = p.findall(q('r'))
    for r in rs[1:]:
        p.remove(r)
    rs[0].find(q('t')).text = text
    out.append(t)

def table(headers, rows, widths, label_col=True):
    """Heritage table: grey header row; label_col shades and bolds the first column.
    A cell given as a list is written as bullet points."""
    t = strip_ids(copy.deepcopy(P_RESP))
    proto_rows = t.findall(q('tr'))
    hdr, body_row = proto_rows[0], proto_rows[1]
    for r in proto_rows:
        t.remove(r)
    grid = t.find(q('tblGrid'))
    for g in list(grid):
        grid.remove(g)
    for w in widths:
        etree.SubElement(grid, q('gridCol')).set(q('w'), str(w))
    hcell = hdr.findall(q('tc'))[0]
    lcell, vcell = body_row.findall(q('tc'))
    vpara_bullet = vcell.find(q('p'))
    def mk(cell_proto, w, value, bold_proto=True, shade=None):
        tc = copy.deepcopy(cell_proto)
        tc.find(q('tcPr')).find(q('tcW')).set(q('w'), str(w))
        shd = tc.find(q('tcPr')).find(q('shd'))
        if shade is False and shd is not None:
            tc.find(q('tcPr')).remove(shd)
        for p in tc.findall(q('p')):
            tc.remove(p)
        values = value if isinstance(value, list) else [value]
        for v in values:
            if isinstance(value, list):
                p = copy.deepcopy(vpara_bullet)
                r = etree.SubElement(p, q('r'))
                rpr = etree.SubElement(r, q('rPr')); etree.SubElement(rpr, q('rFonts')).set(q('cstheme'), 'minorHAnsi')
            else:
                p = copy.deepcopy(cell_proto.find(q('p')))
                for r in p.findall(q('r'))[1:]:
                    p.remove(r)
                r = p.find(q('r'))
                if r is None:
                    r = etree.SubElement(p, q('r'))
                for tt in r.findall(q('t')):
                    r.remove(tt)
                if not bold_proto:
                    for rp in [p.find(q('pPr')).find(q('rPr')), r.find(q('rPr'))]:
                        if rp is not None:
                            for b in rp.findall(q('b')) + rp.findall(q('bCs')):
                                rp.remove(b)
            tt = etree.SubElement(r, q('t')); tt.text = v
            tt.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
            tc.append(p)
        return tc
    hr = copy.deepcopy(hdr)
    for c in hr.findall(q('tc')):
        hr.remove(c)
    for w, h in zip(widths, headers):
        hr.append(mk(hcell, w, h))
    t.append(hr)
    for row in rows:
        br = copy.deepcopy(body_row)
        for c in br.findall(q('tc')):
            br.remove(c)
        br.find(q('trPr')).find(q('trHeight')).set(q('val'), '340')
        br.find(q('trPr')).insert(0, etree.Element(q('cantSplit')))
        for i, (w, v) in enumerate(zip(widths, row)):
            if i == 0 and label_col:
                br.append(mk(lcell, w, v))
            else:
                br.append(mk(lcell, w, v, bold_proto=False, shade=False))
        t.append(br)
    out.append(t)
    out.append(strip_ids(copy.deepcopy(P_SPACER)))

def items(name, kinds=('p', 'li', 'tbl')):
    return [x for x in sec[name] if x[0] in kinds]

# ---------- 5. content ----------
heading(1, 'Purpose and Scope')
for k, x in items('PURPOSE / SCOPE'):
    normal(x)
normal('Document details:')
for label in ['Register area', 'Hazard analyses beneath', 'Work instructions beneath', 'Process owner', 'Document owner', 'Document approver']:
    bullet('%s: %s' % (label, info[label].replace('  ·  ', ', ')))

heading(1, 'Responsibilities')
rows = items('RESPONSIBILITIES', ('tbl',))[0][1]
table(['Staff', 'Responsibilities'], [[r[0][0], r[1]] for r in rows[1:]], [2263, 7931])

heading(1, 'Abbreviations and Definitions')
rows = items('ABBREVIATIONS / DEFINITIONS', ('tbl',))[0][1]
defs = []
for r in rows[1:]:
    term, mean = r[0][0], ' '.join(r[1])
    mean = mean.replace('Standard work instruction', 'Safe work instruction').replace('Standard work procedure', 'Safe work procedure')
    defs.append([term, mean])
table(['Term', 'Meaning'], defs, [2263, 7931])

heading(1, 'Potential Hazards')
for k, x in items('POTENTIAL HAZARDS'):
    (bullet if k == 'li' else normal)(x)

heading(1, 'Personal Protective Equipment')
for k, x in items('PPE'):
    (bullet if k == 'li' else normal)(x)

heading(1, 'Procedure')
proc = sec['PROCEDURE']
tables = [x[1] for x in proc if x[0] == 'tbl']
texts = [x[1] for x in proc if x[0] != 'tbl']
warn = [x for x in texts if x.startswith('Warning:')][0]
heading(2, 'Introduction')
warning(warn[len('Warning:'):].strip())
heading(2, 'Procedure and Implementation Steps')
normal([x for x in texts if x.startswith('The documents below')][0])
wi = tables[0]
table([' '.join(c) for c in wi[0]], [[' '.join(c) for c in r] for r in wi[1:]], [2200, 2200, 4094, 1700], label_col=False)
heading(2, 'Schedule')
sch = tables[1]
table([' '.join(c) for c in sch[0]], [[' '.join(c) for c in r] for r in sch[1:]], [5600, 4594], label_col=False)
heading(2, 'Flowchart')
for k, x in items('FLOWCHART'):
    normal(x.replace(' in Section 6.', '.'))

heading(1, 'Training')
for k, x in items('TRAINING'):
    (bullet if k == 'li' else normal)(x)

heading(1, 'Register Traceability')
for k, x in sec['REGISTER TRACEABILITY']:
    if k == 'tbl':
        table([' '.join(c) for c in x[0]], [[' '.join(c) for c in r] for r in x[1:]], [7000, 3194])
    else:
        normal(x)

heading(1, 'Review Criteria')
rev = ' '.join(x for k, x in items('REVIEW'))
m_ = re.match(r'This procedure and the documents beneath it are reviewed every (.+?), and (immediately after .+)\.$', rev)
assert m_, rev
normal('This Procedure and the documents beneath it shall be reviewed as follows:')
bullet('Every %s; or' % m_.group(1))
bullet(m_.group(2)[0].upper() + m_.group(2)[1:] + '.')

heading(1, 'Legislation & References')
heading(2, 'Legislation')
bullet('Queensland Mining and Quarrying Safety and Health Act 1999')
bullet('Queensland Mining and Quarrying Safety and Health Regulation 2017')
heading(2, 'Source Documents by Task')
normal('The source documents and notes held for each task. Register lines are on tabs JSEA_LAB and SWI-LAB (Section %d).' % [i for i, t in enumerate([e for e in toc if e[0] == 1], 1) if t[2] == 'Register Traceability'][0])
task = {r[0][0]: r[2][0] for r in wi[1:]}
ref_rows, pend = [], []
for k, x in items('REFERENCE'):
    mm = re.match(r'Heritage register line (JSEA-PRO-\S+), tab', x)
    if mm:
        ref_rows.append([mm.group(1), task.get(mm.group(1), ''), pend or ['No source document held']])
        pend = []
    else:
        pend.append(x)
assert not pend, ('unpaired references', pend)
table(['JSEA', 'Task', 'Source documents and notes'], [[a, b, c] for a, b, c in ref_rows], [2350, 3200, 4644], label_col=False)

# ---------- 6. table of contents ----------
tc_ = toc_sdt.find(q('sdtContent'))
tps = list(tc_)
head_p, first_p, toc1_p, end_p = tps[0], tps[1], tps[2], tps[-1]
toc2_p = [p for p in tps if p.find('.//' + q('pStyle')) is not None and p.find('.//' + q('pStyle')).get(q('val')) == 'TOC2'][0]
for p in tps[1:-1]:
    tc_.remove(p)
def toc_entry(proto, num, text, name):
    p = strip_ids(copy.deepcopy(proto))
    h = p.find(q('hyperlink'))
    h.set(q('anchor'), name)
    ts = list(h.iter(q('t')))
    ts[0].text, ts[1].text, ts[2].text = num, text, str(PAGES.get(name, 0))
    for it in h.iter(q('instrText')):
        it.text = ' PAGEREF %s \\h ' % name
    return p
for i, (lvl, num, text, name) in enumerate(toc):
    proto = first_p if i == 0 else (toc1_p if lvl == 1 else toc2_p)
    e = toc_entry(proto, num, text, name)
    if i == 0 and lvl == 1:
        pass
    tc_.insert(len(tc_) - 1, e)

# ---------- 7. assemble ----------
body.remove(sectPr)
body.append(strip_ids(copy.deepcopy(P_BREAK)))
for e in out:
    body.append(e)
body.append(sectPr)
tree.write(os.path.join(OUT_X, 'word', 'document.xml'), xml_declaration=True, encoding='UTF-8', standalone=True)

# drop images no longer used by the body
rels_path = os.path.join(OUT_X, 'word', '_rels', 'document.xml.rels')
rels = etree.parse(rels_path)
docxml = open(os.path.join(OUT_X, 'word', 'document.xml'), encoding='utf8').read()
used_media = set()
for rel in list(rels.getroot()):
    if rel.get('Type').endswith('/image'):
        if 'r:embed="%s"' % rel.get('Id') not in docxml and 'r:id="%s"' % rel.get('Id') not in docxml:
            rels.getroot().remove(rel)
        else:
            used_media.add(rel.get('Target'))
rels.write(rels_path, xml_declaration=True, encoding='UTF-8', standalone=True)
for f in os.listdir(os.path.join(OUT_X, 'word', '_rels')):
    if f != 'document.xml.rels':
        for rel in etree.parse(os.path.join(OUT_X, 'word', '_rels', f)).getroot():
            if rel.get('Type').endswith('/image'):
                used_media.add(rel.get('Target'))
for f in os.listdir(os.path.join(OUT_X, 'word', 'media')):
    if 'media/' + f not in used_media:
        os.remove(os.path.join(OUT_X, 'word', 'media', f))

os.makedirs(os.path.dirname(os.path.abspath(OUT_DOCX)), exist_ok=True)
if os.path.exists(OUT_DOCX):
    os.remove(OUT_DOCX)
subprocess.run(['zip', '-q', '-X', '-r', os.path.abspath(OUT_DOCX), '[Content_Types].xml', '_rels', 'docProps', 'word', 'customXml'], cwd=OUT_X, check=True)
json.dump([t for t in toc], open(OUT_DOCX + '.toc.json', 'w'))
print('built', OUT_DOCX, len(toc), 'headings')
