import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '204-001'
TITLE = 'Met Lab Sample Receipt, Logging and Storage'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB
DESC = desc204(['Receive samples into the metallurgical laboratory with a chain of custody that holds.', 'A sample that cannot be traced back to a point, a time and a shift is worthless no matter how well it is analysed.'], 'Every delivery from the plant.', NUM, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA), None, ['Sample register or LIMS entry', 'Balance', 'Storage racks and bins', 'Labels and marker'] + [PPE_EQ]),
    ('Delivery Check', ['Sample missing or not listed', 'Leaking or unlabelled sample accepted'], ['Check the delivery against the handover sheet - every sample listed is present and every sample present is listed.', 'Reject and record any sample that is unlabelled, illegible, leaking or clearly the wrong material.'], None, None),
    ('Logging and Numbering', ['Sample not traceable to point, time and shift', 'Receipt mass not recorded'], ['Log each sample against its point, date, time, shift and the analyses requested.', 'Assign a laboratory number and mark it on the container.', 'Weigh the sample where the method requires a receipt mass.'], None, None),
    ('Storage and Handover', ['High-grade sample stored with low-grade', 'Manual handling of heavy containers', 'Handover not signed'], ['Store to the storage rack for its stream. Keep high-grade streams separate from low-grade.', 'Sign the handover and return a copy to the plant.'], 'CAUTION: Two-person lift or a trolley for containers above the site manual handling limit.', None),
    CLOSE_LAB_STEP,
]
REFS = refs204(NUM, TITLE, [('KBK-MIR-LAB-PRE-SOP-001 and PRE-SOP-002', 'Penerimaan Sampel and Sortir Sampel'), ('4034-PR-PRO-002', 'Sampling Protocol')])
EMERG = emerg(['hcn', 'cn', 'skin', 'slip'], 'bench equipment')
