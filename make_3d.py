from p4a.formats.rap import Klass
from p4a.formats.rap.text import Reader, Writer

mish2d = Reader('KingsHorses.Chernarus_Summer/mission.sqm').read()
mish3d = Reader('kingshorses_3dbase.chernarus_Summer/mission.biedi').read()

parts3d = mish3d.filter(lambda x: x['objectType'] == "vehicle")

if "Vehicles" in mish2d("Mission"):
	c = mish2d("Mission")("Vehicles")["items"]
else:
	mish2d("Mission")(Klass("Vehicles"))
	c = mish2d("Mission")("Vehicles")["items"] = 0
id = mish2d("Mission").nextid()

dic = {}

vics = [
	'rhsusf_m1025_w_s_m2',
	'rhsusf_m1025_w_s_Mk19',
	'RHS_AH64D',
	'RHS_CH_47F',
	'RHS_UH60M_d',
	'rhsusf_m1a1fep_wd',
	'B_Heli_Light_01_armed_F',
	'RHS_Ural_Fuel_VMF_01',
	'rhs_gaz66o_msv',
	'rhs_gaz66_ammo_vmf',
	'ffaa_et_rg31_samson',
	'B_UAV_02_CAS_F',
	'RHS_UAZ_MSV_01',
	'B_Quadbike_01_F',
	'rhs_gaz66_repair_vdv',
	'rhs_gaz66_repair_msv'
]
medical = ['US_WarfareBFieldhHospital_Base_EP1','MASH_EP1']
for part in parts3d:
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
	k['init'] = "this setPos [%f, %f, %f];" % tuple(pos)
	if k['vehicle'] not in vics and not k['vehicle'].startswith('sh_alive_'):
		k['init'] += "[this] call kh_fnc_disable_sim;"
	
	if part('Arguments')['NAME']:
		k['text'] = part('Arguments')['NAME']
	if part('Arguments')['INIT']:
		k['init'] += part('Arguments')['INIT']
	if k['vehicle'] in medical:
		k['init'] += 'this setvariable["cse_medical_facility", true];'
	mish2d("Mission")("Vehicles")(k)
	
	# increment our item counter and set the number of items in our Vehicles class
	c+=1
	id+=1
	mish2d("Mission")("Vehicles")["items"] = c
	dic[part('Arguments')['TYPE']] = 1
mish2d("Mission")("Intel")["briefingName"] = "Kings Horses";
Writer('KingsHorses.Chernarus_Summer/mission.sqm').write(mish2d)

for k in dic.keys():
	if k not in vics and k not in medical:
		print k