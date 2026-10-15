import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '206-010'
TITLE = 'Drying Oven and Muffle Furnace Operation'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc206(['Operate the drying ovens, ashing furnace and muffle furnace safely and at the right temperature.', 'Hot surfaces, hot glassware and a wrong set temperature that quietly ruins a batch of results.'], 'Every drying and ashing operation.', NUM, True, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, [LAB_ALONE] + []), None, ['2 x drying oven 560 L and 70 trays', 'Ashing furnace 3.5 kW', 'Muffle furnace SF-3-SD 3 L', 'Long tongs', 'Heat-resistant gloves', 'Heat mats', 'Desiccator', 'Oven log'] + [PPE_EQ]),
    ('Set Temperature and Loading', ['Wrong set temperature', 'Volatile or flammable material in the oven', 'Overloaded oven'], ['Confirm the set temperature against the method before loading. A drying oven set to an ashing temperature destroys the sample and can start a fire.', 'Do not put volatile or flammable material in a drying oven.', 'Load trays so air can circulate. An overloaded oven does not reach constant mass in the stated time.'], None, None),
    ('Handling Hot Items', ['Burns from hot trays and glassware', 'Hot item set on the bench', 'Sample weighed warm'], ['Use long tongs and heat-resistant gloves for everything going in or out. Set hot items on a heat mat, never on the bench.', 'Cool samples in the desiccator before weighing, not on the open bench.'], 'CAUTION: Long tongs and heat-resistant gloves for everything going in or out.', None),
    ('Ashing and Muffle Furnaces and Records', ['Fume from the furnace', 'Face in front of a hot furnace door', 'Temperature not logged'], ['For the ashing and muffle furnaces, confirm the extraction is running before the door is opened.', 'Never open a muffle furnace at temperature with your face in front of the door.', 'Record the oven or furnace identity, set temperature and period against every batch, and log the daily temperature check.'], 'CAUTION: Stand to the side when opening a hot furnace door.', None),
    CLOSE_LAB_STEP,
]
REFS = refs206(NUM, TITLE, [('KBK-MIR-LAB-PRE-SOP-003 and WET-SOP-024', 'Pengeringan Sampel and ashing furnace'), ('ILS quotation Q0023979', '2 x drying oven 560 L with 70 trays, ashing furnace 3.5 kW, muffle furnace SF-3-SD')])
EMERG = emerg(['cn', 'chem', 'burn', 'cut', 'slip'], 'bench equipment')
