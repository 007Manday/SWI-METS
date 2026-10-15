import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '203-003'
TITLE = 'Screen and Cyclone Performance Survey - Size Split Determination'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = [h for h in hazards_from(os.environ['SRC_DOCX']) if not h.startswith('[JSEA to confirm]')]
PPE = list(PPE_STD)
PPE[0] = 'Safety helmet, safety glasses and hearing protection (double at the mill)'
DESC = desc203(['Determine the actual size split across each screen and cyclone against what the design assumes.',
                'A screen or cyclone not doing what the flowsheet says it does moves the problem downstream, usually into the mill or the adsorption circuit.'],
               '203 Plant Surveys', ['021-SC-001 - Trash screen', '032-SC-002/003 - Loaded carbon and carbon safety screens',
                                     '041 / 051 - Adsorption interstage and recovery screens', 'Cyclones - overflow and underflow'],
               'Quarterly, and after any panel change or aperture change.', NUM)
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Hearing damage in the mill and screen areas'],
     prestart203(NEW_JSEA, ['Wear hearing protection in signed areas, with double protection at the mill and compressor.']), None,
     ['Sieve set and Ro-Tap shaker', 'Filter press and filter paper', 'Drying oven', 'Balance', 'Sample containers by stream', 'Field data sheets', PPE_EQ]),
    ('Simultaneous Sampling', ['HCN released at the open sample point', 'Splash of cyanide-bearing slurry', 'Fall from height at the screen or cyclone', 'Streams not sampled at the same time'],
     ['Sample feed, oversize and undersize on the screen, or feed, overflow and underflow on the cyclone, at the same time.',
      'Take increments across the full width or the full discharge, not one grab from the near end.'],
     'CAUTION: Open the sample valve slowly, with the container positioned first and the body out of the spray path. Hearing protection is mandatory in signed areas.', None),
    ('Filtering, Drying and Weighing', ['Splash of cyanide-bearing filtrate', 'Streams mixed up'],
     ['Filter, dry and weigh each stream.'], None, None),
    ('Sizing', ['Sieves not cleaned between streams', 'Mass retained not recorded on every aperture'],
     ['Screen each to the full sieve set and record the mass retained on each aperture.'], None, None),
    ('Partition Curve and Report', ['Cut size not compared with the aperture', 'Torn or wrong panel not reported'],
     ['Calculate the partition curve and the actual cut size.',
      'Compare the cut size against the stated aperture for the screen, and against the design cut for the cyclone.',
      'Report any screen where the cut size and the aperture do not agree - it usually means a torn or wrong panel.'], None, None),
    CLOSE203_STEP,
]
REFS = refs203(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0008', 'Cyclone Efficiency'),
    ('KBK-MIR-MP-PRO-MET-SOP-0029 and SOP-0020', 'Sizing Harian COF and Distribusi Logam dan Ukuran, received 11 Aug 2026'),
    ('MM-4034-033', 'Screen Aperture Register'),
    ('4034-004-VE-025 and 4034-011-VE-022', 'Goldquip screen manuals, received 11 Aug 2026')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'fall', 'slip'], 'a screen, pump or sample cutter')
