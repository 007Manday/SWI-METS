import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '204-017'
TITLE = 'Sieve Cleaning, Integrity Check and Aperture Verification'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_HEAR
DESC = desc204(['Keep the sieve set clean, intact and verified, so a sizing result means what it says.', 'A blinded or torn sieve produces a wrong size distribution that looks perfectly normal on the sheet.'], 'After every use for cleaning; quarterly for integrity and aperture verification.', NUM, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA), None, ['Ultrasonic sieve cleaner FSS Sieve 200 DH', 'Soft brushes', 'Compressed air at low pressure', 'Magnifier or microscope', 'Sieve register', 'Certified reference sieves or a check sample'] + [PPE_EQ]),
    ('Cleaning', ['Mesh damaged by forcing material through', 'Wire brush used on a sieve', 'Dust or residue from the sieve'], ['Clean each sieve immediately after use - brush from the underside, never force material through from above.', 'Use the ultrasonic cleaner for blinded fine sieves. Do not use a wire brush on any sieve.'], None, None),
    ('Integrity Inspection', ['Damaged sieve left in the rack', 'Cuts from a damaged frame'], ['Inspect the mesh under magnification for tears, stretched apertures, and separation from the frame.', 'Withdraw and mark any damaged sieve immediately. A damaged sieve left in the rack will be used.'], None, None),
    ('Aperture Verification and Register', ['Verification not recorded', 'Sieve used past its replacement interval'], ['Verify apertures quarterly against certified reference sieves or by running a check sample of known distribution.', 'Record every clean, inspection and verification in the sieve register against the sieve identity.', 'Replace sieves on the interval the register sets, or on failure, whichever comes first.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs204(NUM, TITLE, [('ILS quotation Q0023979', 'Ultrasonic sieve cleaner FSS Sieve 200 DH'), ('Note', 'No cleaning or aperture verification procedure was held before this revision')])
EMERG = emerg(['cn', 'skin', 'cut'], 'bench equipment')
