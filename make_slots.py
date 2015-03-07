from p4a.formats.rap.text import Reader, Writer
from p4a.formats.rap import Klass
from copy import deepcopy
import math, os
import settings as cfg

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
		pos = Vector(5157,2370),
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
	name = '5th Spetsnaz',
	faction = 'det5',
	side = 'WEST',
	groups = [
		[
			{ 'role': "MAJ Singleton", 'loadout': 'officer_det5', 'medic': 1, 'callsign': 'SPEARHEAD',},
			{ 'role': "SGM Dodds", 'loadout': 'sniper_det5', 'medic': 1, },
			{ 'role': "CPT Moore", 'loadout': 'officer_det5', 'medic': 1, },
			{ 'role': "CW4 Pierce", 'loadout': 'officer_det5', 'medic': 1, },
			{ 'role': "MSG Nichols", 'loadout': 'rifleman_det5', 'medic': 1, },
			{ 'role': "SFC Furlong", 'loadout': 'sniper_det5', 'medic': 1, },
			{ 'role': "SFC Cannon", 'loadout': 'gunner_det5', 'medic': 1, },
			{ 'role': "SFC Bryhni", 'loadout': 'gunner_det5', 'medic': 1, },
			{ 'role': "SFC Cline", 'loadout': 'demolitions_det5', 'medic': 1, },
			{ 'role': "SFC Lee", 'loadout': 'medic_det5', 'medic': 1},
			{ 'role': "SSG Andresen", 'loadout': 'medic_det5', 'medic': 1},
			{ 'role': "SFC Sage", 'loadout': 'commo_det5', 'medic': 1, },
		],
	],
)
teams['sfqc'] = dict(
	spawn = 'det5',
	name = 'SOT-A',
	faction = 'det5',
	side = 'WEST',
	groups = [
		[
			{ 'role': "SGT Smith", 'loadout': 'rifleman_det5', 'medic': 1, },
			{ 'role': "SGT Bayley", 'loadout': 'commo_det5', 'medic': 1, },
			{ 'role': "SGT Griffin", 'loadout': 'medic_det5', 'medic': 1, },
		]
	],
)
teams['sasr'] = dict(
	spawn = 'sasr',
	name = 'CDF Recon',
	faction = 'sasr',
	side = 'WEST',
	groups = [
		[
			{ 'role': "MAJ Pursehouse", 'loadout': 'cdf_recce_rto', 'callsign': 'SNAKEYES',},
			{ 'role': "CPT Constanti", 'loadout': 'cdf_recce_medic', 'medic': 1, },
			{ 'role': "SSGT MacDowell", 'loadout': 'cdf_recce_tl', },
			{ 'role': "CPL Sowers", 'loadout': 'cdf_recce_lmg', },
			{ 'role': "CPL Deckert", 'loadout': 'cdf_recce_svd', },
		],
	],
)

teams['soar'] = dict(
	spawn = 'cdn',
	name = 'CDFAF',
	side = 'WEST',
	faction = 'cdn',
	groups = [
		[
			{ 'role': "Pilot", 'loadout': 'soar_pilot', 'callsign': 'JESTER',},
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
	name = 'A CO',
	side = 'WEST',
	faction = 'marines',
	groups = [
		[
			{ 'role': "Company Commander", 'loadout': 'marine_pl', 'callsign': 'IRONMAN 6', },
			{ 'role': "Executive Officer", 'loadout': 'marine_pl', 'callsign': 'IRONMAN 7', },
			{ 'role': "First Sergeant", 'loadout': 'marine_pl', },
			{ 'role': "Gunnery Sergeant", 'loadout': 'marine_pl', },
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
			{ 'role': "Platoon Leader", 'loadout': 'marine_pl', 'callsign': 'IRONMAN 1-6', },
			{ 'role': "Platoon Sergeant", 'loadout': 'marine_pl', 'callsign': 'IRONMAN 1-7', },
			{ 'role': "Platoon Guide", 'loadout': 'marine_rto', },
			{ 'role': "Corpsmen", 'loadout': 'marine_corpsman', 'medic': 1},
			{ 'role': "Corpsmen", 'loadout': 'marine_corpsman', 'medic': 1},			
		],
		# rifles squad 1
	],
)

for i in range(1,4):
	teams['rifles']['groups'].append([
		{ 'role': "Squad Leader", 'loadout': 'marine_sl', 'callsign': 'IRONMAN 1-%d' % i },
		
		{ 'role': "Team Leader", 'loadout': 'marine_tl', 'callsign': 'IRONMAN 1-%d-A' % i },
		{ 'role': "Automatic Rifleman", 'loadout': 'marine_ar' },
		{ 'role': "Assistant AR", 'loadout': 'marine_aar' },
		{ 'role': "Rifleman", 'loadout': 'marine_rifleman' },
		
		{ 'role': "Team Leader", 'loadout': 'marine_tl', 'callsign': 'IRONMAN 1-%d-B' % i },
		{ 'role': "Automatic Rifleman", 'loadout': 'marine_ar' },
		{ 'role': "Assistant AR", 'loadout': 'marine_aar' },
		{ 'role': "Rifleman", 'loadout': 'marine_rifleman' },
		
		{ 'role': "Team Leader", 'loadout': 'marine_tl', 'callsign': 'IRONMAN 1-%d-C' % i },
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
			{ 'role': "Platoon Leader", 'loadout': 'marine_pl', 'callsign': 'IRONMAN 4-6', },
			{ 'role': "Platoon Sergeant", 'loadout': 'marine_pl', 'callsign': 'IRONMAN 4-7', },
			{ 'role': "Corpsmen", 'loadout': 'marine_corpsman', 'medic': 1},
			{ 'role': "Corpsmen", 'loadout': 'marine_corpsman', 'medic': 1},
		],
	],
)
teams['weapons']['groups'].append([
	{ 'role': "MG Section Leader", 'loadout': 'marine_sl', 'callsign': 'IRONMAN 4-%d' % i, },
])
for i in range(1,4):
	teams['weapons']['groups'].append([
		{ 'role': "MG Squad Leader", 'loadout': 'marine_sl', 'callsign': 'IRONMAN 4-%d' % i, },
		
		{ 'role': "Assistant Gunner", 'loadout': 'marine_amg', 'callsign': 'IRONMAN 4-%d-G' % i },
		{ 'role': "Gunner", 'loadout': 'marine_mg' },
		{ 'role': "Ammuntion Bearer", 'loadout': 'marine_amg' },
		{ 'role': "Assistant Gunner", 'loadout': 'marine_amg', 'callsign': 'IRONMAN 4-%d-H' % i },
		{ 'role': "Gunner", 'loadout': 'marine_mg' },
		{ 'role': "Ammuntion Bearer", 'loadout': 'marine_amg' },
	])
teams['weapons']['groups'].append([
	{ 'role': "MG Section Leader", 'loadout': 'marine_sl', 'callsign': 'IRONMAN 4-%d' % i, },
])
for i in range(1,4):
	teams['weapons']['groups'].append([
		{ 'role': "Squad Leader/Gunner", 'loadout': 'marine_at_sl', 'callsign': 'IRONMAN 4-%d' % i, },
		{ 'role': "Assistant Gunner", 'loadout': 'marine_aat' },
		{ 'role': "Team Leader/Gunner", 'loadout': 'marine_at', 'callsign': 'IRONMAN 4-%d-G' % i },
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
			{ 'role': "Platoon Leader", 'loadout': 'cdf_pl', 'callsign': 'HOMELAND 1-6', },
			{ 'role': "Assistant Platoon Leader", 'loadout': 'cdf_rto', 'callsign': 'HOMELAND 1-7', },
		],
		[
			{ 'name': '3ACR', 'role': "SL / BMP-1 Commander", 'loadout': 'cdf_asl_gunner', 'callsign': 'THUNDER 1-1'},
			{ 'name': '3ACR', 'role': "BMP-1 Driver", 'loadout': 'cdf_crew', },
			{ 'name': '3ACR', 'role': "BMP-1 Gunner", 'loadout': 'cdf_asl_gunner', },
			{ 'role': "Senior Rifleman", 'loadout': 'cdf_tl', 'callsign': 'HOMELAND 1-1'},
			{ 'role': "Machine Gunner", 'loadout': 'cdf_mg', },
			{ 'role': "Medic", 'loadout': 'cdf_medic', 'medic': 1},
			{ 'role': "Grenadier", 'loadout': 'cdf_grenadier' },
			{ 'role': "Asst. Grenadier", 'loadout': 'cdf_grenadier' },
			{ 'role': "Rifleman", 'loadout': 'cdf_rifleman' },
		],
		[
			{ 'name': '3ACR', 'role': "SL / BMP-1 Commander", 'loadout': 'cdf_asl_gunner', 'callsign': 'THUNDER 1-2'},
			{ 'name': '3ACR', 'role': "BMP-1 Driver", 'loadout': 'cdf_crew', },
			{ 'name': '3ACR', 'role': "BMP-1 Gunner", 'loadout': 'cdf_asl_gunner', },
			{ 'role': "Senior Rifleman", 'loadout': 'cdf_tl', 'callsign': 'HOMELAND 1-2'},
			{ 'role': "Machine Gunner", 'loadout': 'cdf_mg', },
			{ 'role': "Medic", 'loadout': 'cdf_medic', 'medic': 1},
			{ 'role': "Grenadier", 'loadout': 'cdf_grenadier' },
			{ 'role': "Asst. Grenadier", 'loadout': 'cdf_grenadier' },
			{ 'role': "Rifleman", 'loadout': 'cdf_rifleman' },
		],
		[
			{ 'name': '3ACR', 'role': "SL / BMP-1 Commander", 'loadout': 'cdf_asl_gunner', 'callsign': 'THUNDER 1-3'},
			{ 'name': '3ACR', 'role': "BMP-1 Driver", 'loadout': 'cdf_crew', },
			{ 'name': '3ACR', 'role': "BMP-1 Gunner", 'loadout': 'cdf_asl_gunner', },
			{ 'role': "Senior Rifleman", 'loadout': 'cdf_tl', 'callsign': 'HOMELAND 1-3'},
			{ 'role': "Machine Gunner", 'loadout': 'cdf_mg', },
			{ 'role': "Medic", 'loadout': 'cdf_medic', 'medic': 1},
			{ 'role': "Grenadier", 'loadout': 'cdf_grenadier' },
			{ 'role': "Asst. Grenadier", 'loadout': 'cdf_grenadier' },
			{ 'role': "Rifleman", 'loadout': 'cdf_rifleman' },
		],
		[
			{ 'name': '3ACR', 'role': "T-72 Commander", 'loadout': 'cdf_asl_gunner', 'callsign': 'THUNDER 1-3' },
			{ 'name': '3ACR', 'role': "Driver", 'loadout': 'cdf_crew' },
			{ 'name': '3ACR', 'role': "Gunner", 'loadout': 'cdf_crew' },
		],	
	]
)

mish = Reader('KingsHorses.Chernarus_Summer/mission.sqm').read()
top_id = id_count = mish.nextid()
g_count = mish('Mission')('Groups')['items']

fh = open('slots.txt', 'w')

kys = ['pubs','sasr','company_hq','rifles','weapons','tanks','soar','det5','sfqc']

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
			t = teams[team]['name']
			if 'name' in unit:
				t = unit['name']
			u['description'] = "%s // %s" % (t, unit['role'])
			if 'callsign' in unit:
				u['description'] += " // %s" % (unit['callsign'])

			#u['init'] = "this setVariable ['sux_loadout', '%s'];" % unit['loadout']
			u['init'] = '[this, "%s"] call suxlo_fnc_init_loadout;' % unit['loadout']

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

Writer(os.path.join(cfg.mish,'mission.sqm')).write(mish)

