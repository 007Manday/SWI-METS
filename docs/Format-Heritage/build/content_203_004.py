import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '203-004'
TITLE = 'Residence Time and Tracer Test on Leach and Adsorption Trains'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc203(['Measure the actual residence time and the degree of short-circuiting in the leach and adsorption trains.',
                'Design residence time assumes ideal mixing. Real tanks short-circuit, and a train that short-circuits loses recovery no matter how good the chemistry is.'],
               '203 Plant Surveys', ['031-TK-001 - Leach tank', '032-TK-002 to -006 - CIL train', '041-TK-007/008 - Metal adsorption', '051-TK-009/010 - Cyanide adsorption'],
               'Once at commissioning, then after any change to feed rate, agitator or tank configuration.', NUM)
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Unapproved tracer introduced to the circuit'],
     prestart203(NEW_JSEA, ['Agree the tracer with the Metallurgist and confirm it is compatible with a cyanide circuit and with the downstream product. Do NOT introduce anything to the circuit that has not been approved.',
                            'Confirm the circuit is at steady state and will be held there for the full test.']), None,
     ['Tracer approved for use in a cyanide circuit', 'Sample containers, timed series, pre-labelled', 'Stopwatch', 'Field data sheets', PPE_EQ]),
    ('Tracer Injection', ['Tracer handling splash', 'Clock not started at injection'],
     ['Inject the tracer as a pulse at the train inlet and start the clock at injection.'], None, None),
    ('Outlet and Intermediate Sampling', ['HCN released at the sample points', 'Fall from the tank top', 'Samples missed or mislabelled'],
     ['Sample the outlet at the stated interval for at least three theoretical residence times.',
      'Sample intermediate tanks where the arrangement allows it, so short-circuiting can be located, not just detected.'], CAUTION_VALVE, None),
    ('Analysis and Report', ['Wrong residence time distribution'],
     ['Analyse the tracer concentration series and construct the residence time distribution.',
      'Compare the measured mean residence time against the design, and report the degree of short-circuiting by tank.'], None, None),
    CLOSE203_STEP,
]
REFS = refs203(NUM, TITLE, [('Plant Operating Manual Sections 3.4 and 3.5', 'Train configuration and design residence time'),
    ('Note', 'No direct source held - written from first principles')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'fall'])
