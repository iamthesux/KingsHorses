import base

class marine_base(base.Base):
	class NoWrite: pass
	headgear = 'rhsusf_mich_helmet_marpatwd'

	class Primary:
		optic = 'rhsusf_acc_ACOG_USMC'
		rail = 'rhsusf_acc_anpeq15'
	
	class Uniform:
		type = 'rhs_uniform_FROG01_wd'
		items = base.Base.Uniform.items + [
		]
	class Vest:
		type = 'rhsusf_spc'
		items = [
			['rhs_mag_m67', 1],
			['rhs_mag_an_m8hc', 1],
		]
	class Backpack:
		type = 'rhsusf_assault_eagleaiii_coy'
		items = [
			['rhsusf_ANPVS_14', 1],
			['rhs_mag_m67', 1],
			['rhs_mag_an_m8hc', 1],
		]

class marine_rifleman(marine_base):
	class Primary(marine_base.Primary):
		weapon = 'rhs_weap_m16a4_carryhandle'
		mags = [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_No_Tracer', 30],
		]
	class Vest(marine_base.Vest):
		items = marine_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_No_Tracer', 2],
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 2],
		]
	class Backpack(marine_base.Backpack):
		items = marine_base.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_No_Tracer', 2],
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 2],
		]

class marine_tl(marine_rifleman):
	binoc = 'Binocular'
	items = marine_rifleman.items + ['tf_rf7800str']
	class Primary(marine_base.Primary):
		weapon = 'RH_M16A4gl'
		mags = [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_No_Tracer', 30],
			['rhs_mag_M433_HEDP', 1],
		]
	class Uniform(marine_base.Uniform):
		items = marine_base.Uniform.items + [
			['cw_item_9liner_medivac', 1],
			['cw_item_9liner_cas', 1],
			['cw_item_5liner_gcff', 1],
		]
	class Vest(marine_base.Vest):
		items = marine_base.Vest.items + [
			['rhs_mag_M433_HEDP', 3],
			['rhs_mag_M714_white', 3],
		]

	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 5],
			['rhs_mag_M433_HEDP', 8],
			['rhs_mag_M714_white', 6],
			['rhs_mag_M713_red', 2],
			['rhs_mag_M585_white', 2],
		]

class marine_sl(marine_tl):
	binoc = 'Binocular'
	class Backpack(marine_tl.Backpack):
		items = marine_tl.Backpack.items + [
			['tf_anprc152', 1],
		]
	class Primary(marine_tl.Primary):
		weapon = 'RH_M4A1_ris_M203'
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(marine_base.Uniform):
		items = marine_base.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

class marine_ar(marine_base):
	class Primary(marine_base.Primary):
		weapon = 'rhs_weap_m249_pip'
		mags = [
			['rhsusf_100Rnd_556x45_soft_pouch', 100],
		]

	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(marine_base.Uniform):
		items = marine_base.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

	class Vest(marine_base.Vest):
		items = marine_base.Vest.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 2],
		]
	class Backpack(marine_base.Backpack):
		items = marine_base.Backpack.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 3],
		]

class marine_aar(marine_rifleman):
	binoc = 'Binocular'
	class Vest(marine_base.Vest):
		items = marine_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 5],
		]
	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 3],
			['rhsusf_200Rnd_556x45_soft_pouch', 2],
		]

class marine_mg(marine_base):
	class Primary(marine_base):
		weapon = 'rhs_weap_m240B'
		optic = 'RH_ta648'
		mags = [['rhsusf_100Rnd_762x51', 100]]
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(marine_base.Uniform):
		items = marine_base.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

	class Vest(marine_base.Vest):
		items = marine_base.Vest.items + [
			['rhsusf_100Rnd_762x51', 2],
		]

	class Backpack(marine_base.Backpack):
		items = marine_base.Backpack.items + [
			['rhsusf_100Rnd_762x51', 2],
		]

class marine_amg(marine_rifleman):
	items = marine_rifleman.items + ['tf_rf7800str']
	binoc = 'Binocular'
	class Vest(marine_base.Vest):
		items = marine_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 6],
		]
	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 2],
			['rhsusf_100Rnd_762x51', 3],
		]

class marine_at(marine_rifleman):
	class Secondary:
		weapon = 'rhs_weap_fgm148'
		mags = [
			['rhs_fgm148_magazine_AT', 1],
		]

	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['rhs_fgm148_magazine_AT', 1],
		]

class marine_aat(marine_rifleman):
	items = marine_rifleman.items + ['tf_rf7800str']
	binoc = 'AGM_Vector'
	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['rhs_fgm148_magazine_AT', 2],
		]

class marine_pl(marine_rifleman):
	items = marine_rifleman.items + ['tf_rf7800str']
	binoc = 'AGM_Vector'

	class Primary(marine_tl.Primary):
		weapon = 'rhs_weap_m4a1'
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(marine_base.Uniform):
		items = marine_base.Uniform.items + [
			['RH_15Rnd_9x19_M9', 2],
			['cw_item_9liner_medivac', 1],
			['cw_item_9liner_cas', 1],
			['cw_item_5liner_gcff', 1],
		]

	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['tf_anprc152', 2],
			['alive_tablet', 1],
		]
	
class marine_rto(marine_rifleman):
	items = marine_rifleman.items + ['tf_rf7800str']
	binoc = 'Binocular'
	class Backpack(marine_rifleman.Backpack):
		type = "tf_rt1523g_big"
		items = marine_rifleman.Backpack.items + [
			['alive_tablet', 1],
			['tf_anprc152', 2],
		]

class marine_corpsman(marine_rifleman):
	items = marine_rifleman.items + ['tf_rf7800str']
	class Backpack(marine_base.Backpack):
		items = marine_base.Backpack.items + base.MedicSupplies + [
			['tf_anprc152', 1],
		]

class marine_crewman(marine_rifleman):
	items = marine_rifleman.items + ['tf_rf7800str']
	headgear = 'rhsusf_cvc_green_helmet'

class marine_commander(marine_rifleman):
	items = marine_rifleman.items + ['tf_rf7800str']
	headgear = 'rhsusf_cvc_green_ess'
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(marine_base.Uniform):
		items = marine_rifleman.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

	class Backpack:		
		items = marine_crewman.Backpack.items + [
			['tf_anprc152', 2],
		]