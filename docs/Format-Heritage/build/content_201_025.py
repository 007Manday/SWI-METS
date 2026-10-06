import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

NUM = '201-025'
TITLE = 'Sampling Under Cyanide Alarm or Restricted Access Conditions'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = ['Safety helmet and safety glasses', 'Chemical splash goggles and face shield', 'High-visibility long-sleeved shirt and long trousers',
       'Safety boots with sound tread - nitrile PVC boots at the sample point',
       'Chemical resistant suit, nitrile rubber gloves and apron',
       'Personal HCN gas monitor and personal multi-gas monitor including H2S, calibrated and in test date',
       'Full or half gas mask with A2B2E2K2P3 cartridge, carried and available for immediate use']
DESC = desc(['Set what happens to the sampling round when a gas alarm sounds or access is restricted.',
             'The short answer is that sampling stops. This instruction says how it stops, and how it restarts.'],
            '201 Plant Sampling', ['All cyanide-area sample points - under gas alarm or restricted access'],
            'Whenever a gas alarm sounds or access is restricted.', NUM)
STEPS = [
    ('Pre-start Check', ['Working alone in a cyanide area', 'Monitor not carried or not healthy', 'No radio contact'],
     prestart(NEW_JSEA, ['Confirm the personal HCN monitor and, where H2S is credible, the multi-gas monitor are carried, calibrated and switched on.',
                         'Confirm you carry a radio.'], rinse=False, steady=False), None,
     ['Personal HCN gas monitor', 'Personal multi-gas monitor where H2S is credible', 'Radio', PPE_EQ]),
    ('On a Personal Monitor Alarm', ['HCN or H2S exposure', 'Returning for the sample or equipment'],
     ['On any personal monitor alarm: stop, hold your breath, move upwind and uphill, and do not return to collect the sample or the equipment.'],
     'CAUTION: Do not return to collect the sample or the equipment.', None),
    ('On a Fixed Detection Alarm or Siren', ['Delay leaving the area', 'Alarm not reported'],
     ['On any fixed detection alarm or area siren: leave the area by the nearest safe route to the muster point. The site has 20 gas detectors set at 5 ppm alarm and 10 ppm high-high.',
      'Report the alarm and your location to the control room as soon as you are clear.'], None, None),
    ('Account for Others and Do Not Re-enter', ['Person left in the area', 'Re-entering to close a valve', 'Area entered before it is clear'],
     ['Account for anyone else who was in the area with you. Sampling in cyanide areas is never done alone, so there is always someone to account for.',
      'Do NOT re-enter to close a sample valve you have left open. Tell the control room it is open and let the response deal with it.',
      'Do not return to the area until the Shift Supervisor confirms it is clear and the cause is understood.'],
     'CAUTION: Do not re-enter until the Shift Supervisor confirms the area is clear.', None),
    ('Missed Samples and Restart', ['Missed samples not recorded', 'Open sample point not inspected'],
     ['Record the missed samples as missed, with the alarm time and the restriction period.',
      'Once the area is released, inspect every sample point you had opened before restarting the round.'], None, None),
    ('Restricted Access', ['Finding a way round the restriction'],
     ['Where access is restricted for another reason - a lift, a confined space entry, hot work - the affected points are not sampled and are recorded as restricted. Do not find a way around the restriction to get the sample.'], None, None),
    ('Completion', ['Control room not told the round stopped', 'Register not completed'],
     ['Notify the control room that the round is complete, or that it is stopped and why.',
      'Record any step not completed, with the reason.',
      'Report to the Shift Supervisor, and record, any control in Part 2 found not in place.',
      'Make the register or logbook entry and any handover signature.'], None, None),
]
REFS = refs(NUM, TITLE, [('SWI-022', 'Gas Detector Alarm Response (HCN and H2S), issued Rev A'),
    ('Control Philosophy 3.1.x', '20 gas detectors at 5 ppm alarm and 10 ppm high-high'),
    ('KBK-MIR-MP-PRO-OPE-SOP-0076', 'Fasilitas Cyanide, received 11 Aug 2026')])
EMERG = emerg(['hcn', 'h2s', 'cn', 'slip'])
