from base import Base

class cdfsf_base(Base):
	class NoWrite: pass
	
	headgear = 'H_Booniehat_oli'
	items = Base.items + [
		'tf_rf7800str',
		'rhsusf_ANPVS_15',
	]
	class HandGun:
		weapon = 'RH_tt33'
		mags = [['RH_8Rnd_762_tt33', 8]]

	class Uniform:
		type = 'Niko_USA_M81'
		items = Base.Uniform.items + [
			['AGM_IR_Strobe_Item', 1],
		]
	class Vest:
		type = 'TRYK_V_ChestRig'
		items = [
			['HandGrenade', 1],
			['SmokeShell', 1],
		]
	class Backpack:
		type = 'TRYK_B_FieldPack_Wood'
		items = [
			['SmokeShell', 1],
			['HandGrenade', 3],
		]

class cdfsf_rifleman(cdfsf_base):
	class Primary:
		weapon = 'rhs_weap_ak74m_2mag_camo'
		optic = 'rhs_acc_1p29'
		supressor = 'rhs_acc_tgpa'
		mags = [
			['rhs_30Rnd_545x39_7n10_AK', 30],
		]
	class Vest(cdfsf_base.Vest):
		items = cdfsf_base.Vest.items + [
			['rhs_30Rnd_545x39_7n10_AK', 5],
		]
	class Backpack(cdfsf_base.Backpack):
		items = cdfsf_base.Backpack.items + [
			['rhs_30Rnd_545x39_7n10_AK', 5],
		]

class cdfsf_sl(cdfsf_rifleman):
	class Primary:
		weapon = 'rhs_weap_ak74m_camo'
		optic = 'rhs_acc_1p29'
		supressor = 'rhs_acc_tgpa'		
		mags = [
			['rhs_30Rnd_545x39_7n10_AK', 30],
		]
	class Backpack(cdfsf_rifleman.Backpack):
		items = cdfsf_rifleman.Backpack.items + [
			['rhs_30Rnd_545x39_7n10_AK', 5],
			['tf_anprc152', 1],
			['alive_tablet', 1],
		]
class cdfsf_tl(cdfsf_rifleman):
	class Primary:
		weapon = 'rhs_weap_ak74m_gp25'
		optic = 'rhs_acc_1p29'
		supressor = 'rhs_acc_tgpa'
		mags = [
			['rhs_30Rnd_545x39_7n10_AK', 30],
			['1Rnd_HE_Grenade_shell', 1],
		]
	class Vest(cdfsf_rifleman.Vest):
		type = 'TRYK_V_ChestRig_L'

	class Backpack(cdfsf_rifleman.Backpack):
		items = cdfsf_rifleman.Backpack.items + [
			['rhs_vg40op_white', 2],
			['rhs_GRD40_white', 4],
			['rhs_GRD40_green', 2],
			['rhs_GRD40_red', 2],
			['rhs_VOG25', 10],
		]

class cdfsf_gren(cdfsf_base):
	class Primary:
		weapon = 'rhs_weap_ak74m_gp25'
		optic = 'rhs_acc_1p29'
		supressor = 'rhs_acc_tgpa'
		mags = [
			['rhs_30Rnd_545x39_7n10_AK', 30],
			['1Rnd_HE_Grenade_shell', 1],
		]
	class Vest(cdfsf_base.Vest):
		type = 'TRYK_V_ChestRig_L'

	class Backpack(cdfsf_rifleman.Backpack):
		items = cdfsf_rifleman.Backpack.items + [
			['rhs_vg40op_white', 2],
			['rhs_GRD40_white', 4],
			['rhs_GRD40_green', 2],
			['rhs_GRD40_red', 2],
			['rhs_VOG25', 10],
		]

class cdfsf_svd(cdfsf_rifleman):
	class Primary:
		weapon = 'rhs_weap_svdp'
		optic = 'rhs_acc_pso1m2'
		mags = [
			['rhs_10Rnd_762x54mmR_7N1', 10],
		]
	class Vest(cdfsf_rifleman.Vest):
		type = 'TRYK_V_ChestRig'

	class Backpack(cdfsf_rifleman.Backpack):
		items = cdfsf_rifleman.Backpack.items + [
			['rhs_10Rnd_762x54mmR_7N1', 5],
		]
