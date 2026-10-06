import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '206-001'
TITLE = 'Met Lab Chemical Receipt, Storage and Decanting'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc206(['Receive, store and decant laboratory chemicals safely and in a way that keeps them fit for use.', 'The laboratory holds concentrated acids, cyanide and oxidisers in one room. Segregation and labelling are the controls.'], 'Every delivery, and every decant.', NUM, True, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, [LAB_ALONE] + []), None, ['160 L flammable, 160 L corrosive and 60 L toxic cabinets', 'Fume cupboard', 'Decanting equipment', 'Spill kit', 'Chemical register', 'Labels', 'Safety data sheets'] + [PPE_EQ]),
    ('Receipt and Register', ['Damaged container accepted', 'No safety data sheet', 'Chemical not traceable'], ['Check the delivery against the order and the safety data sheet before accepting it.', 'Reject anything with a damaged container, an illegible label or no safety data sheet.', 'Log the chemical into the register with quantity, batch, date received and expiry.'], None, None),
    ('Segregated Storage', ['Acid stored where a leak could reach cyanide', 'Oxidiser stored with flammables', 'Manual handling of containers'], ['Store to the correct cabinet. Acids away from cyanide, oxidisers away from flammables, and nothing on the floor.', 'NEVER store an acid where a leak could reach cyanide. Acid on cyanide releases hydrogen cyanide gas.'], 'CAUTION: Acid on cyanide releases hydrogen cyanide gas. Segregation is the control.', None),
    ('Decanting', ['Acid or caustic splash', 'Acid fume or reagent vapour', 'Unlabelled decanted container'], ['Decant only in the fume cupboard, with the airflow confirmed and a spill kit at hand.', 'Label every decanted container immediately with contents, concentration, date and preparer.', 'Return the parent container to its cabinet before leaving the bench.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs206(NUM, TITLE, [('KBK-MIR-LAB-WET-SOP-025 and WET-SOP-047', 'Chemical issue and acid transfer'), ('ILS quotation Q0023979', '160 L flammable, 160 L corrosive and 60 L toxic/poisons cabinets')])
EMERG = emerg(['hcn', 'cn', 'chem', 'acid', 'cut', 'slip'], 'bench equipment')
