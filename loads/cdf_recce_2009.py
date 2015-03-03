import base

class cdf_recce_base(base.Base):
	class NoWrite: pass
	binoc = 'VTN_B15'
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
			['VTN_RDG2B', 1],
		]
	class Backpack:
		type = 'B_Kitbag_rgr'
		items = [
			['VTN_1PN74', 1],
			['VTN_RDG2B', 1],
			['rhs_mag_rgd5', 2],
		]

class cdf_recce_rifleman(cdf_recce_base):
	class Primary:
		weapon = 'VTN_AKMSN_40s'
		optic = 'VTN_OPTIC_1P76'
		mags = [
			['VTN_RPK_40s_SC', 40],
		]
	class Vest(cdf_recce_base.Vest):
		items = cdf_recce_base.Vest.items + [
			['VTN_RPK_40s_SC', 2],
		]
	class Backpack(cdf_recce_base.Backpack):
		items = cdf_recce_base.Backpack.items + [
			['VTN_RPK_40s_AP', 1],
			['VTN_RPK_40s_TRC', 1],
			['VTN_MUZZLE_PBS1', 1],
			['VTN_6CH3', 1],
			['VTN_MUZZLE_DTK1L', 1],
		]

class cdf_recce_sl(cdf_recce_rifleman):
	class Primary:
		weapon = 'VTN_AKMS_T_P'
		optic = 'VTN_OPTIC_1P76'
		mags = [
			['VTN_RPK_40s_SC', 40],
		]
	class Backpack(cdf_recce_rifleman.Backpack):
		items = cdf_recce_rifleman.Backpack.items + [
			['tf_anprc148jem', 1],
			['alive_tablet', 1],
		]

class cdf_recce_tl(cdf_recce_base):
	class Primary:
		weapon = 'VTN_AK74M_GP30M'
		optic = 'VTN_OPTIC_1P76'
		mags = [
			['VTN_AK74_30p_SC', 30],
			['VTN_VOG25', 1],
		]
	class Vest(cdf_recce_base.Vest):
		type = 'V_I_G_resistanceLeader_F'
		items = cdf_recce_base.Vest.items + [
			['tf_anprc148jem', 1],
			['VTN_AK74_30p_SC', 3],
		]

	class Backpack(cdf_recce_base.Backpack):
		items = cdf_recce_base.Backpack.items + [
			['VTN_MUZZLE_DTK_AKS545', 1],
			['VTN_VG40MD', 5],
			['VTN_VG40OP', 10],
			['VTN_VGS401', 2],
			['VTN_VGS402', 2],
		]

class cdf_recce_lmg(cdf_recce_base):
	class Primary:
		weapon = 'VTN_PKP'
		mags = [
			['VTN_PK_100s_SC', 100],
		]
	class Vest(cdf_recce_base.Vest):
		items = cdf_recce_base.Vest.items + [
			['VTN_PK_100s_SC', 1],
		]
	class Backpack(cdf_recce_base.Backpack):
		items = cdf_recce_base.Backpack.items + [
			['VTN_PK_100s_SC', 2],
			['VTN_PK_100s_TRC', 1],
		]

class cdf_recce_medic(cdf_recce_base):
	class Primary:
		weapon = 'VTN_AK74M'
		optic = 'VTN_OPTIC_1P76'
		mags = [
			['VTN_AK74_30b_SC', 30],
		]
	class Vest(cdf_recce_base.Vest):
		items = cdf_recce_base.Vest.items + [
			['VTN_RDG2B', 2],
			['VTN_AK74_30b_SC', 2],
		]
	class Backpack(cdf_recce_base.Backpack):
		items = cdf_recce_base.Backpack.items + base.MedicSupplies + [
			['VTN_AK74_30b_SC', 3],
			['VTN_MUZZLE_DTK_545', 1],
			['VTN_RDG2B', 3],
		]

class cdf_recce_gren(cdf_recce_tl):
	class Primary(cdf_recce_tl.Primary):
		weapon = 'VTN_AKS74N_GP25_30p'

	class Backpack(cdf_recce_tl.Backpack):
		items = cdf_recce_tl.Backpack.items + [
			['VTN_VOG25P', 5],
		]

class cdf_recce_rto(cdf_recce_base):
	class Primary:
		weapon = 'VTN_AKMS_T_P'
		mags = [
			['VTN_RPK_40s_SC', 40],
		]
	class Vest(cdf_recce_base.Vest):
		items = cdf_recce_base.Vest.items + [
			['VTN_RPK_40s_SC', 3],
			['tf_anprc148jem', 2],
		]
	class Backpack:
		type = 'VTN_BP_R168KNE_FLORA'


class cdf_recce_svd(cdf_recce_base):
	class Primary:
		weapon = 'VTN_SVD'
		optic = 'VTN_OPTIC_1P43M2'
		mags = [
			['VTN_SVD_10s_SC', 10],
		]
	class Vest(cdf_recce_base.Vest):
		items = cdf_recce_base.Vest.items + [
			['VTN_SVD_10s_TRC', 1],
		]
	class Backpack(cdf_recce_base.Backpack):
		items = cdf_recce_base.Backpack.items + [
			['VTN_SVD_10s_SC', 3],
			['VTN_SVD_10s_AP', 4],
		]
