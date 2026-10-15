import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '204-009'
TITLE = 'Static and Dynamic Settling Test'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB
DESC = desc204(['Measure how fast solids settle, with and without flocculant, and what underflow density results.', 'This is the test behind every thickener decision - flux, flocculant dose and underflow density.'], 'On each new ore type, and whenever thickener performance changes.', NUM, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA), None, ['Settling cylinders', 'Stopwatch', 'Flocculant solutions at known strength', 'Pipettes', 'Plunger', 'Marcy scale'] + [PPE_EQ]),
    ('Sample and Flocculant Preparation', ['Splash of cyanide-bearing slurry', 'Flocculant not at plant strength'], ['Prepare the sample at the thickener feed density and record it.', 'Make up flocculant at the plant strength. A test run on differently prepared flocculant does not transfer to the plant.'], None, None),
    ('Settling Test', ['Over-mixing shearing the floc', 'Cuts from a broken cylinder', 'HCN from the open sample'], ['Fill the cylinder, add the flocculant dose and mix with the plunger using the standard number of strokes. Over-mixing shears the floc and understates the settling rate.', 'Start the clock and record the interface height at set intervals.', 'Continue until the interface stops moving, then record the compaction over time.', 'Repeat at three or more flocculant doses to find the response curve.'], None, None),
    ('Calculation and Report', ['Dose not related to the design basis'], ['Calculate the settling rate and the achievable underflow density for each dose.', 'Report the optimum dose and the flux against the thickener design basis.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs204(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0014', 'Uji Pengendapan'), ('4034-018A-VE-007', 'Roytec tails thickener control philosophy, received 11 Aug 2026')])
EMERG = emerg(['hcn', 'cn', 'skin', 'cut'], 'bench equipment')
