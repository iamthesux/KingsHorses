from base import Base

class marine_base(Base):
	class NoWrite: pass

	headgear = 'H_VTN_LWH_WDL'
	
	items = Base.items + [
		'rhsusf_ANPVS_14',
		'tf_rf7800str',
	]

	class Uniform:
		type = 'VTN_U_FROG_WDL'
		items = Base.Uniform.items + [
			['AGM_IR_Strobe_Item', 1],
		]
	class Vest:
		type = 'V_MBAV_RFL'
		items = [
			['rhs_mag_m67', 1],
			['SmokeShell', 1],
		]
	class Backpack:
		type = 'B_Kitbag_mcamo'
		items = [
			['SmokeShell', 1],
			['rhs_mag_m67', 3],
		]

class marine_rifleman(marine_base):
	class Primary:
		weapon = 'RH_M16A4'
		optic = 'RH_ta31rco_2D'
		rail = 'RH_peq15'
		mags = [
			['RH_30Rnd_556x45_M855A1', 30],
		]
	class Vest(marine_base.Vest):
		items = marine_base.Vest.items + [
			['RH_30Rnd_556x45_M855A1', 5],
		]
	class Backpack(marine_base.Backpack):
		items = marine_base.Backpack.items + [
			['RH_30Rnd_556x45_M855A1', 5],
		]


class marine_tl(marine_rifleman):
	class Primary:
		weapon = 'RH_M16A4gl'
		optic = 'RH_ta31rco_2D'
		rail = 'RH_peq15'
		mags = [
			['RH_30Rnd_556x45_M855A1', 30],
			['1Rnd_HE_Grenade_shell', 1],
		]
	class Vest(marine_rifleman.Vest):
		type = 'V_MBAV_GL'

	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['UGL_FlareWhite_F', 2],
			['UGL_FlareRed_F', 1],
			['tf_anprc152', 1],
			['1Rnd_Smoke_Grenade_shell', 4],
			['1Rnd_SmokeRed_Grenade_shell', 2],
			['1Rnd_SmokeGreen_Grenade_shell', 2],
			['1Rnd_HE_Grenade_shell', 10],
		]

class marine_sl(marine_tl):
	binoc = 'Binocular'
	class Primary:
		weapon = 'RH_M4_ris_M203'
		optic = 'RH_ta31rco_2D'
		rail = 'RH_peq15'
		mags = [
			['RH_30Rnd_556x45_M855A1', 30],
			['1Rnd_HE_Grenade_shell', 1],
		]
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]

class marine_ar(marine_base):
	class Primary:
		weapon = 'rhs_weap_m249_pip'
		optic = 'RH_ta31rco_2D'
		rail = 'RH_peq15'
		mags = [
			['rhsusf_100Rnd_556x45_soft_pouch', 100],
		]
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Vest(marine_base.Vest):
		type = 'V_MTV_MG'

	class Backpack(marine_base.Backpack):
		items = marine_base.Backpack.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 5],
		]

class marine_aar(marine_rifleman):
	class Vest(marine_rifleman.Vest):
		type = 'V_MTV_MG'

	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 5],
		]

class marine_mg(marine_base):
	class Primary:
		weapon = 'rhs_weap_m240B'
		optic = 'RH_ta31rco_2D'
		rail = 'RH_peq15'
		mags = [
			['rhsusf_100Rnd_762x51', 100],
		]
	class Vest(marine_base.Vest):
		type = 'V_MTV_MG'

	class Backpack(marine_base.Backpack):
		items = marine_base.Backpack.items + [
			['rhsusf_100Rnd_762x51', 5],
		]

class marine_amg(marine_rifleman):
	class Vest(marine_rifleman.Vest):
		type = 'V_MTV_MG'

	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['rhsusf_100Rnd_762x51', 5],
			['tf_anprc152', 1],
		]

class marine_at(marine_rifleman):
	class Secondary:
		weapon = 'CUP_launch_Mk153Mod0'
		mags = [
			['CUP_SMAW_HEAA_M', 1],
		]

	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['tf_anprc152', 1],
			['CUP_SMAW_HEAA_M', 1],
			['CUP_SMAW_HEDP_M', 1],
			['CUP_optic_SMAW_Scope', 1],
		]

class marine_aat(marine_rifleman):
	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['CUP_SMAW_HEDP_M', 1],
			['CUP_SMAW_HEAA_M', 1],
		]

class marine_pl(marine_base):
	binoc = 'AGM_Vector'
	class Primary:
		weapon = 'RH_M4_ris'
		optic = 'RH_ta31rco_2D'
		rail = 'RH_peq15'
		mags = [
			['RH_30Rnd_556x45_M855A1', 30],
			['1Rnd_HE_Grenade_shell', 1],
		]
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Vest(marine_base.Vest):
		items = marine_base.Vest.items + [
			['RH_30Rnd_556x45_M855A1', 5],
		]
	class Backpack(marine_base.Backpack):
		items = marine_base.Backpack.items + [
			['RH_30Rnd_556x45_M855A1', 5],
			['tf_anprc152', 2],
			['alive_tablet', 1],
			['1Rnd_HE_Grenade_shell', 5],
		]
	
class marine_rto(marine_rifleman):
	binoc = 'Binocular'
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
			['cse_bandage_basic', 10],
			['cse_packing_bandage', 10],
			['cse_tourniquet', 2],
			['cse_morphine', 2],
			['cse_epinephrine', 2],
			['cse_saline_iv_250', 2],
			['cse_quikclot', 10],
			['cse_nasopharyngeal_tube', 2],
			['cse_personal_aid_kit', 1],
		]

class marine_crewman(marine_rifleman):
	headgear = 'rhsusf_cvc_green_helmet'
		
class marine_commander(marine_crewman):
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Backpack(marine_base.Backpack):
		items = marine_crewman.Backpack.items + [
			['tf_anprc152', 2],
		]

		