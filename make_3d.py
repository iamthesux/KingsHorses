from p4a.formats.rap import Klass
from p4a.formats.rap.text import Reader, Writer
import os
import settings as cfg

mish2d = Reader(os.path.join(cfg.mish,'mission.sqm')).read()
mish3d = Reader(os.path.join(cfg.mish_3d,'mission.biedi')).read()

parts3d = mish3d.filter(lambda x: x['objectType'] == "vehicle")

if "Vehicles" in mish2d("Mission"):
	c = mish2d("Mission")("Vehicles")["items"]
else:
	mish2d("Mission")(Klass("Vehicles"))
	c = mish2d("Mission")("Vehicles")["items"] = 0
id = mish2d("Mission").nextid()

dic = {}
vics = [
	'B_Quadbike_01_F',
	'B_G_Quadbike_01_F',
	'sh_cdf_uaz',
]
medical = ['US_WarfareBFieldhHospital_Base_EP1','MASH_EP1']

# find zeus
zues_mod = mish2d("Mission")("Groups").filter(lambda x: x('Vehicles') and x('Vehicles')('Item0') and x('Vehicles')('Item0')['vehicle'] == "ModuleCuratorAddEditableObjects")[0]('Vehicles')('Item0')
if 'syncId' not in zues_mod:
	zues_mod['syncId'] = mish2d.nextsid()
	zues_mod['synchronizations'] = []
zues_sid = zues_mod['syncId']
	

base_vic_mod = mish2d("Mission")("Groups").filter(lambda x: x('Vehicles') and x('Vehicles')('Item0') and x('Vehicles')('Item0')['text'] == "kh_mod_base_trans_respawn")[0]('Vehicles')('Item0')
if 'syncId' not in base_vic_mod:
	base_vic_mod['syncId'] = mish2d.nextsid()
	base_vic_mod['synchronizations'] = []
base_vic_id = base_vic_mod['syncId']

print "z %d" % zues_sid
print "bv %d" % base_vic_id


for part in parts3d:
	# if part('Arguments')['TYPE'] not in vics:
		# continue

	k = Klass('Item'+str(c))
	
	pos = eval(part('Arguments')['POSITION'])
	while len(pos) < 3: pos.append(0)

	k['position'] = [pos[0], pos[2], pos[1]]

	if part('Arguments')['AZIMUT']:
		k['azimut'] = float(part('Arguments')['AZIMUT'])

	k['id'] = id
	k['side'] = "EMPTY"
	k['vehicle'] = part('Arguments')['TYPE']
	k['skill'] = 1.0
	if part('Arguments')['NAME']:
		k['text'] = part('Arguments')['NAME']

	if part('Arguments')['INIT']:
		k['init'] = part('Arguments')['INIT']
		if k['init'][-1] != ';': k['init'] += ';'
	else:
		k['init'] = ''
	if k['vehicle'] not in vics:
		k['init'] += "this setPos [%f, %f, %f];" % tuple(pos)
	if k['vehicle'] not in vics and not k['vehicle'].startswith('sh_alive_') and k['vehicle'] not in ['Land_Cargo20_military_green_F','Land_Campfire_F']:
		k['init'] += "[this] call kh_fnc_disable_sim;"
	if k['vehicle'] == 'Land_Cargo20_military_green_F':
		k['init'] += "_nul = [this] execVM 'base_part_box.sqf'"
		
	if k['vehicle'].startswith('sh_alive_'):
		k['init'] += "this setVariable ['R3F_LOG_disabled', true];this allowDamage false;"
		k['syncId'] = mish2d.nextsid()
		k['synchronizations'] = [zues_mod['syncId']]
		zues_mod['synchronizations'].append(k['syncId'])
 
	if k['vehicle'] == 'sh_cdf_uaz':
		k['syncId'] = mish2d.nextsid()
		k['synchronizations'] = [base_vic_mod['syncId']]
		base_vic_mod['synchronizations'].append(k['syncId'])

	if k['vehicle'] in medical:
		k['init'] += 'this setvariable["cse_medical_facility", true];'
		
	# increment our item counter and set the number of items in our Vehicles class
	c+=1
	id+=1
	mish2d("Mission")("Vehicles")(k)
	mish2d("Mission")("Vehicles")["items"] = c
	dic[part('Arguments')['TYPE']] = 1
mish2d("Mission")("Intel")["briefingName"] = "%s v%d" % (cfg.name, cfg.version)
Writer(os.path.join(cfg.mish, 'mission.sqm')).write(mish2d)

for k in dic.keys():
	if k not in vics and k not in medical:
		print k