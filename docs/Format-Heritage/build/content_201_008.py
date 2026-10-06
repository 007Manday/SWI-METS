import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '201-008'
TITLE = 'CIL Tail Sampling at Carbon Safety Screen 032-SC-003 Undersize'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc(['Set the CIL tail grade - the number that closes the gold balance across the leach and adsorption circuits.',
             'Check that carbon is not reporting to the undersize. 032-SC-003 is the sole carbon barrier between the CIL circuit and the resin circuit.'],
            '032 Carbon in Leach',
            ['032-SC-003 - Carbon safety screen, undersize',
             '032-XV-003 / 032-XV-004 - Feed valves, position confirmed manually before sampling',
             '032-XM-012 - CIL tails automatic sampler, the manual sample cross-checks it'],
            'Hourly spot sample, composited per shift. Carbon check on every sample.', '201-008',
            extra_bold=['Safety-critical finding - read before starting. 032-SC-003 is the SOLE carbon barrier between the CIL circuit and the resin circuit. The Control Philosophy mark-up dated 07-08-2026 deletes every automatic action that closed feed valves 032-XV-003 and 032-XV-004 - item PCP-054 removes the high-level close, PCP-079 removes ILHH-041001 closing them, and PCP-122 removes the same action again from Section 3.1.7. RA-02 Rev A had already found that 032-XV-004 had no interlock. After the mark-up NEITHER valve has one. The barrier is this screen and the operator watching it. Carbon seen in the undersize is reported immediately.'])
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Feed valve position not confirmed - no automatic protection'],
     prestart(NEW_JSEA, ['Confirm valve positions on 032-XV-003 and 032-XV-004 by eye before approaching. There is no automatic protection - see the safety-critical finding in Part 2.'], rinse=False), None,
     ['Sampling bucket 5 to 8 L', '1 mm sieve', 'Marcy scale', 'Filter press and filter paper', 'Bottles 250 mL', 'Spatula', PPE_EQ]),
    ('Sample Collection', ['HCN released at the open sample point', 'Splash of cyanide-bearing slurry', 'Fall from height at the screen', 'Equipment starting without warning'],
     ['Flush the point and discard the first flow.', 'Collect 4 litres of undersize slurry.'], CAUTION_VALVE, None),
    ('Carbon Check', ['Carbon in the undersize not seen', 'Carbon in the undersize not reported'],
     ['Pass a measured volume over the 1 mm sieve and inspect the retained solids for carbon.',
      'ANY carbon in the undersize is reported to the Shift Supervisor immediately, before the round continues.'],
     'CAUTION: 032-SC-003 is the sole carbon barrier between the CIL circuit and the resin circuit. Carbon in the undersize is reported immediately.', None),
    ('Per Cent Solids and Assay', ['Scale not zeroed - wrong per cent solids', 'Result not compared with the automatic sampler'],
     ['Determine per cent solids on the Marcy scale.',
      'Filter and bottle for tail assay and for WAD cyanide.',
      'Record the result against the reading from automatic sampler 032-XM-012 taken at the same time.'], None, None),
    CLOSE_STEP,
]
REFS = refs('201-008', TITLE, [('HM-PRC-V01-PRO005', 'Carbon in Leach (CIL) Circuit'),
    ('4034-PR-PRO-002', 'Sampling Protocol item 5 - the sample point is still marked (TBC) in the protocol'),
    ('4034-004-VE-025 Rev B', 'Goldquip vibrating screen IOM (032-SC-003), received 11 Aug 2026'),
    ('RA-02', 'Carbon Contamination Register Rev A')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'fall', 'slip', 'carbon'], 'an agitator, pump or screen')
