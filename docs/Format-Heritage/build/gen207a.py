"""207-001 to 006: automatic samplers. 001-005 stay NOT FOR USE (sampler design not held)."""
HEAD = '''import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '%s'
TITLE = %r
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
PPE = PPE_STD
'''
NFU = ('ISSUED BUT NOT FOR USE. This document is a placeholder against the register line so the line is not empty. '
       'It cannot be used until the sampler general arrangement and cutter design are held: %s. '
       'The method, frequency and equipment are written when that input arrives.')
def write(num, title, d):
    s = HEAD % ('207-' + num, title)
    s += 'DESC = desc207(%r, %r, %r, NUM, extra_bold=%r)\n' % (d['desc'], d['points'], d['freq'], d.get('bold', []))
    steps = ["    ('Pre-start Check', PRESTART_HAZ + %r, prestart203(NEW_JSEA, %r), None, %r + [PPE_EQ])," % (d.get('prehaz', []), d.get('pre', []), d['equip'])]
    for t, hz, bl, cau in d['steps']:
        steps.append('    (%r, %r, %r, %r, None),' % (t, hz, bl, cau))
    steps.append('    CLOSE203_STEP,')
    s += 'STEPS = [\n' + '\n'.join(steps) + '\n]\n'
    s += 'REFS = refs207(NUM, TITLE, %r)\n' % d['refs']
    s += 'EMERG = emerg(%s, %r)\n' % (d['emerg'], 'the sampler, a pump or a sample cutter')
    open('content_207_%s.py' % num, 'w').write(s)

nfu_step = [('Status - Not for Use', ['Task attempted without the sampler design'],
             ['This task cannot be completed until the sampler general arrangement and cutter design are held.',
              'The document is issued so the register line is not empty, and is marked NOT FOR USE.'], None)]
eq = ['To be confirmed once the sampler general arrangement is held']
em = "['hcn', 'equip', 'cn', 'skin', 'elec']"
write('001', 'Automatic Sampler Operation and Cut Verification - IsaMill Feed 022-XM-011 and 022-XM-017', dict(
    desc=['Operate the IsaMill feed automatic samplers and prove the cut they take is representative.',
          'An automatic sampler that takes a biased cut produces a wrong number all day, every day, with no obvious sign that anything is wrong.'],
    points=['022-XM-011 - IsaMill feed automatic sampler', '022-XM-017 - IsaMill feed automatic sampler'],
    freq='To be set once the sampler design is known.',
    bold=[NFU % '022-XM-011 and 022-XM-017 are shop-fabricated with the vendor and cutter design TBA, and the mechanical equipment list shows conflicting status (NEW on one tab, FUTURE on another)'],
    equip=eq, steps=nfu_step,
    refs=[('Note', 'No source held. 022-XM-011 and 022-XM-017 are shop-fabricated with the vendor and cutter design TBA.'),
          ('Note', 'The mechanical equipment list shows conflicting status - NEW on one tab, FUTURE on another.')], emerg=em))
write('002', 'Automatic Sampler Operation and Cut Verification - CIL Tails 032-XM-012', dict(
    desc=['Operate the CIL tails automatic sampler and prove the cut is representative.', 'This sampler feeds the tail grade, which closes the plant gold balance.'],
    points=['032-XM-012 - CIL tails automatic sampler'], freq='To be set once the sampler design is known.',
    bold=[NFU % 'vendor and cutter design TBA, and the status conflicts (NEW versus FUTURE) across the equipment list tabs'],
    equip=eq, steps=nfu_step,
    refs=[('Note', 'No source held. Vendor and cutter design TBA; status conflict NEW versus FUTURE across the equipment list tabs.')], emerg=em))
write('003', 'Automatic Sampler Operation and Cut Verification - Metal Adsorption Tails 041-XM-013', dict(
    desc=['Operate the metal adsorption tails automatic sampler and prove the cut is representative.'],
    points=['041-XM-013 - Metal adsorption tails automatic sampler'], freq='To be set once the sampler design is known.',
    bold=[NFU % 'vendor and cutter design TBA'],
    equip=eq, steps=nfu_step,
    refs=[('Note', 'No source held. Vendor and cutter design TBA.')], emerg=em))
write('004', 'Automatic Sampler Operation and Cut Verification - Final Tails 051-XM-014', dict(
    desc=['Operate the final tails automatic sampler and prove the cut is representative.', 'Final tails carries the environmental licence obligation as well as the metal balance.'],
    points=['051-XM-014 - Final tails automatic sampler'], freq='To be set once the sampler design is known.',
    bold=[NFU % 'vendor and cutter design TBA, and no P&ID reference is given on the equipment list'],
    equip=eq, steps=nfu_step,
    refs=[('Note', 'No source held. Vendor and cutter design TBA; no P&ID reference given on the equipment list.')], emerg=em))
write('005', 'Automatic Sampler Cleaning, Unblocking and Cutter Wear Check', dict(
    desc=['Clean and unblock the automatic samplers and check the cutters for wear.',
          'A worn cutter changes the cut it takes. A blocked sampler takes no cut at all and often still reports a sample.'],
    points=['022-XM-011 / -017 - IsaMill feed', '032-XM-012 - CIL tails', '041-XM-013 - Metal adsorption tails', '051-XM-014 - Final tails'],
    freq='To be set once the sampler design is known.',
    bold=[NFU % 'no source is held for any of the five samplers'],
    equip=eq, steps=nfu_step,
    refs=[('Note', 'No source held for any of the five samplers.')], emerg="['hcn', 'equip', 'cn', 'skin', 'elec']"))
write('006', 'Automatic versus Manual Sample Bias Check and Reconciliation', dict(
    desc=['Compare what the automatic samplers report against a manual sample taken at the same point and time.',
          'This is the only check that an automatic sampler is telling the truth, and it is the one that most often gets skipped.'],
    points=['022-XM-011 / -017 - IsaMill feed', '032-XM-012 - CIL tails', '041-XM-013 - Metal adsorption tails', '051-XM-014 - Final tails'],
    freq='Monthly on every sampler, and after any sampler repair or cutter change.',
    prehaz=['Samples not analysed in the same batch'],
    pre=['Arrange the check with the control room and the laboratory so both samples are analysed in the same batch.'],
    equip=['Manual sampling equipment per the Area 201 instructions', 'Pre-labelled containers', 'Stopwatch', 'Field data sheets'],
    steps=[('Paired Sampling', ['HCN released at the open sample point', 'Splash of cyanide-bearing slurry', 'Grab compared against a composite', 'Fall from a tank top or platform'],
            ['Take the manual sample at the same point and over the same period the automatic sampler composites over. A grab against a composite is not a comparison.',
             'Take at least ten paired samples across the period - a single pair proves nothing.',
             'Submit the pairs to the laboratory as blind duplicates where possible.'],
            'CAUTION: Sample from the manual point following the Area 201 instruction for that point. Keep clear of the sampler cutter - it can start without warning.'),
           ('Bias Test', ['Scatter mistaken for bias', 'Laboratory blamed before the sampler is checked'],
            ['Plot the automatic result against the manual result and test for bias, not just for scatter. A consistent offset in one direction is bias; scatter about the line is precision.',
             'Where bias is found, inspect the cutter and the sampler installation before concluding the laboratory is at fault.'], None),
           ('Report and Correction', ['Accounting not corrected', 'Check not repeated after the correction'],
            ['Report the bias with the monthly close and correct the accounting where a bias is confirmed.',
             'Repeat the check after any correction.'], None)],
    refs=[('4034-PR-PRO-002', 'Sampling Protocol - the manual points to compare against'),
          ('SWI-PRO-MET-201-001 to -018', 'Manual sampling instructions, issued')],
    emerg="['hcn', 'equip', 'cn', 'skin', 'fall']"))
print('ok')
