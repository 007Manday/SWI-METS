"""Read hazard rows from an original SWI docx so the hazard text is copied, not retyped."""
import zipfile
from lxml import etree
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
def hazards_from(path):
    root = etree.fromstring(zipfile.ZipFile(path).read('word/document.xml'))
    ns = {'w': W}
    for tbl in root.iter('{%s}tbl' % W):
        rows = tbl.findall('w:tr', ns)
        cells0 = [''.join(c.itertext()).strip() for c in rows[0].findall('w:tc', ns)]
        if cells0 == ['Hazard', 'Control']:
            out = []
            for r in rows[1:]:
                a, b = [''.join(c.itertext()).strip() for c in r.findall('w:tc', ns)]
                out.append('%s — %s' % (a, b))
            return out
    raise SystemExit('hazard table not found')
