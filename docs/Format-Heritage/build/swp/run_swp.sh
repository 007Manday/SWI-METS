#!/bin/bash
# Build one Heritage SWP in two passes so the table of contents carries real page numbers.
# Usage: run_swp.sh old.docx out_dir
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
SRC=$1; OUTD=$2
NAME=$(basename "$SRC" | sed 's/^[0-9a-f]\{8\}-//')
N=$(echo "$NAME" | grep -o 'SWP-2[0-9][0-9]')
mkdir -p "$OUTD"
python3 "$HERE/build_swp.py" "$SRC" "${TPL_X:-$HERE/../swp_tpl/x}" "$HERE/w$N" "$OUTD/$NAME" >/dev/null
(cd "$OUTD" && soffice --headless --convert-to pdf "$NAME" >/dev/null 2>&1)
python3 "$HERE/pages.py" "$OUTD/${NAME%.docx}.pdf" "$OUTD/$NAME.toc.json" "$HERE/pages_$N.json"
python3 "$HERE/build_swp.py" "$SRC" "${TPL_X:-$HERE/../swp_tpl/x}" "$HERE/w$N" "$OUTD/$NAME" "$HERE/pages_$N.json"
(cd "$OUTD" && soffice --headless --convert-to pdf "$NAME" >/dev/null 2>&1)
python3 "$HERE/pages.py" "$OUTD/${NAME%.docx}.pdf" "$OUTD/$NAME.toc.json" "$HERE/pages_${N}_check.json"
cmp -s "$HERE/pages_$N.json" "$HERE/pages_${N}_check.json" && echo "$N TOC pages stable" || echo "$N TOC pages CHANGED"
rm -f "$OUTD/$NAME.toc.json"
