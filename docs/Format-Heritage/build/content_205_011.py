import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '205-011'
TITLE = 'Carbon Activity and Ball-Pan Hardness Test'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID_HEAR
DESC = desc205(['Measure carbon activity and mechanical hardness.', 'Activity says whether the carbon still adsorbs. Hardness says how fast it will turn into fines and be lost.'], 'Monthly, and on every new carbon delivery.', NUM, False, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, []), None, ['Ball-pan hardness apparatus', 'Sieve set', 'Ro-Tap', 'K[Ag(CN)2] solution', 'Balance', 'Drying oven', 'Bottle roller', 'Fume cupboard'] + [PPE_EQ]),
    ('Carbon Activity', ['Cyanide-bearing silver solution splash', 'Contact with the bottle roller'], ['For activity, contact a weighed carbon sample with K[Ag(CN)2] solution of known strength for the stated period.', 'Assay the residual solution and calculate the activity as the proportion adsorbed against the reference.'], None, None),
    ('Ball-Pan Hardness', ['Noise from the Ro-Tap and ball-pan apparatus', 'Carbon dust'], ['For hardness, screen the carbon to the test size fraction and weigh it.', 'Run the ball-pan apparatus for the standard number of cycles with the standard ball charge.', 'Re-screen and weigh the fraction retained on the test screen.'], 'CAUTION: Hearing protection on while the Ro-Tap or ball-pan apparatus is running.', None),
    ('Calculation and Reporting', ['Hardness reported without regeneration history'], ['Calculate the hardness number from the mass retained.', 'Report activity and hardness together with the number of regeneration cycles the carbon has seen.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs205(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0005', 'Uji Kekerasan Ball-Pan Karbon Aktif'), ('KBK-MIR-MP-PRO-MET-SOP-0026', 'Uji Aktifitas Karbon Dengan K[Ag(CN)2] (received 11 Aug 2026) - the activity half, which SOP-0005 does not cover')])
EMERG = emerg(['hcn', 'cn', 'equip', 'chem'], 'the bottle roller, Ro-Tap or ball-pan apparatus')
