from p4a.formats.rap.text import Reader, Writer
from p4a.formats.rap import Klass
from copy import deepcopy
import math

class Vector:
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)
	def __add__(self, v):
		return Vector(self.x + v.x, self.y + v.y)
	def __mul__(self, v):
		return Vector(self.x * v, self.y * v)
	def perp(self):
		return Vector(self.y, -self.x)

spawns = dict(
	sasr = dict(
		azimuth = 30.05,
		pos = Vector(4812,2544),
		limit = 'x',
		max = 2,
	),
	cdf = dict(
		azimuth = 30.05,
		pos = Vector(4725,2572),
		limit = 'y',
		max = 10,
	),
	marines = dict(
		azimuth = 30.05,
		pos = Vector(4760.5,2551.5),
		limit = 'y',
		max = 10,
	),
	det5 = dict(
		azimuth = 27.5045,
		pos = Vector(4392,2248),
		limit = 'x',
		max = 2,
	),
	cdn = dict(
		azimuth = 356.2,
		pos = Vector(4710,2612),
		limit = 'y',
		max = 2,
	),
)

for v in spawns.values():
	v['count'] = 0
	v['curpos'] = v['pos']
	
	v['unit'] = Vector(round(math.sin(v['azimuth']*math.pi/180), 3), round(math.cos(v['azimuth']*math.pi/180), 3))

teams = {}
teams['det5'] = dict(
	spawn = 'det5',
	name = 'SFOD-A 4125',
	faction = 'det5',
	side = 'WEST',
	groups = [
		[
			{ 'role': "MAJ Singleton", 'loadout': 'officer_det5', },
			{ 'role': "SGM Dodds", 'loadout': 'sniper_det5', },
			{ 'role': "CW2 Moore", 'loadout': 'officer_det5', },
			{ 'role': "MSG Nichols", 'loadout': 'rifleman_det5', },
			{ 'role': "SFC Furlong", 'loadout': 'sniper_det5', },
			{ 'role': "SFC Cannon", 'loadout': 'gunner_det5', },
			{ 'role': "SFC Bryhni", 'loadout': 'gunner_det5', },
			{ 'role': "SFC Cline", 'loadout': 'demolitions_det5', },
			{ 'role': "SFC Lee", 'loadout': 'medic_det5', 'medic': 1},
			{ 'role': "SSG Andresen", 'loadout': 'medic_det5', 'medic': 1},
			{ 'role': "SFC Sage", 'loadout': 'commo_det5', },
		],
	],
)
teams['sfqc'] = dict(
	spawn = 'det5',
	name = 'SFQC',
	faction = 'det5',
	side = 'WEST',
	groups = [
		[
			{ 'role': "SGT Bayley", 'loadout': 'rifleman_det5', },
		]
	],
)
teams['sasr'] = dict(
	spawn = 'sasr',
	name = 'CDFSF',
	faction = 'sasr',
	side = 'WEST',
	groups = [
		[
			{ 'role': "C/Sgt Pursehouse", 'loadout': 'cdf_recce_sl', },
			{ 'role': "C/Sgt Constanti", 'loadout': 'cdf_recce_gren', },
			{ 'role': "C/Sgt MacDowell", 'loadout': 'cdf_recce_tl', },
			{ 'role': "Cpl Sowers", 'loadout': 'cdf_recce_svd', },
			{ 'role': "Cpl Deckert", 'loadout': 'cdf_recce_rifleman', },
		],
	],
)

teams['soar'] = dict(
	spawn = 'cdn',
	name = '10th TAB',
	side = 'WEST',
	faction = 'det5',
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
	spawn = 'marines',
	name = 'HQ',
	side = 'WEST',
	faction = 'marines',
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
	spawn = 'marines',
	name = '1st Plt.',
	side = 'WEST',
	faction = 'marines',
	groups = [
		# rifles plt hq
		[
			{ 'role': "Platoon Leader", 'loadout': 'marine_pl', 'callsign': 'RAIDER 1-6', },
			{ 'role': "Platoon Sergeant", 'loadout': 'marine_pl', 'callsign': 'RAIDER 1-7', },
			{ 'role': "Platoon Guide", 'loadout': 'marine_rto', },
			{ 'role': "Corpsmen", 'loadout': 'marine_medic', 'medic': 1},
			{ 'role': "Corpsmen", 'loadout': 'marine_medic', 'medic': 1},			
			{ 'role': "Corpsmen", 'loadout': 'marine_medic', 'medic': 1},			
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
	spawn = 'marines',
	name = 'Wpns Plt.',
	side = 'WEST',
	faction = 'marines',
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
	spawn = 'marines',
	name = 'M1A1 Plt.',
	side = 'WEST',
	faction = 'marines',
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
	spawn = 'cdf',
	name = 'CDF',
	faction = 'cdf',
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
			{ 'role': "Medic", 'loadout': 'cdf_medic', 'medic': 1},
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
			{ 'role': "Medic", 'loadout': 'cdf_medic', 'medic': 1},
			{ 'role': "Grenadier", 'loadout': 'cdf_grenadier' },
			{ 'role': "Asst. Grenadier", 'loadout': 'cdf_grenadier' },
			{ 'role': "Senior Rifleman", 'loadout': 'cdf_rifleman' },
			{ 'role': "Rifleman", 'loadout': 'cdf_rifleman' },
		],		
		
	]
)
teams['tbd'] = dict(
	spawn = 'cdf',
	name = 'tbd',
	side = 'WEST',
	faction = 'cdf',
	groups = [
		[
			{ 'role': "SL / BTR Commander", 'loadout': 'cdf_sl', 'callsign': 'LANCER 1-3'},
			{ 'role': "BTR Driver", 'loadout': 'cdf_crew', },
			{ 'role': "BTR Gunner", 'loadout': 'cdf_asl_gunner', },
			{ 'role': "Machine Gunner", 'loadout': 'cdf_mg', },
			{ 'role': "Medic", 'loadout': 'cdf_medic', 'medic': 1},
			{ 'role': "Grenadier", 'loadout': 'cdf_grenadier' },
			{ 'role': "Asst. Grenadier", 'loadout': 'cdf_grenadier' },
			{ 'role': "Senior Rifleman", 'loadout': 'cdf_rifleman' },
			{ 'role': "Marksman", 'loadout': 'cdf_rifleman' },
		],
	]
)
mish = Reader('KingsHorses.Chernarus_Summer/mission.sqm').read()
top_id = id_count = mish.nextid()
g_count = mish('Mission')('Groups')['items']

fh = open('slots.txt', 'w')

kys = ['pubs','tbd','sasr','company_hq','rifles','weapons','tanks','soar','det5','sfqc']

for team in kys:
	for grp in teams[team]['groups']:
		for unit in grp:
			s =  "%s | %s" % (teams[team]['name'], unit['role'])
			if 'callsign' in unit:
				s += " // %s" % (unit['callsign'])
			fh.write(s+"\n")
		fh.write("\n")

for team in kys:
	for grp in teams[team]['groups']:
		
		g = Klass('Item' + str(g_count))
		g['side'] = teams[team]['side']
		
		v = Klass('Vehicles')
		v_count = 0
		for unit in grp:
			u = Klass('Item' + str(v_count))
			
			spwn = spawns[teams[team]['spawn']]
			if spwn['limit'] == 'x':
				pos = spwn['pos'] + (spwn['unit'] * int(spwn['count']/spwn['max'])) + (spwn['unit'].perp() * int(spwn['count'] % spwn['max']))
			else:
				pos = spwn['pos'] + (spwn['unit'].perp() * int(spwn['count']/spwn['max'])) + (spwn['unit'] * int(spwn['count'] % spwn['max']))
			spwn['count'] += 1
			u['position'] = [pos.x, 0, pos.y]
			u['azimut'] = spwn['azimuth']
			u['id'] = id_count
			u['side'] = teams[team]['side']
			u['vehicle'] = 'sh_faction_%s_unit' % teams[team]['faction']

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

			if 'medic' in unit:
				u['init'] += "[this] call kh_fnc_make_medic;"
			id_count += 1
			v_count += 1
			v['items'] = v_count
			v(u)
		g(v)
		g_count += 1
		mish('Mission')('Groups')['items'] = g_count
		mish('Mission')('Groups')(g)

Writer('KingsHorses.Chernarus_Summer/mission.sqm').write(mish)

