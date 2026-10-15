import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '206-009'
TITLE = 'Bottle Roller, Bench Mill and Agitator Operation'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID_HEAR
DESC = desc206(['Operate the bottle roller, bench mill and magnetic stirrers safely.', 'These are the rotating machines in the laboratory and the guarding is what keeps hands out of them.'], 'Every testwork run using them.', NUM, False, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, []), None, ['Bottle Roller MkII 12-place with guarding', '4 x MS8 magnetic stirrers', 'Bench mill', 'Bottles, caps and seals', 'Timer'] + [PPE_EQ]),
    ('Bottle Roller', ['Hands caught in the rollers', 'Bottle opening and spraying cyanide slurry', 'Unbalanced load'], ['Confirm the guard is in place and the guard interlock stops the machine before loading anything.', 'Check every bottle cap and seal before loading. A bottle that opens on the roller sprays cyanide slurry across the room.', 'Load bottles evenly across the rollers so the load is balanced.', 'Set the speed and the timer to the method and start.', 'Never reach in to adjust a bottle while the rollers are turning. Stop the machine first.'], 'CAUTION: Stop the machine before reaching in. The guard interlock must stop the rollers.', None),
    ('Bench Mill', ['Contact with the rotating mill', 'Hearing damage at the mill', 'Lid opened while turning'], ['For the bench mill, confirm the charge and the lid clamp before starting, and do not open it until it has stopped.'], 'CAUTION: Wear hearing protection at the bench mill.', None),
    ('Magnetic Stirrers and Clean-up', ['Liquid thrown by the vortex', 'Heated stirrer left unattended'], ['For magnetic stirrers, set the speed so the vortex does not throw liquid, and never leave a heated stirrer unattended.', 'Clean the rollers and the bench after every run.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs206(NUM, TITLE, [('ILS quotation Q0023979', 'Bottle Roller MkII 12-place with guarding, 4 x MS8 magnetic stirrers'), ('KBK-MIR-MP-PRO-OPE-SOP-0003', 'Pulverized Bottle Roll Test')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'cut', 'slip'], 'the bottle roller, bench mill or stirrer')
