import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '206-005'
TITLE = 'Cyanide Solution Handling and Spill Response'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc206(['Handle cyanide solutions at the bench and respond correctly to a cyanide spill in the laboratory.', 'A cyanide spill in a small enclosed room with acids present is the worst credible laboratory event on this site.'], 'Every cyanide handling task; drill at the set interval.', NUM, True, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, [LAB_ALONE] + []), None, ['Fume cupboard', 'Cyanide antidote kit', 'Hazchem spill kit 120 L', 'Caustic for neutralisation', 'Safety shower and eyewash', 'Personal HCN monitor', 'Emergency contact list'] + [PPE_EQ]),
    ('Cyanide Handling at the Bench', ['HCN released from the solution', 'Acid in the cupboard with cyanide', 'Solution pH below 10.5'], ['Handle cyanide solutions only in the fume cupboard with the airflow confirmed.', 'Keep all acids out of the cupboard while cyanide work is in progress. Acid on cyanide releases HCN.', 'Keep the solution pH above 10.5 at all times. Confirm it before starting.'], 'CAUTION: Acid on cyanide releases HCN. No acid in the cupboard during cyanide work.', None),
    ('Spill Response', ['HCN from a spill', 'Re-entering an evacuated laboratory'], ['On a small spill inside the cupboard: leave the sash down and the fan running, neutralise with caustic, then absorb and bag for cyanide waste disposal.', 'On a spill outside the cupboard: evacuate the laboratory, close the door, raise the alarm and do not re-enter.'], 'CAUTION: A spill outside the cupboard is an evacuation, not a clean-up.', None),
    ('Exposure Response and Reporting', ['Cyanide on the skin', 'Suspected inhalation', 'Rescuer exposed'], ['On skin contact: flood with water at the safety shower for at least 15 minutes, remove contaminated clothing under the water, and get the antidote kit and a trained first aider.', 'On suspected inhalation: move the person to fresh air, do not enter to retrieve them without protection, and call for the antidote kit and emergency response immediately.', 'Report every spill, however small, and record it.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs206(NUM, TITLE, [('SWI-022 and SWI-025', 'Gas Detector Alarm Response and Cyanide Bearing Spill Response, both issued (plant versions)'), ('KBK-MIR-MP-PRO-OPE-SOP-0076', 'Fasilitas Cyanide, received 11 Aug 2026'), ('ILS quotation Q0023979', 'Safety shower with eye wash, 3 x eye wash stations, 120 L hazchem spill kit')])
EMERG = emerg(['hcn', 'cn', 'chem', 'acid', 'cut'], 'bench equipment')
