import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '201-016'
TITLE = 'Cyanide Elution, Stripping and AVR Sampling'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = ['Safety helmet and safety glasses', 'Chemical splash goggles and face shield', 'High-visibility long-sleeved shirt and long trousers',
       'Safety boots with sound tread - nitrile PVC boots at the sample point',
       'Chemical resistant suit, acid-resistant, nitrile rubber and heat-resistant gloves, and apron',
       'Personal HCN gas monitor, calibrated and in test date',
       'Full or half gas mask with A2B2E2K2P3 cartridge, carried and available for immediate use',
       'Harness and fall arrest where no fixed platform exists']
DESC = desc(['Track cyanide recovery through elution, stripping and acidification-volatilisation-regeneration.',
             'This circuit runs acidified cyanide solution. The sampling is the check that the recovery is working and that the scrubbers are holding.'],
            '081 Cyanide Elution and Stripping',
            ['081-CL-005 / 081-CL-006 - Cyanide elution columns',
             '081-CL-007 / 081-CL-008 - Stripping and scrubbing columns, identity in dispute, see holds',
             '081-SC-007 - Cyanide circuit screen'],
            'Each elution and stripping batch; scrubber solution each shift.', NUM)
STEPS = [
    ('Pre-start Check', ['Scrubber or exhaust fan not running', 'Ventilation interlock not healthy', 'Gas monitor or fixed detection not healthy', 'Circuit on a heating cycle or under pressure'],
     prestart(NEW_JSEA, ['Confirm with the control room where the batch is in the cyanide elution sequence.',
                         'Confirm the scrubber and its exhaust fan are running and the ventilation interlock is healthy BEFORE opening any sample point on this circuit. This circuit acidifies cyanide solution - the scrubber is the control.',
                         'Confirm the circuit is not on a heating cycle before sampling. Do not sample a column under pressure.']), None,
     ['Sample bottles 250 mL', 'pH meter', 'Free cyanide titration kit and rhodanine indicator', 'Burette, pipette, conical flask, stand and wash bottle',
      'Filter paper and funnel', 'Distilled water', PPE_EQ]),
    ('Sample Collection', ['HCN released from an acidified stream', 'Contact with hot solution', 'Release from a pressurised sample line', 'Fall from the column platform'],
     ['Flush the point and discard the first flow.', 'Collect the sample with the body clear of the discharge, and close the point immediately.'],
     CAUTION_VALVE, None),
    ('Field Determinations', ['HCN released when the sample is opened', 'Cyanide volatilising from the sample'],
     ['Determine pH and free cyanide in the field.',
      'On the acidified streams, take the sample straight to a fume-controlled position before opening it.'],
     'CAUTION: Acidified cyanide solution releases HCN. Never open the sample outside a fume-controlled position.', None),
    ('Laboratory Splits and Records', ['Splits mislabelled', 'Stage conditions not recorded'],
     ['Bottle the laboratory splits for WAD and total cyanide and for metal assay.',
      'Record batch number, stage, column temperature and scrubber solution pH at the time of sampling.'], None, None),
    CLOSE_STEP,
]
REFS = refs(NUM, TITLE, [('HM-PRC-V01-PRO019 and PRO020', 'Cyanide elution and stripping circuit procedures'),
    ('Mt. Morgan site procedures 13, 15, 16, 17 and 18', 'Cyanide circuit sampling [LIVE]'),
    ('KBK SOP-PROC-CNREC-13', 'Sampling for the cyanide elution, stripping and scrubbing circuit, received 11 Aug 2026 - a worked procedure for this exact duty'),
    ('KBK SOP-PROC-CNREC-02 and CNREC-03', 'Cyanide elution and Cyanide stripping and scrubbing, received 11 Aug 2026'),
    ('4034-017-VE-096 Rev B', 'Goldquip ReCYN column IOM (081-CL-005/006), received 11 Aug 2026')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'burn', 'acid', 'fall', 'slip'], 'an agitator, pump or screen')
