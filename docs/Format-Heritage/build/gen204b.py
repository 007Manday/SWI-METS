"""204-006, 008, 010: series 204 SWIs that carried Martabe additions (decisions 2026-10-06)."""
HEAD = '''import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(CONTENT)))
from src_helpers import hazards_from
from swi_common import *
NUM = '%s'
TITLE = %r
NEW_TITLE = TITLE
NEW_JSEA = 'JSEA-PRO-MET-' + NUM
'''
def write(num, title, hazards_expr, d):
    s = HEAD % ('204-' + num, title)
    s += 'HAZARDS = %s\n' % hazards_expr
    s += 'PPE = PPE_LAB\n'
    s += 'DESC = desc204(%r, %r, NUM, extra_bold=%r)\n' % (d['desc'], d['freq'], d.get('bold', []))
    steps = ["    ('Pre-start Check', PRESTART_LAB_HAZ, prestart_lab(NEW_JSEA, %r), None, %r + [PPE_EQ])," % (d.get('pre', []), d['equip'])]
    for t, hz, bl, cau in d['steps']:
        steps.append('    (%r, %r, %r, %r, None),' % (t, hz, bl, cau))
    steps.append('    CLOSE_LAB_STEP,')
    s += 'STEPS = [\n' + '\n'.join(steps) + '\n]\n'
    s += 'REFS = refs204(NUM, TITLE, %r)\n' % d['refs']
    s += 'EMERG = emerg(%s, %r)\n' % (d['emerg'], d.get('eqp', 'bench equipment'))
    open('content_204_%s.py' % num, 'w').write(s)

# ---- 006: Martabe moisture analyser verification dropped (no moisture analyser at Mt. Morgan)
write('006', 'Moisture Content Determination', "[h for h in hazards_from(os.environ['SRC_DOCX']) if not h.startswith('[JSEA to confirm]')]", dict(
 desc=['Determine the moisture content of a sample by oven drying to constant mass.', 'Every assay is reported on a dry basis. A wrong moisture makes every grade wrong.'],
 freq='Every solid sample requiring a dry mass.',
 equip=['Drying oven', 'Moisture tins', 'Analytical balance', 'Desiccator', 'Tongs'],
 steps=[('Tare and Wet Mass', ['Tin not clean and dry', 'Sample not spread evenly'],
         ['Weigh the clean dry tin and record the tare.',
          'Add the sample, spread it evenly and weigh to get the wet mass.'], None),
        ('Drying to Constant Mass', ['Burns from the hot oven and tins', 'Hot sample weighed light', 'Constant mass assumed from a set time'],
         ['Dry in the oven at the method temperature until constant mass. Constant mass means two successive weighings agree, not one weighing after a set time.',
          'Cool in the desiccator before every weighing. A hot sample reads light.',
          'Weigh and record the dry mass.'],
         'CAUTION: Handle hot tins with tongs and set them down on a heat mat.'),
        ('Calculation and Record', ['Moisture calculated on the wrong basis', 'Oven conditions not recorded'],
         ['Calculate moisture as a percentage of the wet mass.',
          'Record the oven temperature, the drying period and the balance identity.'], None)],
 refs=[('KBK-MIR-MP-PRO-OPE-SOP-0022', 'Moisture Content'), ('KBK-MIR-MP-PRO-MET-SOP-0032', 'Moisture Content, Bahasa master received 11 Aug 2026')],
 emerg="['cn', 'skin', 'burn', 'cut']"))

# ---- 008: Martabe method adopted with the same instruments (Brookfield DV2TLV, Marsh funnel)
write('008', 'Slurry Viscosity and Rheology Test', "hazards_from(os.environ['SRC_DOCX'])", dict(
 desc=['Measure the viscosity and flow behaviour of a slurry at the operating density.',
       'Viscosity governs pumping duty, mixing and thickener behaviour, and rises sharply with fines.',
       'Daily viscosity is read on a Brookfield DV2TLV viscometer at 20 rpm, with a Marsh funnel quick check, following the Martabe method with the same instruments.'],
 freq='On each new ore type, and whenever pumping or mixing behaviour changes.',
 bold=['Draft for review: Steps 3 to 5 follow the Martabe work instructions Measure Viscosity Using Brookfield DV2TLV Viscometer (DOC-3-MET-PMC-WIN-00128-IE) and Measure Viscosity of Slurry Using Marsh Funnel Test (DOC-3-MET-PMC-WIN-00127-IE), v1.0, 25/12/2024. The Martabe method and instruments are adopted. JSEA-PRO-MET-204-008 must be updated for the added hazard before this instruction is approved.',
       'Open items: (1) the Marsh funnel source names the ASTM standard funnel but gives no fill volume, no sieving of coarse particles and no result in seconds per quart - set the fill volume and the reporting unit before use; (2) the Brookfield DV2T operating instruction and instrument manual are not received - confirm the spindle range for the plant slurries; (3) set the spindle and speed used for each slurry so all samples are read the same way.'],
 pre=['Take 5 and prepare the viscometer, spindles and measuring cup, and the Marsh funnel, bucket and stopwatch; check they work. Have clean water ready.'],
 equip=['Brookfield DV2TLV viscometer with spindles and its measuring cup', 'Marsh funnel, bucket and receiving container', 'Sample container and stand', 'Thermometer', 'Marcy scale', 'Stopwatch', 'Clean water for cleaning'],
 steps=[('Sample Preparation', ['Sample not at the operating density', 'Settled slurry reading low', 'Splash of cyanide-bearing slurry'],
         ['Prepare the sample at the density the circuit actually runs at, not at a convenient density.',
          'Record the density and temperature - both change the result substantially.',
          'Homogenise the sample immediately before measuring; a settled slurry reads low.'], None),
        ('Brookfield DV2TLV Set-up', ['Viscometer not level', 'Autozero with the spindle fitted', 'Spindle outside its range'],
         ['Make sure the viscometer is level. Switch it on with the power button.',
          'Autozero by pressing next on the screen. The spindle must not be fitted during autozero.',
          'Choose the spindle. Each spindle has a minimum and maximum viscosity it can measure; see the range in the manual. The spindle and speed chosen must be able to measure all the samples, and all samples must be measured with the same spindle and speed.',
          'Fit the spindle. In the settings menu choose configure viscosity test. Set the speed between 1 and 200 rpm (20 rpm for daily work) and the measuring time for each sample.'], None),
        ('Viscosity Measurement', ['Sample contact and splash to the eyes', 'Torque outside 10 to 90 per cent', 'Single point taken as a rheology curve'],
         ['Pour the sample into the cup. Bring the sample surface level with the mark on the spindle. Lower the spindle into the sample by adjusting the viscometer position.',
          'Press run and record the viscosity reading.',
          'If the torque is below 10 per cent or above 90 per cent, change the speed and the spindle. A slower speed and a smaller spindle can measure higher viscosity.',
          'Where the test is used to size equipment, measure at the range of speeds the method calls for, record the full shear rate against shear stress series, and repeat at two other densities.'],
         'CAUTION: Mineral slurries are not Newtonian. A single 20 rpm reading is for daily comparison only, not a rheology curve.'),
        ('Marsh Funnel Check', ['Slurry spilled while pouring', 'Fill volume not the same each time'],
         ['Hold the funnel and close the bottom opening with a finger of the left hand. With the right hand pour the slurry from the bucket into the funnel.',
          'Position the funnel over the receiving container.',
          'Open the bottom opening and start the stopwatch at the same moment. Record the time for the sample to flow fully out of the funnel.',
          'Stop the stopwatch when nothing more comes out of the funnel.'],
         'CAUTION: Pour slurry slowly to avoid spills and splashes. A funnel time is a quick check, not a rheology curve.'),
        ('Report and Instrument Clean-up', ['Viscosity reported without density and temperature', 'Spindle stored dirty'],
         ['Report the viscosity or the rheology curve, the density and the temperature together. A viscosity quoted without them means nothing.',
          'Switch the viscometer off, take the spindle off, clean it with clean water and put it back in its box.',
          'Clean the Marsh funnel and store it safely.'], None)],
 refs=[('KBK-MIR-MP-PRO-OPE-SOP-0016', 'Uji Viskositas'),
       ('DOC-3-MET-PMC-WIN-00128-IE v1.0', 'Martabe WI Measure Viscosity Using Brookfield DV2TLV Viscometer (25/12/2024) - source of Steps 3 and 4'),
       ('DOC-3-MET-PMC-WIN-00127-IE v1.0', 'Martabe WI Measure Viscosity of Slurry Using Marsh Funnel Test (25/12/2024) - source of Step 5'),
       ('DOC-IV-MET-CHH-SOP-00039', 'Martabe SOP referenced by the Martabe WI - not received')],
 emerg="['equip', 'cn', 'skin', 'slip']", eqp='the viscometer or stirrer'))

# ---- 010: Martabe Parts B, C, D adopted as draft; 1 L graduated cylinders approved for Part A until settling cylinders are bought
write('010', 'Flocculant Screening and Dose Optimisation Test', "hazards_from(os.environ['SRC_DOCX'])", dict(
 desc=['Compare flocculant types and doses to find the cheapest one that does the job.',
       'Flocculant is a significant consumable and the wrong grade costs both money and thickener performance.',
       'Find the settling time at each flocculant solution strength (Step 4), set up the effective treatment dosage test (Step 5), and run the flocculant sieve test on tailing (Steps 6 and 7).'],
 freq='On each new ore type and when a flocculant change is proposed.',
 bold=['Draft for review: Steps 4 to 8 are taken from the Martabe work instructions Settling Test with Variance %Strength Flocc (22/03/2025), Effective Treatment Dosage (DOC-3-MET-PMC-WIN-00122-IE) and Flocculant Testwork on Tailing Using Sieve (DOC-3-MET-PMC-WIN-00124-IE), v1.0, 25/12/2024. They are approved for inclusion. Settling cylinders are not purchased; plain 1 L graduated cylinders are approved for use until they are. JSEA-PRO-MET-204-010 must be updated for the added hazards before this instruction is approved.',
       'Open items: (1) how the 4 strengths and 4 doses are laid out across the 4 cylinders of a set (Step 4); (2) the basis for 276 g and 12 samples (Step 5); (3) name the Mt. Morgan tailing sample point and the cyanide-bearing return point that replace the Martabe safety carbon screen distributor door and pump PU-372 (see SWI-PRO-MET-201-008); (4) flocculant mixing and ageing time are not stated - Step 2 requires the same ageing for every candidate; (5) bucket size, 10 L or 20 L; (6) the Martabe flocculant make-up SOP is not received; (7) the source reads the settling times as 60, 24 hours, 48 hours - minute 60 is assumed (Step 4); (8) confirm the record folders and forms exist at Mt. Morgan.'],
 pre=['Take 5 and prepare the sampling equipment, cylinders, balance, syringes, beakers, sieve and pan, measuring cylinders, turbidity meter, camera, ruler, calipers, stopwatch and clip bags. Make sure the acetone is in date.',
      'Confirm settling cylinders and a flocculant test rig are available before planning the test. Until settling cylinders are purchased, use 1 L graduated cylinders.'],
 equip=['Settling cylinders - NOT PURCHASED; 1 L graduated cylinders used until they are', 'Flocculant samples from candidate suppliers', 'Stopwatch', 'Pipettes', 'Plunger',
        'Balance, syringe, beakers, 250 mL sample bottles, vertical stirrer, filter press, drying oven',
        'Laboratory flocculant, process water, acetone; slurry characterisation spreadsheet (density to per cent solids)',
        'Level gauge, sieve, turbidity meter with cuvettes, cone, bucket, iron stirrer',
        '2 m dip sampler, lab sample shovel, bucket, 1.18 mm sieve with pan, cylinder, 500 mL and 120 mL measuring cylinders, camera, ruler, calipers, clip sample bags'],
 steps=[('Flocculant Make-up and Shortlist', ['Candidates made up at different strengths', 'Flocculant solution splash and spill'],
         ['Make up each candidate flocculant at the same strength and ageing time.',
          'Run the settling test at a fixed dose across all candidates first, to shortlist.'], None),
        ('Dose Response and Costing', ['Cuts from a broken cylinder', 'Result not related to the plant basis'],
         ['Run the dose response on the shortlist.',
          'Record settling rate, overflow clarity and underflow density for each.',
          'Cost each option per tonne treated at its optimum dose.',
          'Report against the plant flocculant basis in the Roytec control philosophies.'], None),
        ('Settling Test with Solution Strength Variance', ['Cylinder weights not matched', 'Wrong flocculant volume added', 'Splash of cyanide-bearing tailing'],
         ['Make up flocculant solutions at 0.35, 0.40, 0.45 and 0.50 per cent with process water.',
          'Stir the tailing sample until even with the vertical stirrer.',
          'Put 1 L of tailing slurry in a graduated cylinder and weigh it. Prepare 4 cylinders for one test set.',
          'Check the weight difference between cylinders is below 4 g. If it is above 4 g, stir again and repeat the previous step.',
          'Open the slurry characterisation spreadsheet. Enter ore density 2.6 t/m3. Enter the 1 L slurry weight as pulp density (RHOP): 1.5 kg per litre is entered as 1.5 (1.5 kg/L = 1.5 t/m3). Read off solids mass and per cent solids.',
          'Record the solution strength and the dose.',
          'Flocculant volume (mL) = dose (g/t) x slurry mass (g) x per cent solids / (solution strength in per cent x 1,000,000). The source writes this as 100 x solids mass (g) / 1,000,000 x 100 / 0.5, where 100 and 0.5 are an example dose of 100 g/t and a 0.5 per cent solution; use the actual dose and strength for each cylinder.',
          'Add flocculant at doses of 70, 80, 90 and 100 g/t.',
          'Mix the sample with the stirring rod 8 times.',
          'Record the solids level at minute 5, 10, 15, 30, 60 and at 24 hours and 48 hours.',
          'Separate the solids from the water with the filter press.',
          'Dry the sample in the oven and weigh it dry to correct the dose to g/t.'], None),
        ('Effective Treatment Dosage (ETD) Test', ['Solids settling in the bucket', 'Pinch point on the level gauge', 'Turbidity read on a dirty cuvette'],
         ['Have the flocculant and the slurry sample ready.',
          'Stir the slurry in the bucket with the iron stirrer so no solids settle.',
          'While stirring, take slurry and weigh 276 g into a beaker. Repeat 12 times to get 12 samples.',
          'Carry out the flocculant test as in Step 7.',
          'Check the turbidity of the water that came through the sieve: power on the turbidity meter, put the cuvette in the sample holder, press read, wait for the result and record it. Take the cuvette out.',
          'Record the ETD data in G:\\\\Processing\\\\5. Metallurgy\\\\Metallurgy Lab\\\\04 Metlab Data\\\\ETD & Settling Test or on form DOC-4-MET-PMC-DFR-00140-EN (Form ETD Data.xlsx).'],
         'CAUTION: Keep hands clear of the level gauge pinch point. Clean spills at once.'),
        ('Tailing and Flocculant Sampling for the Sieve Test', ['HCN at the tailing sampling point', 'Stairs and uneven or slippery ground', 'Acetone is flammable'],
         ['Tailing: use the dip sampler with the 2 m handle at the tailing sample point (to be confirmed). Lower the sampler until slurry fills the cylinder.',
          'Pour into the Marcy scale tube and measure per cent solids. The Marcy scale must be calibrated per the per cent solids procedure. Record the per cent solids.',
          'Fill a bucket with tailing sample.',
          'Flocculant from the bag: sample from one stack of bags only. Untie the top of the bag and use the lab shovel to take 5 to 10 g into a clip bag. Retie the bag.',
          'Dilution: weigh the flocculant to the strength the metallurgist asks for (0.5 per cent means 0.5 g). Add 3 mL acetone, then 97 mL water to make 100 mL.'],
         'CAUTION: The tailing slurry is cyanide-bearing. Apply the cyanide controls of SWI-PRO-MET-201-008 and 201-017 and keep the personal HCN monitor on at the sampling point. Keep acetone away from flame and smoking.'),
        ('Flocculant Sieve Testwork', ['Pinch points at the sieve and calipers', 'Splash of cyanide-bearing slurry', 'Dose calculated wrongly'],
         ['Put a 500 mL beaker on the balance and tare. Stir the tailing slurry, pour 300 mL into the beaker and weigh it.',
          'Flocculant volume (mL) = dose (g/t) x slurry mass (g) x per cent solids / (solution strength in per cent x 1,000,000). Example: 60 g/t, 400 g slurry, 46 per cent solids, 0.4 per cent strength: 60 x 400 x 46 / 400,000 = 2.76 mL.',
          'Draw the flocculant into a syringe and add it to the slurry in the beaker.',
          'Pour the slurry into a second beaker and back into the first, 8 pours in all.',
          'Wait 2 minutes, then pour slowly into the cylinder standing on the 1.18 mm screen. The water drains first into the pan under the screen.',
          'Wait 2 minutes, lift the cylinder slowly and measure the height of the slump with the calipers.',
          'Lift the 1.18 mm sieve. Photograph the slump on the sieve and in the pan from the side and the front, with the date, name and type of flocculant, solution strength and dose.',
          'Tilt the lower tray. Draw the surface water with a syringe into the measuring cylinder and record the volume.',
          'Filter the solids on the sieve and in the pan separately on different filter papers, labelled sieve and pan. Pour the liquid into the bucket.',
          'Dry the solids and weigh them.',
          'Repeat for 30, 40, 60, 80 and 120 g/t, or as the metallurgist instructs.',
          'Record the results in G:\\\\Processing\\\\5. Metallurgy\\\\Metallurgy Lab\\\\04 Metlab Data\\\\ETD & Settling Test or on form DOC-4-MET-PMC-DFR-00146-EN (Form Settling Test calc.xlsx).'],
         'CAUTION: Keep hands clear of the sieve and caliper pinch points.'),
        ('Waste Return', ['Cyanide-bearing waste to the wrong drain'],
         ['Return all leftover flocculant, slurry and wash water to the plant. Take the bucket to the cyanide-bearing return point (to be confirmed) and pour it near the pump. Clean the bucket with process water in the plant.'],
         'CAUTION: Tailing slurry and wash water are cyanide-bearing. They do NOT go to the general drain.')],
 refs=[('4034-019-VE-006 and 4034-019B-VE-007', 'Roytec Model 01 and Model 05 flocculant plant control philosophies, received 11 Aug 2026 - the plant make-up concentration and dose basis'),
       ('Settling Test with Variance %Strength Flocc (22/03/2025)', 'Martabe WI (Indonesian) - source of Step 4'),
       ('DOC-3-MET-PMC-WIN-00122-IE v1.0', 'Martabe WI Effective Treatment Dosage (25/12/2024) - source of Step 5'),
       ('DOC-3-MET-PMC-WIN-00124-IE v1.0', 'Martabe WI Flocculant Testwork on Tailing Using Sieve (25/12/2024) - source of Steps 6 to 8'),
       ('DOC-IV-MET-CHH-SOP-00039', 'Martabe SOP referenced by the Martabe WIs - not received'),
       ('DOC-4-MET-PMC-DFR-00140-EN and 00146-EN', 'Form ETD Data and Form Settling Test calc'),
       ('SWI-PRO-MET-201-008 and 201-017', 'Cyanide controls at the tailing and thickener sampling points'),
       ('SWI-PRO-MET-201-020', 'Flocculant solution sampling (reagent area)')],
 emerg="['hcn', 'cn', 'skin', 'cut', 'slip']"))
print('ok')
