import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '205-001'
TITLE = 'Free Cyanide Titration - Silver Nitrate Method'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc205(['Determine free cyanide by titration against standardised silver nitrate.', 'Free cyanide is the single most important solution number on this plant - it drives dosing, recovery and the environmental obligation.', 'Two checks are taken from the Martabe method: a digital burette reads 0.00 before the titration starts, and the AgNO3 is in date.'], 'Every shift on every cyanide-bearing stream on the schedule.', NUM, True, extra_bold=[], points=('Met lab bench - physical testwork bench and instrument',))
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, [LAB_ALONE] + []), None, ['Burette 50 mL and stand', 'Pipette 10 or 25 mL', 'Conical flasks 250 mL', 'Standardised AgNO3 0.01 M, in date', 'Rhodanine indicator', 'Wash bottle and distilled water', 'Fume cupboard', 'Digital burette and syringe for the aliquot (optional)'] + [PPE_EQ]),
    ('Sample and Burette Preparation', ['HCN from cyanide solution, faster at low pH', 'AgNO3 out of date', 'Air in the burette tip'], ['Work in the fume cupboard with the airflow confirmed. Cyanide solutions release HCN, faster if the pH has dropped.', 'Filter the sample if it is not already clear, and titrate as soon after filtration as possible to limit volatilisation loss.', 'Check the AgNO3 expiry date. Out-of-date titrant is not used.', 'Rinse the burette with distilled water then condition it three times with standardised AgNO3.', 'Fill the burette and expel air from the tip. Where a digital burette is used, check the display reads 0.00 before starting.'], 'CAUTION: Cyanide solutions release HCN. Work in the fume cupboard with the airflow confirmed.', None),
    ('Titration', ['Cyanide splash', 'End point overshot'], ['Pipette the aliquot into a conical flask, or take it with the syringe where the digital burette is used.', 'Add 3 to 5 drops of rhodanine indicator - the solution turns pale yellow.', 'Add AgNO3 dropwise with continuous swirling. As the endpoint nears a salmon pink precipitate forms and redissolves slowly; slow the addition there.', 'Continue dropwise until a permanent salmon pink holds for 30 seconds without swirling. This is the end point, not a plain pink.'], None, None),
    ('Calculation and Quality Checks', ['Result not checked by duplicate or standard'], ['Record the burette reading and calculate free cyanide.', 'Run a duplicate on every tenth sample and a standard once per shift.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs205(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0010', 'Titrasi Sianida'), ('KBK-MIR-MP-PRO-MET-SOP-0037', 'Titrasi Sianida dengan Perak Nitrat (received 11 Aug 2026)'), ('KBK-MIR-MP-PRO-MET-SOP-0043', 'AgNO3 0.01 M standard (received 11 Aug 2026)'), ('DOC-3-MET-PMC-WIN-00115-IE v1.0', 'Martabe WI Cyanide Measurement by AgNO3 Titration (25/12/2024) - comparison; digital burette zero check and AgNO3 expiry check taken from it'), ('DOC-IV-MET-CHH-SOP-00039', 'Martabe reagent lifetime system referenced by the Martabe WI - not received')])
EMERG = emerg(['hcn', 'cn', 'chem', 'cut'], 'bench equipment')
