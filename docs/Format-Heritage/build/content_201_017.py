import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '201-017'
TITLE = 'Tails Thickener Feed, Overflow and Underflow Sampling'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = [h for h in hazards_from(os.environ['SRC_DOCX']) if not h.startswith('[JSEA to confirm]')]
PPE = PPE_STD
DESC = desc(['Set the thickener feed, overflow and underflow solids and assay.',
             'Overflow solids is the direct measure of whether flocculation is working. Underflow density sets the tailings pumping duty.'],
            '051 Tails Thickener',
            ['051-TH-006 - Tails thickener, feed, overflow launder and underflow', 'Flocculant dosing - dose rate read at the time of sampling'],
            'Hourly on overflow and underflow; each shift on feed.', NUM)
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Thickener in a bed upset'],
     prestart(NEW_JSEA, ['Confirm the thickener is at steady bed level and rake torque before sampling - a sample taken during a bed upset is not representative.']), None,
     ['Sampling bucket 5 to 8 L', 'Marcy scale', 'pH meter', 'TSS meter or filter set for overflow', 'Filter press and filter paper', 'Bottles 250 mL', 'Spatula', PPE_EQ]),
    ('Sample Collection', ['HCN released at the open sample point', 'Splash of cyanide-bearing slurry', 'Fall from the launder platform', 'Weir turbulence in the overflow sample'],
     ['Take the overflow sample from the launder, clear of the weir turbulence.',
      'Take the underflow sample from the designated valve on the underflow line, flushing first.'], CAUTION_VALVE, None),
    ('Solids, pH and Cyanide', ['Flocculation failure not noticed', 'Cyanide volatilising from the overflow sample'],
     ['Determine per cent solids on the underflow with the Marcy scale.',
      'Determine suspended solids on the overflow - the overflow should be clear; visible solids means flocculation has failed and is reported immediately.',
      'Determine pH and free cyanide on the overflow, because the overflow returns to process water.'],
     'CAUTION: Visible solids in the overflow means flocculation has failed. Report it to the Shift Supervisor immediately.', None),
    ('Operating Data', ['Operating conditions not recorded against the samples'],
     ['Record bed level, rake torque, underflow flow and flocculant dose rate at the time of sampling.'], None, None),
    CLOSE_STEP,
]
REFS = refs(NUM, TITLE, [('HM-PRC-V01-PRO008', 'Tails Thickener and Tailings Disposal'),
    ('Mt. Morgan site procedure 23', 'Slurry Tail Sampling [LIVE]'),
    ('Tail Thickener Field Operator Procedure', 'Site procedure'),
    ('4034-018A-VE-007 Rev 0', 'Roytec tails thickener functional specification and control philosophy (051-TH-006), received 11 Aug 2026'),
    ('4034-018A-VE-045 Rev A', 'Roytec 25 m tailings thickener IOM, received 11 Aug 2026'),
    ('4034-019B-VE-007 Rev A', 'Roytec Model 05 continuous flocculant plant control philosophy, received 11 Aug 2026')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'fall', 'slip'], 'an agitator, rake, pump or sample cutter')
