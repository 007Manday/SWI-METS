import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '204-003'
TITLE = 'Particle Size Distribution by Laser Sizer'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB
DESC = desc204(['Determine sub-sieve particle size distribution by laser diffraction.', 'The IsaMill product is finer than the finest sieve held, so without this the fine end of the distribution is unknown.'], 'To be set once the instrument is resolved.', NUM, extra_bold=['ISSUED BUT NOT FOR USE. This document is a placeholder against the register line so the line is not empty. It cannot be used until the named input arrives: a laser particle size analyser has not been purchased (no laser sizer in ILS quotation Q0023979). The method, frequency and equipment are written when the instrument is resolved.'])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA), None, ['Laser particle size analyser - NOT PURCHASED'] + [PPE_EQ]),
    ('Status - Not for Use', ['Task attempted without the instrument'], ['This task cannot be completed until a laser particle size analyser is purchased.', 'The document is issued so the register line is not empty, and is marked NOT FOR USE.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs204(NUM, TITLE, [('Note', 'No source held. No laser sizer in ILS quotation Q0023979.')])
EMERG = emerg(['hcn', 'cn', 'skin'], 'bench equipment')
