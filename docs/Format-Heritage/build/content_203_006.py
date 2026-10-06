import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '203-006'
TITLE = 'Adsorption Profile Survey - Metal and Cyanide Resin Circuits'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc203(['Build the profile across the metal and cyanide adsorption trains - solution metal, solution cyanide and resin loading tank by tank.',
                'This is the measure of whether the ReCYN circuit is recovering what it was bought to recover.'],
               '203 Plant Surveys', ['041-TK-007/008 - Metal adsorption train', '051-TK-009/010 - Cyanide adsorption train'],
               'Quarterly, and after any change to resin inventory or transfer rate.', NUM)
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Plant not at steady state'],
     prestart203(NEW_JSEA, ['Confirm steady state and hold the circuit through the survey.']), None,
     ['Sample containers pre-labelled by tank', 'pH meter', 'Free cyanide titration kit', '0.9 mm sieve', 'Measuring glass', 'Filter press and filter paper', 'Field data sheets', PPE_EQ]),
    ('Profile Sampling', ['HCN released at the sample points', 'Fall from the tank top', 'Tanks not sampled in one pass'],
     ['Sample every adsorption tank in sequence in one pass.',
      'Take resin concentration and a resin sample from each tank on the same pass.'], CAUTION_VALVE, None),
    ('Field Determinations and Submission', ['Cyanide volatilising from the sample', 'Samples mixed up between tanks'],
     ['Determine pH and free cyanide in the field.',
      'Submit solution for metal assay and resin for loading assay.'], None, None),
    ('Profile, Isotherm and Bead Size', ['Deviation from the isotherm not reported', 'Resin attrition not noticed'],
     ['Plot solution metal, solution cyanide and resin loading down each train.',
      'Compare the measured profile against the design adsorption isotherm and report the deviation.',
      'Check the bead size distribution on the resin samples as an attrition indicator.'], None, None),
    CLOSE203_STEP,
]
REFS = refs203(NUM, TITLE, [('4034-PR-PRO-002', 'Sampling Protocol, ReCYN Adsorption table'),
    ('KBK-MIR-MP-PRO-MET-SOP-0049 and SOP-0058', 'Resin tank sampling and profile, and resin PSD, received 11 Aug 2026'),
    ('KBK SOP-PROC-CNREC-01', 'Resin transfer between adsorption tanks, received 11 Aug 2026'),
    ('HM-PRC-V01-PRO006 and PRO007', 'Metal Adsorption and Cyanide Adsorption circuits')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'fall', 'slip'])
