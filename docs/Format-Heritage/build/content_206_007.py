import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '206-007'
TITLE = 'Met Lab Waste, Residue and Effluent Disposal'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc206(['Dispose of laboratory waste, residues and effluent to the correct route.', 'Cyanide-bearing laboratory effluent going to the wrong drain is an environmental incident and a reportable one.'], 'Every day, and at the end of every test.', NUM, True, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, [LAB_ALONE] + []), None, ['750 L tipping bin', '2 x 240 L Sulo bins', '60 L drum', 'Crossflow scrubber with pH control', 'Waste labels', 'Waste register'] + [PPE_EQ]),
    ('Segregation at the Bench', ['Acidic waste added to cyanide waste', 'Wastes mixed in one container'], ['Segregate at the bench. Cyanide-bearing, acidic, and general waste go to separate containers - never the same one.', 'NEVER put acidic waste into a cyanide-bearing waste container. That is an HCN generation event in a closed bin.'], 'CAUTION: Acid into a cyanide waste container generates HCN in a closed bin.', None),
    ('Neutralisation and Routing', ['Acidic waste to a shared route', 'Cyanide effluent to the wrong drain'], ['Neutralise acidic waste before it goes to any shared route, and confirm with pH paper.', 'Route cyanide-bearing effluent to the designated destination only. Confirm where that is before the first litre is generated.'], None, None),
    ('Labelling, Register and Removal', ['Unlabelled waste container', 'Register filled from memory', 'Manual handling of bins and drums'], ['Label every waste container with contents, hazard and accumulation start date.', 'Log the waste in the register as it is generated, not from memory at the end of the week.', 'Keep solid residues from testwork until the result is reported and accepted, then dispose.', 'Arrange removal at the set interval and file the disposal documentation.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs206(NUM, TITLE, [('KBK-MIR-LAB-ENV-SOP-058 and ENV-SOP-106', 'Sludge transfer and container neutralisation'), ('ILS quotation Q0023979', '750 L tipping bin, 2 x 240 L Sulo, 60 L drum, crossflow scrubber with pH control')])
EMERG = emerg(['hcn', 'cn', 'chem', 'acid', 'slip'], 'bench equipment')
