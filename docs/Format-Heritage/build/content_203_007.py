import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '203-007'
TITLE = 'Thickener Performance Survey - Flux, Bed Level and Flocculant Response'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc203(['Measure what the thickeners are actually doing - solids flux, bed level behaviour, underflow density and how they respond to flocculant.',
                'A thickener that is not making underflow density costs water, and one that is losing solids to overflow costs metal and puts solids into process water.'],
               '203 Plant Surveys', ['051-TH-006 - Tails thickener', '071 - Copper precipitate thickener', '106 - Flocculant plants, Model 01 and Model 05'],
               'Quarterly, and whenever overflow clarity or underflow density moves.', NUM)
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Thickener not at steady state'], prestart203(NEW_JSEA), None,
     ['Sampling buckets', 'Marcy scale', 'TSS meter or filter set', 'Settling cylinders', 'Stopwatch', 'Field data sheets', PPE_EQ]),
    ('Steady-State Record and Sampling', ['HCN released at the open sample point', 'Splash of cyanide-bearing slurry', 'Fall from the launder platform', 'Samples not taken at the same moment'],
     ['Record the thickener at steady state - feed rate, feed density, bed level, rake torque, underflow rate and flocculant dose.',
      'Sample feed, overflow and underflow simultaneously.',
      'Determine feed and underflow density on the Marcy scale and overflow suspended solids.'], CAUTION_VALVE, None),
    ('Solids Flux', ['Flux compared with the wrong design value'],
     ['Calculate solids flux and compare against the design flux from the Roytec control philosophy.'], None, None),
    ('Settling and Flocculant Dose Tests', ['Dose varied outside the agreed range', 'Response read before the change has settled'],
     ['Run a settling test on the feed at the current flocculant dose and at two other doses, and record the settling rate for each.',
      'Vary the flocculant dose within the agreed range and record the overflow clarity response after each change has settled.'], None, None),
    ('Survey Report', ['Optimum dose reported without data'],
     ['Report the optimum dose, the achieved flux and any deviation from the vendor design basis.'], None, None),
    CLOSE203_STEP,
]
REFS = refs203(NUM, TITLE, [('Tail Thickener and Cu Thickener Field Operator Procedures', 'Site procedures'),
    ('4034-018A-VE-007 and 4034-018A-VE-045', 'Roytec tails thickener control philosophy and IOM, received 11 Aug 2026 - rake torque, bed level and underflow density limits'),
    ('4034-019-VE-006 and 4034-019B-VE-007', 'Roytec Model 01 and Model 05 flocculant control philosophies, received 11 Aug 2026'),
    ('KBK-MIR-MP-PRO-OPE-SOP-0014', 'Settling Test'),
    ('HM-PRC-V01-PRO008 and PRO016', 'Tails thickener and copper circuit procedures')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'fall', 'slip'], 'an agitator, rake, pump or sample cutter')
