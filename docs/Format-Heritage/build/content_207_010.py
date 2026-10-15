import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '207-010'
TITLE = 'Cyanide Analyser Sample and Booster Pump Service - 032-PP-207/208 and 041-PP-2xx'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc207(['Service the sample and booster pumps that feed the online cyanide analysers.'], ['032-PP-207 / 032-PP-208 - Analyser sample and booster pumps', '041-PP-2xx - Analyser sample pumps, tag to be confirmed'], 'To be set once the vendor manual is held.', NUM, extra_bold=['ISSUED BUT NOT FOR USE. This document is a placeholder against the register line so the line is not empty. It cannot be used until the named input arrives: the Vender Dura 10 pump manual is not held (the pumps are listed as part of the Molycop package). The method, frequency and equipment are written when that input arrives.'])
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + [], prestart203(NEW_JSEA, []), None, ['To be confirmed once the Vender Dura 10 pump manual is held'] + [PPE_EQ]),
    ('Status - Not for Use', ['Task attempted without the vendor documentation'], ['This task cannot be completed until the Vender Dura 10 pump manual is held.', 'The document is issued so the register line is not empty, and is marked NOT FOR USE.'], None, None),
    CLOSE203_STEP,
]
REFS = refs207(NUM, TITLE, [('Note', 'Vender Dura 10 pumps are listed as part of the Molycop package. No vendor manual held.')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'elec'], 'a pump or the analyser sample system')
