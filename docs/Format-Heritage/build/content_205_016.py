import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '205-016'
TITLE = 'Precipitate and Platelet Content Determination'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc205(['Determine the precipitate and platelet content of the copper product.', 'It is the measure of precipitation performance and of product quality.'], 'Every lot and per the analysis schedule.', NUM, False, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, []), None, ['Filter apparatus', 'Drying oven', 'Balance', 'Microscope or magnifier', 'Sieves', 'Beakers'] + [PPE_EQ]),
    ('Subsample and Drying', ['H2S from an acidified sulphide sample', 'Hot items from the oven'], ['Take a representative subsample of the precipitate.', 'Filter, wash and dry to constant mass.', 'Determine the solids content and the moisture.'], 'CAUTION: Never acidify a sulphide-bearing precipitate outside the fume cupboard. It releases H2S.', None),
    ('Platelet Content', ['Dust from dry precipitate', 'Platelet not quantified to the method'], ['Screen or inspect for platelet material and quantify it against the method.'], None, None),
    ('Assay and Reporting', ['Deleterious elements not assayed'], ['Assay for copper and for the deleterious elements the offtake specifies.', 'Report against the product specification.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs205(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0001', 'Platelet Content')])
EMERG = emerg(['h2s', 'acid', 'burn', 'cut'], 'bench equipment')
