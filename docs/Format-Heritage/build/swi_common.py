"""Shared wording for the 201 series Heritage conversions (taken from the original SWI boilerplate)."""
PPE_STD = [
    'Safety helmet and safety glasses',
    'Chemical splash goggles and face shield',
    'High-visibility long-sleeved shirt and long trousers',
    'Safety boots with sound tread - nitrile PVC boots at the sample point',
    'Chemical resistant suit, nitrile rubber gloves and apron',
    'Personal HCN gas monitor, calibrated and in test date',
    'Full or half gas mask with A2B2E2K2P3 cartridge, carried and available for immediate use',
    'Harness and fall arrest where no fixed platform exists',
]
SAFETY_CRITICAL = 'This is a safety-critical task. It is not carried out alone in a cyanide area, and not without the Shift Supervisor knowing it is in progress.'
PARENT = 'This instruction sits under Standard Work Procedure HM-PRC-VXX-PRO205 - Plant Sampling and Metallurgical Data Collection. Read that procedure before carrying out this task for the first time.'

def register(num):
    return 'Register line: SWI-PRO-MET-%s in HM-MMM-WHS-REG-XXX-R00-SWI-SWMS, tab SWI-MET. The matching hazard analysis is JSEA-PRO-MET-%s.' % (num, num)

def desc(setpoints, area, points, frequency, num, extra_bold=()):
    d = [('n', s) for s in setpoints] + [('b', None), ('n', 'Area: %s.' % area), ('n', 'Points and equipment covered:')]
    d += [('n', p) for p in points]
    d += [('b', None), ('n', 'Frequency: %s' % frequency), ('b', None), ('n', PARENT), ('b', None), ('n', register(num)), ('b', None)]
    for t in extra_bold:
        d += [('B', t), ('b', None)]
    d.append(('B', SAFETY_CRITICAL))
    return d

def prestart(jsea, extra=(), alone=True, rinse=True):
    b = ['Confirm you are trained and signed off against this SWI, signed on to %s at a communication session, and authorised by the Shift Supervisor.' % jsea]
    if alone:
        b.append('Confirm a second person is in the area. Cyanide-area sampling is not done alone.')
    b += list(extra)
    b += ['Confirm the plant is in steady-state operation - normal operation for a minimum of 15 to 20 minutes before sampling. A sample taken during a swing is not representative.',
          'Notify the control room or DCS operator that the sampling round is starting, and which points it covers.',
          'Confirm the personal gas monitor is on, in calibration date and reading clean, and that fixed detection in the area is healthy.',
          'Confirm the safety shower and eyewash nearest the point are within reach and proven flowing.',
          'Label every container BEFORE sampling - point, date, time and shift.']
    if rinse:
        b.append('Rinse the container, cutter or sieve with process water and then with the stream being sampled. Discard the rinse.')
    return b

PRESTART_HAZ = ['Working alone in a cyanide area', 'Gas monitor or fixed detection not healthy', 'Safety shower or eyewash not proven flowing']

CLOSE = ['Close the sample valve or stop the sample pump and confirm the point is not weeping.',
      'Wash down the point and the surrounding walkway. Leave nothing on the grating.',
      'Record sampling time, operator name and the operating conditions read at the time - flow, density and any instrument value available.',
      'Deliver the labelled samples to the laboratory or to the composite station as the schedule requires, and sign the handover.',
      'Notify the control room that the round is complete.',
      'Record the result, the method used and the instrument or balance identity on the field or bench data sheet - date, time, shift, operator and every value determined. Make the register or logbook entry and any handover signature.',
      'Record any step not completed, with the reason.',
      'Report to the Shift Supervisor, and record, any control in Part 2 found not in place.']
CLOSE_STEP = ('Completion and Clean Up',
    ['Sample valve left weeping', 'Samples not handed over with a signed record', 'Control room not told the round is complete'],
    CLOSE, None, None)

PPE_EQ = 'Personal protective equipment as listed in PPE Requirements'
CAUTION_VALVE = 'CAUTION: Open the sample valve slowly, with the container positioned first and the body out of the spray path. Never open a valve whose discharge cannot be seen.'

_E = {
 'hcn': '%d. HCN Gas Alarm If the personal monitor or fixed detection alarms (5 ppm alarm, 10 ppm high-high), stop work, leave the area upwind and call CH19 “EMERGENCY”. Do not re-enter until the Shift Supervisor clears the area.',
 'equip': '%d. Contact with Moving Equipment If a person is caught by or struck by %s, hit the nearest emergency stop, call CH19 “EMERGENCY” and call 000. Do not approach the equipment until it is isolated and locked out.',
 'cn': '%d. Suspected Cyanide Exposure If a person becomes dizzy, short of breath or collapses, call CH19 “EMERGENCY”, call 000, and bring the cyanide antidote kit and a trained first aider. Do not give mouth-to-mouth resuscitation.',
 'skin': '%d. Skin or Eye Contact with Slurry Flush with copious water at the safety shower or eyewash for a minimum of 15 minutes. Remove contaminated clothing while flushing. Report to the first aider.',
 'burn': '%d. Burns Cool the burn under cool running water for 20 minutes. Do not apply ice. Seek first aid.',
 'fall': '%d. Fall from Height Do not move the injured person unless they are in danger. Call CH19 “EMERGENCY”, call 000, and notify the Shift Supervisor.',
 'slip': '%d. Slip, Fall or Lifting Injury Call CH19 “EMERGENCY”, call 000 if the injury is serious, and notify the Shift Supervisor.',
 'acid': '%d. HCl Gas or Acid Contact Leave the area upwind. Flush skin or eyes with copious water at the safety shower or eyewash for a minimum of 15 minutes. If breathing is affected call CH19 “EMERGENCY” and call 000.',
 'carbon': '%d. Carbon in the Undersize Report it to the Shift Supervisor and the control room immediately, before the round continues. Do not restart sampling until the Shift Supervisor clears it.',
}
def emerg(keys, equip='an agitator, pump, screen or sample cutter'):
    out = []
    for i, k in enumerate(keys, 1):
        out.append(_E[k] % ((i, equip) if k == 'equip' else (i,)))
    return out

def refs(num, title, rows):
    base = [('HM-PRC-VXX-PRO205', 'Plant Sampling and Metallurgical Data Collection'),
            ('JSEA-PRO-MET-' + num, 'JSEA — ' + title),
            ('HM-MMM-WHS-REG-XXX-R00-SWI-SWMS', 'SWI / SWMS Register — tab SWI-MET')]
    return base + list(rows)
