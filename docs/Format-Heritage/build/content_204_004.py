import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '204-004'
TITLE = 'Slurry Density Determination by Marcy Scale'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB
DESC = desc204(['Determine slurry density and per cent solids in the field or at the bench with a Marcy scale.', 'It is the fastest density measurement available and the one every operator uses, so it has to be done the same way every time.'], 'Every slurry sample requiring a density.', NUM, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA), None, ['Marcy scale', '1 litre density container', 'Cloth or tissue', 'Stable hanging support'] + [PPE_EQ]),
    ('Scale Set-up', ['Scale not level or not hung securely', 'Scale not zeroed'], ['Confirm the Marcy scale is level and properly hung on a stable support.', 'Zero the scale with the empty dry 1 litre container on the hook, once per shift.'], None, None),
    ('Filling the Container', ['Splash of cyanide-bearing slurry', 'Trapped air giving a low reading', 'HCN from the open sample'], ['Rinse the container with the sample and discard the rinse.', 'Fill to the 1 litre mark and tap gently to release trapped air.', 'Wipe the outside of the container clean and dry.'], None, None),
    ('Reading and Recording', ['Wrong scale read', 'Solids SG not recorded'], ['Hang the filled container and allow the pointer to settle.', 'Read per cent solids from the inner scale and specific gravity from the outer.', 'Record the reading with the solids SG used, the date, time and operator.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs204(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0004', 'SG Determination by Marcy Scale'), ('KBK-MIR-MP-PRO-MET-SOP-0045', 'Pengukuran Densitas Lumpur, received 11 Aug 2026')])
EMERG = emerg(['hcn', 'cn', 'skin', 'slip'], 'bench equipment')
