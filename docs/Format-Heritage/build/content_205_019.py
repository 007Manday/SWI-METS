import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '205-019'
TITLE = 'Automatic Titrator Electrode Care, Standardisation and Verification'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc205(['Keep the titrator electrodes in condition and prove they are reading correctly.', 'Electrodes drift and age. An unverified electrode is the most common cause of a titrator giving wrong results that nobody questions.'], 'Daily standardisation; weekly verification; replacement on failure.', NUM, False, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, []), None, ['pH buffers 4, 7 and 10', 'ISE standards', 'Electrode storage solution', 'Distilled water', 'Soft tissue', 'Electrode log'] + [PPE_EQ]),
    ('Daily Standardisation', ['Electrode slope out of range', 'Out-of-date buffer'], ['Standardise the pH electrode daily against buffers 4, 7 and 10, and record the slope and offset.', 'Reject the electrode where the slope falls outside the acceptable range - do not keep using it because it still gives a number.', 'Standardise the ISE against its standards at the interval the method sets.'], None, None),
    ('Electrode Care', ['Junction stripped by wiping', 'Electrode stored in distilled water'], ['Rinse electrodes with distilled water between samples and blot dry - never wipe, which strips the junction.', 'Store electrodes in the correct storage solution. Never store in distilled water; it leaches the reference.', 'Check and top up the reference electrolyte at the interval the manual sets.'], None, None),
    ('Verification and Records', ['Verification missed', 'Record not traceable to the electrode'], ['Verify against an independent standard weekly and record it in the electrode log.', 'Record every standardisation, verification and replacement against the electrode serial number.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs205(NUM, TITLE, [('KBK-MIR-MP-PRO-MET-SOP-0030', 'Kalibrasi DO-meter (received 11 Aug 2026)'), ('KBK-MIR-MP-PRO-MET-SOP-0031', 'Kalibrasi pH-meter (received 11 Aug 2026)'), ('KBK-MIR-MP-PRO-MET-SOP-0043', 'AgNO3 standard (received 11 Aug 2026)'), ('ILS quotation Q0023979', 'Hanna HI902C titrator and electrodes')])
EMERG = emerg(['acid', 'chem', 'elec', 'cut'], 'bench equipment')
