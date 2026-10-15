import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '203-009'
TITLE = 'Reagent Dosing Verification and Dosing Pump Calibration Check'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
PPE = ['Safety helmet and safety glasses', 'Chemical splash goggles and face shield', 'High-visibility long-sleeved shirt and long trousers',
       'Safety boots with sound tread - nitrile PVC boots at the sample point',
       'Chemical resistant suit, acid-resistant and nitrile rubber gloves, and apron',
       'Personal HCN gas monitor and personal multi-gas monitor including H2S, calibrated and in test date',
       'Full or half gas mask with A2B2E2K2P3 cartridge, carried and available for immediate use']
DESC = desc203(['Prove that each dosing pump is delivering what the control system says it is delivering.',
                'A dosing pump out of calibration means the circuit is being dosed at a rate nobody knows, and the reagent reconciliation will never close.'],
               '203 Plant Surveys', ['101 to 107 - All reagent dosing pumps'],
               'Quarterly, and after any dosing pump repair or replacement.', NUM)
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Wrong pump or reagent', 'Off-strength reagent'],
     prestart203(NEW_JSEA, ['Confirm with the control room which pump is being checked and that the circuit can tolerate a short interruption to that dose.',
                            'Read the strength of the made-up reagent from the current batch record - a dose check against an off-strength reagent proves nothing.']), None,
     ['Calibrated measuring cylinder', 'Stopwatch', 'Bucket', 'Field data sheets', 'PPE matched to the reagent being checked']),
    ('Dose Check', ['Acid or caustic burn to skin or eyes', 'H2S released from sodium hydrosulphide', 'HCN released at the cyanide pump', 'Live dosing line broken'],
     ['Divert the pump discharge to a measuring cylinder for a timed period, using the designated calibration connection. Never break a live dosing line to do this.',
      'Record the volume delivered and the time, and calculate the actual rate.',
      'Compare against the rate the control system indicates and against the setpoint.',
      'Repeat three times and take the mean.'],
     'CAUTION: Never break a live dosing line. Use the designated calibration connection only. Match the PPE to the reagent.', None),
    ('Out of Tolerance and Restoration', ['Pump left out of service', 'Correction factor not recorded'],
     ['Report any pump outside tolerance for recalibration, and record the correction factor in the interim.',
      'Restore the pump to service and confirm the dose has resumed.'], None, None),
    CLOSE203_STEP,
]
REFS = refs203(NUM, TITLE, [('HM-PRC-V01-PRO021 to PRO027', 'Reagent procedures'),
    ('HM-PP-006B', 'Reagents Consumption 2026 - design dose rates'),
    ('4034-046-VE-019 Rev A', 'Transmin quicklime slaking plant functional description, received 11 Aug 2026')])
EMERG = emerg(['hcn', 'h2s', 'cn', 'chem', 'acid', 'elec', 'slip'], 'a pump, agitator or sample cutter')
