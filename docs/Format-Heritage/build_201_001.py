"""Build SWI-PRO-MET-201-001 in Heritage format, using the heritage 304-008 docx as template."""
import copy, os, re, shutil, subprocess, sys
from lxml import etree

SRC_X, OUT_X, OUT_DOCX = sys.argv[1], sys.argv[2], sys.argv[3]
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
ns = {'w': W}
q = lambda t: '{%s}%s' % (W, t)

OLD_TITLE = 'WAD Cyanide - Distillation and Determination'
NEW_TITLE = 'Front-End Sampling Round - Scrubber Discharge Hopper and Trash Screen'
NEW_ID = 'SWI-PRO-MET-201-001'
NEW_JSEA = 'JSEA-PRO-MET-201-001'

if os.path.exists(OUT_X):
    shutil.rmtree(OUT_X)
shutil.copytree(SRC_X, OUT_X)

# ---------- 1. global identity swap (header, footer, core props, cover) ----------
def swap(path):
    s = open(path, encoding='utf8').read()
    s = s.replace(OLD_TITLE, NEW_TITLE).replace('PRO-LAB-304-008', 'PRO-MET-201-001')
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
ppe = [
    'Safety helmet and safety glasses',
    'Chemical splash goggles and face shield',
    'High-visibility long-sleeved shirt and long trousers',
    'Safety boots with sound tread - nitrile PVC boots at the sample point',
    'Chemical resistant suit, nitrile rubber gloves and apron',
    'Hearing protection - double protection at the mill and compressor',
    'Personal HCN gas monitor, calibrated and in test date',
    'Full or half gas mask with A2B2E2K2P3 cartridge, carried and available for immediate use',
]
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

desc = [
    ('n', 'Set the scrubber mill discharge passing grade (P80).'),
    ('n', 'Set the scrubber mill discharge solids percentage.'),
    ('n', 'Set the scrubber mill discharge pH, which is the check that lime addition is neutralising the tailings ore before the slurry reaches downstream equipment.'),
    ('b', None),
    ('n', 'Area: 021 Scrubber.'),
    ('n', 'Points and equipment covered:'),
    ('n', '021-ML-001 - Rotary scrubber, discharge'),
    ('n', '021-SC-001 - Trash screen, undersize'),
    ('n', '021-PP-123 / 021-PP-124 - Scrubber discharge pumps, sample taken downstream'),
    ('n', 'AIT-021002 - Density transmitter downstream of the discharge pumps, read at the time of sampling'),
    ('b', None),
    ('n', 'Frequency: Hourly spot sample, composited to four 12-litre composites per shift.'),
    ('b', None),
    ('n', 'This instruction sits under Standard Work Procedure HM-PRC-VXX-PRO205 - Plant Sampling and Metallurgical Data Collection. Read that procedure before carrying out this task for the first time.'),
    ('b', None),
    ('n', 'Register line: SWI-PRO-MET-201-001 in HM-MMM-WHS-REG-XXX-R00-SWI-SWMS, tab SWI-MET. The matching hazard analysis is JSEA-PRO-MET-201-001.'),
]
for p in dps:
    desc_cell.remove(p)
for kind, txt in desc:
    if kind == 'b':
        desc_cell.append(copy.deepcopy(P_BLANK))
    else:
        desc_cell.append(mk(P_NORMAL, txt))

# potential hazards
haz_cell = cell(rows[6], 1)
hps = haz_cell.findall('w:p', ns)
H_NORMAL, H_BLANK, H_ITAL = hps[0], hps[1], hps[-1]
hazards = [
    'Hydrogen cyanide gas released at the open sample point — Personal HCN monitor worn, switched on and in calibration date. Fixed detection healthy - alarm 5 ppm, high-high 10 ppm. Sample point approached from upwind. Stream pH confirmed above 10.5 before opening. Second person in sight and clear. Antidote kit on site and a trained first aider on shift. Withdraw upwind and report any reading above the site action level.',
    'Splash of cyanide-bearing slurry or solution to skin or eyes — Sample valve opened slowly with the container positioned first and the body out of the spray path. Face shield, chemical splash goggles, chemical-resistant gloves and apron. Never open a sample valve whose discharge cannot be seen. Safety shower and eyewash proven flowing before the round starts.',
    'Contact with an agitator, sample cutter, pump or screen that starts without warning — Plant is largely automated. Guards confirmed in place before approaching. Control room notified before the round starts and again on completion. Isolation and lock-out before any guard or cutter housing is opened.',
    'Hearing damage in the mill, screen, compressor and blower areas — Hearing protection mandatory in signed areas. Double protection at the mill and compressor. Time at the point kept to what the task needs.',
    'Slip, trip or fall on wet or slurry-covered walkways around sample points — Spillage cleaned up immediately and the point left clean. Walkways kept clear of hoses, buckets and containers. Safety boots with sound tread. Damaged or missing grating reported before use.',
    'Manual handling injury from carrying sample buckets, containers and composite drums — Sample volume kept to the schedule, no over-filling. Two-person lift or a trolley for composite containers above the site manual handling limit. Route cleared before lifting.',
    'Non-representative sample leading to a wrong process decision — Line flushed for the stated time before collecting. Sample taken at the same point, in the same way and at the same frequency every time. Container labelled BEFORE sampling with point, date, time and shift. Steady-state confirmed for 15 to 20 minutes before sampling. A sample taken off-condition is marked as such or discarded.',
    'Cross-contamination from a container or cutter not cleaned between points — Bucket, container, cutter and sieve rinsed with process water and then with the stream being sampled, and the rinse discarded, before every sample. Dedicated containers for high-grade streams. Labels checked against the schedule before handover.',
]
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

steps = [
    ('Pre-start Check',
     ['Plant not at steady state', 'Gas monitor or fixed detection not healthy',
      'Safety shower or eyewash not proven flowing', 'Control room not aware the round is starting'],
     ['Confirm you are trained and signed off against this SWI, signed on to %s at a communication session, and authorised by the Shift Supervisor.' % NEW_JSEA,
      'Confirm the plant is in steady-state operation - normal operation for a minimum of 15 to 20 minutes before sampling. A sample taken during a swing is not representative.',
      'Notify the control room or DCS operator that the sampling round is starting, and which points it covers.',
      'Confirm the personal gas monitor is on, in calibration date and reading clean, and that fixed detection in the area is healthy.',
      'Confirm the safety shower and eyewash nearest the point are within reach and proven flowing.',
      'Label every container BEFORE sampling - point, date, time and shift.',
      'Rinse the container, cutter or sieve with process water and then with the stream being sampled. Discard the rinse.'],
     None,
     ['Sampling bucket 5 to 8 L', 'pH meter', 'Marcy scale', '212 um sieve', '150 um sieve', '106 um sieve',
      'Pan sieve', 'Filter press and filter paper', 'Spatula', 'Personal protective equipment as listed in PPE Requirements']),
    ('Sample Collection',
     ['HCN released at the open sample point', 'Splash of cyanide-bearing slurry',
      'Equipment starting without warning', 'Container not clean or not labelled'],
     ['Collect 4 litres of slurry from the scrubber discharge sample point, discarding the first 5 to 10 seconds of flow as a line flush.',
      'Stir the sample thoroughly with the spatula, then split 2 litres for the operator determinations and 2 litres for the laboratory.'],
     'CAUTION: Open the sample valve slowly, with the container positioned first and the body out of the spray path. Never open a valve whose discharge cannot be seen.',
     None),
    ('Instrument Reading and pH',
     ['Instrument reading not recorded against the sample', 'Meter out of calibration - wrong pH'],
     ['Read AIT-021002 at the moment of sampling and record it against the sample.',
      'Determine pH on the operator split. Calibrate the meter once per shift against pH 4, 7 and 10 buffers.',
      'Rinse the electrode, immerse fully and wait about 30 seconds for a stable reading. Record the value and temperature.'],
     None, None),
    ('Per Cent Solids',
     ['Scale not zeroed - wrong per cent solids', 'Spillage on the walkway - slip hazard'],
     ['Zero the Marcy scale with the empty dry 1 litre container.',
      'Rinse the container with the sample and discard the rinse.',
      'Fill the container to the 1 litre mark and wipe the outside dry.',
      'Hang the container and read the inner scale. Record the value.'],
     None, None),
    ('Sizing (P80) and Compositing',
     ['Sieves not rinsed between samples - cross-contamination', 'Composite container too heavy to carry alone'],
     ['Screen the sizing split through the 212, 150 and 106 um sieves and the pan.',
      'Record the mass retained on each to give the P80.',
      'Add the laboratory split to the running composite and record the volume added.'],
     'CAUTION: Use a two-person lift or a trolley for composite containers above the site manual handling limit.',
     None),
    ('Completion and Clean Up',
     ['Sample valve left weeping', 'Samples not handed over with a signed record',
      'Control room not told the round is complete'],
     ['Close the sample valve or stop the sample pump and confirm the point is not weeping.',
      'Wash down the point and the surrounding walkway. Leave nothing on the grating.',
      'Record sampling time, operator name and the operating conditions read at the time - flow, density and any instrument value available.',
      'Deliver the labelled samples to the laboratory or to the composite station as the schedule requires, and sign the handover.',
      'Notify the control room that the round is complete.',
      'Record the result, the method used and the instrument or balance identity on the field or bench data sheet - date, time, shift, operator and every value determined. Make the register or logbook entry and any handover signature.',
      'Record any step not completed, with the reason.',
      'Report to the Shift Supervisor, and record, any control in Part 2 found not in place.'],
     None, None),
]

# numbering: step i letter list uses numId 15+i (15..19 exist, 20 is added)
num_path = os.path.join(OUT_X, 'word/numbering.xml')
ntree = etree.parse(num_path); nroot = ntree.getroot()
src_num = [n for n in nroot.findall('w:num', ns) if n.get(q('numId')) == '19'][0]
new_num = copy.deepcopy(src_num); new_num.set(q('numId'), '20')
src_num.addnext(new_num)
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
refs = [
    ('HM-PRC-VXX-PRO205', 'Plant Sampling and Metallurgical Data Collection'),
    (NEW_JSEA, 'JSEA — %s' % NEW_TITLE),
    ('HM-MMM-WHS-REG-XXX-R00-SWI-SWMS', 'SWI / SWMS Register — tab SWI-MET'),
    ('HM-PRC-V01-PRO002', 'Scrubber and Trash Screening Circuit'),
    ('Mt. Morgan site procedure 1', 'Scrubber Mill Discharge Sampling [LIVE]'),
    ('4034-PR-PRO-002', 'Sampling Protocol'),
    ('4034-002-VE-025 Rev A', 'McLanahan rotary scrubber IO&M (021-ML-001), received 11 Aug 2026'),
    ('4034-004-VE-025 Rev B', 'Goldquip vibrating screen IOM (021-SC-001), received 11 Aug 2026'),
]
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
emerg = [
    '1. HCN Gas Alarm If the personal monitor or fixed detection alarms (5 ppm alarm, 10 ppm high-high), stop work, leave the area upwind and call CH19 “EMERGENCY”. Do not re-enter until the Shift Supervisor clears the area.',
    '2. Contact with Moving Equipment If a person is caught by or struck by an agitator, sample cutter, pump or screen, hit the nearest emergency stop, call CH19 “EMERGENCY” and call 000. Do not approach the equipment until it is isolated and locked out.',
    '3. Suspected Cyanide Exposure If a person becomes dizzy, short of breath or collapses, call CH19 “EMERGENCY”, call 000, and bring the cyanide antidote kit and a trained first aider. Do not give mouth-to-mouth resuscitation.',
    '4. Skin or Eye Contact with Slurry Flush with copious water at the safety shower or eyewash for a minimum of 15 minutes. Remove contaminated clothing while flushing. Report to the first aider.',
    '5. Slip, Fall or Lifting Injury Do not move the injured person unless they are in danger. Call CH19 “EMERGENCY”, call 000 if the injury is serious, and notify the Shift Supervisor.',
]
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
