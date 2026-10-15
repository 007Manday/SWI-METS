import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '204-011'
TITLE = 'Filter Press Simulation and Cake Filtration Test'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB
DESC = desc204(['Measure filtration rate, cake moisture and washing behaviour at the bench.', 'It is how the plant filter press cycle time and cake moisture are predicted and troubleshot.'], 'On each new ore type and whenever plant cake moisture moves.', NUM, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA), None, ['Bench filter press or pressure filter', 'Filter cloths', 'Vacuum pump - Becker VT4.8 and manifold', 'Measuring cylinders', 'Drying oven', 'Balance', 'Stopwatch'] + [PPE_EQ]),
    ('Set-up', ['Release from a pressurised line or fitting', 'Pressure set above the plant operating pressure'], ['Record the feed slurry density and solids content.', 'Set the filtration pressure to the plant operating pressure.'], 'CAUTION: Check hoses and fittings before pressurising and stand clear of the discharge path.', None),
    ('Filtration and Wash', ['Splash of cyanide-bearing slurry or filtrate', 'HCN from the filtrate', 'Acid contact where the test uses acid'], ['Record filtrate volume against time through the whole cycle - the curve is the result, not the final volume.', 'Continue until filtrate flow effectively stops.', 'Apply the wash where the plant cycle includes one, and record the wash volume and time separately.', 'Blow or draw air through for the plant air-dry period.'], None, None),
    ('Cake Recovery and Report', ['Manual handling of the filter press plates', 'Cake moisture not determined'], ['Recover the cake, weigh it, and determine moisture by oven drying.', 'Report filtration rate, cake moisture, cycle time and the filtrate clarity.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs204(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0023', 'Filter Press'), ('ILS quotation Q0023979', 'Becker VT4.8 oil-free pump, 4-place manifold and filter flasks'), ('KBK SOP-PROC-CNREC-09', 'Filtration of copper precipitation, received 11 Aug 2026')])
EMERG = emerg(['hcn', 'cn', 'skin', 'acid', 'slip'], 'bench equipment')
