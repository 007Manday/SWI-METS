import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '206-008'
TITLE = 'Glassware Cleaning and Drying'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc206(['Clean and dry laboratory glassware so it does not carry contamination into the next result.', 'A trace of gold or cyanide carried over on glassware contaminates the next sample and the error is invisible.'], 'After every use.', NUM, False, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, []), None, ['Wash sinks', 'Detergent', 'Acid wash bath where the method requires it', 'Distilled or RO/DI water', 'Drying oven and drying racks', 'Brushes', 'Fume cupboard for acid washing'] + [PPE_EQ]),
    ('Rinsing and Washing', ['Cyanide rinse to the general drain', 'Residues dried on'], ['Rinse glassware immediately after use, before residues dry on.', 'Discard the rinse to the correct waste stream - a cyanide rinse is cyanide waste.', 'Wash with detergent and a brush, then rinse with tap water.'], None, None),
    ('Acid Wash and Final Rinse', ['Acid splash or fume', 'Acid on cyanide residue'], ['Acid wash where the method requires it, in the fume cupboard, then rinse thoroughly.', 'Give a final rinse with distilled or RO/DI water. Tap water leaves dissolved solids.'], 'CAUTION: Rinse all cyanide residue off before acid washing. Acid on cyanide releases HCN.', None),
    ('Inspection, Drying and Storage', ['Cuts from damaged glassware', 'Burns from the oven', 'Volumetric glassware dried in the oven'], ['Inspect for chips and cracks and discard anything damaged into the sharps bin.', 'Dry in the oven or on the rack. Do not dry volumetric glassware in an oven - heat changes its volume.', 'Store clean glassware inverted or covered so it stays clean.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs206(NUM, TITLE, [('KBK-MIR-LAB-WET-SOP-049 and ENV-SOP-060', 'Glassware drying and washing')])
EMERG = emerg(['hcn', 'cn', 'chem', 'acid', 'burn', 'cut'], 'bench equipment')
