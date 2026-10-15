import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '206-003'
TITLE = 'Balance Verification and Calibration Check'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc206(['Verify the laboratory balances against certified weights so every mass is defensible.', 'Every assay, every moisture and every solution standard depends on a balance reading truly.'], 'Daily verification before use; full calibration at the external interval.', NUM, False, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, []), None, ['Class F1 weight set 10 mg to 200 g', 'GR-200 0.1 mg analytical balance', 'BM-22 micro balance', '150 kg platform balance', 'Draught shield', 'Balance log'] + [PPE_EQ]),
    ('Balance Set-up', ['Balance not level or in a draught', 'Balance not warmed up'], ['Confirm the balance is level, clean and in a draught-free position before use.', 'Allow the balance to warm up for the period the manual specifies.'], None, None),
    ('Verification with Certified Weights', ['Weight handled by hand', 'Reading outside tolerance not acted on'], ['Zero the balance, then verify with at least a low, a mid and a high certified weight from the F1 set.', 'Handle certified weights only with tongs or gloves. A fingerprint on a 10 mg weight is a real error.', 'Record each reading against the certified value and the allowable tolerance.'], None, None),
    ('Out of Tolerance and Records', ['Out-of-tolerance balance used for rough work', 'External calibration missed'], ['Where any point is outside tolerance, take the balance out of service and label it. Do not use it for rough work in the meantime.', 'Record every verification in the balance log against the balance identity.', 'Arrange external calibration at the set interval and file the certificate.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs206(NUM, TITLE, [('KBK-MIR-LAB-PRE-SOP-012 and WET-SOP-013, -014, -015', 'Balance verification'), ('ILS quotation Q0023979', 'Class F1 weight set 10 mg to 200 g, GR-200 and BM-22 balances, 150 kg platform balance')])
EMERG = emerg(['cn', 'skin', 'cut'], 'bench equipment')
