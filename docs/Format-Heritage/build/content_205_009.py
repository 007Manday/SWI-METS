import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '205-009'
TITLE = 'CIL/CIP Sequential Triple Contact Testwork'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc205(['Run the sequential triple contact test to measure adsorption performance and predict circuit behaviour.', 'It is the standard bench test for sizing and troubleshooting a carbon or resin adsorption circuit.'], 'On each new ore type and when adsorption performance is being investigated.', NUM, True, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, [LAB_ALONE] + []), None, ['Bottle roller', 'Bottles', 'Activated carbon or resin at known mass', 'Screens to separate carbon or resin', 'Filter apparatus', 'Balance', 'pH meter', 'Fume cupboard'] + [PPE_EQ]),
    ('Pulp Preparation and First Contact', ['HCN released below pH 10.5', 'Contact with the bottle roller'], ['Prepare the leached pulp at the plant conditions - density, pH and free cyanide.', 'Charge the first contact with the stated mass of carbon or resin and roll for the stated period.'], 'CAUTION: Confirm the pulp is at or above pH 10.5 before it is opened or transferred.', None),
    ('Second and Third Contacts', ['Cyanide-bearing pulp splash', 'Carbon or resin lost on the screen'], ['Separate the carbon or resin on the screen, wash it and retain it for assay.', 'Carry the pulp forward to the second contact with fresh carbon or resin, and repeat.', 'Repeat for the third contact.'], None, None),
    ('Assay and Calculation', ['Contact not assayed', 'Loading reported without kinetics'], ['Assay the solution before and after each contact and the loaded carbon or resin from each.', 'Calculate the loading achieved and the solution depletion at each contact.', 'Report the equilibrium loading and the kinetics implied by the three contacts.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs205(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0021', 'CIL Testwork Sequential Triple Contact')])
EMERG = emerg(['hcn', 'cn', 'equip', 'chem', 'cut'], 'the bottle roller')
