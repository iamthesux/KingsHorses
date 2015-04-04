import base

class cdf_recce_base(base.Base):
	class NoWrite: pass
	binoc = 'Binocular'
	headgear = 'H_Booniehat_oli'
	items = base.Base.items + ['tf_pnr1000a']

	class HandGun:
		weapon = 'RH_tt33'
		mags = [['RH_8Rnd_762_tt33', 8]]

	class Uniform:
		type = 'Niko_USA_M81'
		items = base.Base.Uniform.items + [
			['RH_8Rnd_762_tt33', 2],
		]
	class Vest:
		type = 'sh_chdkz_v_carrierlite_olv'
		items = [
			['rhs_mag_rdg2_white', 1],
		]
	class Backpack:
		type = 'B_Kitbag_rgr'
		items = [
			['rhsusf_ANPVS_14', 1],
			['tf_anprc148jem', 1],
			['alive_tablet', 1],
			['rhs_mag_rdg2_white', 1],
			['rhs_mag_rgd5', 2],
		]

class cdf_recce_rifleman(cdf_recce_base):
	class Primary:
		weapon = 'rhs_weap_ak74m_2mag'
		optic = 'rhs_acc_pkas'
		mags = [
			['rhs_45Rnd_545X39_7N10_AK', 45],
		]
	class Vest(cdf_recce_base.Vest):
		items = cdf_recce_base.Vest.items + [
			['rhs_45Rnd_545x39_7n10_AK', 2],
		]
	class Backpack(cdf_recce_base.Backpack):
		items = cdf_recce_base.Backpack.items + [
			['rhs_45Rnd_545X39_7N10_AK', 1],
			['rhs_45Rnd_545x39_AK_green', 1],
			['rhs_acc_tgpa', 1],
		]

class cdf_recce_sl(cdf_recce_rifleman):
	class Backpack(cdf_recce_rifleman.Backpack):
		items = cdf_recce_rifleman.Backpack.items + [
			['tf_anprc148jem', 1],
		]

class cdf_recce_gren(cdf_recce_rifleman):
	class Primary:
		weapon = 'rhs_weap_ak74m_gp25'
		optic = 'rhs_acc_pkas'
		mags = [
			['rhs_45Rnd_545X39_7N10_AK', 45],
			['rhs_VOG25p', 1],
		]
	class Vest:
		type = 'V_I_G_resistanceLeader_F'
		items = cdf_recce_rifleman.Vest.items + [
			['rhs_45Rnd_545X39_7N10_AK', 3],
		]

	class Backpack(cdf_recce_base.Backpack):
		items = cdf_recce_base.Backpack.items + [
			['rhs_VOG25p', 5],
			['rhs_VOG25', 5],
			['rhs_GRD40_white', 10],
			['rhs_vg40op_green', 2],
			['rhs_vg40op_red', 2],
		]

class cdf_recce_medic(cdf_recce_rifleman):

	class Vest(cdf_recce_rifleman.Vest):
		items = cdf_recce_rifleman.Vest.items + [
			['rhs_mag_rdg2_white', 2],
		]
	class Backpack(cdf_recce_base.Backpack):
		items = cdf_recce_base.Backpack.items + base.MedicSupplies + [
			['rhs_45Rnd_545X39_AK', 3],
			['rhs_mag_rdg2_white', 3],
		]

class cdf_recce_tl(cdf_recce_gren):
	class Vest(cdf_recce_gren):
		items = cdf_recce_gren.Vest.items + [
			['tf_anprc148jem', 1],
		]

class cdf_recce_rto(cdf_recce_rifleman):
	class Vest(cdf_recce_rifleman.Vest):
		items = cdf_recce_rifleman.Vest.items + [
			['tf_anprc148jem', 1],
		]
	class Backpack:
		type = 'VTN_BP_R168KNE_FLORA'


class cdf_recce_svd(cdf_recce_base):
	class Primary:
		weapon = 'rhs_weap_svds'
		optic = 'rhs_acc_pso1m2'
		mags = [
			['rhs_10Rnd_762x54mmR_7N1', 10],
		]
	class Vest(cdf_recce_base.Vest):
		items = cdf_recce_base.Vest.items + [
			['rhs_10Rnd_762x54mmR_7N1', 1],
		]
	class Backpack(cdf_recce_base.Backpack):
		items = cdf_recce_base.Backpack.items + [
			['rhs_10Rnd_762x54mmR_7N1', 3],
			['rhs_10Rnd_762x54mmR_7N1', 4],
		]
