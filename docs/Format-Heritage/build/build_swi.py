"""Build a Heritage-format SWI from the heritage 304-008 template.
Usage: python build_swi.py content.py heritage_unpacked_dir work_dir out.docx"""
import copy, os, re, shutil, subprocess, sys
from lxml import etree

CONTENT, SRC_X, OUT_X, OUT_DOCX = sys.argv[1:5]
C = {'CONTENT': os.path.abspath(CONTENT)}
exec(open(CONTENT, encoding='utf8').read(), C)
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
ns = {'w': W}
q = lambda t: '{%s}%s' % (W, t)

OLD_TITLE = 'WAD Cyanide - Distillation and Determination'
NEW_TITLE = C['TITLE']
NEW_ID = 'SWI-PRO-MET-' + C['NUM']
NEW_JSEA = 'JSEA-PRO-MET-' + C['NUM']

if os.path.exists(OUT_X):
    shutil.rmtree(OUT_X)
shutil.copytree(SRC_X, OUT_X)

# ---------- 1. global identity swap (header, footer, core props, cover) ----------
def swap(path):
    s = open(path, encoding='utf8').read()
    s = s.replace(OLD_TITLE, NEW_TITLE).replace('PRO-LAB-304-008', 'PRO-MET-' + C['NUM'])
    open(path, 'w', encoding='utf8').write(s)
for f in ['word/header1.xml', 'word/footer1.xml', 'docProps/core.xml']:
    swap(os.path.join(OUT_X, f))

tree = etree.parse(os.path.join(OUT_X, 'word/document.xml'))
body = tree.getroot().find('w:body', ns)
for t in tree.getroot().iter(q('t')):
    if t.text:
        t.text = t.text.replace(OLD_TITLE, NEW_TITLE)

# ---------- helpers ----------
def set_text(p_or_tc, text):
    """Put text in first run, drop other runs, keep first run formatting."""
    runs = list(p_or_tc.iter(q('r')))
    first = runs[0]
    for r in runs[1:]:
        r.getparent().remove(r)
    ts = first.findall('w:t', ns)
    for t in ts[1:]:
        first.remove(t)
    ts[0].text = text
    ts[0].set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')

def clone_with(p, text=None, numId=None):
    c = copy.deepcopy(p)
    if text is not None:
        set_text(c, text)
    if numId is not None:
        for n in c.iter(q('numId')):
            n.set(q('val'), str(numId))
    return c

def drop_ids(e):
    for x in e.iter():
        for a in list(x.attrib):
            if a.endswith('paraId') or a.endswith('textId'):
                del x.attrib[a]

# ---------- 2. PPE requirements (page 2) ----------
ppe = C['PPE']
ppe_paras = body[13:21]
tmpl = ppe_paras[0]
anchor = ppe_paras[0].getprevious()
for p in ppe_paras:
    body.remove(p)
for txt in reversed(ppe):
    anchor.addnext(clone_with(tmpl, txt))

# drop the spacer paragraph before the emergency box so it stays on page 2 with the longer header
last_ppe = [e for e in body if e.tag == q('p') and 'Full or half gas mask' in ''.join(e.itertext())][0]
sp = last_ppe.getnext()
if sp.tag == q('p') and not ''.join(sp.itertext()).strip():
    body.remove(sp)

# tighten page 2 further: drop the spacer before the PPE heading (kept only when the list is short)
if len(ppe) >= 8 or len(NEW_TITLE) > 45:
    hd = [e for e in body if e.tag == q('p') and ''.join(e.itertext()).strip() == 'PPE REQUIREMENTS'][0]
    prev = hd.getprevious()
    if prev.tag == q('p') and not ''.join(prev.itertext()).strip():
        body.remove(prev)

# ---------- 3. Part 1 / Part 2 table ----------
tb = [e for e in body if e.tag == q('tbl') and 'Part 1: Information' in ''.join(e.itertext())][0]
rows = tb.findall('w:tr', ns)

def cell(r, i): return r.findall('w:tc', ns)[i]

set_text(cell(rows[1], 1), '%s - %s' % (NEW_ID, NEW_TITLE))
set_text(cell(rows[3], 3), NEW_JSEA)

# description of work
desc_cell = cell(rows[5], 1)
dps = desc_cell.findall('w:p', ns)
P_NORMAL, P_BLANK, P_BOLD = dps[0], dps[1], dps[10]
def mk(base, text):
    return clone_with(base, text)

desc = C['DESC']
for p in dps:
    desc_cell.remove(p)
for kind, txt in desc:
    if kind == 'b':
        desc_cell.append(copy.deepcopy(P_BLANK))
    elif kind == 'B':
        desc_cell.append(mk(P_BOLD, txt))
    else:
        desc_cell.append(mk(P_NORMAL, txt))

# potential hazards
haz_cell = cell(rows[6], 1)
hps = haz_cell.findall('w:p', ns)
H_NORMAL, H_BLANK, H_ITAL = hps[0], hps[1], hps[-1]
hazards = C['HAZARDS']
for p in hps:
    haz_cell.remove(p)
for h in hazards:
    haz_cell.append(mk(H_NORMAL, h))
    haz_cell.append(copy.deepcopy(H_BLANK))
haz_cell.append(mk(H_ITAL, 'The full step-by-step hazard analysis, with the risk ranking, is in %s Section 4.' % NEW_JSEA))

# ---------- 4. Part 3 steps ----------
step_rows = rows[11:16]
r_first, r_other = step_rows[0], step_rows[1]
c1_t = r_other.findall('w:tc', ns)[0].findall('w:p', ns)
c2_t = r_other.findall('w:tc', ns)[1].findall('w:p', ns)
T_SPACER1, T_TITLE, T_BLANK1, T_HAZ, T_HSP = c1_t[0], c1_t[1], c1_t[2], c1_t[3], c1_t[4]
T_SPACER2, T_BUL, T_BSP, T_CAUT, T_CAUT_END = c2_t[0], c2_t[1], c2_t[2], c2_t[-2], c2_t[-1]
c2_first = r_first.findall('w:tc', ns)[1].findall('w:p', ns)
T_EQHEAD = [p for p in c2_first if 'Equipment Required' in ''.join(p.itertext())][0]
T_EQITEM = [p for p in c2_first if 'Cyanide distillation train' in ''.join(p.itertext())][0]
T_EQEND = c2_first[-1]

steps = C['STEPS']

# numbering: step i letter list uses numId 15+i (15..19 exist, 20 is added)
num_path = os.path.join(OUT_X, 'word/numbering.xml')
ntree = etree.parse(num_path); nroot = ntree.getroot()
src_num = [n for n in nroot.findall('w:num', ns) if n.get(q('numId')) == '19'][0]
prev = src_num
for nid in range(20, 15 + len(steps)):
    new_num = copy.deepcopy(src_num); new_num.set(q('numId'), str(nid))
    prev.addnext(new_num); prev = new_num
ntree.write(num_path, xml_declaration=True, encoding='UTF-8', standalone=True)

tbl_steps = rows[11].getparent()
anchor = rows[15]
for r in step_rows:
    tbl_steps.remove(r)

new_rows = []
for i, (title, hz, bullets, caution, equip) in enumerate(steps):
    r = copy.deepcopy(r_first if i == 0 else r_other)
    tcs = r.findall('w:tc', ns)
    c1, c2 = tcs[0], tcs[1]
    for p in c1.findall('w:p', ns) + c2.findall('w:p', ns):
        p.getparent().remove(p)
    c1.append(copy.deepcopy(T_SPACER1))
    c1.append(clone_with(T_TITLE, title))
    c1.append(copy.deepcopy(T_BLANK1))
    for j, h in enumerate(hz):
        c1.append(clone_with(T_HAZ, h, numId=15 + i))
        if j < len(hz) - 1:
            c1.append(copy.deepcopy(T_HSP))
    c2.append(copy.deepcopy(T_SPACER2))
    for b_ in bullets:
        c2.append(clone_with(T_BUL, b_))
        c2.append(copy.deepcopy(T_BSP))
    if caution:
        c2.append(clone_with(T_CAUT, caution))
        c2.append(copy.deepcopy(T_CAUT_END))
    if equip:
        c2.append(copy.deepcopy(T_EQHEAD))
        for e in equip:
            c2.append(clone_with(T_EQITEM, e))
        c2.append(copy.deepcopy(T_EQEND))
    new_rows.append(r)
for r in reversed(new_rows):
    anchor_prev = tbl_steps  # placeholder
for r in new_rows:
    tbl_steps.append(r)

# ---------- 5. Referenced documents ----------
ref = [e for e in body if e.tag == q('tbl') and 'Referenced Documents' in ''.join(e.itertext())][0]
rrows = ref.findall('w:tr', ns)
tmpl_row = rrows[2]
for r in rrows[2:]:
    ref.remove(r)
refs = C['REFS']
for a, b_ in refs:
    r = copy.deepcopy(tmpl_row)
    tcs = r.findall('w:tc', ns)
    set_text(tcs[0], a)
    set_text(tcs[1], b_)
    ref.append(r)

# ---------- 6. Emergency page (last table) ----------
em = [e for e in body if e.tag == q('tbl') and '1. HCN Gas Alarm' in ''.join(e.itertext())][0]
em_cell = em.findall('w:tr', ns)[1].findall('w:tc', ns)[0]
eps = em_cell.findall('w:p', ns)
E_BLANK, E_TXT = eps[0], eps[1]
for p in eps:
    em_cell.remove(p)
emerg = C['EMERG']
for t in emerg:
    em_cell.append(copy.deepcopy(E_BLANK))
    em_cell.append(clone_with(E_TXT, t))
em_cell.append(copy.deepcopy(E_BLANK))

# ---------- write + zip ----------
tree.write(os.path.join(OUT_X, 'word/document.xml'), xml_declaration=True, encoding='UTF-8', standalone=True)
if os.path.exists(OUT_DOCX):
    os.remove(OUT_DOCX)
subprocess.check_call(['zip', '-Xqr', os.path.abspath(OUT_DOCX), '[Content_Types].xml', '_rels', 'docProps', 'word', 'customXml'], cwd=OUT_X)
print('built', OUT_DOCX)
