import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '205-003'
TITLE = 'Sulphuric Acid Strength Titration'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc205(['Determine sulphuric acid strength by titration, on both a volume and a weight basis.', 'Acid strength sets the copper precipitation pH and the acid wash. An off-strength acid batch dosed at the normal rate overshoots.'], 'Every made-up batch and once per shift on standing solution.', NUM, True, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, [LAB_ALONE] + []), None, ['Burette and stand', 'Pipette', 'Conical flasks', 'Standardised NaOH', 'Phenolphthalein indicator', 'Analytical balance for the weight per volume method', 'Fume cupboard', 'Hanna HI902C titrator'] + [PPE_EQ]),
    ('Sampling and Dilution', ['Concentrated acid sampled', 'Acid splash or fume', 'Water added to acid'], ['Take the sample from the designated diluted-acid valve. Never sample the concentrated storage tank for this test.', 'Work in the fume cupboard. Always add acid to water when diluting, never the reverse.'], 'CAUTION: Always add acid to water, never the reverse. Never sample the concentrated storage tank.', None),
    ('Titration', ['Wrong aliquot basis', 'Endpoint overshot'], ['For the volume per volume method, pipette the aliquot; for weight per volume, weigh it on the analytical balance.', 'Add phenolphthalein indicator.', 'Titrate with standardised NaOH to the first permanent pink.'], None, None),
    ('Calculation and Reporting', ['Off-strength batch dosed', 'Titrator endpoint not verified'], ['Record the titre and calculate strength on the basis the method calls for.', 'Where the Hanna HI902C is used, run the ported method and confirm the endpoint against a manual titration once per week.', 'Report any batch outside the target range before it is dosed.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs205(NUM, TITLE, [('KBK-MIR-MP-PRO-MET-SOP-0041', 'Titrasi Asam Sulfat volume per volume for purity (received 11 Aug 2026)'), ('KBK-MIR-MP-PRO-MET-SOP-0042', 'Titrasi Asam Sulfat weight per volume (received 11 Aug 2026)'), ('ILS quotation Q0023979', 'Hanna HI902C automatic titrator')])
EMERG = emerg(['acid', 'cn', 'chem', 'cut'], 'bench equipment')
