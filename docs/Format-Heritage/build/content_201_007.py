import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '201-007'
TITLE = 'Barren Carbon Sampling at Carbon Dewatering Screen 061-SC-013'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD[:7] + ['Heat-resistant gloves'] + PPE_STD[7:]
DESC = desc(['Set the residual gold on barren carbon returning to the CIL circuit.',
             'Barren loading is the direct measure of elution efficiency. A rising barren assay is the first sign the elution circuit is underperforming.'],
            '061 Gold Elution', ['061-SC-013 - Carbon dewatering screen, oversize'],
            'Every elution batch, on the barren carbon returning to CIL.', '201-007')
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Circuit on a heating cycle or column under pressure'],
     prestart(NEW_JSEA, ['Confirm the elution batch has finished and the carbon is being returned.',
                         'Confirm the circuit is not on a heating cycle before sampling. Do not sample a column under pressure.']), None,
     ['Sample scoop or cutter', '1 mm sieve', 'Sample bags, labelled', 'Process water hose', 'Heat-resistant gloves and face shield', PPE_EQ]),
    ('Sample Collection', ['HCN released at the open sample point', 'Contact with hot solution or hot surface', 'Fall from height at the screen', 'Equipment starting without warning'],
     ['Allow the sample line to flush and cool before collecting.',
      'Sample the screen oversize as the carbon discharges, taking increments across the whole discharge period rather than one grab at the start.'],
     'CAUTION: Wear heat-resistant gloves and a face shield. Do not sample a column under pressure.', None),
    ('Washing and Submission', ['Carbon not washed free of solution', 'Sample not traceable to the elution batch'],
     ['Wash free of solution over the 1 mm sieve.',
      'Bag, label with the elution batch number, and submit to the laboratory.',
      'Record the elution batch number, strip conditions and time against the sample.'], None, None),
    CLOSE_STEP,
]
REFS = refs('201-007', TITLE, [('HM-PRC-V01-PRO012', 'Carbon Regeneration and Kiln Operation'),
    ('4034-PR-PRO-002', 'Sampling Protocol, CIL table item 4'),
    ('4034-013-VE-028 Rev A', 'Applied Heat Thermomat 2300 O&M manual, received 11 Aug 2026')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'burn', 'fall', 'slip'], 'the screen, a pump or a sample cutter')
