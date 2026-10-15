import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '204-005'
TITLE = 'Solids Specific Gravity by Pycnometer'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB
DESC = desc204(['Determine the true specific gravity of a dry solid by pycnometer.', 'Every Marcy scale reading and every volumetric inventory depends on the solids SG being right.'], 'On each new ore type, and quarterly on plant feed.', NUM, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA), None, ['Pycnometer', 'Analytical balance 0.1 mg', 'Distilled water', 'Drying oven', 'Desiccator', 'Thermometer'] + [PPE_EQ]),
    ('Sample Preparation and Weighing', ['Sample not at constant mass', 'Burns from the drying oven'], ['Dry and cool the sample in the desiccator to constant mass.', 'Weigh the clean dry pycnometer empty.', 'Add the sample and weigh again to get the sample mass.'], None, None),
    ('De-airing and Filling', ['Trapped air giving a wrong SG', 'Cuts from broken glassware'], ['Fill part way with distilled water, agitate and apply vacuum to remove entrained air. Trapped air is the main source of error in this test.', 'Top up to the mark, bring to the reference temperature and weigh.', 'Empty, clean and refill the pycnometer with distilled water alone and weigh.'], None, None),
    ('Calculation and Duplicates', ['Duplicates outside tolerance reported'], ['Calculate SG from the four masses and the water density at the measured temperature.', 'Run in duplicate. Repeat if the duplicates differ by more than the allowed tolerance.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs204(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0015', 'SG solid determination by pycnometer')])
EMERG = emerg(['cn', 'skin', 'burn', 'cut'], 'bench equipment')
