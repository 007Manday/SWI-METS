import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '206-013'
TITLE = 'Ductless Fume Cabinet Filter Change and Breakthrough Check'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc206(['Change the carbon filters on the ductless fume cabinet and check for breakthrough before it happens.', 'A ductless cabinet with a saturated filter discharges everything it has captured straight back into the room, and gives no indication that it is doing so.'], "Breakthrough check monthly; filter change on indication or at the manufacturer's interval.", NUM, True, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, [LAB_ALONE] + []), None, ['Purair 30-PP ductless cabinet', 'Replacement carbon filters', 'Airflow indicator', 'Detector tubes or photoionisation detector for breakthrough', 'Gloves and disposal bags', 'Filter log'] + [PPE_EQ]),
    ('Airflow and Breakthrough Check', ['Spent filter discharging fume into the room', 'Airflow out of range'], ['Confirm the cabinet airflow is within range before any use, and record it.', 'Carry out the breakthrough check at the interval set - sample the discharge air with detector tubes or a suitable detector while a representative solvent or reagent is in use.', 'Any detection in the discharge means the filter is spent. Take the cabinet out of service immediately and label it.', 'Track filter life by usage, not by calendar alone. A cabinet used heavily saturates faster.'], 'CAUTION: Any detection in the discharge means the filter is spent. Take the cabinet out of service.', None),
    ('Filter Change', ['Contact with a spent filter', 'Seal not made on the new filter', 'Manual handling of the filter'], ['To change: isolate the cabinet, wear gloves, remove the spent filter and bag it immediately as chemical waste.', 'Fit the new filter, confirm the seal and re-check the airflow.', 'Record the change date, the filter batch and the airflow reading in the filter log.'], None, None),
    ('Use Limits', ['Reagent the filter is not rated for'], ['Do not use the cabinet for any reagent the filter is not rated for. Carbon does not capture everything.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs206(NUM, TITLE, [('ILS quotation Q0023979', 'Purair 30-PP ductless cabinet with carbon filters'), ('Note', 'No procedure was held for this cabinet before this revision')])
EMERG = emerg(['cn', 'chem', 'acid', 'slip'], 'bench equipment')
