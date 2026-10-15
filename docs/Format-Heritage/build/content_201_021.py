import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '201-021'
TITLE = 'Composite Sample Build-Up, Splitting and Handover to Laboratory'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD[:-1]
DESC = desc(['Build the shift composites from the hourly spot samples so the laboratory result represents the shift and not one moment in it.',
             'Get the samples to the laboratory with a chain of custody that holds up when a result is later questioned.'],
            '201 Plant Sampling', ['Composite station - composite containers by stream, one set per shift'],
            'Continuous through the shift, with handover at the end of each composite period.', NUM, safety=False)
STEPS = [
    ('Pre-start Check', ['Composite container dirty or mislabelled', 'Gas monitor or fixed detection not healthy', 'Safety shower or eyewash not proven flowing'],
     prestart(NEW_JSEA, ['Confirm the composite containers are clean, labelled by stream and composite number, and empty at the start of the period.'], alone=False, rinse=False), None,
     ['Composite containers, labelled by stream and composite number', 'Measuring cylinder for the volume added at each increment', 'Riffle splitter or rotary divider',
      'Spatula and stirring rod', 'Sample bags and bottles', 'Sample register or logbook', PPE_EQ]),
    ('Building the Composite', ['Wrong volume added', 'Missed increment hidden', 'Cross-contamination between streams'],
     ['Add the stated volume from each hourly spot sample. The site schedule is 4 litres collected per hour, split 2 litres to the operator and 2 litres to the laboratory, building four 12-litre composites per shift on the main streams.',
      'Record the volume added and the time for every increment. A missed increment is recorded as missed, not quietly skipped.'],
     'CAUTION: Two-person lift or a trolley for composite containers above the site manual handling limit. Clear the route before lifting.', None),
    ('Stirring and Splitting', ['Biased split', 'Splash of cyanide-bearing solution', 'Split not recorded'],
     ['At the end of the composite period, stir the container thoroughly to homogenise before splitting.',
      'Split with the riffle splitter or rotary divider, not by scooping - a scooped split is biased towards the coarse fraction.',
      'Bag or bottle the laboratory split, label it fully, and record it in the sample register.'], None, None),
    ('Handover and Retention', ['Handover without a signature', 'Operator split discarded too early'],
     ['Hand over to the laboratory and obtain a signature. Handover without a signature is not a handover.',
      'Retain the operator split until the laboratory result is reported and accepted.'], None, None),
    CLOSE_STEP,
]
REFS = refs(NUM, TITLE, [('4034-PR-PRO-002', 'Sampling Protocol - 4-hourly to 12-hour shift compositing'),
    ('KBK-MIR-MP-PRO-MET-SOP-0036 and SOP-0035', 'Preparasi Sampel Komposit and Preparasi Sampel Leach Profile, received 11 Aug 2026'),
    ('KBK-MIR-LAB-PRE-SOP-001 and PRE-SOP-002', 'Sample receipt and Sample sorting')])
EMERG = emerg(['hcn', 'cn', 'skin', 'slip'])
