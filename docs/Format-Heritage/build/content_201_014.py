import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '201-014'
TITLE = 'Copper Elution, Reactor and Thickener Sampling'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = ['Safety helmet and safety glasses', 'Chemical splash goggles and face shield', 'High-visibility long-sleeved shirt and long trousers',
       'Safety boots with sound tread - nitrile PVC boots at the sample point',
       'Chemical resistant suit, acid-resistant and nitrile rubber gloves, and apron',
       'Personal HCN gas monitor and personal multi-gas monitor including H2S, calibrated and in test date',
       'Full or half gas mask with A2B2E2K2P3 cartridge, carried and available for immediate use',
       'Harness and fall arrest where no fixed platform exists']
DESC = desc(['Set copper precipitation solids percentage and pH.', 'Set free and WAD cyanide on the copper circuit.',
             'Set the solution and solid assay - Cl, Au, Ag and Cu - across elution, the reactor and the thickener.'],
            '071 Copper Elution and Precipitation',
            ['071-CL-002 / 071-CL-003 - Copper elution columns', 'Copper reactor tank - precipitation under agitation, acid and NaSH dosed',
             'Copper thickener - underflow and overflow'],
            'Each elution batch on the columns; hourly on the reactor and thickener while precipitating.', NUM)
STEPS = [
    ('Pre-start Check', ['Sodium hydrosulphide dosing in progress', 'H2S monitor not healthy', 'Gas monitor or fixed detection not healthy', 'Working alone in a cyanide area'],
     prestart(NEW_JSEA, ['Confirm with the control room whether acid or sodium hydrosulphide dosing is in progress. Do NOT sample the reactor while NaSH is being dosed - hydrogen sulphide is released on acid contact.',
                         'Confirm the personal multi-gas monitor including H2S is on, in calibration date and reading clean.'], rinse=True), None,
     ['pH meter', 'TSS meter', 'Free cyanide titration kit - AgNO3', 'Rhodanine indicator', 'Burette 50 mL, pipette 10 or 25 mL, conical flask 250 mL, stand and wash bottle',
      'Lead nitrate', 'Beaker 50 mL', 'Bottles 250 mL', 'Bucket 1 litre', 'Filter press, filter paper', 'Distilled water', PPE_EQ]),
    ('Sample Collection', ['HCN released at the open sample point', 'Acid splash to skin or eyes', 'Fall from the tank top or column platform', 'Equipment starting without warning'],
     ['Flush the point and discard the first flow.', 'Collect the sample.'], CAUTION_VALVE, None),
    ('pH and Suspended Solids', ['HCN released from an acidic stream', 'Meter out of calibration - wrong pH'],
     ['Determine pH immediately. The reactor runs at pH 3 to 5 on 10 per cent w/v sulphuric acid, so this stream is acidic and will release HCN on contact with any cyanide-bearing carry-over.',
      'Determine total suspended solids with the TSS meter.'],
     'CAUTION: The sample is acidic. Keep it clear of any cyanide-bearing solution and keep the personal monitors on.', None),
    ('Cyanide and Assay', ['Splash of cyanide-bearing solution', 'Doses not recorded against the sample'],
     ['Titrate free cyanide and bottle the laboratory split for WAD cyanide.', 'Filter for solution and solid assay and submit both.',
      'Record acid and NaSH dose rates at the time of sampling.'], None, None),
    CLOSE_STEP,
]
REFS = refs(NUM, TITLE, [('HM-PRC-V01-PRO014, PRO015 and PRO016', 'Copper circuit procedures'),
    ('Mt. Morgan site procedures 10 and 11', 'Copper Reactor Tank Sampling and Copper Thickener Underflow Sampling [LIVE]'),
    ('KBK SOP-PROC-CNREC-05 and CNREC-09', 'Metal elution and Filtration of copper precipitation, received 11 Aug 2026'),
    ('4034-017-VE-096 Rev B', 'Goldquip fabricated ReCYN column IOM (071-CL-002/003), received 11 Aug 2026'),
    ('4034-024-VE-061 Rev 0', 'AirEng cyanide scrubbing column No.1 exhaust fan IOM (071-FA-008), received 11 Aug 2026')])
EMERG = emerg(['hcn', 'h2s', 'equip', 'cn', 'skin', 'acid', 'fall', 'slip'])
