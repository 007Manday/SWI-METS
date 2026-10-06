import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '204-006'
TITLE = 'Moisture Content Determination'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = [h for h in hazards_from(os.environ['SRC_DOCX']) if not h.startswith('[JSEA to confirm]')]
PPE = PPE_LAB
DESC = desc204(['Determine the moisture content of a sample by oven drying to constant mass.', 'Every assay is reported on a dry basis. A wrong moisture makes every grade wrong.'], 'Every solid sample requiring a dry mass.', NUM, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, []), None, ['Drying oven', 'Moisture tins', 'Analytical balance', 'Desiccator', 'Tongs'] + [PPE_EQ]),
    ('Tare and Wet Mass', ['Tin not clean and dry', 'Sample not spread evenly'], ['Weigh the clean dry tin and record the tare.', 'Add the sample, spread it evenly and weigh to get the wet mass.'], None, None),
    ('Drying to Constant Mass', ['Burns from the hot oven and tins', 'Hot sample weighed light', 'Constant mass assumed from a set time'], ['Dry in the oven at the method temperature until constant mass. Constant mass means two successive weighings agree, not one weighing after a set time.', 'Cool in the desiccator before every weighing. A hot sample reads light.', 'Weigh and record the dry mass.'], 'CAUTION: Handle hot tins with tongs and set them down on a heat mat.', None),
    ('Calculation and Record', ['Moisture calculated on the wrong basis', 'Oven conditions not recorded'], ['Calculate moisture as a percentage of the wet mass.', 'Record the oven temperature, the drying period and the balance identity.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs204(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0022', 'Moisture Content'), ('KBK-MIR-MP-PRO-MET-SOP-0032', 'Moisture Content, Bahasa master received 11 Aug 2026')])
EMERG = emerg(['cn', 'skin', 'burn', 'cut'], 'bench equipment')
