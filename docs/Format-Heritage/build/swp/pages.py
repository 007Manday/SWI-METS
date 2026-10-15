"""Find the PDF page of every heading. Usage: pages.py doc.pdf toc.json out.json"""
import json, re, subprocess, sys
pdf, tocf, out = sys.argv[1:4]
toc = json.load(open(tocf))
n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
pages = [subprocess.run(['pdftotext', '-layout', '-f', str(i), '-l', str(i), pdf, '-'], capture_output=True, text=True).stdout for i in range(1, n + 1)]
start = max(i for i, t in enumerate(pages) if 'Table of Contents' in t or re.search(r'\.{10,}', t)) + 1
res, cur = {}, start
for lvl, num, text, name in toc:
    pat = re.compile(r'^\s*%s\s+%s\s*$' % (re.escape(num), re.escape(text)), re.M)
    for i in range(cur, n):
        if pat.search(pages[i]):
            res[name] = i + 1; cur = i; break
    else:
        sys.exit('heading not found: %s %s' % (num, text))
json.dump(res, open(out, 'w'), indent=0)
