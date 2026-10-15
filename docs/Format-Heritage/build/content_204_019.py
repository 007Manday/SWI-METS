import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '204-019'
TITLE = 'Centrifuge Operation for Solution Clarification'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB
DESC = desc204(['Clarify a solution sample by centrifuge where filtration is impractical or too slow.', 'Used where a fine or gelatinous solid blinds a filter paper.'], 'As required by the analysis schedule.', NUM, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA), None, ['Ohaus FC5706 centrifuge', '15 mL centrifuge tubes', 'Balance for tube pairing', 'Timer'] + [PPE_EQ]),
    ('Tube Preparation and Loading', ['Cracked tube failing at speed', 'Unbalanced rotor', 'Splash of cyanide-bearing solution'], ['Inspect the tubes for cracks before loading. A cracked tube fails at speed.', "Fill opposing tubes to the same level and balance them on the balance to within the manufacturer's tolerance. An unbalanced rotor is the main failure mode of a centrifuge.", 'Load opposing positions symmetrically. Never run with a single tube.'], None, None),
    ('Running the Centrifuge', ['Lid opened while spinning', 'Rotor braked by hand'], ['Close and latch the lid before starting.', 'Run at the speed and for the period the method specifies.', 'Allow the rotor to come to a complete stop on its own. Never brake it by hand.'], 'CAUTION: Never open the lid or touch the rotor until it has stopped on its own.', None),
    ('Decanting and Records', ['Pellet disturbed', 'Run conditions not recorded'], ['Decant the clarified supernatant without disturbing the pellet.', 'Record speed, time and the tube set used.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs204(NUM, TITLE, [('ILS quotation Q0023979', 'Ohaus FC5706 centrifuge and 15 mL tubes'), ('Note', 'No procedure was held for this instrument before this revision')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'cut'], 'the centrifuge')
