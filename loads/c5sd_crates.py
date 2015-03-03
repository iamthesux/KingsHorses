from p4a.loadout import Crate

class det5_crate(Crate):
	def __init__(self, **kwargs):
		super(det5_crate, self).__init__(**kwargs)
		self.remove('all')

	title = '5th Spetsnaz Detachment Weapons'
	base = 'VTN_WPNE_LMG_BOX'
	
	weapons = [
		['rhs_weap_svd', 50],
		['VTN_PKMN_P', 50],
		['VTN_PKP', 50],
		['VTN_AK103', 50],
		['VTN_AK103_GP25', 50],
		['VTN_AK103_GP30M', 50],
		['VTN_AK104', 50],
		['VTN_AK105_P', 50],
		['VTN_AKMS_T_P', 50],
		['VTN_AKS74N_GP25', 50],
		['VTN_AKS74N', 50],
		['VTN_AKMSN', 50],
		['VTN_AKMSN_GP25', 50],
		['VTN_AK74M_GP30M', 50],
		['VTN_AK74M_GP25', 50],
		['VTN_AK74M', 50],

		['rhs_weap_rpg7', 10],
		['rhs_weap_rpg26', 100],
		['rhs_weap_rshg2', 100],

		['VTN_SP81', 50],

		['VTN_B15', 50],
		['VTN_LPR2', 50],

		['VTN_RSP30_RED', 100],
		['VTN_RSP30_GREEN', 100],
		['VTN_RSP30_WHITE', 100],
	]
	magazines = [
		['VTN_OP_1k_WHITE', 100],
		['VTN_SP_1k_WHITE', 100],
		['VTN_SP_1k_RED', 100],
		['VTN_SP_1k_GREEN', 100],
		['VTN_SP_1k_YELLOW', 100],
		
		['rhs_mag_fakel', 100],
		['rhs_mag_fakels', 100],
		['rhs_mag_zarya2', 100],
		['rhs_mag_plamyam', 100],
		
		['VTN_RDG2B', 100],
		['VTN_RDG2CH', 100],

		['VTN_NSPD', 100],
		['VTN_NSP_RED', 100],
		['VTN_NSP_YELLOW', 100],
		['VTN_NSP_GREEN', 100],
		
		['rhs_mag_rgd5', 100],
		['VTN_RGO', 100],
		['VTN_RGN', 100],
		['VTN_RDGM', 100],
		['VTN_F1', 100],
		
		['VTN_VOG25', 100],
		['VTN_VOG25P', 100],
		['VTN_VG40MD', 100],
		['VTN_VG40OP', 100],
		['VTN_VGS401', 100],
		['VTN_VGS402', 100],
		['VTN_VG40TB', 100],

		['rhs_10Rnd_762x54mmR_7N1', 500],
		
		['VTN_AK74_30p_SC', 500],
		['VTN_AK74_30p_TRC', 500],
		['VTN_AK74_30p_AP', 500],
		['VTN_AK74_30p_AP2', 500],

		['VTN_AKM_30s_SC', 500],
		['VTN_AKM_30s_TRC', 500],
		['VTN_AKM_30s_AP', 500],
		['VTN_AKM_30s_INC', 500],
		['VTN_AKM_30s_API', 500],
		['VTN_AKM_30s_SS', 500],

		['VTN_RPK_40s_SC', 500],
		['VTN_RPK_40s_TRC', 500],
		['VTN_RPK_40s_AP', 500],
		['VTN_RPK_40s_INC', 500],
		['VTN_RPK_40s_API', 500],

		['VTN_RPK_75s_SC', 500],
		['VTN_RPK_75s_TRC', 500],
		['VTN_RPK_75s_AP', 500],
		['VTN_RPK_75s_INC', 500],
		['VTN_RPK_75s_API', 500],

		['VTN_AK103_30p_SC', 500],
		['VTN_AK103_30p_TRC', 500],
		['VTN_AK103_30p_AP', 500],
		['VTN_AK103_30p_INC', 500],
		['VTN_AK103_30p_API', 500],
		['VTN_AK103_30p_SS', 500],

		['rhs_rpg7_PG7VL_mag', 200],
		['rhs_rpg7_PG7VR_mag', 200],
		['rhs_rpg7_TBG7V_mag', 200],

		['rhs_rshg2_mag', 100],
		['rhs_rpg26_mag', 100],

		['VTN_PK_100s_SC', 200],
		['VTN_PK_100s_TRC', 200],
		['VTN_PK_100s_AP', 200],
		['VTN_PK_100s_INC', 200],
		['VTN_PK_100s_API', 200],

		['SLAMDirectionalMine_Wire_Mag', 50],
		['ClaymoreDirectionalMine_Remote_Mag', 50],
		['DemoCharge_Remote_Mag', 50],
		['SatchelCharge_Remote_Mag', 50],
		['APERSTripMine_Wire_Mag', 50],
		['rhs_mine_pmn2_mag', 50],
		['rhs_mine_tm62m_mag', 50],
	]
	
	backpacks = [
		['tf_rt1523g_green', 10],
		['B_Parachute', 10],
	]

	items = [
		['V_KORA_K_CHICOM', 5],
		['V_KORA_K_6Sh104AKGP', 5],
		['V_KORA_K_6Sh104SVD', 5],
		['V_KORA_K_6Sh104PK', 5],
		
		['VTN_MUZZLE_DTK1P', 5],
		['VTN_MUZZLE_FS_105_545', 5],
		['VTN_MUZZLE_DTK4M', 5],
		['VTN_MUZZLE_DTK_762', 5],
		['VTN_MUZZLE_COMP_762', 5],
		['VTN_MUZZLE_COUPL_AKM', 5],
		['VTN_MUZZLE_PBS1', 5],

		['VTN_FLASHLIGHT_2PS_KLESHCH', 5],

		['VTN_OPTIC_1P76', 5],
		['VTN_OPTIC_1P77', 5],
		['VTN_OPTIC_1P78', 5],
		['VTN_OPTIC_TA_01NSN', 5],
		['VTN_OPTIC_RAKURS_PM', 5],
		['rhs_acc_pgo7v', 5],

		['VTN_6CH3_3', 5],
		['rhs_acc_pso1m2', 5],

		['ItemGPS', 5],
		['tf_microdagr', 5],
		['rhsusf_ANPVS_15', 10],
		['tf_rf7800str', 100],
		['tf_anprc152', 50],
	]
