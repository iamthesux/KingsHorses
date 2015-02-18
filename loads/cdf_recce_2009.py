from base import Base

class cdf_recce_base(Base):
	class NoWrite: pass
	binoc = 'VTN_B15'
	headgear = 'H_Booniehat_oli'
	items = Base.items + [
		'tf_rf7800str',
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
		type = 'sh_chdkz_v_carrierlite_olv'
		items = [
			['rhs_mag_rdg2_white', 1],
		]
	class Backpack:
		type = 'B_Kitbag_rgr'
		items = [
			['VTN_BN3', 1],
			['rhs_mag_rdg2_white', 1],
			['HandGrenade', 2],
		]

class cdf_recce_rifleman(cdf_recce_base):
	class Primary:
		weapon = 'VTN_AKMSN_40s'
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
		mags = [
			['VTN_RPK_40s_SC', 40],
		]
	class Backpack(cdf_recce_rifleman.Backpack):
		items = cdf_recce_rifleman.Backpack.items + [
			['tf_anprc152', 1],
			['alive_tablet', 1],
		]

class cdf_recce_tl(cdf_recce_base):
	class Primary:
		weapon = 'VTN_AK74M_GP30M'
		mags = [
			['VTN_AK74_30p_SC', 30],
			['VTN_VOG25', 1],
		]
	class Vest(cdf_recce_base.Vest):
		type = 'V_I_G_resistanceLeader_F'
		items = cdf_recce_base.Vest.items + [
			['VTN_VOG25P', 5],
			['VTN_VG40MD', 5],
		]

	class Backpack(cdf_recce_base.Backpack):
		items = cdf_recce_base.Backpack.items + [
			['VTN_MUZZLE_DTK_AKS545', 1],
			['VTN_VG40MD', 5],
			['VTN_VG40OP', 10],
			['VTN_VGS401', 2],
			['VTN_VGS402', 2],
		]

class cdf_recce_gren(cdf_recce_tl):
	class Primary(cdf_recce_tl.Primary):
		weapon = 'VTN_AKS74N_GP25_30p'

	class Backpack(cdf_recce_tl.Backpack):
		items = cdf_recce_tl.Backpack.items + [
			['VTN_VOG25P', 5],
		]

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
