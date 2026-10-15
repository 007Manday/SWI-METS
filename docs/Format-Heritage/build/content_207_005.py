import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '207-005'
TITLE = 'Automatic Sampler Cleaning, Unblocking and Cutter Wear Check'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc207(['Clean and unblock the automatic samplers and check the cutters for wear.', 'A worn cutter changes the cut it takes. A blocked sampler takes no cut at all and often still reports a sample.'], ['022-XM-011 / -017 - IsaMill feed', '032-XM-012 - CIL tails', '041-XM-013 - Metal adsorption tails', '051-XM-014 - Final tails'], 'To be set once the sampler design is known.', NUM, extra_bold=['ISSUED BUT NOT FOR USE. This document is a placeholder against the register line so the line is not empty. It cannot be used until the sampler general arrangement and cutter design are held: no source is held for any of the five samplers. The method, frequency and equipment are written when that input arrives.'])
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + [], prestart203(NEW_JSEA, []), None, ['To be confirmed once the sampler general arrangement is held'] + [PPE_EQ]),
    ('Status - Not for Use', ['Task attempted without the sampler design'], ['This task cannot be completed until the sampler general arrangement and cutter design are held.', 'The document is issued so the register line is not empty, and is marked NOT FOR USE.'], None, None),
    CLOSE203_STEP,
]
REFS = refs207(NUM, TITLE, [('Note', 'No source held for any of the five samplers.')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'elec'], 'the sampler, a pump or a sample cutter')
