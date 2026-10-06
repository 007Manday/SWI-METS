import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '201-010'
TITLE = 'Cyanide Adsorption Sampling Round - 051-TK-009 and 051-TK-010 (ReCYN)'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc(['Set the free and WAD cyanide profile across the cyanide adsorption train.',
             'Cyanide recovery here is the whole point of the ReCYN circuit - this profile is the measure of whether it is working.'],
            '051 Cyanide Adsorption',
            ['051-TK-009 - Cyanide adsorption tank 1', '051-TK-010 - Cyanide adsorption tank 2',
             '051-SC-005 / 051-SC-006 / 051-SC-020 - Adsorption screens'],
            'Once per shift on each tank; hourly during commissioning and after any upset.', '201-010')
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Equipment damaged or not in good condition'],
     prestart(NEW_JSEA), None,
     ['Sampling bucket 5 to 8 L', 'pH meter', 'Free cyanide titration kit and rhodanine indicator',
      'Burette, pipette, conical flask, stand and wash bottle', 'Filter press and filter paper', 'Bottles 250 mL',
      '0.9 mm sieve for resin check', PPE_EQ]),
    ('Sample Collection', ['HCN released at the open sample point', 'Splash of cyanide-bearing solution', 'Fall from the tank top', 'Resin carry-over not noticed'],
     ['Work tank 1 then tank 2 in sequence.',
      'Flush each point and discard the first flow.',
      'Check the sample for resin beads over the 0.9 mm sieve and report any carry-over.'],
     CAUTION_VALVE, None),
    ('pH and Free Cyanide', ['Meter out of calibration - wrong pH', 'Cyanide volatilising from the sample'],
     ['Determine pH and free cyanide in the field.'], None, None),
    ('Filtration and Profile Sheet', ['Splash of cyanide-bearing filtrate', 'Result not compared with the online analyser'],
     ['Filter and bottle for WAD cyanide and metal assay.',
      'Record both tanks on one profile sheet against the reading from the online cyanide analyser.'], None, None),
    CLOSE_STEP,
]
REFS = refs('201-010', TITLE, [('HM-PRC-V01-PRO007', 'Cyanide Adsorption Circuit (ReCYN) and Resin Transfer'),
    ('Mt. Morgan site procedure 14', 'Cyanide Adsorption 1 & 2 Tank Sampling [LIVE]'),
    ('KBK-MIR-MP-PRO-MET-SOP-0049', 'Pengambilan Sampel dan Pengukuran Profil Tangki Resin, received 11 Aug 2026'),
    ('KBK SOP-PROC-CNREC-01 and CNREC-12', 'Resin transfer and Fresh resin conditioning, received 11 Aug 2026'),
    ('4034-004-VE-025 Rev B', 'Goldquip vibrating screen IOM (051-SC-005/006/020), received 11 Aug 2026')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'fall', 'slip'])
