import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '205-005'
TITLE = 'Lime Availability Test'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc205(['Determine the available lime content of the delivered quicklime and of the slaked slurry.', 'Lime availability sets the addition rate. A low-availability delivery under-doses the whole circuit.'], 'Every delivery and weekly on the slaked slurry.', NUM, False, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, []), None, ['Burette and stand', 'Pipette', 'Conical flasks', 'Standardised HCl', 'Phenolphthalein indicator', 'Balance', 'Beakers', 'Stirrer', 'Distilled water'] + [PPE_EQ]),
    ('Sampling', ['Lime dust inhaled or in the eyes', 'Grab sample from the top of the load'], ['Take a representative sample of the delivery, not a grab from the top of the load.'], 'CAUTION: Quicklime heats as it slakes and burns skin and eyes. Goggles and gloves on.', None),
    ('Slaking and Titration', ['Heat and splash while slaking', 'Hydrochloric acid splash'], ['Weigh the sample accurately and slake it in distilled water under the method conditions.', 'Titrate the slaked suspension with standardised HCl to the phenolphthalein endpoint, stirring continuously.'], None, None),
    ('Calculation and Reporting', ['Below-specification delivery used', 'Trend not kept'], ['Record the titre and calculate available lime as per cent CaO.', 'Compare against the supply specification and report any delivery below specification before it is used.', 'Trend availability by delivery - a downward trend is a supplier problem, not a plant problem.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs205(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0024', 'Uji Kandungan Kapur'), ('4034-046-VE-019', 'Transmin quicklime slaking plant functional description (received 11 Aug 2026)')])
EMERG = emerg(['chem', 'acid', 'cut'], 'bench equipment')
