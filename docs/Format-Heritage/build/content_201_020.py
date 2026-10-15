import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *

import glob
NUM = '201-020'
TITLE = 'Reagent Solution Strength Sampling - NaCN, NaOH, H2SO4, NaCl, Lime and NaSH'
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
_floc_src = glob.glob(os.path.join(os.path.dirname(os.environ['SRC_DOCX']), '*201-017-*.docx'))
HAZARDS = hazards_from(os.environ['SRC_DOCX'])
# flocculant solution sampling moved here from 201-017 (reagent area): carry its hazard row too
HAZARDS += [h for h in hazards_from(os.environ.get('FLOC_SRC_DOCX', _floc_src[0] if _floc_src else '')) if 'locculant' in h and h.startswith('[JSEA')]
PPE = ['Safety helmet and safety glasses', 'Chemical splash goggles and face shield', 'High-visibility long-sleeved shirt and long trousers',
       'Safety boots with sound tread - nitrile PVC boots at the sample point',
       'Chemical resistant suit, acid-resistant and nitrile rubber gloves, and apron',
       'Personal HCN gas monitor and personal multi-gas monitor including H2S, calibrated and in test date',
       'Full or half gas mask with A2B2E2K2P3 cartridge, carried and available for immediate use']
DESC = desc(['Confirm every made-up reagent is at the strength the process assumes before it is dosed.',
             'A reagent made up off-strength is dosed at the wrong rate everywhere it is used, and the error is not visible until the circuit drifts.',
             'Sample lime slaker feed, product and final product, bagged hydrated lime, ReCYN plant caustic, and the made-up flocculant solution (Steps 4 to 7).'],
            '101 to 107 Reagents',
            ['101 - Sodium cyanide, solution and briquettes', '102 - Sodium hydroxide, diluted', '103 - Lime, slaked slurry',
             '104 - Sodium chloride, made-up solution', '105 - Sulphuric acid, diluted', '107 - Sodium hydrosulphide, as delivered and dosed',
             'Flocculant mixing area - made-up flocculant solution (moved here from the tails thickener SWI)'],
            'Every batch made up, and once per shift on the standing solutions.', NUM,
            extra_bold=['Draft for review: Steps 4 to 6 are taken from the Martabe work instructions Sampling Feed, Product and Final Product of Lime Slaker (DOC-3-MET-PRS-WIN-00059-IE), Sampling Hydrated Lime (DOC-3-MET-PRS-WIN-00061-IE) and ReCYN Plant Caustic Strength Measurement (DOC-3-MET-PMC-WIN-00088-IE). Step 7 is taken from Tailing Flocculant Solution Sampling (DOC-3-MET-PRS-WIN-00064-IE), moved here from the area of the tails thickener. All v1.0, 25/12/2024. JSEA-PRO-MET-201-020 must be updated for the added hazards before this instruction is approved.',
                        'Open items: (1) map the Martabe lime slaker feed hopper, product hopper and lime tank to the Transmin slaking plant points; (2) the source gives no test for the lime samples, no slurry temperature and no bag type; (3) confirm the test on hydrated lime - per cent solids on dry lime is unusual (lime availability is in SWI-PRO-MET-205-005); (4) confirm the ReCYN caustic pump drain pipe carries the diluted solution; (5) the flocculant solution strength test is not stated; (6) confirm the record folders and forms exist at Mt. Morgan.'])
STEPS = [
    ('Pre-start Check', PRESTART_HAZ + ['Wrong reagent procedure or PPE'],
     prestart(NEW_JSEA, ['Read the reagent-specific site sampling procedure before starting - the PPE and the approach differ between cyanide, acid, caustic and NaSH.',
                         'NEVER use a container that has held a different reagent. Dedicated, labelled containers only.'], rinse=False), None,
     ['Sample bottles 250 mL, one dedicated set per reagent', 'pH meter', 'Hydrometer or density meter',
      'Titration set - burette, pipette, conical flask, stand, wash bottle', 'Standardised AgNO3 for cyanide; standardised HCl for caustic; standardised NaOH for acid',
      'Rhodanine and phenolphthalein indicators', 'Distilled water',
      'Sample containers (sampler) kept at the lime slaker, dry plastic bags, scoop, marker, cable ties, forklift (hydrated lime bags), N95 mask, hazmat overall',
      '100 mL sample bottle with a closing lid, fume cupboard, sulphuric acid solution prepared per the Martabe instruction (not received)', 'Small sample bottle for the flocculant solution',
      'Personal protective equipment as listed in PPE Requirements, matched to the reagent being sampled']),
    ('Made-up Reagent Strength Sampling',
     ['HCN released at the cyanide sample point', 'Acid or caustic burn to skin or eyes', 'H2S released from sodium hydrosulphide', 'Dust from cyanide briquettes'],
     ['For sodium cyanide solution, sample only from the designated valve with full cyanide PPE, including the gas mask with A2B2E2K2P3 cartridge available for immediate use.',
      'For sodium cyanide briquettes, sample the solid with the dust controls in place and do not open the sample in an unventilated space.',
      'For sulphuric acid and sodium hydroxide, sample slowly from the designated diluted-solution valve, never from the concentrated storage tank.',
      'For sodium hydrosulphide, confirm no acid dosing is running anywhere that could contact the stream, and wear the multi-gas monitor including H2S.'],
     'CAUTION: Add acid to water, never the reverse. Never sample from a concentrated storage tank.', None),
    ('Field Measurement and Records', ['Batch outside target dosed', 'Strength not recorded against the sample'],
     ['Titrate or measure density in the field where the method allows, and bottle the laboratory split for confirmation.',
      'Record batch number, make-up time, measured strength and the target strength against each sample. Report any batch outside the target range to the Shift Supervisor before it is dosed.'], None, None),
    ('Lime Slaker Feed, Product and Final Product Sampling',
     ['Lime dust and contact with the product', 'Heat from the lime slurry', 'Sampler striking the head', 'Wet bag or damaged bag'],
     ['Take 5 minutes before starting (Take 5). Check the plastic bags are not damaged or leaking.',
      'Feed: the sampling point is the feed hopper. Use the sampler kept near the lime slaker. Put the sampler into the feed bin and fill it. Take it out of the bin. Make sure the bag is dry (change a wet bag for a dry one). Put the sample in the bag and tie it tightly.',
      'Product: the sampling point is the product hopper. Open the product bin cover, put the sampler in and fill it, lift it out. Use a dry bag, put the sample in and tie it tightly. Close the product bin cover.',
      'Final product: the sampling point is the lime tank. Put the sampler into the final product bin, fill it, lift it out. Use a dry bag, put the sample in and tie it tightly.'],
     'CAUTION: Hazards are dust, contact with the product, the sampler hitting the head, and heat from the lime slurry. Hard hat on. Make sure there is no water in the lime feed pocket.', None),
    ('Bagged Hydrated Lime Sampling',
     ['Lime dust to the eyes or skin', 'Forklift operated by an unauthorised person', 'Sample not homogeneous', 'Sample bag leaking'],
     ['Check the nearest eyewash works. Prepare plastic bags, marker and scoop. Have the lime safety data sheet available.',
      'Bring the sample bag down with the forklift as the forklift operation instruction requires. Only an authorised forklift operator does this.',
      'Write the ID number on the plastic bag. Untie the sample bag and level the surface of the opened lime bag so lime does not spill.',
      'Take the sample with a scoop, spread evenly so the sample is homogeneous across the bag. Take it at least 10 cm below the surface.',
      'Put the sample in the labelled plastic bag. Twist the bag tightly and tie it by hand so no air is left inside. Also tie it with a cable tie. Double-bag it and tie the outer bag the same way.',
      'Close the sample container again. Send the sample and the dispatch form to the Mt. Morgan laboratory.',
      'Record the per cent solids of the hydrated lime in G:\\Processing\\5. Metallurgy\\Metallurgy Lab\\04 Metlab Data\\Lime\\% Solid Hydrated Lime.'],
     None, None),
    ('ReCYN Plant Caustic - Sampling and Strength',
     ['Caustic or sulphuric acid spill and fumes', 'Sample bottle overfilled', 'Wrong titration result'],
     ['Take 5 and prepare the fume cupboard, beakers, 100 mL sample bottle, dropper and burette. Check them and the reagents (water, NaOH, phenolphthalein, sulphuric acid) are good to use.',
      'Take the NaOH sample from the drain pipe of the ReCYN plant caustic pump into the 100 mL bottle. Fill the bottle to the level of the lid so it does not overflow, then close it tightly.',
      'Prepare the sulphuric acid and titrate the sample in the fume cupboard as SWI-PRO-MET-205-002 Part B describes.',
      'Record the caustic strength in G:\\Processing\\5. Metallurgy\\Metallurgy Lab\\04 Metlab Data\\Concentrasi NaOH or on form DOC-4-MET-PMC-DFR-00135-EN (Form Caustic Strength.xlsx).'],
     'CAUTION: Sample only the diluted solution, never the concentrated tank. Carry reagents in closed bottles or glassware.', None),
    ('Flocculant Solution Sampling',
     ['Flocculant solution contact', 'Slippery floor at the flocculant mixing area', 'Pinch point at the feed valve', 'Sampling during flocculant lifting or handling'],
     ['Take 5 minutes before starting (Take 5). Confirm the controls in Part 2 are in place and the sample bottle is ready and in good condition. If not, stop and report.',
      'Do not sample while flocculant lifting or handling is under way - wait until it has finished.',
      'The sampling point is the flocculant tube in the flocculant mixing area. Open one of the control valves next to the sampling tube, on the line with the pump running.',
      'Open the tube cover and wait for the tube to fill with flocculant solution. Close the valve when the tube is full.',
      'Put the bottle into the tube and fill it to the top with flocculant solution.',
      'To empty the tube, close the feed valve and the control valve together, then return the valves to their normal position. Close the tube cover.'],
     'CAUTION: Slippery floors and pinch points at the feed valve are the main hazards. Keep hands clear of the feed valve and wear gloves, hard hat, glasses and safety boots.', None),
    CLOSE_STEP,
]
REFS = refs(NUM, TITLE, [('HM-PRC-V01-PRO021 to PRO027', 'Reagent circuit procedures'),
    ('Mt. Morgan site procedures 19, 20, 21 and 22', 'Sodium Cyanide Solution, Sodium Cyanide Briquettes, Diluted Sulphuric Acid and Diluted Sodium Hydroxide Sampling [LIVE]'),
    ('KBK-MIR-MP-PRO-MET-SOP-0009', 'Caustic soda titration'),
    ('KBK-MIR-MP-PRO-MET-SOP-0010', 'Cyanide titration'),
    ('KBK-MIR-MP-PRO-MET-SOP-0025, 0039 and 0040', 'Hydrochloric acid titration, received 11 Aug 2026'),
    ('KBK-MIR-MP-PRO-MET-SOP-0041 and 0042', 'Sulphuric acid titration, received 11 Aug 2026'),
    ('KBK-MIR-MP-PRO-MET-SOP-0043', 'AgNO3 standard preparation, received 11 Aug 2026'),
    ('KBK-MIR-MP-PRO-OPE-SOP-0076', 'Fasilitas Cyanide, received 11 Aug 2026'),
    ('4034-046-VE-019 Rev A', 'Transmin quicklime slaking plant functional description, received 11 Aug 2026'),
    ('SWI-PRO-MET-205-002', 'Caustic Soda Strength Titration (Part B)'),
    ('SWI-PRO-MET-205-005', 'Lime availability'),
    ('SWI-PRO-MET-204-010', 'Flocculant Screening and Dose Optimisation Test'),
    ('DOC-3-MET-PRS-WIN-00059-IE v1.0', 'Martabe WI Sampling Feed, Product and Final Product of Lime Slaker (25/12/2024) - source of Step 4'),
    ('DOC-3-MET-PRS-WIN-00061-IE v1.0', 'Martabe WI Sampling Hydrated Lime (25/12/2024) - source of Step 5'),
    ('DOC-3-MET-PMC-WIN-00088-IE v1.0', 'Martabe WI ReCYN Plant Caustic Strength Measurement (25/12/2024) - source of Step 6'),
    ('DOC-3-MET-PRS-WIN-00064-IE v1.0', 'Martabe WI Tailing Flocculant Solution Sampling (25/12/2024) - source of Step 7'),
    ('DOC-2-MET-PRM-SOP-00037-IE', 'Martabe SOP referenced by the Martabe WIs - not received')])
EMERG = emerg(['hcn', 'h2s', 'cn', 'chem', 'acid', 'slip'])
