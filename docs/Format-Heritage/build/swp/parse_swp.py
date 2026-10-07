"""Parse an old-format SWP into a dict of sections (JSON)."""
import sys, zipfile, json, re
from lxml import etree
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
def t(e): return ''.join(x.text or '' for x in e.iter(W+'t')).strip()
def cells(tc):  # paragraphs inside a cell
    return [t(p) for p in tc.iter(W+'p') if t(p)]
r=etree.fromstring(zipfile.ZipFile(sys.argv[1]).read('word/document.xml'))
body=r.find(W+'body')
d={'info':{}, 'sec':{}}
cur=None; sub=None
for el in body:
    if el.tag==W+'p':
        s=el.find('.//'+W+'pStyle'); s=s.get(W+'val') if s is not None else ''
        x=t(el)
        if not x: continue
        if s=='Heading1':
            cur=re.sub(r'^\d+\s+','',x); d['sec'][cur]=[]; continue
        if cur is None: continue
        d['sec'][cur].append(('li' if s=='ListParagraph' else 'p', x))
    elif el.tag==W+'tbl':
        rows=[[cells(tc) for tc in tr.findall(W+'tc')] for tr in el.iter(W+'tr')]
        if cur is None:
            for row in rows: d['info'][' '.join(row[0])]=' '.join(row[1])
        else:
            d['sec'][cur].append(('tbl', rows))
json.dump(d, open(sys.argv[2],'w'), indent=1, ensure_ascii=False)
