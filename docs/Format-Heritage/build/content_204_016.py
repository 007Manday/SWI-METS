import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '204-016'
TITLE = 'Dry Sieve Analysis - Ro-Tap RX29 and 200 mm Sieve Set'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_HEAR
DESC = desc204(['Determine the size distribution of a dry sample by mechanical sieving.', 'The standard sizing method for anything that does not need wet screening first.'], 'As required by the analysis schedule.', NUM, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA), None, ['Ro-Tap RX29 and sound enclosure', '200 mm sieve set 38 um to 2 mm', 'Balance', 'Brushes', 'Ultrasonic sieve cleaner', 'Receiving pan'] + [PPE_EQ]),
    ('Sieve and Sample Preparation', ['Damaged or blinded sieve used', 'Dust from the dry sample'], ['Confirm the sieve set is clean and the apertures are intact before use.', 'Dry the sample to constant mass and record the dry mass.', 'Stack the sieves in descending aperture order with the pan at the bottom.'], None, None),
    ('Sieving', ['Overloaded sieve blinding', 'Hearing damage at the shaker', 'Hands caught in the shaker'], ['Load the sample onto the top sieve. Do not overload - an overloaded sieve blinds and under-reports the fines.', 'Shake on the Ro-Tap for the standard period with the sound enclosure closed.'], 'CAUTION: Close the sound enclosure and wear hearing protection. Keep hands clear until the shaker has stopped.', None),
    ('Weighing and Mass Check', ['Loss above tolerance reported', 'Sieve set not recorded'], ['Weigh each retained fraction and the pan.', 'Check the sum against the dry mass and repeat if the loss exceeds tolerance.', 'Clean the sieves immediately after use and record the sieve set identity against the result.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs204(NUM, TITLE, [('ILS quotation Q0023979', 'Ro-Tap RX29 shaker, sound enclosure and twelve 200 mm sieves'), ('KBK-MIR-LAB-PRE-SOP-008', 'Uji Kehalusan Sampel')])
EMERG = emerg(['equip', 'cn', 'skin', 'slip'], 'the shaker or other bench equipment')
