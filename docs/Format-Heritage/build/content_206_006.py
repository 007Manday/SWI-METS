import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '206-006'
TITLE = 'Acid Spill Response and Neutralisation'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc206(['Respond to an acid spill in the laboratory and neutralise it safely.', 'The laboratory holds concentrated sulphuric, hydrochloric and perchloric acid, and cyanide is in the same room.'], 'Every acid handling task; drill at the set interval.', NUM, True, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, [LAB_ALONE] + []), None, ['Hazchem spill kit', 'Neutralising agent - soda ash or proprietary acid neutraliser', 'Safety shower and eyewash', 'Acid PPE', 'Waste containers', 'Fume cupboard'] + [PPE_EQ]),
    ('Containment', ['Acid flushed to drain untreated', 'Acid near cyanide releasing HCN'], ['Contain the spill first, then neutralise. Never flush an acid spill to drain untreated.', 'Where the spill is anywhere near cyanide-bearing material or waste, treat it as a potential HCN release - evacuate, raise the alarm and do not attempt to clean it up unprotected.'], 'CAUTION: An acid spill near cyanide is a potential HCN release. Evacuate and raise the alarm.', None),
    ('Neutralisation and Clean-up', ['Heat and spatter from fast neutralisation', 'Acid fume'], ['Apply neutralising agent from the outside of the spill inwards, slowly. Adding neutraliser fast to a concentrated acid generates heat and spatter.', 'Confirm neutralisation with pH paper before absorbing.', 'Absorb, bag and label for chemical waste disposal.', 'Ventilate the area and confirm the fume cupboard and general extraction are running.'], None, None),
    ('Exposure Response and Reporting', ['Acid on the skin or in the eyes', 'Hydrofluoric acid burn under-treated'], ['On skin or eye contact, flood at the safety shower or eyewash for at least 15 minutes and get medical attention. For hydrofluoric acid, apply calcium gluconate gel and treat as a medical emergency regardless of how the skin looks.', 'Report and record every spill.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs206(NUM, TITLE, [('KBK-MIR-LAB-WET-SOP-051', 'Acid spill handling'), ('ILS quotation Q0023979', '120 L hazchem spill kit, safety shower and eye wash stations')])
EMERG = emerg(['hcn', 'cn', 'chem', 'acid', 'cut'], 'bench equipment')
