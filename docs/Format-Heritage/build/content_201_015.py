import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '201-015'
TITLE = 'Copper Filtrate and Precipitate Sampling'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = ['Safety helmet and safety glasses', 'Chemical splash goggles and face shield', 'High-visibility long-sleeved shirt and long trousers',
       'Safety boots with sound tread - nitrile PVC boots at the sample point',
       'Chemical resistant suit, acid-resistant and nitrile rubber gloves, and apron',
       'Personal HCN gas monitor, calibrated and in test date',
       'Full or half gas mask with A2B2E2K2P3 cartridge, carried and available for immediate use']
DESC = desc(['Set the copper grade and moisture of the filter cake, which is the saleable product.',
             'Set the filtrate assay, which shows how much copper is being lost to the filtrate.'],
            '072 Copper Precipitate Filtering',
            ['Copper filtrate tank - filtrate from the filter press', 'Filter press - cake, sampled on discharge'],
            'Every filter press cycle on the cake; each shift on the filtrate.', NUM)
STEPS = [
    ('Pre-start Check', ['Press not depressurised', 'Gas monitor or fixed detection not healthy', 'Safety shower or eyewash not proven flowing', 'Working alone in a cyanide area'],
     prestart(NEW_JSEA, ['Confirm the press cycle has finished and the press is depressurised before approaching.']), None,
     ['Sample scoop', 'Sample bags and bottles, labelled', 'Moisture tin', 'pH meter', 'Filter paper', PPE_EQ]),
    ('Cake Sampling', ['Release from a pressurised press or line', 'Contact with acid in the cake', 'Equipment starting without warning', 'Non-representative cake sample'],
     ['Sample the cake by taking increments from several plates across the press, not one grab from the nearest plate.',
      'Bag the composite cake sample, label it with the cycle number, and submit for copper grade and moisture.'],
     'CAUTION: Wear full acid PPE. The cake may carry acid and cyanide-bearing solution.', None),
    ('Filtrate Sampling', ['HCN released at the filtrate tank', 'Splash of acidic filtrate', 'Cycle details not recorded'],
     ['Take the filtrate sample from the filtrate tank, determine pH in the field, and bottle for assay.',
      'Record cycle number, cake mass and cycle time against the samples.'], CAUTION_VALVE, None),
    CLOSE_STEP,
]
REFS = refs(NUM, TITLE, [('HM-PRC-V01-PRO018', 'Copper Precipitate Filtering'),
    ('Mt. Morgan site procedure 12', 'Copper Filtrate Tank Sampling [LIVE]'),
    ('KBK SOP-PROC-CNREC-09 and CNREC-10', 'Filtration of copper precipitation and Release of precipitated copper, received 11 Aug 2026')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'acid', 'slip'], 'the press, a pump or a sample cutter')
