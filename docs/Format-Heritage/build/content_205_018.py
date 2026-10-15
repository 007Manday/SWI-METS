import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '205-018'
TITLE = 'Automatic Titrator Operation and Method Set-Up'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc205(['Set up and run the Hanna HI902C automatic titrator with the methods the plant needs.', 'The titrator replaces manual titration for routine work. A wrongly configured method produces confident wrong answers all shift.'], 'At set-up, and whenever a method is added or changed.', NUM, False, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, []), None, ['Hanna HI902C pH/ORP/ISE titrator', 'Electrodes and ISE probes', 'Standard solutions', 'Titrant reservoirs', 'Beakers and stirrers', 'Fume cupboard'] + [PPE_EQ]),
    ('Electrode and Titrant Set-up', ['Titrant splash while priming', 'Air in the burette'], ['Confirm the correct electrode or ISE is fitted for the determination and that it is conditioned.', 'Load the titrant and prime the burette, expelling all air.'], None, None),
    ('Method Entry and Proving', ['Method run on samples before a standard', 'Result adjusted instead of the method'], ['Enter the method parameters from the manual method being ported - aliquot, titrant concentration, endpoint criterion, stirring and dosing rate.', 'Run the method against a known standard first. Do not run samples until the standard reads correctly.', 'Compare the titrator result against a manual titration on the same sample, in duplicate.', 'Where the two disagree beyond tolerance, correct the method - do not adjust the result.'], None, None),
    ('Method Control', ['Uncontrolled method version', 'Verification missed'], ['Save the method under a controlled name and version and record it in the method register.', 'Re-verify against a manual titration weekly and after any electrode change.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs205(NUM, TITLE, [('ILS quotation Q0023979', 'Hanna HI902C automatic titrator with ISE'), ('KBK-MIR-MP-PRO-MET-SOP-0025, -0037, -0039, -0040, -0041, -0042 and -0043', 'The seven titration methods to port (all received 11 Aug 2026)')])
EMERG = emerg(['hcn', 'acid', 'chem', 'elec', 'cut'], 'bench equipment')
