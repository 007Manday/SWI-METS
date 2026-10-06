import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '205-010'
TITLE = 'Carbon Adsorption Capacity and Isotherm Test'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc205(['Measure the equilibrium loading capacity of the activated carbon in use.', 'Capacity falls with fouling and with regeneration cycles. Falling capacity is the reason a CIL circuit quietly stops working.'], 'Monthly, and on every new carbon delivery.', NUM, False, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, []), None, ['Bottle roller', 'Bottles', 'Gold solution at known concentrations', 'Carbon samples', 'Screens', 'Balance', 'Filter apparatus', 'Fume cupboard'] + [PPE_EQ]),
    ('Solutions and Charging', ['Cyanide-bearing gold solution splash', 'Unequal carbon mass'], ['Prepare gold solutions across the concentration range the isotherm needs.', 'Charge each bottle with the same mass of carbon and a different solution concentration.'], None, None),
    ('Rolling to Equilibrium', ['Contact with the bottle roller', 'Rolled short of equilibrium'], ['Roll for long enough to reach equilibrium - the period the method sets, not until convenient.', 'Separate, wash and assay the carbon and the residual solution from each bottle.'], None, None),
    ('Isotherm and Reporting', ['No comparison with fresh carbon', 'Trend not kept'], ['Plot carbon loading against equilibrium solution concentration to give the isotherm.', "Compare against fresh carbon and against the previous month's result on the same carbon.", 'Report the capacity and the activity trend against regeneration cycles.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs205(NUM, TITLE, [('KBK-MIR-MP-PRO-OPE-SOP-0007', 'Pengujian Kapasitas Adsorpsi Karbon'), ('KBK-MIR-MP-PRO-MET-SOP-0018', 'Uji Ekuilibrium Karbon (received 11 Aug 2026) - the equilibrium and isotherm half')])
EMERG = emerg(['hcn', 'cn', 'equip', 'cut'], 'the bottle roller')
