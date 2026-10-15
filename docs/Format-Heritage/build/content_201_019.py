import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '201-019'
TITLE = 'Water Treatment Plant Feed and Discharge Sampling'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD[:-1]
DESC = desc(['Set the feed and discharge quality across the water treatment plant.',
             'Discharge quality carries the environmental licence obligation.',
             'Check the raw (input) water and the filtrate water at the water filter, using the sampling technique in Steps 2 and 3.'],
            '092 / 093 Water Treatment',
            ['092 - Water treatment plant No. 1, feed and discharge', '093 - Water treatment plant No. 2, feed and discharge',
             'Water filter - raw (input) water and filtrate water'],
            'To be set.', NUM,
            extra_bold=['Note: the sampling points need to be updated. The points for water treatment plant No. 1 and No. 2 feed and discharge, and for the raw and filtrate water, are to be confirmed against the plant. The sampling technique in Steps 2 and 3 is taken from the Martabe work instruction Sampling Raw and Filtrat Water (DOC-3-MET-PRS-WIN-00063-IE, v1.0, 25/12/2024), where the raw water point is next to the vertical SLS ladder and the filtrate point is below it. The assay suite and the laboratory are to be set. JSEA-PRO-MET-201-019 must be updated for the added hazard.'])
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Filter plant not in its filtration sequence'],
     prestart(NEW_JSEA, ['Take 5 minutes before starting (Take 5). Prepare 1 L sample bottles.',
                         'Make sure the filter plant is running in its filtration sequence.']), None,
     ['1 L sample bottles', 'Other equipment to be confirmed once the plant configuration is known', PPE_EQ]),
    ('Raw (Input) Water Sampling', ['Water splash and wet floor', 'Overhead pipes', 'Sample not representative', 'HCN released from cyanide-bearing water'],
     ['Go to the raw water sampling point (to be updated). Stand so you are not under the sampling point.',
      'Open the tap upward slowly and wait about 30 to 60 seconds so the sample is representative. Rinse the bottle with raw water.',
      'Hold the bottle right under the outflow and wait until it is full. Collect at least 900 mL.',
      'Close the tap downward. Make sure no water is still coming out of the tap.'],
     'CAUTION: Watch footing on wet floors and watch overhead pipes with the hard hat on. Water from the treatment circuit can carry cyanide, so the HCN controls in Part 2 apply.', None),
    ('Filtrate Water Sampling', ['Water splash and wet floor', 'Raw and filtrate samples swapped'],
     ['Go to the filtrate water sampling point, below the raw water point (to be updated).',
      'Take the sample with the same steps as for the raw water.'], None, None),
    ('Dispatch and Records', ['Samples not traceable', 'Result not recorded'],
     ['Send the samples to the Mt. Morgan laboratory for assay.',
      'Record the result in G:\\\\Processing\\\\5. Metallurgy\\\\Metallurgy\\\\34. Water\\\\Assay sample Potable Water Final.xlsb.'], None, None),
    CLOSE_STEP,
]
REFS = refs(NUM, TITLE, [('DOC-3-MET-PRS-WIN-00063-IE v1.0', 'Martabe WI Sampling Raw and Filtrat Water (25/12/2024) - source of Steps 2 and 3'),
    ('Note', 'No Mt. Morgan circuit source held for the water treatment plant - sampling points to be updated')])
EMERG = emerg(['hcn', 'cn', 'skin', 'slip'])
