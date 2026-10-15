import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '205-008'
TITLE = 'Extended and Diagnostic Leach Test'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc205(['Run an extended leach, and a diagnostic sequence, to find out where the unrecovered gold actually is.', 'A tail assay says how much gold was lost. A diagnostic leach says why, which is the only version that can be acted on.'], 'On tail investigation and on each new ore type.', NUM, True, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, [LAB_ALONE] + []), None, ['Bottle roller', 'Bottles', 'Leachwell reagent set', 'Acids for the diagnostic sequence', 'Fume cupboard', 'Filter apparatus', 'Balance', 'pH meter'] + [PPE_EQ]),
    ('Extended Leach', ['HCN released below pH 10.5', 'Contact with the bottle roller'], ['Run the extended leach first - the same charge as a bottle roll but for a longer period with cyanide and pH maintained throughout.', 'Sample at intervals through the extension and plot extraction against time. If extraction is still climbing at the plant residence time, the problem is kinetics, not locking.'], None, None),
    ('Diagnostic Sequence', ['Acid added to cyanide-bearing residue', 'Acid fume', 'Carry-over between stages'], ['For the diagnostic sequence, leach the residue in stages with progressively stronger reagents, assaying the residue after each stage.', 'Carry out every acid stage in the fume cupboard with the scrubber running.', 'Neutralise and wash the residue between stages so carry-over does not corrupt the next stage.'], 'CAUTION: Acid on a cyanide-bearing residue releases HCN. Wash the residue free of cyanide and work in the fume cupboard.', None),
    ('Assay and Deportment', ['Stage not assayed', 'Total reported without deportment'], ['Assay the solution and residue from every stage.', 'Attribute the gold to each mineral association from the stage in which it dissolved.', 'Report the deportment, not just the total - which fraction is free, which is locked in sulphide, and which is in silicate.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs205(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0011', 'Extended Leaching Untuk Leach dan CIL Tail'), ('KBK-MIR-MP-PRO-MET-SOP-0038', 'Uji Tail Diagnostik Menggunakan Leachwell (received 11 Aug 2026)')])
EMERG = emerg(['hcn', 'cn', 'acid', 'equip', 'cut'], 'the bottle roller')
