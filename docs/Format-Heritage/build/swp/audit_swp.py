"""Every text fragment of the old SWP must appear in the new one (whitespace-normalised)."""
import sys, zipfile, re, glob
from lxml import etree
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
def frags(path, cells=True):
    r=etree.fromstring(zipfile.ZipFile(path).read('word/document.xml'))
    return [re.sub(r'\s+',' ',''.join(x.text or '' for x in p.iter(W+'t'))).strip() for p in r.iter(W+'p')]
for old in sorted(glob.glob(sys.argv[1] if len(sys.argv)>1 else '../swp_in/*.docx')):
    n=re.search(r'SWP-2\d\d',old).group(0)
    new=glob.glob((sys.argv[2] if len(sys.argv)>2 else 'out')+'/*%s*.docx'%n)[0]
    alltext=' '.join(frags(new))
    norm=lambda s: re.sub(r'\s+',' ',s.replace('  ·  ',', ')).strip()
    allt=norm(alltext)
    miss=[f for f in frags(old) if f and norm(f) not in allt]
    print('==',n,len(miss))
    for m in miss: print('   ',m[:170])
