import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '203-005'
TITLE = 'Leach and CIL Profile Survey - Tank-by-Tank Gold and Cyanide Profile'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc203(['Build the tank-by-tank gold and cyanide profile down the leach and CIL trains.',
                'The profile shows where the leach is finishing and where adsorption is actually happening. Without it, carbon is moved and cyanide is dosed on guesswork.'],
               '203 Plant Surveys', ['031-TK-001 - Leach tank', '032-TK-002 to -006 - CIL tanks 1 to 5'],
               'Quarterly, and whenever recovery moves without an obvious cause.', NUM)
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Plant not at steady state'],
     prestart203(NEW_JSEA, ['Confirm steady state and hold the circuit through the survey.']), None,
     ['Sample containers pre-labelled by tank', 'pH meter', 'DO meter', 'Free cyanide titration kit', 'Filter press and filter paper', 'Field data sheets', PPE_EQ]),
    ('Profile Sampling', ['HCN released at the sample points', 'Fall from the tank top', 'Confined space atmosphere at the tank top hatch', 'Tanks not sampled in one pass'],
     ['Sample every tank in the train in sequence, in one pass, so the profile represents one moment.',
      'Determine pH, dissolved oxygen and free cyanide in the field at each tank.',
      'Take carbon concentration and carbon loading for each CIL tank on the same pass.'],
     'CAUTION: No entry. Sample from outside the tank top hatch or launder opening only.', None),
    ('Filtration and Assay', ['Splash of cyanide-bearing filtrate', 'Samples mixed up between tanks'],
     ['Filter each sample and submit solution and solids for gold assay.'], None, None),
    ('Profile and Report', ['Profile plotted against the wrong tank order'],
     ['Plot solution gold, solids gold and carbon loading down the train.',
      'Identify the tank where leaching finishes and the tank where adsorption stops being effective.',
      'Report against the design profile and recommend any carbon movement or dosing change.'], None, None),
    CLOSE203_STEP,
]
REFS = refs203(NUM, TITLE, [('4034-PR-PRO-002', 'Sampling Protocol, Leach Area table'),
    ('KBK-MIR-MP-PRO-MET-SOP-0019 and SOP-0048', 'Profil Leaching and leach tank sampling and profile, received 11 Aug 2026'),
    ('HM-PRC-V01-PRO004 and PRO005', 'Leach Circuit and Carbon in Leach')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'tankdown', 'fall', 'slip'])
