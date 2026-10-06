import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '201-022'
TITLE = 'Online Analyser Verification Sampling - pH, Cyanide and Dissolved Oxygen'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
DESC = desc(['Prove that the online analysers are telling the truth.',
             'The plant runs on 243 analog loops including pH, cyanide and dissolved oxygen. If an analyser drifts and nobody checks it against a manual sample, the whole circuit is controlled to a wrong number.',
             'Verify the leach analyser reading against the actual solution in leach tanks 1, 2 and 3 (Step 4), and check the online tailings pH probe against buffers (Step 5).'],
            '201 / 207 Sampling and analysers',
            ['032-CA-001 / 051-CA-002 - Online cyanide analysers', 'Various pH transmitters - leach, CIL, adsorption and tails circuits', 'Various DO probes - leach and CIL circuits'],
            'Once per shift on each analyser, and after any calibration or maintenance on it.', NUM,
            extra_bold=['Draft for review: Steps 4 and 5 are taken from the Martabe work instructions Verifikasi Analyzer Leaching (12/05/2025) and Check pH Tailing Slurry Solution (DOC-3-MET-PMC-WIN-00106-IE, 25/01/2025). JSEA-PRO-MET-201-022 must be updated for the added hazards before this instruction is approved.',
                        'Open items: (1) the quantity of caustic or the target pH is not stated in the source - hold the solution above pH 10.5 in line with the HCN controls; (2) the tolerance for the pH probe check is only given by an example of about 0.2 pH, which must not erode the cyanide safety margin of pH 10.5; (3) the source uses buffers 7 and 10 only, whereas SWI-PRO-MET-206-004 uses 4, 7 and 10 - confirm the buffers cover the working range of the probe; (4) the tolerance per loop is to be set; (5) confirm the record folders exist at Mt. Morgan.'])
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Field meter not calibrated'],
     prestart(NEW_JSEA, ['Calibrate the field pH meter once per shift on pH 4, 7 and 10 buffers, and the field DO meter once per shift.']), None,
     ['Sample bottles 250 mL', 'Field pH meter', 'Field DO meter', 'Free cyanide titration kit and rhodanine indicator', 'Burette, pipette, conical flask, stand and wash bottle',
      'Distilled water', 'Analyser verification log', 'Leach analyser (reading the solution sample) and black 250 mL sample bottles', '100 mL measuring cylinder and filter press',
      'Sodium hydroxide (caustic) to stabilise the solution sample', 'Bucket, water, pH 7 and pH 10 buffer solutions in their bottles', PPE_EQ]),
    ('Verification at the Analyser Sample Point', ['HCN released at the open sample point', 'Splash of cyanide-bearing slurry', 'Contact with live electrical equipment', 'Reading taken at a different time to the sample'],
     ['Take the manual sample from the point the analyser draws from, or as close to it as the arrangement allows, and at the same moment.',
      'Record the analyser reading at the instant the sample is taken. A reading taken five minutes later is not a comparison.',
      'Determine the same parameter in the field by the manual method.',
      'Record both values and the difference in the analyser verification log.',
      'Submit a laboratory split so the field result itself is checked.'], CAUTION_VALVE, None),
    ('Difference Above Tolerance', ['Analyser adjusted by the sampler', 'Drift not reported'],
     ['Where the difference exceeds the tolerance set for that loop, report it to the Shift Supervisor and raise it with instrumentation.',
      'Do not adjust the analyser.'], None, None),
    ('Leach Analyser Verification - Leach Tanks 1, 2 and 3', ['HCN released from the solution', 'Slurry pressed on the filter press', 'Caustic added to cyanide solution', 'Samples mixed up between tanks'],
     ['Sample slurry from leach tank 1, 2 and 3, 3 L from each tank, then press each sample to obtain solution.',
      'Take 200 mL of each sample solution and add caustic. Add enough to hold the solution pH above 10.5, in line with the HCN controls in Part 2.',
      'Read each solution on the leach analyser and record the NaCN and WAD CN values for each tank.',
      'Take 10 mL of the same solution, titrate (free cyanide, silver nitrate method) and record the NaCN found.',
      'Send the remaining sample to the Mt. Morgan laboratory for NaCN, WAD CN and Cu in solution assay.',
      'Record the analyser, titration and laboratory results for each tank side by side in the analyser verification log. Apply the tolerance rule of Step 3 to any difference - do not adjust the analyser.'],
     'CAUTION: Wear full PPE when pressing slurry and when adding caustic to cyanide solution. Keep the solution above pH 10.5.', None),
    ('Tailings pH Probe Check Against Buffers', ['Slippery surface and tailings slurry spill', 'Splash and dust at the tailings pH probe', 'Probe reading wrong'],
     ['Take 5 minutes before starting (Take 5). Prepare the bucket, water and the pH 7 and pH 10 buffer solutions, and check the equipment is in good condition.',
      'Read the tailings pH on the panel.',
      'Wash the slurry off the tailings pH probe with water.',
      'Pour pH 7 buffer into the cap of the buffer bottle and put the pH probe in the cap.',
      'Read the panel. Wait until the pH reads 7.',
      'Pour pH 10 buffer into the cap and put the probe in. Read the panel: the reading must be 10 or round to 10, for example 9.8.',
      'If the reading does not match the buffer, the tailings pH probe must be repaired. Report it to instrumentation and do not adjust it.'],
     'CAUTION: The source tolerance (about 0.2 pH) must not erode the cyanide safety margin of pH 10.5.', None),
    CLOSE_STEP,
]
REFS = refs(NUM, TITLE, [('Control Philosophy 3.1.x', '243 analog loops including pH, CN and DO analysers'),
    ('KBK-MIR-MP-PRO-MET-SOP-0033', 'Penentuan Konsentrasi Sianida dengan Kolorimetri'),
    ('KBK-MIR-MP-PRO-MET-SOP-0053, 0030 and 0031', 'Potassium chloride solution for the cyanide analyser, DO meter calibration and pH meter calibration, received 11 Aug 2026'),
    ('MM-4034-033-P-09', 'Tag Register (942 tags)'),
    ('Verifikasi Analyzer Leaching (12/05/2025)', 'Martabe WI (Indonesian) - source of Step 4'),
    ('DOC-3-MET-PMC-WIN-00106-IE v1.0', 'Martabe WI Check pH Tailing Slurry Solution (25/01/2025) - source of Step 5'),
    ('DOC-2-MET-PRM-SOP-00037-IE and DOC-2-MET-MEL-SOP-00087-IE', 'Martabe SOPs referenced by the Martabe WI - not received')])
EMERG = emerg(['hcn', 'cn', 'skin', 'elec', 'fall', 'slip'])
