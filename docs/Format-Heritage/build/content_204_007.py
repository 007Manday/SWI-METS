import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '204-007'
TITLE = 'Total Suspended Solids Determination'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB
DESC = desc204(['Determine suspended solids in a solution or overflow sample by filtration and drying.', 'Thickener overflow clarity and process water quality are both judged on this number.'], 'Per the sampling schedule; each shift on thickener overflow.', NUM, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA), None, ['Filtration apparatus and vacuum pump', 'Pre-weighed filter papers', 'Drying oven', 'Analytical balance', 'Desiccator', 'Measuring cylinder'] + [PPE_EQ]),
    ('Filtration', ['HCN from the open sample', 'Vacuum line or fitting releasing', 'Dissolved salts reporting as solids'], ['Record the exact volume of sample filtered.', 'Filter through a pre-dried, pre-weighed filter paper.', 'Wash the filter with distilled water to remove dissolved salts, which would otherwise report as solids.'], None, None),
    ('Drying and Weighing', ['Burns from the drying oven', 'Filter not at constant mass'], ['Dry the filter and residue to constant mass at the method temperature.', 'Cool in the desiccator and weigh.'], None, None),
    ('Calculation and Blank', ['Blank not run', 'Wrong volume used in the calculation'], ['Calculate suspended solids as milligrams per litre from the mass gain and the filtered volume.', 'Run a blank filter through the same sequence and correct the result.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs204(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0017', 'Total Suspended Solid'), ('KBK-MIR-LAB-ENV-SOP-072', 'Analisa TSS Gravimetri')])
EMERG = emerg(['hcn', 'cn', 'skin', 'burn', 'cut'], 'bench equipment')
