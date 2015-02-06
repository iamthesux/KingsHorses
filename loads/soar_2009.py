from base import Base

class soar_base(Base):
	headgear = 'rhsusf_hgu56p'
	
	items = Base.items + [
		'tf_anprc152_2',
		'rhsusf_ANPVS_15',
	]
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]

	class Uniform:
		type = 'U_mas_usn_B_CombatUniform_mcam'
		items = Base.Uniform.items + [
			['AGM_IR_Strobe_Item', 1],
		]
	class Vest:
		type = 'AV_PlateCarrier2_OCP'
		items = [
			['SmokeShellBlue', 1],
			['SmokeShell', 1],
			['SmokeShellGreen', 1],
			['tf_anprc152_2', 1],
		]
	class Backpack:
		type = 'tf_anarc210'
		items = [
			['SmokeShell', 1],
		]

class soar_pilot(soar_base):
	class Primary:
		weapon = 'RH_M4_ris'
		optic = 'RH_compM2l'
		rail = 'RH_peq15b'
		mags = [
			['30Rnd_556x45_Stanag', 30],
		]
	class Vest(soar_base.Vest):
		items = soar_base.Vest.items + [
			['30Rnd_556x45_Stanag', 4],
		]

class soar_crew(soar_pilot):
	headgear = 'rhsusf_hgu56p_mask'
