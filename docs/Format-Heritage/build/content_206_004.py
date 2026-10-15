import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '206-004'
TITLE = 'pH, DO and Conductivity Meter Calibration'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = [h.replace('Latex gloves', 'Chemical-resistant gloves') for h in hazards_from(os.environ['SRC_DOCX'])]
PPE = PPE_LAB_ACID
DESC = desc206(['Calibrate the laboratory and field pH, dissolved oxygen and conductivity meters.',
                'pH governs cyanide safety as well as process control. An uncalibrated pH meter is a safety issue, not just a data issue.'],
               'Every shift before use, and after any electrode change.', NUM, False,
               points=('Met lab bench - physical testwork bench and instrument', 'Plant tanks - dissolved oxygen measured in slurry'),
               extra_bold=['Draft for review: Steps 3 and 4 follow the Martabe work instructions pH Meter TPS Cube Calibration (DOC-3-MET-PMC-WIN-00087-IE) and Operating pH Cube Meter (DOC-3-MET-PMC-WIN-00089-IE), and Steps 5 and 6 follow Operate DO Meter Portable (DOC-3-MET-PRS-WIN-00055-IE), v1.0, 25/12/2024. The TPS pH cube meter is adopted as at Martabe. pH calibration stays at three points (pH 4, 7 and 10) with the slope and offset recorded; the Martabe two-point calibration is not used. The Martabe DO method is applied to the Hanna HI9142 meter without the Oxyguard menu steps. JSEA-PRO-MET-206-004 must be updated for the added hazards before this instruction is approved.',
                           'Open items: (1) confirm the TPS pH cube meter is on site, or procure it, and add it to the asset list; (2) take the DO calibration acceptance limit in air from the HI9142 manual - the Martabe value of 6 to 8 has no unit and is not used; (3) confirm from the TPS cube manual which control sets pH 4 - the source says "the same as pH 7"; (4) set the acceptable pH electrode slope range; (5) confirm the Mt. Morgan records for DO results and pH calibration - the Martabe Daily Task Checklist (DOC-FRM-00052-EN) and form DOC-4-MET-PMC-DFR-00142-EN are source names; (6) conductivity standards are not held - conductivity meters cannot be calibrated until they are.'])
STEPS = [
    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, ['Take 5 and prepare the meters, the buffer solutions, a beaker and a small bucket. Check the equipment is in good condition and the buffers are in date.']), None,
     ['pH buffers 4, 7 and 10, in date', 'TPS pH cube meter with pH and temperature sensors', 'pH/ORP meters (ILS quotation)', 'Hanna HI9142 DO meters with their manual and a spare membrane', 'Conductivity standards - NOT HELD', 'Flat screwdriver for the calibrate and slope controls', 'Beaker and small bucket', 'Distilled water, soft tissue and electrode storage solution', 'Meter log and DO checklist', PPE_EQ]),
    ('pH Meter Calibration - Three Point', ['Out-of-date buffer', 'Buffer splash to the eyes', 'Electrode slope out of range'],
     ['Check the buffer expiry date. An out-of-date buffer calibrates the meter to the wrong value.',
      'Rinse the electrode with distilled water and blot dry between buffers.',
      'Calibrate the pH meter across pH 4, 7 and 10 and record the slope and offset. Two-point calibration is not used.',
      'Reject the electrode if the slope is outside the acceptable range.',
      'Record the temperature at calibration - pH is temperature dependent.'], None, None),
    ('TPS Cube pH Calibration', ['Buffer splash and spill', 'Scratch from the screwdriver', 'Calibration not recorded'],
     ['pH 7: wash the pH probe with water. Pour pH 7 buffer into the beaker and put the pH and temperature sensors in it. Wait until the reading is steady at 7. Adjust to 7 with the \'calibrate\' knob. Clean the sensors in water.',
      'pH 10: pour pH 10 buffer into the beaker and put the sensors in. Wait until the reading is steady. Adjust to 10 with the slope control, using the screwdriver. Clean the sensors in water.',
      'pH 4: pour pH 4 buffer into the beaker and put the sensors in. Wait until the reading is steady and adjust to 4 as the meter manual directs (see Open items). Clean the sensors in water.',
      'Record the readings, the slope and offset, and the condition of the meter before and after calibration in the pH calibration logsheet.'],
     'CAUTION: Pour buffers slowly and clean any spill at once. Check the screwdriver is in good condition and watch hand position on the slope control.', None),
    ('Measuring pH with the TPS Cube', ['Sample contact and splash to the eyes', 'Probe allowed to dry out', 'Cyanide-bearing sample to the wrong waste stream'],
     ['Calibrate the meter first (Step 3).',
      'Set the pH cube to pH mode. Plug the pH sensor and the temperature sensor into their sockets. Remove the cap from the pH probe.',
      'Rinse the probe with clean water and dry it.',
      'Dip both sensors in the solution to be measured. Wait until the reading is stable, then record it.',
      'Rinse the probe with clean water and keep it in water so it stays wet.',
      'Pour the sample to the site waste stream for its classification. Cyanide-bearing samples go to the cyanide waste stream, never the general drain.'], None, None),
    ('DO Meter Calibration in Air - HI9142', ['Damaged or dry membrane', 'Reading outside the manual limit', 'Meter used out of calibration'],
     ['Switch on the DO meter and calibrate it to 100 per cent air saturation, in air or against air-saturated water, following the HI9142 manual. If the membrane needs wiping or changing, do it first.',
      'Check the reading in air against the acceptance limit in the HI9142 manual. Outside the limit, calibrate again; if it is still outside, change the membrane and electrolyte or take the meter out of service.',
      'Record the temperature at calibration - DO is temperature dependent.'], None, None),
    ('DO Measurement in Slurry', ['HCN at an open cyanide tank', 'Slurry splash when lifting the probe', 'Trip on the meter cable'],
     ['At a cyanide-bearing tank apply the cyanide controls of SWI-PRO-MET-201-003: personal HCN monitor on, approach from upwind, second person in sight.',
      'Tidy the DO meter cable and do not hurry when walking.',
      'Put the DO probe in the tank and wait until the reading is stable. Record the reading, then lift the probe out of the slurry slowly.',
      'Rinse the probe with clean water.',
      'Enter the DO result in the DO checklist (see Open items).'],
     'CAUTION: Cyanide-bearing slurry. Personal HCN monitor on, upwind approach and a second person in sight.', None),
    ('Electrode Storage and Meter Log', ['Electrode stored in distilled water', 'Calibration not traceable to the meter'],
     ['Store electrodes in the correct storage solution, never in distilled water.',
      'Record every calibration in the meter log against the meter and electrode identity.'], None, None),
    CLOSE_LAB_STEP,
]
REFS = refs206(NUM, TITLE, [('KBK-MIR-MP-PRO-MET-SOP-0030', 'Kalibrasi DO-meter (received 11 Aug 2026)'),
                            ('KBK-MIR-MP-PRO-MET-SOP-0031', 'Kalibrasi pH-meter (received 11 Aug 2026)'),
                            ('ILS quotation Q0023979', '2 x pH/ORP meters and 2 x DO meter HI9142'),
                            ('DOC-3-MET-PMC-WIN-00087-IE v1.0', 'Martabe WI pH Meter TPS Cube Calibration (25/12/2024) - source of Step 3'),
                            ('DOC-3-MET-PMC-WIN-00089-IE v1.0', 'Martabe WI Operating pH Cube Meter (25/12/2024) - source of Step 4'),
                            ('DOC-3-MET-PRS-WIN-00055-IE v1.0', 'Martabe WI Operate DO Meter Portable (25/12/2024) - source of Steps 5 and 6'),
                            ('DOC-2-MET-PRM-SOP-00037-IE, DOC-2-MET-MEL-SOP-00087-IE, DOC-IV-MET-CHH-SOP-00039', 'Martabe SOPs referenced by the Martabe WIs - not received'),
                            ('SWI-PRO-MET-201-003', 'Leach Tank Sampling Round - cyanide controls at the tank')])
EMERG = emerg(['hcn', 'cn', 'chem', 'acid', 'cut'], 'bench equipment')
