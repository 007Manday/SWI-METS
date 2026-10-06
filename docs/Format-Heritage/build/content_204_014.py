import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '204-014'
TITLE = 'Carbon Particle Size Distribution and Fines Determination'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_HEAR
DESC = desc204(['Measure the size distribution of activated carbon and the proportion of fines.', 'Carbon fines carry gold out of the circuit. A rising fines fraction predicts a loss before the balance shows it.'], 'Monthly, and after every regeneration campaign.', NUM, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA), None, ['Sieve set suited to carbon', 'Ro-Tap shaker', 'Balance', 'Drying oven', 'Wash bottle'] + [PPE_EQ]),
    ('Washing and Drying', ['Cyanide-bearing slurry on the carbon', 'Burns from the oven', 'Carbon degraded by overheating'], ['Wash the carbon sample free of slurry and drain it.', 'Dry to constant mass at the method temperature. Do not overheat - carbon degrades.'], None, None),
    ('Screening', ['Hearing damage at the shaker', 'Hands caught in the shaker'], ['Screen through the carbon sieve set for the standard period.', 'Weigh each fraction and calculate the distribution.'], 'CAUTION: Wear hearing protection and keep hands clear until the shaker has stopped.', None),
    ('Fines Report and Trend', ['Fines fraction not reported separately'], ['Report the fines fraction below the retention screen aperture separately - that is the fraction that will be lost.', 'Trend the fines fraction against the regeneration cycles and against the carbon loss accounting.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs204(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0013', 'Distribusi Ukuran Partikel Karbon Aktivasi')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'burn'], 'the shaker or other bench equipment')
