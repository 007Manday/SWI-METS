import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '206-011'
TITLE = 'Met Lab Emergency Response - Power Failure and Evacuation'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc206(['Respond to a power failure or an evacuation order in the laboratory.', 'On a power failure the fume cupboards and the scrubber stop. Everything that was safe because it was being extracted is no longer safe.'], 'On any power failure or evacuation; drill at the set interval.', NUM, True, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, [LAB_ALONE] + []), None, ['Emergency lighting', 'UPS-backed instruments', 'Emergency contact list', 'Muster point', 'Personal HCN monitor'] + [PPE_EQ]),
    ('Immediate Actions on Power Loss', ['Work continued by torchlight', 'Fume venting into the room', 'Heating equipment restarting unattended'], ['On loss of power, stop all work immediately. Do not continue by torchlight.', 'Assume the fume cupboards and the scrubber have stopped. Anything generating fume is now venting into the room.', 'Cap or cover open cyanide and acid containers if it can be done in seconds without leaning into a cupboard. If not, leave them.', 'Switch off heating equipment - hotplates, ovens, furnaces - so they do not restart unattended when power returns.'], 'CAUTION: Do not lean into a stopped fume cupboard. Leave open containers if they cannot be covered in seconds.', None),
    ('Evacuation and Muster', ['Person left in the laboratory', 'Door left open'], ['Leave the laboratory, close the door behind you and report to the muster point.', 'Account for everyone who was in the laboratory.'], None, None),
    ('Re-entry', ['Re-entry before extraction is running', 'Interrupted test resumed'], ['Do not re-enter until power is restored, extraction is confirmed running and the Laboratory Supervisor releases the room.', "On re-entry, check every instrument's state before restarting work, and discard any test that was interrupted rather than resuming it."], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs206(NUM, TITLE, [('KBK-MIR-LAB-WET-SOP-050', 'Evacuation on sudden power failure'), ('ILS quotation Q0023979', '2 x Riello UPS 2200VA')])
EMERG = emerg(['hcn', 'cn', 'chem', 'acid', 'elec', 'burn'], 'bench equipment')
