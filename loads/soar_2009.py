from p4a.loadout import Crate
from base import Base

class soar_pilot(Base):
	headgear = 'rhs_gssh18'
	items = Base.items + [
		'ItemGPS',
		'tf_fadak'
	]

	class Primary:
		weapon = 'rhs_weap_akms'
		mags = [['rhs_30Rnd_762x39mm_tracer', 30],]

	class HandGun:
		weapon = 'RH_mak'
		rail = 'RH_pmIR'
		mags = [['RH_8Rnd_9x18_Mak', 8]]

	class Uniform:
		type = 'VTN_VVS_VKK15'
		items = Base.Uniform.items + [
			['cw_item_9liner_medivac', 1],
			['cw_item_9liner_cas', 1],
			['cw_item_5liner_gcff', 1],
			['cw_item_cas_check_in_breef', 1],
			['rhs_30Rnd_762x39mm_tracer', 2],
			['RH_8Rnd_9x18_Mak', 2],
		]
	class Vest:
		type = 'rhs_vest_commander'
		items = [
			['rhs_mag_nspn_green', 2],
			['tf_fadak', 1],
		]
	class Backpack:
		type = 'tf_anprc155'
		items = [
			['rhsusf_ANPVS_15', 1],
			['ToolKit', 1],
		]

class soar_crew(soar_pilot):
	pass

