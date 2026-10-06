import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '201-018'
TITLE = 'Final Tailings and TSF Return Water Sampling'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc(['Set the final tailings grade and the cyanide concentration going to the storage facility.',
             'Set the return water quality coming back to the plant.',
             'These are the numbers that carry the environmental licence obligation.'],
            '091 Tailings',
            ['091 - Final tailings line to the storage facility', 'TSF return water - return water line to process water'],
            'Each shift on final tailings; daily on return water, or as the licence requires.', NUM)
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Tailings line blocked or not flowing'],
     prestart(NEW_JSEA, ['Confirm the tailings line is flowing and the point is not blocked before opening it.']), None,
     ['Sampling bucket 5 to 8 L', 'Marcy scale', 'pH meter', 'Free cyanide titration kit and rhodanine indicator', 'Filter press and filter paper',
      'Bottles 500 mL for WAD and total cyanide', PPE_EQ]),
    ('Final Tailings Sampling', ['HCN released at the open sample point', 'Splash of cyanide-bearing slurry', 'Fall from height at the sample point', 'pH below the level that holds cyanide as cyanide'],
     ['Flush the point and discard the first flow.',
      'Collect the sample, determine pH immediately, and record it. pH is the control that keeps cyanide as cyanide rather than HCN.'],
     CAUTION_VALVE, None),
    ('Solids and Cyanide', ['Scale not zeroed - wrong per cent solids', 'Splash of cyanide-bearing filtrate'],
     ['Determine per cent solids on the Marcy scale.',
      'Filter and bottle for tail assay, WAD cyanide and total cyanide.'], None, None),
    ('Return Water Sampling', ['Return water sample taken at the wrong point', 'Flow, density and time not recorded'],
     ['Take the return water sample from the designated return line point.',
      'Record flow, density and the time against both samples.'], None, None),
    CLOSE_STEP,
]
REFS = refs(NUM, TITLE, [('HM-PRC-V01-PRO008', 'Tails Thickener and Tailings Disposal'),
    ('4034-PR-PRO-002', 'Sampling Protocol, Reagent Area table - TSF solution')])
EMERG = emerg(['hcn', 'cn', 'skin', 'fall', 'slip'])
