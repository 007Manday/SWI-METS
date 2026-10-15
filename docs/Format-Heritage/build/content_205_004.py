import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '205-004'
TITLE = 'Sodium Chloride (Chloride) Titration'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc205(['Determine chloride concentration in the made-up sodium chloride solution and in process streams.', 'Chloride affects the elution chemistry and is tracked in the copper circuit.'], 'Every made-up batch and per the analysis schedule.', NUM, False, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, []), None, ['Burette and stand', 'Pipette', 'Conical flasks', 'Standardised AgNO3', 'Potassium chromate indicator', 'Hanna HI902C with ISE channel', 'Distilled water'] + [PPE_EQ]),
    ('Sample Preparation', ['Sample outside the method pH range', 'Splash of cyanide-bearing solution'], ['Confirm the sample is near neutral pH before titrating - the argentometric method fails outside its pH range.', 'Pipette the aliquot into a conical flask.'], None, None),
    ('Titration', ['Silver nitrate or chromate contact with skin', 'Endpoint overshot'], ['Add the indicator.', 'Titrate with standardised AgNO3 to the first persistent colour change.', 'Record the titre and calculate chloride.'], None, None),
    ('ISE Channel and Standards', ['ISE not calibrated', 'Batch reported without a standard'], ['Where the HI902C ISE channel is used, calibrate against chloride standards before the run.', 'Run a standard with each batch of samples.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs205(NUM, TITLE, [('ILS quotation Q0023979', 'HI902C with ISE channel'), ('KBK titration method set', 'Chloride titration')])
EMERG = emerg(['cn', 'chem', 'cut'], 'bench equipment')
