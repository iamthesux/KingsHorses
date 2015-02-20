from base import Base

class marine_base(Base):
	class NoWrite: pass
	headgear = 'H_VTN_LWH_WDL'
	items = Base.items + [
		'tf_rf7800str',
	]

	class Primary:
		optic = 'VTN_OPTIC_TA_31RCO_USMC'
		rail = 'VTN_TPIAL_ANPEQ15_B'
	
	class Uniform:
		type = 'VTN_U_FROG_WDL'
		items = Base.Uniform.items + [
			['AGM_IR_Strobe_Item', 1],
		]
	class Vest:
		type = 'V_SPC_RFL'
		items = [
			['rhs_mag_m67', 2],
		]
	class Backpack:
		type = 'B_VTN_ILBE'
		items = [
			['rhsusf_ANPVS_14', 1],
			['rhs_mag_m67', 1],
		]

class marine_rifleman(marine_base):
	class Primary(marine_base.Primary):
		weapon = 'VTN_FN_M16A4'
		mags = [
			['VTN_STANAG4172_30p_SC', 30],
		]
	class Vest(marine_base.Vest):
		items = marine_base.Vest.items + [
			['VTN_STANAG4172_30p_SC', 8],
			['VTN_STANAG4172_30p_TRC', 2],
		]
	class Backpack(marine_base.Backpack):
		items = marine_base.Backpack.items + [
			['VTN_M83W', 2],
		]


class marine_tl(marine_rifleman):
	items = Base.items + [
		'ItemGPS',
	]
	class Primary(marine_base.Primary):
		weapon = 'VTN_FN_M16A4_M203'
		mags = [
			['VTN_STANAG4172_30p_SC', 30],
			['VTN_M406', 1],
		]
	class Vest:
		type = "V_SPC_GL"
		items = marine_base.Vest.items + [
			['VTN_M406', 4],
			['VTN_M713', 2],
			['VTN_M18R', 1],
			['VTN_M16P', 1],
		]

	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['VTN_STANAG4172_30p_TRC', 5],
			['VTN_M406', 8],
			['VTN_M992', 1],
			['VTN_M662', 1],
			['VTN_M583A1', 1],
			['tf_anprc152', 1],
		]

class marine_sl(marine_tl):
	binoc = 'VTN_M24'
	items = Base.items + [
		'ItemGPS',
	]
	class Primary(marine_tl.Primary):
		weapon = 'VTN_C_M4A1_M203'
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(marine_base.Uniform):
		items = marine_base.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

class marine_ar(marine_base):
	class Primary(marine_base.Primary):
		weapon = 'VTN_M249_PARA'
		mags = [
			['VTN_M249_100c_SC', 100],
		]

	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(marine_base.Uniform):
		items = marine_base.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

	class Vest:
		type = 'V_SPC_MG'
		items = marine_base.Vest.items + [
			['VTN_M249_200c_SC', 1],
			['VTN_M249_200c_TRC', 1],
		]
	class Backpack(marine_base.Backpack):
		items = marine_base.Backpack.items + [
			['VTN_M249_200c_SC', 2],
			['VTN_M249_200c_TRC', 2],
		]

class marine_aar(marine_rifleman):
	binoc = 'VTN_M24'
	class Vest:
		type = 'V_SPC_MG'
		items = marine_base.Vest.items + [
			['VTN_STANAG4172_30p_TRC', 5],
			['VTN_M249_100c_SC', 1],
			['VTN_M249_100c_TRC', 1],
		]
	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['VTN_STANAG4172_30p_SC', 3],
			['VTN_M249_200c_TRC', 2],
		]

class marine_mg(marine_base):
	class Primary(marine_base):
		weapon = 'VTN_M240G'
		mags = [['VTN_M240_50c_TRC', 50]]

	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(marine_base.Uniform):
		items = marine_base.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

	class Vest:
		type = 'V_SPC_MG'
		items = marine_base.Vest.items + [
			['VTN_M240_100c_SC', 1],
			['VTN_M240_100c_TRC', 1],
		]

	class Backpack(marine_base.Backpack):
		items = marine_base.Backpack.items + [
			['VTN_M240_100c_SC', 1],
		]

class marine_amg(marine_rifleman):
	binoc = 'AGM_Vector'
	class Vest:
		type = 'V_MTV_MG'
		items = marine_base.Vest.items + [
			['VTN_STANAG4172_30p_TRC', 5],
			['VTN_M240_100c_SC', 1],
		]
	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['VTN_STANAG4172_30p_SC', 3],
			['VTN_M240_100c_SC', 1],
			['VTN_M240_100c_TRC', 1],
			['tf_anprc152', 1],
		]

class marine_at(marine_rifleman):
	class Secondary:
		weapon = 'VTN_MK153MOD0'
		rail = 'VTN_TPIAL_ANPEQ15_D'
		optic = 'VTN_OPTIC_TA_31F'
		mags = [
			['VTN_MK6MOD0', 1],
		]

	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['tf_anprc152', 1],
			['VTN_MK6MOD0', 1],
		]

class marine_aat(marine_rifleman):
	binoc = 'AGM_Vector'
	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['VTN_MK3MOD0', 1],
		]

class marine_pl(marine_rifleman):
	binoc = 'AGM_Vector'

	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(marine_base.Uniform):
		items = marine_base.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

	class Backpack(marine_rifleman.Backpack):
		type = 'tf_rt1523g_green'
		items = marine_rifleman.Backpack.items + [
			['tf_anprc152', 2],
			['alive_tablet', 1],
		]
	
class marine_rto(marine_rifleman):
	binoc = 'VTN_M24'
	class Backpack:
		type = 'tf_rt1523g_green'
		items = marine_rifleman.Backpack.items + [
			['alive_tablet', 1],
			['tf_anprc152', 5],
		]

class marine_corpsman(marine_rifleman):
	class Backpack(marine_base.Backpack):
		items = marine_base.Backpack.items + [
			['tf_anprc152', 1],
			['cse_bandage_basic', 16],
			['cse_packing_bandage', 16],
			['cse_tourniquet', 8],
			['cse_morphine', 4],
			['cse_epinephrine', 4],
			['cse_saline_iv_250', 4],
			['cse_quikclot', 16],
			['cse_nasopharyngeal_tube', 4],
			['cse_personal_aid_kit', 2],
		]

class marine_crewman(marine_rifleman):
	headgear = 'H_VTN_DH132A'
		
class marine_commander(marine_crewman):
	items = Base.items + [
		'ItemGPS',
	]
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(marine_base.Uniform):
		items = marine_base.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

	class Backpack:		
		items = marine_crewman.Backpack.items + [
			['tf_anprc152', 2],
		]		