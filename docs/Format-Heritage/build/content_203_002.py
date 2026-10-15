import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '203-002'
TITLE = 'Slurry Flow, Density and Tonnage Verification Survey'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = [h for h in hazards_from(os.environ['SRC_DOCX']) if not h.startswith('[JSEA to confirm]')]
PPE = PPE_STD
DESC = desc203(['Prove that the flow, density and tonnage instruments are telling the truth.',
                'Every mass balance on the plant is built on these instruments. If a weightometer or a density transmitter is out, every number downstream is out with it.'],
               '203 Plant Surveys', ['021-PP-123/124 - Scrubber discharge, flow and density', 'AIT-021002 - Density transmitter', '022 - IsaMill feed and discharge',
                                     '031 / 032 - Leach and CIL feed', '051 - Tails'],
               'Quarterly, and after any instrument replacement or recalibration.', NUM)
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Plant not at steady state'],
     prestart203(NEW_JSEA, ['Confirm the circuit is at steady state and will be held there for the survey window.']), None,
     ['Marcy scale', '1 litre density container', 'Stopwatch', 'Bucket and measuring cylinder for cut samples', 'Field data sheets', PPE_EQ]),
    ('Timed Cut Sampling', ['HCN released at the sample point', 'Splash of cyanide-bearing slurry', 'Fall from height at the sample point', 'Equipment starting without warning'],
     ['Take a timed cut sample at the point where the arrangement allows a full stream cut, and measure the volume and time.',
      'Measure the slurry density on the Marcy scale on the same sample.'], CAUTION_VALVE, None),
    ('Flow and Tonnage Calculation', ['Single cut taken as a verification', 'Instrument reading not logged at the same moment'],
     ['Calculate volumetric flow and dry solids tonnage from the cut, and compare against the instrument reading logged at the same moment.',
      'Repeat at least three times at each point. A single cut is not a verification.',
      'Record the difference between measured and indicated for each instrument.'], None, None),
    ('Out of Tolerance and Accounting', ['Instrument adjusted by the sampler', 'Unverified tonnage used in the accounting'],
     ['Report any instrument outside its tolerance to instrumentation. Do not adjust it yourself.',
      'Feed the verified tonnage into the metallurgical accounting for the period.'], None, None),
    CLOSE203_STEP,
]
REFS = refs203(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0004', 'SG Determination by Marcy Scale'),
    ('KBK-MIR-MP-PRO-MET-SOP-0045', 'Pengukuran Densitas Lumpur, received 11 Aug 2026'),
    ('4034-002-VE-025 and 4034-001-VE-038', 'McLanahan rotary scrubber IO&M and IsaMill control philosophy, received 11 Aug 2026')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'fall', 'slip'], 'an agitator, pump or sample cutter')
