import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '204-015'
TITLE = 'Resin Particle Size Distribution and Fines Determination'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_HEAR
DESC = desc204(['Measure the bead size distribution of the resin and the proportion of fines and broken beads.', 'Bead integrity is the resin equivalent of carbon fines, and the leading indicator of a resin loss.'], 'Monthly, and after any osmotic shock event or conditioning batch.', NUM, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA), None, ['200 mm sieve set 38 um to 2 mm', 'Ro-Tap RX29', 'Balance', 'Wash bottle', 'Stereo microscope - NOT HELD'] + [PPE_EQ]),
    ('Washing and Draining', ['Cyanide-bearing slurry on the resin', 'Resin dried to shrinkage'], ['Wash the resin sample free of slurry over the retention aperture and drain it.', 'Do not dry the resin to the point of shrinkage - measure it in the drained wet state the method specifies.'], None, None),
    ('Screening', ['Hearing damage at the shaker', 'Hands caught in the shaker'], ['Screen through the sieve set on the Ro-Tap for the standard period.', 'Weigh or measure the volume of each fraction.', 'Calculate the distribution and report the fraction below the screen retention aperture as the at-risk fraction.'], 'CAUTION: Wear hearing protection and keep hands clear until the shaker has stopped.', None),
    ('Bead Integrity and Trend', ['Broken beads not counted'], ['Inspect a counted subsample for broken and cracked beads and report whole bead count as a percentage.', 'Trend against the previous month and against the resin loss accounting.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs204(NUM, TITLE, [('KBK-MIR-MP-PRO-MET-SOP-0058', 'Distribusi Ukuran Partikel Resin, received 11 Aug 2026'), ('ILS quotation Q0023979', '200 mm sieve set 38 um to 2 mm and Ro-Tap RX29'), ('RA-01', 'Resin Loss Register Rev A')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin'], 'the shaker or other bench equipment')
