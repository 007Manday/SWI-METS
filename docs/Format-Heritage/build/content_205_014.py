import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '205-014'
TITLE = 'Resin Fouling, Osmotic Shock and Bead Integrity Assessment'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID_HEAR
DESC = desc205(['Assess resin condition - fouling, osmotic damage and bead breakage.', 'Resin is the most expensive consumable on the circuit and the damage is cumulative and irreversible.'], 'Monthly, and after any osmotic shock event.', NUM, False, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, []), None, ['200 mm sieve set 38 um to 2 mm', 'Ro-Tap RX29', 'Balance', 'Wash bottle', 'Beakers', 'Acid and caustic for the fouling check', 'Fume cupboard'] + [PPE_EQ]),
    ('Sampling and Washing', ['HCN at the transfer stream', 'Sample from a settled hopper'], ['Take the resin sample from the transfer stream, not from a settled hopper.', 'Wash free of slurry over the retention aperture.'], None, None),
    ('Bead Size and Integrity', ['Noise from the Ro-Tap', 'Fines lost in washing'], ['Run the bead size distribution per the resin PSD method and record the fraction below the retention aperture.', 'Count a subsample for whole, cracked and broken beads and report whole bead count as a percentage.'], 'CAUTION: Hearing protection on while the Ro-Tap is running.', None),
    ('Fouling Check and Reporting', ['Acid on cyanide-bearing resin', 'Acid or caustic splash'], ['Inspect for fouling - discolouration, coating and change in bulk density against fresh resin.', 'Where fouling is suspected, run the acid and caustic wash sequence at the bench and re-measure capacity against an unwashed split.', 'Trend all measures against the conditioning and transfer history.', 'Report against the acceptance criteria once Goldquip supplies them - until then, report the trend only.'], 'CAUTION: Wash the resin free of cyanide before any acid wash. Acid on cyanide releases HCN.', None),
    CLOSE_LAB_STEP,
]
REFS = refs205(NUM, TITLE, [('KBK-MIR-MP-PRO-MET-SOP-0058', 'Distribusi Ukuran Partikel Resin (received 11 Aug 2026)'), ('ILS quotation Q0023979', '38 um to 2 mm sieve set and Ro-Tap RX29'), ('RA-01 Rev A', 'Resin Loss Register')])
EMERG = emerg(['hcn', 'cn', 'acid', 'equip'], 'the Ro-Tap')
