import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '205-007'
TITLE = 'Bottle Roll Leach Test - As-Received and Pulverised'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc205(['Determine gold extraction by cyanide leach at the bench, on as-received and on pulverised material.', 'The difference between the two says how much of the remaining gold is locked and how much is simply slow.'], 'On each new ore type, and on any tail sample being investigated.', NUM, True, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, [LAB_ALONE] + []), None, ['Bottle roller MkII 12-place with guarding', 'Bottles and caps', 'pH meter', 'Sodium cyanide solution at known strength', 'Lime', 'Filter apparatus', 'Balance', 'Pulveriser'] + [PPE_EQ]),
    ('Set-up and Charging', ['Roller guard or interlock not working', 'Pulveriser dust'], ['Confirm the bottle roller guarding is in place and the guard interlock works before loading.', 'Split the sample. Leave one split as received; pulverise the other to the method size.', 'Charge each bottle with the stated solids mass and solution volume.'], None, None),
    ('pH and Cyanide Addition', ['HCN released below pH 10.5', 'Cyanide splash'], ['Add lime to the target pH and confirm the pH before adding cyanide. NEVER add cyanide to a slurry below pH 10.5 - it releases HCN.', 'Add cyanide to the stated concentration and record the start time.'], 'CAUTION: NEVER add cyanide to a slurry below pH 10.5. It releases HCN.', None),
    ('Rolling, Sampling and Results', ['Bottle opened outside the fume cupboard', 'Extraction reported on one head only'], ['Roll for the stated period, opening at each interval only inside the fume cupboard to sample solution and to top up cyanide and lime.', 'At each interval record pH, free cyanide and take a solution sample for assay.', 'At the end, filter, wash and dry the residue, and assay both residue and final solution.', 'Calculate extraction against the calculated head and against the assayed head, and report both.'], 'CAUTION: Open bottles only inside the fume cupboard.', None),
    CLOSE_LAB_STEP,
]
REFS = refs205(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0003', 'Uji Pelindian Menggunakan Bottle Roll'), ('ILS quotation Q0023979', 'Bottle Roller MkII 12-place with guarding')])
EMERG = emerg(['hcn', 'cn', 'equip', 'chem', 'cut'], 'the bottle roller')
