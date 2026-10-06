import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '207-011'
TITLE = 'Cyanide Analyser Leak Detector and High Level Alarm Response'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc207(['Respond to a leak detector or high level alarm on an online cyanide analyser.', 'The analyser enclosure holds cyanide-bearing solution. A leak inside it is a confined cyanide release.'], ['Azbil HPQ-D12 - Leak detector, vendor scope', 'E&H FTL31 - High level switch, vendor scope', '032-CA-001 - CIL circuit online cyanide analyser (pH, free cyanide and WAD cyanide)', '051-CA-002 - Cyanide adsorption (ReCYN) online cyanide analyser (pH, free cyanide and WAD cyanide)'], 'To be set once the alarm response is defined.', NUM, extra_bold=['ISSUED BUT NOT FOR USE. This document is a placeholder against the register line so the line is not empty. It cannot be used until the named input arrives: the Azbil HPQ-D12 leak detector and E&H FTL31 level switch are vendor scope and no alarm response is held. The method, frequency and equipment are written when that input arrives.'])
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + [], prestart203(NEW_JSEA, []), None, ['Personal HCN monitor', 'To be confirmed once the vendor documentation is held'] + [PPE_EQ]),
    ('Status - Not for Use and Interim Response', ['Enclosure opened during a leak alarm', 'HCN release from the enclosure'], ['This task cannot be completed until the vendor documentation and the alarm response are held.', 'The document is issued so the register line is not empty, and is marked NOT FOR USE.', 'Until it is written, treat any leak or high level alarm on an analyser as a cyanide release: do not open the enclosure, evacuate the immediate area, and report it to the control room.'], 'CAUTION: Do not open the analyser enclosure on a leak or high level alarm.', None),
    CLOSE203_STEP,
]
REFS = refs207(NUM, TITLE, [('Note', 'Azbil HPQ-D12 leak detector and E&H FTL31 level switch are vendor scope. No alarm response held.')])
EMERG = emerg(['hcn', 'cn', 'skin', 'acid', 'elec'], 'a pump or the analyser sample system')
