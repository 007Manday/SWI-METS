import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '204-012'
TITLE = 'Bond Ball Mill Work Index Test'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_HEAR
DESC = desc204(['Determine the Bond ball mill work index of the ore.', 'The work index sets the milling energy the circuit needs. Getting it wrong sizes the mill wrong.'], 'On each new ore type or ore blend.', NUM, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA), None, ['Bond ball mill and standard charge', 'Sieve set', 'Ro-Tap shaker', 'Balance', 'Riffle splitter', 'Drying oven'] + [PPE_EQ]),
    ('Feed Preparation', ['Dust from crushing', 'Feed reduced by prolonged grinding'], ['Prepare the feed to the standard top size by stage crushing, not by prolonged grinding.', 'Determine the feed size distribution and the F80.'], None, None),
    ('Locked Cycle Test', ['Contact with the rotating mill', 'Hearing damage at the mill', 'Manual handling of the ball charge'], ['Charge the mill with the standard ball charge and the standard sample volume.', 'Run the locked cycle test, screening at the closing screen and returning the oversize each cycle.', 'Continue cycles until the circulating load stabilises at 250 per cent within the allowed tolerance.'], 'CAUTION: Stop and isolate the mill before opening it. Wear hearing protection. Two-person lift for the ball charge.', None),
    ('Product Sizing and Report', ['Work index reported without F80 and P80'], ['Determine the product size distribution and the P80 on the last cycles.', 'Calculate the work index from the standard Bond equation.', 'Report with the closing screen size, the F80 and the P80 - a work index without them is not usable.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs204(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0006', 'Uji Bond Work Index (BWI)')])
EMERG = emerg(['equip', 'cn', 'skin', 'slip'], 'the mill or shaker')
