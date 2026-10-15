import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '201-011'
TITLE = 'Resin Concentration Measurement in Adsorption Tanks'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc(['Set the resin concentration in each adsorption tank in millilitres of resin per litre of slurry, which is the control on resin inventory.',
             'Give early warning of resin loss, which is the single largest consumable risk on a ReCYN circuit.'],
            '041 / 051 Adsorption',
            ['041-TK-007 / 041-TK-008 - Metal adsorption tanks', '051-TK-009 / 051-TK-010 - Cyanide adsorption tanks'],
            'Once per shift on every adsorption tank.', '201-011')
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Cutter or container carrying resin from the previous tank'],
     prestart(NEW_JSEA, ['Flush the cutter, sieve and container with process water so no resin carries over from the previous tank.'], rinse=False), None,
     ['Sample cutter', '0.9 mm sieve', 'Measuring glass, graduated', '1 litre measuring container', 'Process water hose', PPE_EQ]),
    ('Sampling and Resin Volume', ['HCN released at the open sample point', 'Splash of cyanide-bearing slurry', 'Fall from the tank top', 'Cross-contamination between tanks'],
     ['Take a 1 litre sample with the sample cutter.',
      'Strain the resin from the slurry through the 0.9 mm sieve.',
      'Wash the retained resin free of slurry.',
      'Measure the drained resin volume in the graduated measuring glass and record it as millilitres per litre.',
      'Repeat for every adsorption tank, cleaning between each.'],
     CAUTION_VALVE, None),
    ('Resin Profile', ['Profile not recorded', 'Resin loss not noticed'],
     ['Record the profile and compare it against the resin inventory in the resin line schedule.'], None, None),
    CLOSE_STEP,
]
REFS = refs('201-011', TITLE, [('Mt. Morgan site procedure 7', 'Resin Concentration Sampling [LIVE]'),
    ('KBK-MIR-MP-PRO-MET-SOP-0058', 'Distribusi Ukuran Partikel Resin, received 11 Aug 2026'),
    ('RA-01', 'Resin Loss Register Rev A'),
    ('MM-4034-033-RES', 'Resin Line Schedule (268 lines)')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'fall', 'slip'])
