import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '201-006'
TITLE = 'Loaded Carbon Sampling at Loaded Carbon Screen 032-SC-002'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc(['Set the gold loading on carbon leaving the CIL circuit, in grams per tonne.',
             'This is the number the elution batch is sized against, and the input to carbon inventory accounting.'],
            '032 Carbon in Leach', ['032-SC-002 - Loaded carbon screen, feed and oversize'],
            'Every carbon transfer, and at least once per shift while transfers are running.', '201-006')
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Carbon transfer not in progress'],
     prestart(NEW_JSEA, ['Confirm with the control room that a carbon transfer is in progress or about to start.']), None,
     ['Sample scoop or cutter', '1 mm sieve', 'Sample bags or bottles, labelled', 'Process water hose', 'Drying tray', PPE_EQ]),
    ('Sample Collection', ['HCN released at the open sample point', 'Splash of cyanide-bearing slurry', 'Fall from height at the screen', 'Equipment starting without warning'],
     ['Take the sample from the screen oversize stream, not from the launder, so it represents the carbon actually being transferred.',
      'Cut the full stream where the arrangement allows it. A part-stream cut biases the result.'],
     CAUTION_VALVE, None),
    ('Washing and Submission', ['Carbon not washed free of slurry', 'Sample not traceable to the transfer'],
     ['Wash the carbon free of slurry over the 1 mm sieve.',
      'Bag and label the sample and submit it to the laboratory for gold loading.',
      'Record the transfer batch number, tonnage and time against the sample.'], None, None),
    CLOSE_STEP,
]
REFS = refs('201-006', TITLE, [('HM-PRC-V01-PRO005', 'Carbon in Leach (CIL) Circuit'),
    ('4034-PR-PRO-002', 'Sampling Protocol, CIL table item 3'),
    ('4034-004-VE-025 Rev B', 'Goldquip vibrating screen IOM, received 11 Aug 2026')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'fall', 'slip'], 'the screen, a pump or a sample cutter')
