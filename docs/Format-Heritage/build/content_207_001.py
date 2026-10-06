import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '207-001'
TITLE = 'Automatic Sampler Operation and Cut Verification - IsaMill Feed 022-XM-011 and 022-XM-017'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc207(['Operate the IsaMill feed automatic samplers and prove the cut they take is representative.', 'An automatic sampler that takes a biased cut produces a wrong number all day, every day, with no obvious sign that anything is wrong.'], ['022-XM-011 - IsaMill feed automatic sampler', '022-XM-017 - IsaMill feed automatic sampler'], 'To be set once the sampler design is known.', NUM, extra_bold=['ISSUED BUT NOT FOR USE. This document is a placeholder against the register line so the line is not empty. It cannot be used until the sampler general arrangement and cutter design are held: 022-XM-011 and 022-XM-017 are shop-fabricated with the vendor and cutter design TBA, and the mechanical equipment list shows conflicting status (NEW on one tab, FUTURE on another). The method, frequency and equipment are written when that input arrives.'])
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + [], prestart203(NEW_JSEA, []), None, ['To be confirmed once the sampler general arrangement is held'] + [PPE_EQ]),
    ('Status - Not for Use', ['Task attempted without the sampler design'], ['This task cannot be completed until the sampler general arrangement and cutter design are held.', 'The document is issued so the register line is not empty, and is marked NOT FOR USE.'], None, None),
    CLOSE203_STEP,
]
REFS = refs207(NUM, TITLE, [('Note', 'No source held. 022-XM-011 and 022-XM-017 are shop-fabricated with the vendor and cutter design TBA.'), ('Note', 'The mechanical equipment list shows conflicting status - NEW on one tab, FUTURE on another.')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'elec'], 'the sampler, a pump or a sample cutter')
