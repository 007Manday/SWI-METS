import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '206-014'
TITLE = 'Met Lab Equipment Receipt, Installation and Commissioning Handover'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc206(['Receive, install and commission the laboratory equipment, and hand it over as fit for use.', 'The laboratory is being bought as one package ex works. Nothing in it works until it is installed, connected, calibrated and proven.'], 'Once, at laboratory establishment; then on every new instrument.', NUM, False, extra_bold=[])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, []), None, ['ILS quotation Q0023979 as the asset list', 'Installation drawings and services schedule', 'Calibration certificates', 'Commissioning checklists', 'Asset register'] + [PPE_EQ]),
    ('Receipt and Services Check', ['Shortage or transit damage not found', 'Manual handling of crates'], ['Check every delivery against quotation Q0023979 line by line. The quote is ex works, so shortages and transit damage are found here or not at all.', 'Confirm the services each item needs are in place before installation - power, water, drainage, compressed air, extraction.', 'Note the items that need work not in the vendor scope: the dust collector pulse-system wiring, its isolator, the GPO and the compressed air connection.'], None, None),
    ('Pressure Vessel and Installation', ['Air receiver put into service uninspected', 'Contact with live electrical equipment', 'Release from a pressurised line'], ['Register the 600 L air receiver as a pressure vessel and arrange its statutory inspection before it is put into service. This is a legal requirement in Queensland, not a commissioning nicety.', 'Install, level and connect each instrument per its manual.'], 'CAUTION: The 600 L air receiver is not put into service until it is registered and inspected.', None),
    ('Calibration, Commissioning and Handover', ['Instrument used before calibration', 'Item not entered in the asset register'], ['Calibrate or verify every instrument and balance before it is used for any result, and file the certificates.', 'Run a commissioning check on each instrument against a known standard and record the result.', 'Enter every item in the asset register with serial number, location, calibration interval and PM requirement.', 'Hand over formally, item by item, and record what is accepted and what is outstanding.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs206(NUM, TITLE, [('ILS quotation Q0023979', 'The asset list, ex works, 12 to 18 week lead time, with 10 per cent of value payable against commissioning'), ('Note', "The quotation's stated validity expired 16 February 2026 - it is a quotation, not a purchase order")])
EMERG = emerg(['elec', 'cut', 'slip'], 'bench equipment')
