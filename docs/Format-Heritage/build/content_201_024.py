import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '201-024'
TITLE = 'Sampling During Start-Up, Shutdown and Upset Conditions'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = list(PPE_STD)
PPE[4] = 'Chemical resistant suit, nitrile rubber gloves and apron, heat-resistant gloves'
DESC = desc(['Set what is sampled, and what is NOT sampled, when the plant is not at steady state.',
             'Every routine sampling instruction assumes 15 to 20 minutes of steady operation. This instruction covers the times when that assumption does not hold.'],
            '201 Plant Sampling', ['All sample points - under start-up, shutdown and upset conditions'],
            'Whenever the plant is outside steady-state operation.', NUM)
STEPS = [
    ('Pre-start Check', ['Plant state not known', 'Gas monitor or fixed detection not healthy', 'Working alone in a cyanide area'],
     prestart(NEW_JSEA, ['Establish from the control room what state the plant is in before going out. Do not assume.',
                         'Confirm the personal gas monitor is carried - it is mandatory in all cyanide areas during any transient.'], rinse=False, steady=False), None,
     ['As the underlying routine instruction requires', 'Personal gas monitor - mandatory in all cyanide areas during any transient', PPE_EQ]),
    ('Start-Up Sampling', ['Part-full line surging when flow arrives', 'Meaningless sample from a part-full line'],
     ['During start-up, do not sample a line until flow has been established and held for the period the circuit procedure states. A sample from a part-full line is meaningless and the line may surge when flow arrives.'], None, None),
    ('Shutdown Sampling', ['Line discharging without warning while drained and flushed', 'Contact with hot solution'],
     ['During shutdown, sample only where the circuit procedure calls for it. Lines being drained and flushed can discharge without warning.'],
     'CAUTION: Heat-resistant gloves and face shield on hot circuits. Do not sample a column under pressure.', None),
    ('Off-Condition Samples', ['Off-condition sample not marked', 'Shift result corrupted'],
     ['Mark every sample taken outside steady state as OFF-CONDITION on the label and in the register, with the plant state written on it. An unmarked off-condition sample corrupts the shift result.'], None, None),
    ('When Not to Sample', ['Sampling during a gas alarm or spill response', 'Missed sample invented or back-filled'],
     ['Do NOT sample at all during: a gas alarm, a reagent spill response, a power interruption, a confined space entry in the area, or any time the Shift Supervisor has restricted access.',
      'During an upset, the priority is the plant and the people, not the sample. A missed sample is recorded as missed. It is never invented or back-filled.'],
     'CAUTION: The priority is the plant and the people, not the sample.', None),
    ('Restart and Reporting', ['Routine schedule restarted at the wrong time', 'Gap in the shift balance not known'],
     ['Once steady state is re-established, note the time and restart the routine schedule from the next full interval.',
      'Report to the metallurgist which samples were missed and why, so the shift balance is not closed on a gap nobody knows about.'], None, None),
    CLOSE_STEP,
]
REFS = refs(NUM, TITLE, [('HM-PRC-V01-PRO030 and PRO031', 'Whole-of-Plant Start-up and Whole-of-Plant Shutdown'),
    ('Sequence flowcharts', 'The 24 sequence flowcharts held, of which only 2 are stop sequences'),
    ('Note', 'Written from first principles against the circuit procedures - no direct source held')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'burn', 'slip'], 'an agitator, pump, screen or sample cutter')
