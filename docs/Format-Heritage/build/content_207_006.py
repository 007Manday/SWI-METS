import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '207-006'
TITLE = 'Automatic versus Manual Sample Bias Check and Reconciliation'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc207(['Compare what the automatic samplers report against a manual sample taken at the same point and time.', 'This is the only check that an automatic sampler is telling the truth, and it is the one that most often gets skipped.'], ['022-XM-011 / -017 - IsaMill feed', '032-XM-012 - CIL tails', '041-XM-013 - Metal adsorption tails', '051-XM-014 - Final tails'], 'Monthly on every sampler, and after any sampler repair or cutter change.', NUM, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Samples not analysed in the same batch'], prestart203(NEW_JSEA, ['Arrange the check with the control room and the laboratory so both samples are analysed in the same batch.']), None, ['Manual sampling equipment per the Area 201 instructions', 'Pre-labelled containers', 'Stopwatch', 'Field data sheets'] + [PPE_EQ]),
    ('Paired Sampling', ['HCN released at the open sample point', 'Splash of cyanide-bearing slurry', 'Grab compared against a composite', 'Fall from a tank top or platform'], ['Take the manual sample at the same point and over the same period the automatic sampler composites over. A grab against a composite is not a comparison.', 'Take at least ten paired samples across the period - a single pair proves nothing.', 'Submit the pairs to the laboratory as blind duplicates where possible.'], 'CAUTION: Sample from the manual point following the Area 201 instruction for that point. Keep clear of the sampler cutter - it can start without warning.', None),
    ('Bias Test', ['Scatter mistaken for bias', 'Laboratory blamed before the sampler is checked'], ['Plot the automatic result against the manual result and test for bias, not just for scatter. A consistent offset in one direction is bias; scatter about the line is precision.', 'Where bias is found, inspect the cutter and the sampler installation before concluding the laboratory is at fault.'], None, None),
    ('Report and Correction', ['Accounting not corrected', 'Check not repeated after the correction'], ['Report the bias with the monthly close and correct the accounting where a bias is confirmed.', 'Repeat the check after any correction.'], None, None),
    CLOSE203_STEP,
]
REFS = refs207(NUM, TITLE, [('4034-PR-PRO-002', 'Sampling Protocol - the manual points to compare against'), ('SWI-PRO-MET-201-001 to -018', 'Manual sampling instructions, issued')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'fall'], 'the sampler, a pump or a sample cutter')
