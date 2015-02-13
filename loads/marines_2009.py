from base import Base

class marine_base(Base):
	class NoWrite: pass

	headgear = 'H_VTN_LWH_WDL'
	
	items = Base.items + [
		'rhsusf_ANPVS_14',
		'tf_rf7800str',
	]
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]

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
			['SmokeShell', 1],
			['rhs_mag_m67', 1],
		]

class marine_rifleman(marine_base):
	class Primary:
		weapon = 'rhs_weap_m16a4_carryhandle_pmag'
		optic = 'rhsusf_acc_ACOG2'
		rail = 'rhsusf_acc_anpeq15'
		mags = [
			['RH_30Rnd_556x45_M855A1', 30],
		]
	class Vest(marine_base.Vest):
		items = marine_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag', 8],
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 2],
		]
	class Backpack(marine_base.Backpack):
		items = marine_base.Backpack.items + [
			['VTN_M83W', 2],
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
	class Vest(marine_base.Vest):
		items = marine_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag', 5],
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 1],
			['1Rnd_HE_Grenade_shell', 6],
			['1Rnd_Smoke_Grenade_shell', 2],
		]

	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['1Rnd_HE_Grenade_shell', 6],
			['VTN_M18R', 1],
			['VTN_M16P', 1]
			['UGL_FlareCIR_F', 1],
			['UGL_FlareRed_F', 1],
			['tf_anprc152', 1],
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

class marine_ar(marine_base):
	class Primary:
		weapon = 'rhs_weap_m249_pip'
		optic = 'RH_ta31rco_2D'
		rail = 'RH_peq15'
		mags = [
			['rhsusf_100Rnd_556x45_soft_pouch', 100],
		]
	class Vest(marine_base.Vest):
		type = 'V_SPC_MG'

	class Backpack(marine_base.Backpack):
		items = marine_base.Backpack.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 5],
		]

class marine_aar(marine_rifleman):
	class Vest(marine_rifleman.Vest):
		type = 'V_SPC_RFL'

	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 5],
		]

class marine_mg(marine_base):
	class Primary:
		weapon = 'rhs_weap_m240B'
		optic = 'RH_ta648'
		rail = 'RH_peq15'
		mags = [
			['rhsusf_100Rnd_762x51', 100],
		]
	class Vest(marine_base.Vest):
		type = 'V_SPC_MG'

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
		type = 'tf_anprc155_coyote'
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
	headgear = 'rhsusf_cvc_green_helmet'
		
class marine_commander(marine_crewman):
	class Backpack(marine_base.Backpack):
		items = marine_crewman.Backpack.items + [
			['tf_anprc152', 2],
		]

		