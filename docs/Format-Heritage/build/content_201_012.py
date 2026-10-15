import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '201-012'
TITLE = 'Loaded and Barren Resin Sampling at Screens and Hoppers'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc(['Set the metal loading on resin leaving adsorption and the residual loading on resin returning from elution.',
             'The loaded-to-barren pair is the direct measure of elution efficiency on the resin circuit.'],
            '041 / 051 / 071 / 081 Resin circuits',
            ['041-SC-004 / 041-SC-016 - Metal adsorption resin recovery and safety screens',
             '051-SC-005 / 051-SC-006 / 051-SC-020 - Cyanide adsorption resin screens',
             '041-HP-017 - Metal loaded resin hopper'],
            'Every resin transfer, both directions.', '201-012')
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Resin transfer direction not known'],
     prestart(NEW_JSEA, ['Confirm with the control room that a resin transfer is in progress and which direction it is running.']), None,
     ['Sample scoop or cutter', '0.9 mm sieve', 'Sample bottles, labelled', 'Process water hose', PPE_EQ]),
    ('Sample Collection', ['HCN released at the open sample point', 'Splash of cyanide-bearing slurry', 'Fall from height at the screen or hopper', 'Equipment starting without warning'],
     ['Sample the screen oversize as the resin discharges, taking increments across the whole transfer rather than one grab.'],
     CAUTION_VALVE, None),
    ('Washing and Submission', ['Resin not washed free of slurry', 'Sample not traceable to the transfer'],
     ['Wash the resin free of slurry over the 0.9 mm sieve.',
      'Bottle, label with the transfer number and direction, and submit to the laboratory.',
      'Record transfer number, direction, volume and time against the sample.'], None, None),
    CLOSE_STEP,
]
REFS = refs('201-012', TITLE, [('Mt. Morgan site procedure 9', 'Metal Elution Sampling [LIVE] - covers part of this task'),
    ('KBK SOP-PROC-CNREC-01, -04, -06 and -07', 'Resin transfer procedures, received 11 Aug 2026'),
    ('KBK-MIR-MP-PRO-MET-SOP-0049 and SOP-0058', 'Resin sampling and particle size procedures, received 11 Aug 2026'),
    ('4034-004-VE-025 Rev B', 'Goldquip vibrating screen IOM, received 11 Aug 2026')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'fall', 'slip'], 'the screen, a pump or a sample cutter')
