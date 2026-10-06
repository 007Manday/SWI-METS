import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '204-002'
TITLE = 'Wet Screening and Sizing Analysis'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_HEAR
DESC = desc204(['Determine the size distribution of a slurry sample by wet screening.', 'Sizing drives grind control, cyclone assessment and every liberation question that follows.'], 'Per the sampling schedule; daily on CIL tail and cyclone overflow.', NUM, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA), None, ['Sieve set 38 um to 2 mm', 'Ro-Tap RX29 shaker and sound enclosure', 'Wash bottle and spray', 'Drying oven', 'Balance 0.1 mg', 'Drying trays'] + [PPE_EQ]),
    ('Wet Screening and Drying', ['Undersize not washed clear', 'Burns from the drying oven'], ['Weigh the wet sample and record the receipt mass.', 'Wet screen the sample at the finest aperture to remove the undersize, washing until the water runs clear.', 'Dry both the oversize and the recovered undersize to constant mass.'], None, None),
    ('Dry Screening', ['Hearing damage at the shaker', 'Hands caught in the shaker', 'Fraction lost from the sieve stack'], ['Dry screen the oversize through the full sieve set on the Ro-Tap for the standard period.', 'Weigh each retained fraction and the pan.'], 'CAUTION: Close the sound enclosure before starting the Ro-Tap and wear hearing protection. Keep hands clear until the shaker has stopped.', None),
    ('Mass Check and Calculation', ['Loss above tolerance reported', 'Sieve set not recorded'], ['Check the sum of fractions against the dry receipt mass. A loss above the allowed tolerance means the screening is repeated, not reported.', 'Calculate the cumulative passing distribution and the P80.', 'Record the result with the sieve set identity and the shaking period.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs204(NUM, TITLE, [('KBK-MIR-LAB-PRE-SOP-008', 'Uji Kehalusan Sampel'), ('KBK-MIR-MP-PRO-MET-SOP-0020, 0028 and 0029', 'Distribusi Logam dan Ukuran, Sizing Harian CIL Tail and Sizing Harian COF, received 11 Aug 2026'), ('ILS quotation Q0023979', 'Ro-Tap RX29, sound enclosure and twelve 200 mm sieves 38 um to 2 mm')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'burn', 'slip'], 'the shaker or other bench equipment')
