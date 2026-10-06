import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '203-011'
TITLE = 'Carbon and Resin Loss Quantification Survey'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc203(['Account for total carbon and resin loss across the whole circuit over a period, and locate where it is going.',
                'The screen check finds losses at screens. This survey finds the rest - launders, spillage, transfers, attrition and the tailings line.'],
               '203 Plant Surveys', ['032 / 041 / 051 - Adsorption and CIL circuits', '051 - Tails thickener and tailings line', 'Sumps and launders - spillage recovery points'],
               'Quarterly, and whenever the inventory reconciliation shows an unexplained loss.', NUM)
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Reconciliation gap not known'],
     prestart203(NEW_JSEA, ['Take the inventory reconciliation for the period as the starting point - it says how much is missing.']), None,
     ['Sample containers', 'Sieves 1 mm and 0.9 mm', 'Drying tray and balance', 'Field data sheets', PPE_EQ]),
    ('Stream Sampling', ['HCN released at the open sample point', 'Splash of cyanide-bearing slurry', 'Fall from a launder platform', 'A loss stream not sampled'],
     ['Sample every stream leaving the circuit that could carry carbon or resin: screen undersizes, thickener overflow and underflow, the tailings line, and any launder or sump overflow.'], CAUTION_VALVE, None),
    ('Recovery and Weighing', ['Carbon or resin lost during recovery', 'Cross-contamination between streams'],
     ['Recover, dry and weigh carbon and resin from each stream.'], None, None),
    ('Attrition and Loss Accounting', ['Attrition estimated from one measurement', 'Unrecorded movement or spillage route missed'],
     ['Estimate attrition from the bead and particle size distribution trend rather than from a single measurement.',
      'Add the located losses and compare against the reconciliation gap.',
      'Where the located loss does not account for the gap, look for an unrecorded movement or a spillage route before concluding it is attrition.'], None, None),
    ('Survey Report', ['Registers not updated'],
     ['Report by location so the fix can be targeted, and update RA-01 and RA-02.'], None, None),
    CLOSE203_STEP,
]
REFS = refs203(NUM, TITLE, [('RA-01 and RA-02', 'Resin Loss Register and Carbon Contamination Register Rev A, and their study reports'),
    ('MM-4034-033-RES', 'Resin Line Schedule (268 lines)'),
    ('KBK-MIR-MP-PRO-MET-SOP-0058', 'Distribusi Ukuran Partikel Resin, received 11 Aug 2026')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'fall', 'slip'], 'an agitator, pump or screen')
