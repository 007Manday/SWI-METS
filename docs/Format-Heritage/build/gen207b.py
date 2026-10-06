"""207-007 to 011: online cyanide analysers (Molycop Cynoprobe 032-CA-001, 051-CA-002; read pH, free and WAD cyanide).
Decisions 2026-10-06: the analysers exist; no other analysers; no detox circuit (ReCYN follows CIL)."""
HEAD = '''import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '%s'
TITLE = %r
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = %s
PPE = PPE_STD
'''
def write(num, title, d, haz="hazards_from(os.environ['SRC_DOCX'])"):
    s = HEAD % ('207-' + num, title, haz)
    s += 'DESC = desc207(%r, %r, %r, NUM, extra_bold=%r)\n' % (d['desc'], d['points'], d['freq'], d.get('bold', []))
    steps = ["    ('Pre-start Check', PRESTART_HAZ + %r, prestart203(NEW_JSEA, %r), None, %r + [PPE_EQ])," % (d.get('prehaz', []), d.get('pre', []), d['equip'])]
    for t, hz, bl, cau in d['steps']:
        steps.append('    (%r, %r, %r, %r, None),' % (t, hz, bl, cau))
    steps.append('    CLOSE203_STEP,')
    s += 'STEPS = [\n' + '\n'.join(steps) + '\n]\n'
    s += 'REFS = refs207(NUM, TITLE, %r)\n' % d['refs']
    s += 'EMERG = emerg(%s, %r)\n' % (d['emerg'], d.get('eqp', 'a pump or the analyser sample system'))
    open('content_207_%s.py' % num, 'w').write(s)

AN = ['032-CA-001 - CIL circuit online cyanide analyser (pH, free cyanide and WAD cyanide)',
      '051-CA-002 - Cyanide adsorption (ReCYN) online cyanide analyser (pH, free cyanide and WAD cyanide)']
NFU = ('ISSUED BUT NOT FOR USE. %s cannot be used until the named input arrives: %s. '
       'The method, frequency and equipment are written when that input arrives.')
nfu_step = lambda what: ('Status - Not for Use', ['Task attempted without the vendor documentation'],
                         ['This task cannot be completed until %s is held.' % what,
                          'The document is issued so the register line is not empty, and is marked NOT FOR USE.'], None)

write('007', 'Cyanide Analyser Daily Operation and Check - 032-CA-001 and 051-CA-002', dict(
    desc=['Operate the online cyanide analysers and carry out the daily check.',
          'Cyanide is dosed and recovered on what these analysers say. They also sit in a cyanide-bearing enclosure with their own sample pumps and leak detection.',
          'Replace the analyser filter sock (Step 3).'],
    points=AN, freq='To be set once the vendor manual is held.',
    bold=[NFU % ('The daily operation and check (Step 2)', 'the Molycop Cynoprobe v3 WAD vendor manual is not held and OS-040_B Cyanide Analyser is still open'),
          'Draft for review: the filter sock replacement (Step 3) is taken from the Martabe work instruction Replace Filter Sock (DOC-3-MET-PMC-WIN-00091, undated), written for the Martabe analyser filter probe. JSEA-PRO-MET-207-007 must be updated for the added hazard before it is used.',
          'Open items: (1) confirm the equivalent filter probe and parts on 032-CA-001 and 051-CA-002, and whether these analysers have HCl dosing; (2) the source works from photographs that are not carried here - confirm the filtrate line arrangement for the flush; (3) the source gives no frequency for the filter sock change.'],
    pre=['Take 5 and prepare 1 new filter sock, a 60 mm hose clamp, screwdriver, water hose, cutting knife and silicone. Check they are in good condition.'],
    prehaz=['HCN alarm active at the analyser'],
    equip=['To be confirmed once the Molycop Cynoprobe manual is held', 'New filter sock, 60 mm hose clamp, screwdriver, water hose, cutting knife, silicone'],
    steps=[nfu_step('the Molycop Cynoprobe v3 WAD vendor manual'),
           ('Filter Sock Replacement', ['HCl fume at the filter probe', 'HCN in the cyanide-bearing enclosure', 'Slurry contact', 'Cuts from the cutting knife'],
            ['Switch the cyanide analyser off. Switch off the HCl pump and make sure no HCl fume is left.',
             'Disconnect the pipe from the filter probe, then lift the bracket off the U bolt.',
             'Wash the filter sock with water.',
             'Remove the bolts holding the clamp and filter sock. Cut the old filter sock off with the cutting knife.',
             'Flush the filtrate line: move the pump inlet line to the pump discharge line, and the pump discharge line into a bucket of water (arrangement to be confirmed on this analyser).',
             'Fit the new filter sock. Join it to the filter cage, seal it with silicone and tighten it with the clamp.',
             'Lift and dip the filter probe bracket back in place.',
             'Switch the cyanide analyser on and check it works normally again.'],
            'CAUTION: Work only with no HCN alarm active (alarm 5 ppm, high-high 10 ppm) and the personal HCN monitor on. The enclosure is cyanide-bearing - not done alone. Cut away from the body.')],
    refs=[('Note', 'No source held. Molycop Cynoprobe v3 WAD vendor manual not held; OS-040_B Cyanide Analyser still open.'),
          ('DOC-3-MET-PMC-WIN-00091', 'Martabe WI Replace Filter Sock (Indonesian, undated) - source of Step 3')],
    emerg="['hcn', 'cn', 'skin', 'acid', 'elec', 'slip']"))

write('008', 'Cyanide Analyser Calibration and Standardisation', dict(
    desc=['Calibrate and standardise the online cyanide analysers against known standards.'],
    points=AN, freq='To be set once the vendor calibration data is held.',
    bold=['Draft for review: the calibration method (Steps 2 to 5) is taken from the Martabe work instruction Leach Analyzer Calibration (DOC-3-MET-PMC-WIN-00126-IE, v1.0, 25/12/2024) and applies to both analysers. The Martabe Detox Analyser Calibration is not used: there is no detox circuit at Mt. Morgan - the ReCYN circuit follows CIL. JSEA-PRO-MET-207-008 must be updated for the added hazard before this instruction is approved.',
          'Open items: (1) the source calibrates free NaCN only, with the WAD calibration box NOT ticked; the Mt. Morgan analysers read free and WAD cyanide, so the WAD calibration must be set from the Cynoprobe v3 WAD calibration data, which is not held; (2) standards - the Indonesian source gives 250, 500 and 700 ppm NaCN, its English copy 30, 250 and 500 ppm (taken from the detox instruction); confirm the leach standards and set the range for 051-CA-002 on the ReCYN circuit; (3) the source verification pH range of 9 to 11 reaches below the 10.5 cyanide safety limit; (4) the troubleshooting guide for critical errors is an attachment that was not received; (5) confirm the cyanide-bearing return point for leftover standard (the source says the leach tank) and the record folders.'],
    pre=['Take 5 and prepare the burette, flasks, pipette, dark bottles and bags; check they are in good condition. Confirm the materials are in date. If not, stop and report.',
         'Prepare the potassium chloride electrolyte per KBK MET SOP-0053.'],
    prehaz=['Standards or materials out of date'],
    equip=['Potassium chloride electrolyte per KBK MET SOP-0053', 'NaCN standards at 3 levels, 2 L each, from the Mt. Morgan laboratory', 'AgNO3 0.01 M and rhodanine indicator',
           'Burette, glass flasks, pipette, dark plastic bottles and plastic bags (second containment)', 'Fume-controlled position'],
    steps=[('Standards and Titration', ['Cyanide standard carried and spilled', 'Eye splash', 'HCN from the standards', 'Control room not aware of the calibration'],
            ['Take the NaCN standards at 3 levels, 2 L each, and put them in dark plastic bottles with good lids. Put each bottle in a plastic bag as second containment.',
             'Confirm the nearest safety eyewash works.',
             'Tell the control room the cyanide probe will be calibrated. The operator may take over the cyanide addition to the tank.',
             'Titrate each standard by hand, 3 times per standard, and record the results. Use SWI-PRO-MET-205-001.',
             'Calculate the average titrated concentration for each standard.'],
            'CAUTION: Wear chemical-resistant gloves whenever you contact a cyanide standard. Carry the standards in lidded bottles inside a second bag.'),
           ('Calibration Wizard', ['Wrong calibration points entered', 'Odd reading kept in the calibration'],
            ['On the probe panel press setting. Select calibration with the down button and press enter. Press calibration wizard.',
             'Use 3 calibration points and press continue. The source leaves the WAD calibration box NOT ticked - see open item (1) for the WAD calibration.',
             'Set flushes between standards to 4, flushes between samples to 1 and sample times to 4.',
             'Enter the average titrated concentration for each standard and press next.',
             'Dip the auxiliary line (line 3) into standard 1 and press start, then press done. Repeat for the other two standards. Press next after all standards are measured.',
             'Remove any reading that differs from the others, then press next.'], None),
           ('Acceptance and Verification', ['Calibration accepted with poor fit', 'pH reading below the cyanide safety limit'],
            ['Press accept if R squared is above 0.99. Record M and C before and after the calibration, and R squared after calibration.',
             'Check the verification readings: automatic and manual NaCN within plus or minus 10 ppm; filtrate temperature 25 to 40 degrees C; analyser pH 9 to 11 (source range); probe pH immersed in the filtrate solution. If anything is abnormal, call the metallurgist.',
             'Tell the control room the calibration is finished. Record the before and after readings in G:\\\\Processing\\\\5. Metallurgy\\\\Metallurgy Lab\\\\04 Metlab Data\\\\Calibration Logsheet\\\\Logsheet Cyanide Analyzer Calibration or on form DOC-4-MET-PMC-DFR-00136-EN (Form Cyanide Analyzer Calibration.xlsx).'],
            'CAUTION: Cyanide solution below pH 10.5 releases HCN. Report any analyser pH reading below 10.5 to the metallurgist.'),
           ('Standards Clean-up', ['Leftover standard to the wrong drain'],
            ['Pour all the remaining standard solution into the cyanide-bearing return point (the source says the leach tank). Wash the bottles with water in the analyser hut and return them to storage.'], None)],
    refs=[('KBK-MIR-MP-PRO-MET-SOP-0053', 'Pembuatan Larutan Kalium Klorida untuk Cyanide Analizer, received 11 Aug 2026 - the electrolyte preparation only'),
          ('Note', 'Molycop Cynoprobe v3 WAD calibration data not held'),
          ('DOC-3-MET-PMC-WIN-00126-IE v1.0', 'Martabe WI Leach Analyzer Calibration (25/12/2024) - source of Steps 2 to 5'),
          ('DOC-2-MET-MEL-SOP-00087-IE and DOC-IV-MET-CHH-SOP-00039', 'Martabe SOPs referenced by the Martabe WI - not received'),
          ('SWI-PRO-MET-205-001', 'Free Cyanide Titration - Silver Nitrate Method'),
          ('DOC-4-MET-PMC-DFR-00136-EN', 'Form Cyanide Analyzer Calibration')],
    emerg="['hcn', 'cn', 'skin', 'elec', 'cut', 'slip']"),
    haz="[h for h in hazards_from(os.environ['SRC_DOCX']) if 'detox' not in h.lower()]")

write('009', 'Cyanide Analyser Specialised Electrode Replacement and Conditioning', dict(
    desc=['Replace and condition the specialised electrodes in the online cyanide analysers.'],
    points=['Mintex 3000366 and 3000330 - analyser electrodes identified in the instrument list'] + AN,
    freq='To be set once the vendor manual is held.',
    bold=[NFU % ('This document is a placeholder against the register line so the line is not empty. It', 'the Molycop Cynoprobe vendor manual is not held, and no procedure is held for the Mintex 3000366 and 3000330 electrodes')],
    equip=['To be confirmed once the Molycop Cynoprobe manual is held'],
    steps=[nfu_step('the Molycop Cynoprobe vendor manual')],
    refs=[('Note', 'Electrodes identified as Mintex 3000366 and 3000330 in the instrument list. No procedure held.')],
    emerg="['hcn', 'cn', 'skin', 'elec', 'cut']"))

write('010', 'Cyanide Analyser Sample and Booster Pump Service - 032-PP-207/208 and 041-PP-2xx', dict(
    desc=['Service the sample and booster pumps that feed the online cyanide analysers.'],
    points=['032-PP-207 / 032-PP-208 - Analyser sample and booster pumps', '041-PP-2xx - Analyser sample pumps, tag to be confirmed'],
    freq='To be set once the vendor manual is held.',
    bold=[NFU % ('This document is a placeholder against the register line so the line is not empty. It', 'the Vender Dura 10 pump manual is not held (the pumps are listed as part of the Molycop package)')],
    equip=['To be confirmed once the Vender Dura 10 pump manual is held'],
    steps=[nfu_step('the Vender Dura 10 pump manual')],
    refs=[('Note', 'Vender Dura 10 pumps are listed as part of the Molycop package. No vendor manual held.')],
    emerg="['hcn', 'equip', 'cn', 'skin', 'elec']"))

write('011', 'Cyanide Analyser Leak Detector and High Level Alarm Response', dict(
    desc=['Respond to a leak detector or high level alarm on an online cyanide analyser.',
          'The analyser enclosure holds cyanide-bearing solution. A leak inside it is a confined cyanide release.'],
    points=['Azbil HPQ-D12 - Leak detector, vendor scope', 'E&H FTL31 - High level switch, vendor scope'] + AN,
    freq='To be set once the alarm response is defined.',
    bold=[NFU % ('This document is a placeholder against the register line so the line is not empty. It', 'the Azbil HPQ-D12 leak detector and E&H FTL31 level switch are vendor scope and no alarm response is held')],
    equip=['Personal HCN monitor', 'To be confirmed once the vendor documentation is held'],
    steps=[('Status - Not for Use and Interim Response', ['Enclosure opened during a leak alarm', 'HCN release from the enclosure'],
            ['This task cannot be completed until the vendor documentation and the alarm response are held.',
             'The document is issued so the register line is not empty, and is marked NOT FOR USE.',
             'Until it is written, treat any leak or high level alarm on an analyser as a cyanide release: do not open the enclosure, evacuate the immediate area, and report it to the control room.'],
            'CAUTION: Do not open the analyser enclosure on a leak or high level alarm.')],
    refs=[('Note', 'Azbil HPQ-D12 leak detector and E&H FTL31 level switch are vendor scope. No alarm response held.')],
    emerg="['hcn', 'cn', 'skin', 'acid', 'elec']"))
print('ok')
