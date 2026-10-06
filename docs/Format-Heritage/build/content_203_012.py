import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '203-012'
TITLE = 'Oxygen Utilisation and Sparger Performance Survey'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc203(['Measure how much of the oxygen injected into the leach is actually being used, and whether the spargers are delivering it.',
                'Oxygen is a direct input to gold dissolution. A blocked or worn sparger costs recovery quietly.'],
               '203 Plant Surveys', ['031-TK-001 - Leach tank, oxygen spargers', 'Hypersparge - supersonic gas spargers DN15 and DN25'],
               'Quarterly, and after any sparger clean or replacement.', NUM)
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Oxygen flow not recorded'],
     prestart203(NEW_JSEA, ['Record the oxygen supply pressure and flow to each sparger from the control system.']), None,
     ['DO meter, calibrated', 'Sample containers', 'Stopwatch', 'Field data sheets', 'Oxygen flow readings from the control system', PPE_EQ]),
    ('Dissolved Oxygen Measurement', ['HCN released at the sample point', 'Fall from the tank top', 'DO changed by atmospheric exchange', 'Single reading describing the tank'],
     ['Measure dissolved oxygen at several depths and positions in the tank, not at one point. A single reading at the launder does not describe the tank.',
      'Take the DO reading immediately on sampling - atmospheric exchange starts as soon as the sample is drawn.'], CAUTION_VALVE, None),
    ('Utilisation and Sparger Check', ['Release from a pressurised line or fitting', 'Sparger below design pressure not noticed'],
     ['Calculate oxygen utilisation from the injected flow and the measured dissolved oxygen against the consumption implied by the leach rate.',
      'Compare the sparger operating pressure against the Hypersparge instructions. A sparger operating below its design pressure is not atomising.',
      'Inspect the sparger condition against the vendor criteria where access allows.'], None, None),
    ('Survey Report', ['Sparger due for cleaning not reported'],
     ['Report utilisation, the DO profile and any sparger due for cleaning or replacement.'], None, None),
    CLOSE203_STEP,
]
REFS = refs203(NUM, TITLE, [('4034-044-VE-003 Rev B', 'Glencore Hypersparge supersonic gas sparger installation and operating instructions, received 11 Aug 2026'),
    ('KBK-MIR-MP-PRO-MET-SOP-0046', 'Pengukuran Oksigen Terlarut, received 11 Aug 2026'),
    ('HM-PRC-V01-PRO004', 'Leach Circuit'),
    ('SWI-PRO-OPR-031-004', 'Oxygen Sparger Inspection and Cleaning')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'fall'])
