from base import Base

class det5_base(Base):
	
	items = Base.items + [
		'tf_anprc152_2',
		'rhsusf_ANPVS_15',
	]
	class HandGun:
		weapon = 'RH_p226'
		mags = [['RH_15Rnd_9x19_SIG', 15]]
		rail = [['RH_X300', 15]]
		suppressor = [['RH_suppr9', 15]]

	class Uniform:
		type = 'U_mas_usr_B_IndUniform2_o'
		items = Base.Uniform.items + [
			['AGM_IR_Strobe_Item', 1],
		]
	class Vest:
		type = 'AV_PlateCarrier2_khk'
		items = [
			['rhs_mag_m67', 1],
			['SmokeShell', 1],
		]
	class Backpack:
		type = 'B_Kitbag_cbr'
		items = [
			['SmokeShell', 1],
			['rhs_mag_m67', 3],
		]
	binoc = 'AGM_Vector'

	class singleton_det5(Det5_base):
	class HandGun:
		weapon = 'RH_bull'
		mags = [['RH_6Rnd_454_Mag', 6]]
		rail = [['', 6]]
		suppressor = [['', 6]]
		]
