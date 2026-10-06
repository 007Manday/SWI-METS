import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '203-010'
TITLE = 'Interstage and Safety Screen Efficiency Check and Loss Quantification'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = [h for h in hazards_from(os.environ['SRC_DOCX']) if not h.startswith('[JSEA to confirm]')]
PPE = PPE_STD
DESC = desc203(['Quantify how much carbon and resin is getting past the interstage and safety screens.',
                'Screen losses are the largest recurring consumable loss on this type of circuit, and the carbon safety screen is the only barrier between the CIL circuit and the resin circuit.'],
               '203 Plant Surveys', ['032-SC-003 - Carbon safety screen, undersize', '032-SC-008 to -012 - CIL interstage screens', '041 / 051 - Adsorption interstage and recovery screens'],
               'Monthly, and after any panel replacement.', NUM)
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Equipment damaged or not in good condition'], prestart203(NEW_JSEA), None,
     ['Sample containers', '1 mm sieve for carbon', '0.9 mm sieve for resin', 'Measuring glass', 'Drying tray', 'Balance', 'Field data sheets', PPE_EQ]),
    ('Undersize Sampling', ['HCN released at the open sample point', 'Splash of cyanide-bearing slurry', 'Fall from the screen platform', 'Equipment starting without warning'],
     ['Sample the undersize of each screen over a measured volume and a measured period.'], CAUTION_VALVE, None),
    ('Recovery and Weighing', ['Carbon or resin lost during recovery', 'Cross-contamination between screens'],
     ['Screen the sample and recover any carbon or resin present.',
      'Dry and weigh the recovered carbon or resin.'], None, None),
    ('Loss Calculation and Panel Inspection', ['Loss not expressed per hour and per tonne', 'Torn or worn panel not noticed'],
     ['Express the loss as mass per hour and as mass per tonne of ore treated.',
      'Inspect the screen panels for tears, wear and tensioning at the same time - a loss almost always traces back to a panel.'], None, None),
    ('Comparison and Report', ['Carbon at 032-SC-003 not reported', 'Loss not fed into the inventory accounting'],
     ['Compare against the previous month and against the loss registers.',
      'Report any carbon found at 032-SC-003 immediately - that is a resin circuit contamination event, not a routine loss.',
      'Feed the quantified loss into the carbon and resin inventory accounting.'],
     'CAUTION: Carbon found at 032-SC-003 is reported to the Shift Supervisor immediately.', None),
    CLOSE203_STEP,
]
REFS = refs203(NUM, TITLE, [('MM-4034-033', 'Screen Aperture Register'),
    ('RA-01 and RA-02', 'Resin Loss and Carbon Contamination Registers Rev A'),
    ('KBK-MIR-MP-PRO-MET-SOP-0028', 'Sizing Harian CIL Tail, received 11 Aug 2026'),
    ('4034-004-VE-025 and 4034-011-VE-022', 'Goldquip screen manuals, received 11 Aug 2026'),
    ('SWI-PRO-OPR-032-003, -004 and -005', 'Screen instructions, issued')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'carbon', 'fall', 'slip'], 'a screen, pump or sample cutter')
