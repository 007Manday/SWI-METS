import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '204-013'
TITLE = 'Grind Establishment Test'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_HEAR
DESC = desc204(['Establish the grind time needed to reach a target P80 on a given ore.', 'It is the bench test behind every grind target and every liberation decision.'], 'On each new ore type, and when a change to the grind target is proposed.', NUM, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA), None, ['Laboratory mill and charge', 'Sieve set and Ro-Tap', 'Balance', 'Drying oven', 'Stopwatch', 'Riffle splitter'] + [PPE_EQ]),
    ('Charge Preparation', ['Charges not equal', 'Dust from the dry sample'], ['Split the sample into equal charges, one per grind time.', 'Determine the feed size distribution on one charge.'], None, None),
    ('Grinding and Sizing', ['Contact with the rotating mill', 'Hearing damage at the mill', 'Conditions changed between charges'], ['Grind each charge for a different time under identical conditions - same charge, same solids, same speed.', 'Wet screen, dry and size each product.'], 'CAUTION: Stop and isolate the mill before opening it. Wear hearing protection.', None),
    ('Grind Curve and Recovery', ['Target read from the wrong curve'], ['Plot P80 against grind time.', 'Read the grind time for the target P80 off the curve.', 'Where a liberation or recovery target is being set, run a bottle roll on each grind product and plot recovery against P80.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs204(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0012', 'Uji Pengujian Grind Establishment'), ('KBK-MIR-MP-PRO-MET-SOP-0027', 'Grinding Survey, received 11 Aug 2026')])
EMERG = emerg(['equip', 'cn', 'skin', 'slip'], 'the mill or shaker')
