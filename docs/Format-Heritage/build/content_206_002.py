import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '206-002'
TITLE = 'Fume Cupboard Operation, Scrubber Check and Cleaning'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_LAB_ACID
DESC = desc206(['Operate the fume cupboards and prove the scrubber is working before any fume-generating work.',
                'The fume cupboard and its scrubber are the only thing between the technician and the fume from acid digestion, cyanide work and perchloric acid.',
                'The fume cupboard face velocity is measured with the GM8902 anemometer, following the Martabe method, and accepted against the required face velocity.'],
               'Every use; scrubber checked at the start of every shift; face velocity measured monthly and after any repair to the extraction fan, ductwork or scrubber.', NUM, True,
               extra_bold=['Draft for review: Steps 4 and 5 follow the Martabe work instruction Operating Anemometer GM8902 (DOC-3-MET-PMC-WIN-00130-IE, v1.0, 25/12/2024). The face velocity is measured at the marked working sash height, and the average and the lowest of 20 readings are recorded. JSEA-PRO-MET-206-002 must be updated for the added hazards before this instruction is approved.',
                           'Open items: (1) take the required face velocity from the Safetyflow fume cupboard specification (ILS Q0023979), or from AS/NZS 2243.8 where the specification does not give it - about 0.5 m/s average is typical and must be confirmed before use; (2) set the lowest single reading allowed; (3) confirm the monthly measurement frequency; (4) confirm the GM8902 anemometer and its calibration certificate are on site.'])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, [LAB_ALONE, 'Take 5 and prepare the anemometer, its data logger and a stopwatch where the face velocity is to be measured. Check the equipment is in good condition.']), None,
     ['2 x 2400 mm Safetyflow fume cupboards', 'Model A crossflow scrubber with pH dosing', 'Airflow indicator', 'pH meter for scrubber liquor', 'Washdown hose', 'Benetech GM8902 anemometer with its data logger, in calibration', 'Stopwatch', 'Log sheet', PPE_EQ]),
    ('Fume Cupboard and Scrubber Start-up', ['Extraction fan not running', 'Scrubber liquor out of its pH range', 'Fume released to the laboratory'],
     ['Confirm the extraction fan is running and the airflow indicator reads within its marked range before starting any work.',
      'Confirm the scrubber is running and its pH dosing is operating, and record the scrubber liquor pH.',
      'Where scrubber liquor pH is out of range, stop - a scrubber outside its pH range is not scrubbing.'],
     'CAUTION: No acid or cyanide work at the bench until the airflow and the scrubber are proven.', None),
    ('Working in the Fume Cupboard', ['Sash raised above the working height', 'Rear baffle blocked', 'Perchlorate build-up in the ductwork'],
     ['Work with the sash at the marked working height. Raising the sash breaks the containment.',
      'Keep apparatus at least 150 mm inside the sash line and never block the rear baffle.',
      'For perchloric acid work, use only the cupboard rated for it, and carry out the washdown routine immediately after every use.',
      'Wash down the working surface at the end of every session.'],
     'CAUTION: Perchlorate build-up in ductwork is explosive. Washdown after every perchloric use.', None),
    ('Face Velocity Measurement - GM8902 Anemometer', ['Pinch point at the sash door', 'Breathing hazardous fume during the measurement', 'Anemometer out of calibration'],
     ['Make sure NOTHING is being done in the fume cupboard and the anemometer is calibrated.',
      'Set the sash at the marked working height. Run the fume cupboard.',
      'Plug the anemometer fan cable into the anemometer data logger.',
      'Hold the anemometer vertically in the centre of the sash opening. Switch the anemometer on with the red button.',
      'Record the reading every second, using the stopwatch, until you have 20 readings.'],
     'CAUTION: Open and close the sash slowly and keep hands clear of the pinch point. Do not measure while any work is in the cupboard.', None),
    ('Acceptance and Records', ['Fume cupboard used below its required face velocity', 'Result not recorded'],
     ['Calculate the average of the 20 readings. Record the average and the lowest reading.',
      'Compare the average with the required face velocity from the fume cupboard specification (see Open items).',
      'Where the average is below the required face velocity, tag the fume cupboard out of service, do not use it, and report to the Met Lab supervisor.',
      'Record the airflow reading, the scrubber pH, the face velocity and the washdown in the log.'],
     'CAUTION: A fume cupboard below its required face velocity is not containing fume. Tag it out.', None),
    CLOSE_LAB_STEP,
]
REFS = refs206(NUM, TITLE, [('KBK-MIR-LAB-WET-SOP-054, -059 and ENV-SOP-061', 'Fume cupboard and scrubber'),
                            ('ILS quotation Q0023979', '2 x 2400 mm Safetyflow fume cupboard rated for perchloric and HF, Model A crossflow scrubber, exhaust fans'),
                            ('DOC-3-MET-PMC-WIN-00130-IE v1.0', 'Martabe WI Operating Anemometer GM8902 (25/12/2024) - source of Step 4'),
                            ('AS/NZS 2243.8', 'Safety in laboratories - Fume cupboards (face velocity, see Open items)')])
EMERG = emerg(['hcn', 'cn', 'chem', 'acid', 'cut'], 'bench equipment')
