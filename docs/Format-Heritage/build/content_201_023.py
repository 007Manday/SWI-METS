import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '201-023'
TITLE = 'Sample Point Access, Isolation, Flushing and Housekeeping'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc(['Set the standard for how any sample point is approached, opened, flushed, closed and left.',
             'This is the instruction that sits behind every other sampling task. Most sampling incidents are not about the analysis - they are about how the point was opened.'],
            '201 Plant Sampling', ['All sample points - every point covered by the Area 201 instructions'],
            'Every time a sample point is used.', NUM)
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Equipment missing at the point'],
     prestart(NEW_JSEA, rinse=False), None,
     ['Process water hose or flushing connection at the point', 'Drain or catch container', 'Cleaning brush and rag', 'Spill kit', PPE_EQ]),
    ('Approach and Inspect', ['HCN at the sample point', 'Weeping fitting, cracked hose or missing handle', 'Discharge path not clear'],
     ['Approach the point from upwind with the personal gas monitor on and reading clean.',
      'Look at the point before touching it. A weeping fitting, a cracked hose or a missing handle is reported, not worked around.',
      'Confirm the discharge path is clear and that you can see where the sample will go.'], None, None),
    ('Open, Flush and Collect', ['Release from a pressurised sample line', 'Splash of cyanide-bearing slurry', 'Flush discharged to the walkway'],
     ['Position the container FIRST, then open the valve slowly. Never open a valve and then reach for the container.',
      'Flush the line for the stated period and discharge the flush to drain, not to the walkway.',
      'Collect the sample with the body out of the spray path.'],
     'CAUTION: Open slowly and stand clear of the discharge path. Never open a valve whose discharge cannot be seen.', None),
    ('Close the Point and Blocked Points', ['Valve left weeping', 'Blocked point rodded under pressure'],
     ['Close the valve fully and confirm the point is not weeping.',
      'Where a point is blocked, do NOT rod it under pressure. Isolate, drain, and report it.'],
     'CAUTION: A blocked point can hold pressure. Never rod it under pressure.', None),
    ('Wash Down, Leave Clean and Completion', ['Spillage left on the walkway', 'Equipment left at the point', 'Control room not told the round is complete'],
     ['Wash down the point and the walkway. Recover any spilled slurry to the drain, not to the ground.',
      'Leave nothing at the point - no buckets, no hoses across the walkway, no containers on the grating.'] + CLOSE[2:], None, None),
]
REFS = refs(NUM, TITLE, [('KBK-MIR-MP-PRO-MET-SOP-0047', 'Pengukuran Profil Lumpur Cyclone Over Flow, received 11 Aug 2026'),
    ('KBK-MIR-MP-PRO-MET-SOP-0048 and SOP-0049', 'Leach tank sampling and profile; resin tank sampling and profile, received 11 Aug 2026 - each carries the sample point access and flushing steps for its own point'),
    ('Mt. Morgan site sampling procedures 1 to 23 [LIVE]', 'Common flushing and cleaning practice')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'fall', 'slip'], 'an agitator, pump, screen or sample cutter')
