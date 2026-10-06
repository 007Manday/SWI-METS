import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '203-001'
TITLE = 'Plant Survey Planning, Permitting and Execution'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc203(['Plan and run a plant survey so the data is usable and nobody gets hurt getting it.',
                'A survey puts people at sample points all over the plant at once, often at height and often in cyanide areas, at a time when the plant is deliberately held steady. It needs planning, not improvisation.'],
               '203 Plant Surveys', ['Whole plant - any circuit under survey'],
               'As required for a performance survey; typically quarterly and after any significant plant change.', NUM)
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Area not fit for the survey'], prestart203(NEW_JSEA), None,
     ['Survey plan and point schedule', 'Sample containers pre-labelled by point and time', 'Radios for every survey team member', 'Field data sheets', 'Personal gas monitors for every person', PPE_EQ]),
    ('Survey Plan and Window', ['Survey run without a plan', 'Plant changed during the survey'],
     ['Write the survey plan before anything else - objective, points, number of increments, timing, who is where, and what analyses are wanted.',
      'Agree the survey window with the Shift Supervisor and the control room. The plant is held at steady state for the survey and nothing is changed during it.'], None, None),
    ('Permits, Briefing and Labelling', ['Work at height without a permit', 'Team not briefed', 'Containers swapped'],
     ['Raise the permits the survey needs - working at height, and any restricted access.',
      'Brief every person on the survey: their points, their route, the timing, the hazards and the stop conditions.',
      'Pre-label every container before the survey starts. Labelling during the survey wastes the window and causes swaps.'], None, None),
    ('Running the Survey', ['HCN released at the sample points', 'Fall from height', 'Increments not taken on time', 'Survey run through an upset'],
     ['Run the survey to the timing in the plan. Take increments at the stated interval, not when convenient.',
      'Record the plant conditions throughout - tonnage, densities, dosing rates, levels - not just at the start.',
      'Abandon the survey if the plant leaves steady state, and record why. A survey run through an upset is worse than no survey.'],
     'CAUTION: Stop conditions in the briefing apply to every team member. Nobody works alone in a cyanide area.', None),
    ('Debrief', ['Data sheets or samples outstanding'],
     ['Debrief, collect all data sheets and samples, and confirm nothing is outstanding before the teams stand down.'], None, None),
    CLOSE203_STEP,
]
REFS = refs203(NUM, TITLE, [('KBK-MIR-MP-PRO-MET-SOP-0027', 'Grinding Survey, received 11 Aug 2026 - a worked plant survey end to end'),
    ('KBK-MIR-MP-PRO-MET-SOP-0047', 'Pengukuran Profil Lumpur Cyclone Over Flow, received 11 Aug 2026'),
    ('4034-PR-PRO-002', 'Sampling Protocol')])
EMERG = emerg(['hcn', 'equip', 'cn', 'skin', 'fall', 'slip'])
