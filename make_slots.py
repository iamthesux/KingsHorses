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
            { 'role': "MAJ Singleton", 'loadout': 'det5_base', },
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
		[
			{ 'role': "SGT Bayley", 'loadout': 'det5_base', },
		]
    ],
)
teams['sasr'] = dict(
    name = 'SASR',
    side = 'WEST',
    groups = [
        [
            { 'role': "C/Sgt Pursehouse", 'loadout': 'sasr_base', },
            { 'role': "C/Sgt Constanti", 'loadout': 'sasr_base', },
            { 'role': "C/Sgt MacDowell", 'loadout': 'sasr_base', },
            { 'role': "Sgt Archibald", 'loadout': 'sasr_base', },
            { 'role': "Cpl Sowers", 'loadout': 'sasr_base', },
            { 'role': "Cpl Deckert", 'loadout': 'sasr_base', },
        ],
    ],
)

teams['sasr'] = dict(
    name = 'SASR',
    side = 'WEST',
    groups = [
        [
            { 'role': "C/Sgt Pursehouse", 'loadout': 'sasr_base', },
            { 'role': "C/Sgt Constanti", 'loadout': 'sasr_base', },
            { 'role': "C/Sgt MacDowell", 'loadout': 'sasr_base', },
            { 'role': "Sgt Archibald", 'loadout': 'sasr_base', },
            { 'role': "Cpl Sowers", 'loadout': 'sasr_base', },
            { 'role': "Cpl Deckert", 'loadout': 'sasr_base', },
        ],
    ],
)

teams['rifles'] = dict(
    name = 'MCRU',
    side = 'WEST',

    groups = [
        # rifles plt hq
        [
            { 'role': "Platoon Leader", 'loadout': 'marine_pl', 'callsign': 'RAIDER 1-6', },
            { 'role': "Platoon Sergeant", 'loadout': 'marine_psg', 'callsign': 'RAIDER 1-7', },
            { 'role': "Platoon Guide", 'loadout': 'marine_guide', },
            { 'role': "Corpsmen", 'loadout': 'marine_medic', },
            { 'role': "Corpsmen", 'loadout': 'marine_medic', },			
            { 'role': "Corpsmen", 'loadout': 'marine_medic', },			
		],
        # rifles squad 1
        [
            { 'role': "Squad Leader", 'loadout': 'marine_sl', 'callsign': 'RAIDER 1-1', },
			
            { 'role': "Alpha - Team Leader", 'loadout': 'marine_tl', 'callsign': 'RAIDER 1-1-A' },
            { 'role': "Automatic Rifleman", 'loadout': 'marine_ar' },
            { 'role': "Assistant AR", 'loadout': 'marine_aar' },
            { 'role': "Rifleman", 'loadout': 'marine_rifleman' },
			
            { 'role': "Bravo - Team Leader", 'loadout': 'marine_tl', 'callsign': 'RAIDER 1-1-B' },
            { 'role': "Automatic Rifleman", 'loadout': 'marine_ar' },
            { 'role': "Assistant AR", 'loadout': 'marine_aar' },
            { 'role': "Rifleman", 'loadout': 'marine_rifleman' },
			
            { 'role': "Charlie - Team Leader", 'loadout': 'marine_tl', 'callsign': 'RAIDER 1-1-C' },
            { 'role': "Automatic Rifleman", 'loadout': 'marine_ar' },
            { 'role': "Assistant AR", 'loadout': 'marine_aar' },
            { 'role': "Rifleman", 'loadout': 'marine_rifleman' },
		],
    ],
)
teams['weapons'] = dict(
    name = 'MCRU',
    side = 'WEST',

    groups = [
        # weapons hq
        [
            { 'role': "Platoon Leader", 'loadout': 'marine_pl', 'callsign': 'RAIDER 4-6', },
            { 'role': "Platoon Sergeant", 'loadout': 'marine_psg', 'callsign': 'RAIDER 4-7', },
            { 'role': "Platoon Guide", 'loadout': 'marine_guide', },
            { 'role': "Corpsmen", 'loadout': 'marine_medic', },
            { 'role': "Corpsmen", 'loadout': 'marine_medic', },
            { 'role': "Corpsmen", 'loadout': 'marine_medic', },
		],
        # weapons mg 1
        [
            { 'role': "Squad Leader", 'loadout': 'marine_sl', 'callsign': 'RAIDER 4-1', },
			
            { 'role': "Assistant Gunner", 'loadout': 'marine_tl', 'callsign': 'RAIDER 4-1-A' },
            { 'role': "Gunner", 'loadout': 'marine_ar' },
            { 'role': "Ammuntion Bearer", 'loadout': 'marine_aar' },
            { 'role': "Assistant Gunner", 'loadout': 'marine_tl', 'callsign': 'RAIDER 4-1-B' },
            { 'role': "Gunner", 'loadout': 'marine_ar' },
            { 'role': "Ammuntion Bearer", 'loadout': 'marine_aar' },
			
		],
    ],
)
teams['weapons'] = dict(
    name = 'MCRU',
    side = 'WEST',

    groups = [		
		# tank platoon
		[
			{ 'role': "M1A1 Platoon Leader", 'loadout': 'marine_crew' },
			{ 'role': "Driver", 'loadout': 'marine_crew' },
			{ 'role': "Gunner", 'loadout': 'marine_crew' },
			{ 'role': "Loader", 'loadout': 'marine_crew' },
		],
		[
			{ 'role': "M1A1 Platoon Sergeant", 'loadout': 'marine_crew' },
			{ 'role': "Driver", 'loadout': 'marine_crew' },
			{ 'role': "Gunner", 'loadout': 'marine_crew' },
			{ 'role': "Loader", 'loadout': 'marine_crew' },
		],
		[
			{ 'role': "M1A1 Commander", 'loadout': 'marine_crew' },
			{ 'role': "Driver", 'loadout': 'marine_crew' },
			{ 'role': "Gunner", 'loadout': 'marine_crew' },
			{ 'role': "Loader", 'loadout': 'marine_crew' },
		],
		[
			{ 'role': "M1A1 Commander", 'loadout': 'marine_crew' },
			{ 'role': "Driver", 'loadout': 'marine_crew' },
			{ 'role': "Gunner", 'loadout': 'marine_crew' },
			{ 'role': "Loader", 'loadout': 'marine_crew' },
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

for team in ['pubs', 'marines', '160th', 'sasr', 'det5']:
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
                
                if id_count == 0:
                    u['player'] = 'PLAYER COMMANDER'
                else:
                    u['player'] = 'PLAY CDG'
                u['skill'] = 0.60000002
                u['text'] = "%s_%d_%d" % (team, g_count, v_count)
                u['description'] = "%s // %s" % (teams[team]['name'], unit['role'])
                if 'callsign' in unit:
                    u['description'] += " // %s" % (unit['callsign'])

                u['init'] = "[this, '%s'] call suxlo_fnc_apply_loadout;" % unit['loadout']
                
                id_count += 1
                v_count += 1
                v['items'] = v_count
                v(u)
            g(v)
            g_count += 1
            mish('Mission')('Groups')['items'] = g_count
            mish('Mission')('Groups')(g)

Writer('KingsHorses.Chernarus_Summer/mission.sqm').write(mish)

