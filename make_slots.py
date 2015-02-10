from p4a.formats.rap.text import Reader, Writer
from p4a.formats.rap import Klass
from copy import deepcopy

base_pos = [4800,6,2260]

teams = {}
teams['det5'] = dict(
    name = 'SFOD-A 4125',
    side = 'WEST',
    groups = [
        [
            { 'role': "MAJ Singleton", 'loadout': 'singleton_det5', },
            { 'role': "SGM Dodds", 'loadout': 'det5_base', },
            { 'role': "CW2 Moore", 'loadout': 'det5_base', },
            { 'role': "MSG Nichols", 'loadout': 'det5_base', },
            { 'role': "SFC Furlong", 'loadout': 'det5_base', },
            { 'role': "SFC Cannon", 'loadout': 'det5_base', },
            { 'role': "SFC Bryhni", 'loadout': 'det5_base', },
            { 'role': "SFC Cline", 'loadout': 'det5_base', },
            { 'role': "SSG Lewis", 'loadout': 'det5_base', },
            { 'role': "SFC Lee", 'loadout': 'det5_base', },
            { 'role': "SSG Andresen", 'loadout': 'det5_base', },
            { 'role': "SFC Sage", 'loadout': 'det5_base', },
        ],
    ],
)
teams['sfqc'] = dict(
    name = 'SFQC',
    side = 'WEST',
    groups = [
		[
			{ 'role': "SGT Bayley", 'loadout': 'det5_base', },
		]
    ],
)
teams['sasr'] = dict(
    name = 'CDFSF',
    side = 'WEST',
    groups = [
        [
            { 'role': "C/Sgt Pursehouse", 'loadout': 'cdfsf_sl', },
            { 'role': "C/Sgt Constanti", 'loadout': 'cdfsf_gren', },
            { 'role': "C/Sgt MacDowell", 'loadout': 'cdfsf_tl', },
            { 'role': "Cpl Sowers", 'loadout': 'cdfsf_svd', },
            { 'role': "Cpl Deckert", 'loadout': 'cdfsf_rifleman', },
        ],
    ],
)

teams['soar'] = dict(
    name = '160th SOAR',
    side = 'WEST',
    groups = [
        [
            { 'role': "Pilot", 'loadout': 'soar_pilot', },
            { 'role': "Pilot", 'loadout': 'soar_pilot', },
            { 'role': "Pilot", 'loadout': 'soar_pilot', },
            { 'role': "Pilot", 'loadout': 'soar_pilot', },
            { 'role': "Pilot", 'loadout': 'soar_pilot', },
            { 'role': "Pilot", 'loadout': 'soar_pilot', },
            { 'role': "Pilot", 'loadout': 'soar_pilot', },
            { 'role': "Pilot", 'loadout': 'soar_pilot', },
            { 'role': "Crew Chief", 'loadout': 'soar_crew', },
            { 'role': "Crew Chief", 'loadout': 'soar_crew', },
            { 'role': "Crew Chief", 'loadout': 'soar_crew', },
            { 'role': "Crew Chief", 'loadout': 'soar_crew', },
            { 'role': "Crew Chief", 'loadout': 'soar_crew', },
            { 'role': "Crew Chief", 'loadout': 'soar_crew', },
        ],
    ],
)

teams['company_hq'] = dict(
    name = 'HQ',
    side = 'WEST',

    groups = [
        [
            { 'role': "Company Commander", 'loadout': 'marine_pl', 'callsign': 'RAIDER 1-6', },
            { 'role': "Executive Officer", 'loadout': 'marine_pl', 'callsign': 'RAIDER 1-7', },
            { 'role': "First Sergeant", 'loadout': 'marine_pl', },
            { 'role': "Gunnery Sergeant", 'loadout': 'marine_pl', },
            { 'role': "Property NCO", 'loadout': 'marine_pl', },			
            { 'role': "Messenger", 'loadout': 'marine_rifleman', },			
		],
	]
)
teams['rifles'] = dict(
    name = '1st Plt.',
    side = 'WEST',

    groups = [
        # rifles plt hq
        [
            { 'role': "Platoon Leader", 'loadout': 'marine_pl', 'callsign': 'RAIDER 1-6', },
            { 'role': "Platoon Sergeant", 'loadout': 'marine_pl', 'callsign': 'RAIDER 1-7', },
            { 'role': "Platoon Guide", 'loadout': 'marine_rto', },
            { 'role': "Corpsmen", 'loadout': 'marine_medic', },
            { 'role': "Corpsmen", 'loadout': 'marine_medic', },			
            { 'role': "Corpsmen", 'loadout': 'marine_medic', },			
		],
        # rifles squad 1
    ],
)

for i in range(1,4):
	teams['rifles']['groups'].append([
		{ 'role': "Squad Leader", 'loadout': 'marine_sl', 'callsign': 'RAIDER 1-%d' % i },
		
		{ 'role': "Team Leader", 'loadout': 'marine_tl', 'callsign': 'RAIDER 1-%d-A' % i },
		{ 'role': "Automatic Rifleman", 'loadout': 'marine_ar' },
		{ 'role': "Assistant AR", 'loadout': 'marine_aar' },
		{ 'role': "Rifleman", 'loadout': 'marine_rifleman' },
		
		{ 'role': "Team Leader", 'loadout': 'marine_tl', 'callsign': 'RAIDER 1-%d-B' % i },
		{ 'role': "Automatic Rifleman", 'loadout': 'marine_ar' },
		{ 'role': "Assistant AR", 'loadout': 'marine_aar' },
		{ 'role': "Rifleman", 'loadout': 'marine_rifleman' },
		
		{ 'role': "Team Leader", 'loadout': 'marine_tl', 'callsign': 'RAIDER 1-%d-C' % i },
		{ 'role': "Automatic Rifleman", 'loadout': 'marine_ar' },
		{ 'role': "Assistant AR", 'loadout': 'marine_aar' },
		{ 'role': "Rifleman", 'loadout': 'marine_rifleman' },
	])

teams['weapons'] = dict(
    name = 'Wpns Plt.',
    side = 'WEST',

    groups = [
        # weapons hq
        [
            { 'role': "Platoon Leader", 'loadout': 'marine_pl', 'callsign': 'RAIDER 4-6', },
            { 'role': "Platoon Sergeant", 'loadout': 'marine_pl', 'callsign': 'RAIDER 4-7', },
		],
    ],
)
teams['weapons']['groups'].append([
	{ 'role': "MG Section Leader", 'loadout': 'marine_sl', 'callsign': 'RAIDER 4-%d' % i, },
])
for i in range(1,4):
	teams['weapons']['groups'].append([
		{ 'role': "MG Squad Leader", 'loadout': 'marine_sl', 'callsign': 'RAIDER 4-%d' % i, },
		
		{ 'role': "Assistant Gunner", 'loadout': 'marine_tl', 'callsign': 'RAIDER 4-%d-G' % i },
		{ 'role': "Gunner", 'loadout': 'marine_ar' },
		{ 'role': "Ammuntion Bearer", 'loadout': 'marine_aar' },
		{ 'role': "Assistant Gunner", 'loadout': 'marine_tl', 'callsign': 'RAIDER 4-%d-H' % i },
		{ 'role': "Gunner", 'loadout': 'marine_ar' },
		{ 'role': "Ammuntion Bearer", 'loadout': 'marine_aar' },
	])
teams['weapons']['groups'].append([
	{ 'role': "MG Section Leader", 'loadout': 'marine_sl', 'callsign': 'RAIDER 4-%d' % i, },
])
for i in range(1,4):
	teams['weapons']['groups'].append([
		{ 'role': "Squad Leader/Gunner", 'loadout': 'marine_at_sl', 'callsign': 'RAIDER 4-%d' % i, },
		{ 'role': "Assistant Gunner", 'loadout': 'marine_aat' },
		{ 'role': "Team Leader/Gunner", 'loadout': 'marine_at', 'callsign': 'RAIDER 4-%d-G' % i },
		{ 'role': "Assistant Gunner", 'loadout': 'marine_aat' },
	])

teams['tanks'] = dict(
    name = 'M1A1 Plt.',
    side = 'WEST',

    groups = [		
		# tank platoon
		[
			{ 'role': "M1A1 Platoon Leader", 'loadout': 'marine_commander' },
			{ 'role': "Driver", 'loadout': 'marine_crewman' },
			{ 'role': "Gunner", 'loadout': 'marine_crewman' },
			{ 'role': "Loader", 'loadout': 'marine_crewman' },
		],
		[
			{ 'role': "M1A1 Platoon Sergeant", 'loadout': 'marine_commander' },
			{ 'role': "Driver", 'loadout': 'marine_crewman' },
			{ 'role': "Gunner", 'loadout': 'marine_crewman' },
			{ 'role': "Loader", 'loadout': 'marine_crewman' },
		],
		[
			{ 'role': "M1A1 Commander", 'loadout': 'marine_commander' },
			{ 'role': "Driver", 'loadout': 'marine_crewman' },
			{ 'role': "Gunner", 'loadout': 'marine_crewman' },
			{ 'role': "Loader", 'loadout': 'marine_crewman' },
		],
		[
			{ 'role': "M1A1 Commander", 'loadout': 'marine_commander' },
			{ 'role': "Driver", 'loadout': 'marine_crewman' },
			{ 'role': "Gunner", 'loadout': 'marine_crewman' },
			{ 'role': "Loader", 'loadout': 'marine_crewman' },
		],
    ],
)

teams['pubs'] = dict(
    name = 'CDF',
    side = 'WEST',
    groups = [
        # pubbie hq
        [
            { 'role': "Platoon Leader", 'loadout': 'cdf_pl', 'callsign': 'LANCER 1-6', },
            { 'role': "Assistant Platoon Leader", 'loadout': 'cdf_pl', 'callsign': 'LANCER 1-7', },
        ],
		[
			{ 'role': "SL / BTR Commander", 'loadout': 'cdf_sl', 'callsign': 'LANCER 1-1'},
			{ 'role': "BTR Driver", 'loadout': 'cdf_crew', },
			{ 'role': "BTR Gunner", 'loadout': 'cdf_asl_gunner', },
			{ 'role': "Machine Gunner", 'loadout': 'cdf_mg', },
			{ 'role': "Medic", 'loadout': 'cdf_medic', },
			{ 'role': "Grenadier", 'loadout': 'cdf_grenadier' },
			{ 'role': "Asst. Grenadier", 'loadout': 'cdf_grenadier' },
			{ 'role': "Senior Rifleman", 'loadout': 'cdf_rifleman' },
			{ 'role': "Rifleman", 'loadout': 'cdf_rifleman' },
		],
		[
			{ 'role': "SL / BTR Commander", 'loadout': 'cdf_sl', 'callsign': 'LANCER 1-2'},
			{ 'role': "BTR Driver", 'loadout': 'cdf_crew', },
			{ 'role': "BTR Gunner", 'loadout': 'cdf_asl_gunner', },
			{ 'role': "Machine Gunner", 'loadout': 'cdf_mg', },
			{ 'role': "Medic", 'loadout': 'cdf_medic', },
			{ 'role': "Grenadier", 'loadout': 'cdf_grenadier' },
			{ 'role': "Asst. Grenadier", 'loadout': 'cdf_grenadier' },
			{ 'role': "Senior Rifleman", 'loadout': 'cdf_rifleman' },
			{ 'role': "Rifleman", 'loadout': 'cdf_rifleman' },
		],		
		[
			{ 'role': "SL / BTR Commander", 'loadout': 'cdf_sl', 'callsign': 'LANCER 1-3'},
			{ 'role': "BTR Driver", 'loadout': 'cdf_crew', },
			{ 'role': "BTR Gunner", 'loadout': 'cdf_asl_gunner', },
			{ 'role': "Machine Gunner", 'loadout': 'cdf_mg', },
			{ 'role': "Medic", 'loadout': 'cdf_medic', },
			{ 'role': "Grenadier", 'loadout': 'cdf_grenadier' },
			{ 'role': "Asst. Grenadier", 'loadout': 'cdf_grenadier' },
			{ 'role': "Senior Rifleman", 'loadout': 'cdf_rifleman' },
			{ 'role': "Rifleman", 'loadout': 'cdf_rifleman' },
		],
    ]
)

mish = Reader('KingsHorses.Chernarus_Summer/mission.sqm').read()
top_id = id_count = mish.nextid()
g_count = mish('Mission')('Groups')['items']

fh = open('slots.txt', 'w')

for team in teams.keys():
    if team in teams:
        for grp in teams[team]['groups']:
			for unit in grp:
				s =  "%s | %s" % (teams[team]['name'], unit['role'])
				if 'callsign' in unit:
					s += " // %s" % (unit['callsign'])
				fh.write(s+"\n")
			fh.write("\n")

for team in teams.keys():
    if team in teams:
        for grp in teams[team]['groups']:
			
            g = Klass('Item' + str(g_count))
            g['side'] = teams[team]['side']
            
            v = Klass('Vehicles')
            v_count = 0
            for unit in grp:
				u = Klass('Item' + str(v_count))
				u['position'] = [base_pos[0]+int((id_count-top_id)/10), base_pos[1], base_pos[2]+((id_count-top_id) % 10)]
				u['id'] = id_count
				u['side'] = teams[team]['side']
				u['vehicle'] = 'B_Soldier_F'

				if id_count == top_id:
					u['player'] = 'PLAYER COMMANDER'
				else:
					u['player'] = 'PLAY CDG'
				u['skill'] = 0.60000002
				u['text'] = "%s_%d_%d" % (team, g_count, v_count)
				u['description'] = "%s // %s" % (teams[team]['name'], unit['role'])
				if 'callsign' in unit:
					u['description'] += " // %s" % (unit['callsign'])

				u['init'] = "[this, '%s'] call suxlo_fnc_init_loadout;" % unit['loadout']

				id_count += 1
				v_count += 1
				v['items'] = v_count
				v(u)
            g(v)
            g_count += 1
            mish('Mission')('Groups')['items'] = g_count
            mish('Mission')('Groups')(g)

Writer('KingsHorses.Chernarus_Summer/mission.sqm').write(mish)

