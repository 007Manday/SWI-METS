"""Audit: check every paragraph of the pre-conversion SWI (which carries the agreed Martabe updates)
against the Heritage-format SWI. Prints paragraphs whose content cannot be found in the new file.
Usage: python audit_vs_source.py <base_commit> <out.json> [code ...]
<base_commit> is the commit before the first Heritage conversion (all SWIs still in the old format)."""
import glob, json, re, subprocess, sys, zipfile, io
from lxml import etree

BASE, OUT = sys.argv[1:3]
ONLY = set(sys.argv[3:])
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
STOP = set('the and for are with from that this not any was its into each all has have been than then where which when what will'
           ' must only per out off one two before after there their them they shall can may other more over under also such'.split())

def paras(data):
    root = etree.fromstring(zipfile.ZipFile(io.BytesIO(data)).read('word/document.xml'))
    out = []
    for p in root.iter('{%s}p' % W):
        t = ''.join(x.text or '' for x in p.iter('{%s}t' % W)).strip()
        if t:
            out.append(t)
    return out

def toks(s):
    s = s.lower().replace('—', ' ').replace('–', ' ')
    return [w for w in re.findall(r'[a-z0-9][a-z0-9.\-/]*[a-z0-9]|[a-z0-9]', s) if len(w) > 2 and w not in STOP]

SKIP = re.compile(r'^(\d+ [A-Z][A-Z ]+|Hazard|Control|Tag / point|Description|Document number|JSEA reference|Area|Parent procedure|'
                  r'Classification|Revision|Date|Prepared by|Reviewed by|Approved by|Rev A|11 August 2026|GGT \(cost code 4034-033\)|_+|'
                  r'Mt\. Morgan SITE WORK INSTRUCTION|Standard Work Instruction .*|Every item below must be true.*|Equipment required:|'
                  r'Part [A-D] - .*|Points and equipment covered:|Safety-critical|Operating)$')

files = sorted(glob.glob('SWI/201-Plant-Sampling/*.docx') + glob.glob('SWI/203-Plant-Survey/*.docx'))
report = {}
for f in files:
    code = re.search(r'MET-(\d{3}-\d{3})', f).group(1)
    if ONLY and code not in ONLY:
        continue
    old = paras(subprocess.run(['git', 'show', '%s:%s' % (BASE, f)], capture_output=True).stdout)
    new = paras(open(f, 'rb').read())
    new_t = [set(toks(p)) for p in new]
    new_all = set().union(*new_t)
    missing = []
    for p in old:
        if SKIP.match(p):
            continue
        t = toks(p)
        if len(t) < 3:
            continue
        ts = set(t)
        best = max(len(ts & n) / len(ts) for n in new_t)
        whole = len(ts & new_all) / len(ts)
        if best < 0.75:
            missing.append({'text': p, 'best_para': round(best, 2), 'whole_doc': round(whole, 2),
                            'martabe': '[M]' in p or '[CONFIRM]' in p})
    report[code] = missing
    print('%s  old paras %3d  not found %2d  (of which Martabe/[CONFIRM] %d)' % (
        code, len(old), len(missing), sum(m['martabe'] for m in missing)))
json.dump(report, open(OUT, 'w'), indent=1, ensure_ascii=False)
