import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '207-009'
TITLE = 'Cyanide Analyser Specialised Electrode Replacement and Conditioning'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc207(['Replace and condition the specialised electrodes in the online cyanide analysers.'], ['Mintex 3000366 and 3000330 - analyser electrodes identified in the instrument list', '032-CA-001 - CIL circuit online cyanide analyser (pH, free cyanide and WAD cyanide)', '051-CA-002 - Cyanide adsorption (ReCYN) online cyanide analyser (pH, free cyanide and WAD cyanide)'], 'To be set once the vendor manual is held.', NUM, extra_bold=['ISSUED BUT NOT FOR USE. This document is a placeholder against the register line so the line is not empty. It cannot be used until the named input arrives: the Molycop Cynoprobe vendor manual is not held, and no procedure is held for the Mintex 3000366 and 3000330 electrodes. The method, frequency and equipment are written when that input arrives.'])
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + [], prestart203(NEW_JSEA, []), None, ['To be confirmed once the Molycop Cynoprobe manual is held'] + [PPE_EQ]),
    ('Status - Not for Use', ['Task attempted without the vendor documentation'], ['This task cannot be completed until the Molycop Cynoprobe vendor manual is held.', 'The document is issued so the register line is not empty, and is marked NOT FOR USE.'], None, None),
    CLOSE203_STEP,
]
REFS = refs207(NUM, TITLE, [('Note', 'Electrodes identified as Mintex 3000366 and 3000330 in the instrument list. No procedure held.')])
EMERG = emerg(['hcn', 'cn', 'skin', 'elec', 'cut'], 'a pump or the analyser sample system')
