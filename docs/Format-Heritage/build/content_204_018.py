import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '204-018'
TITLE = 'Vacuum Filtration of Test Products'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB
DESC = desc204(['Filter test products at the bench under vacuum to recover solids and solution for assay.', 'Almost every leach and adsorption test ends with a filtration, and a poor one loses fines and biases the result.'], 'Every test requiring solid and solution separation.', NUM, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA), None, ['Becker VT4.8 oil-free vacuum pump', '4-place manifold', 'Filter flasks', 'Buchner funnels', 'Filter papers', 'Wash bottle', 'Measuring cylinders'] + [PPE_EQ]),
    ('Filter Set-up', ['Wrong paper grade passing fines', 'Cracked flask failing under vacuum'], ['Select the filter paper grade the method specifies. A coarse paper passes fines into the filtrate and biases the solution assay high.', 'Seat and wet the paper before applying vacuum.'], None, None),
    ('Filtration and Wash', ['HCN from the filtrate', 'Splash of cyanide-bearing solution', 'Part sample filtered'], ['Filter the full sample - do not decant and filter only part of it.', 'Record the filtrate volume.', 'Wash the cake with the stated wash volume where the method calls for it, and keep the wash separate from the filtrate if the method requires it.', 'Draw air through for the stated period to dewater the cake.'], 'CAUTION: Work cyanide-bearing filtrations in the fume cupboard.', None),
    ('Cake Recovery and Check', ['Solids loss not reported'], ['Recover the cake with the paper, dry and weigh.', 'Check the solids recovered against the solids charged and report any loss.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs204(NUM, TITLE, [('ILS quotation Q0023979', 'Becker VT4.8, 4-place manifold, four filter flasks and Buchner funnels')])
EMERG = emerg(['hcn', 'cn', 'skin', 'cut'], 'bench equipment')
