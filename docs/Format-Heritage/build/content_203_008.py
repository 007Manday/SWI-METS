import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '203-008'
TITLE = 'Elution and Electrowinning Batch Performance Assessment'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
PPE = list(PPE_STD[:-1])
PPE[4] = 'Chemical resistant suit, nitrile rubber gloves and apron, heat-resistant gloves'
DESC = desc203(['Assess how well each elution batch stripped, and how well electrowinning recovered what was stripped.',
                'Barren carbon loading and barren electrolyte are the two numbers that say whether the gold room is working.'],
               '203 Plant Surveys', ['061 - Elution circuit, loaded and barren carbon, eluate', '062 - Electrowinning, feed and barren'],
               'Every batch, assessed and trended monthly.', NUM)
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Mercury vapour in the gold room', 'Circuit on a heating cycle'],
     prestart203(NEW_JSEA, ['Confirm area ventilation is running before entering the gold room, elution and retort areas.']), None,
     ['Sample bottles, heat resistant', 'Field data sheets', 'Batch records from the control system', PPE_EQ]),
    ('Batch Record and Assays', ['Hot solution contact', 'HCN released at the open sample point', 'Splash of cyanide-bearing solution', 'Contact with live electrical equipment'],
     ['Take the batch record - strip temperature, flow, caustic and cyanide strength, cycle time.',
      'Take loaded carbon and barren carbon assays for the batch.',
      'Take eluate assay through the strip, and electrowinning feed and barren electrolyte assays.'],
     'CAUTION: Wear heat-resistant gloves and a face shield. Do not sample a column under pressure or on a heating cycle.', None),
    ('Efficiency Calculation', ['Wrong efficiency calculated'],
     ['Calculate strip efficiency from loaded and barren carbon loading.',
      'Calculate electrowinning efficiency from feed and barren electrolyte.'], None, None),
    ('Comparison and Report', ['Falling strip efficiency blamed on the carbon without checking conditions'],
     ['Compare against the design strip conditions in the Applied Heat manual and against the previous batches.',
      'Where strip efficiency is falling, check the strip conditions before blaming the carbon - temperature and eluant strength are the usual causes.',
      'Report the batch performance with the monthly close.'], None, None),
    CLOSE203_STEP,
]
REFS = refs203(NUM, TITLE, [('4034-013-VE-028 Rev A', 'Applied Heat Thermomat 2300 O&M manual, received 11 Aug 2026 - strip temperatures and circuit design conditions'),
    ('4034-014-VE-004 and -019', 'Stantil carbon regeneration kiln control philosophy and IOM, received 11 Aug 2026'),
    ('HM-PRC-V01-PRO011 and PRO013', 'Gold Elution and Gold Electrowinning')])
EMERG = emerg(['hcn', 'cn', 'skin', 'burn', 'elec'])
