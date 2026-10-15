import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '205-015'
TITLE = 'Cyanide Destruction (Detox) Bench Test'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = [h for h in hazards_from(os.environ['SRC_DOCX']) if 'TSF water' not in h]
PPE = PPE_LAB_ACID
DESC = desc205(['Test cyanide destruction at the bench by the candidate routes - peroxide and SO2/air.', 'The detox route has to be proven at the bench before it is designed, and the tailings cyanide obligation depends on it.'], 'To be set once the route is chosen.', NUM, True, extra_bold=['ISSUED BUT NOT FOR USE. Mt. Morgan has no detox circuit - the ReCYN circuit follows CIL. The back-up detox route decision (OR-07) is open and no cyanide destruction route has been chosen, so this bench test cannot be defined. The Martabe TSF Toe to WPP Test is a water neutralisation test and has been moved to SWI-PRO-MET-205-006.'], points=('Met lab bench - physical testwork bench and instrument',))
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, [LAB_ALONE] + []), None, ['Reaction vessel with stirring and pH control', 'Peroxide and SO2/air reagents', 'Copper catalyst', 'pH and ORP meters', 'Cyanide analysis set', 'Fume cupboard'] + [PPE_EQ]),
    ('Status - Not for Use', ['Task attempted without a chosen destruction route'], ['This task cannot be completed. Mt. Morgan has no detox circuit and the back-up detox route decision (OR-07) is open.', 'The document is issued so the register line is not empty, and is marked NOT FOR USE.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs205(NUM, TITLE, [('OR-07', 'Back-up Detox definition memo - the decision is open'), ('Martabe WI (undated)', 'TSF Toe to WPP Test (Work_Instruction_Tsf_Toe) - moved to SWI-PRO-MET-205-006'), ('SWI-PRO-MET-205-006', 'Lime Addition and Lime Demand Test - acid water neutralisation')])
EMERG = emerg(['hcn', 'cn', 'acid', 'chem'], 'bench equipment')
