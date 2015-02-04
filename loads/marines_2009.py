from base import Base

class marine_base(Base):
	headgear = 'H_VTN_LWH_WDL'
	
	items = Base.items + [
		'rhsusf_ANPVS_15',
		'tf_rf7800str',
	]
	class HandGun:
		weapon = 'CUP_hgun_M9'
		mags = [['CUP_15Rnd_9x19_M9', 15]]

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
		weapon = 'rhs_weap_m16a4_carryhandle'
		optic = 'RH_ta31rco_2D'
		rail = 'rhsusf_acc_ACOG3'
		mags = [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag', 30],
		]
	class Vest(marine_base.Vest):
		items = marine_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag', 5],
		]
	class Backpack(marine_base.Backpack):
		items = marine_base.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag', 5],
		]


class marine_tl(marine_rifleman):
	items = Base.items + [
		'tf_anprc152',
	]
	class Primary:
		weapon = 'RH_M16A4gl'
		optic = 'RH_ta31rco_2D'
		rail = 'rhsusf_acc_anpeq15A'
		mags = [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag', 30],
			['1Rnd_HE_Grenade_shell', 1],
		]
	class Vest(marine_rifleman.Vest):
		type = 'V_MBAV_GL'

	class Backpack(marine_rifleman.Backpack):
		items = marine_rifleman.Backpack.items + [
			['UGL_FlareWhite_F', 2],
			['UGL_FlareRed_F', 1],
			['1Rnd_Smoke_Grenade_shell', 4],
			['1Rnd_SmokeRed_Grenade_shell', 2],
			['1Rnd_SmokeGreen_Grenade_shell', 2],
			['1Rnd_HE_Grenade_shell', 10],
		]

class marine_sl(marine_tl):
	class Primary:
		weapon = 'RH_M16A4gl'
		optic = 'RH_ta31rco_2D'
		rail = 'rhsusf_acc_anpeq15A'
		mags = [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag', 30],
			['1Rnd_HE_Grenade_shell', 1],
		]

class marine_ar(marine_base):
	class Primary:
		weapon = 'rhs_weap_m249_pip'
		optic = 'rhsusf_acc_ACOG2'
		rail = 'rhsusf_acc_anpeq15A'
		mags = [
			['rhsusf_100Rnd_556x45_soft_pouch', 100],
		]
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
