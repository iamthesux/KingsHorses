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
	'rhsusf_m1a2sep1tuskiwd_usarmy',
	'RHS_M2A3_BUSKIII',
	'B_UAV_02_CAS_F'
]

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
	if k['vehicle'] not in vics:
		k['init'] += "this enableSimulation false; this allowDamage false;"
	
	if part('Arguments')['NAME']:
		k['text'] = part('Arguments')['NAME']
	if part('Arguments')['INIT']:
		k['init'] += part('Arguments')['INIT']

	mish2d("Mission")("Vehicles")(k)
	
	# increment our item counter and set the number of items in our Vehicles class
	c+=1
	id+=1
	mish2d("Mission")("Vehicles")["items"] = c
	dic[part('Arguments')['TYPE']] = 1
mish2d("Mission")("Intel")["briefingName"] = "Kings Horses";
Writer('KingsHorses.Chernarus_Summer/mission.sqm').write(mish2d)

print dic.keys()