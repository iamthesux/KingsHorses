from p4a.loadout import Crate

class det5_crate(Crate):
	def __init__(self, **kwargs):
		super(det5_crate, self).__init__(**kwargs)
		self.remove('all')
	title = '5th Spetsnaz Detachment Weapons'
	base = 'CUP_RUVehicleBox'
	
	weapons = [
		['rhs_weap_rsp30_white', 100],
		['rhs_weap_rsp30_green', 100],
		['rhs_weap_rsp30_red', 100],

		['RH_usp', 50],
		
		['rhs_weap_svd', 50],
		['rhs_weap_ak103', 50],
		['rhs_weap_ak103_npz', 50],
		['rhs_weap_ak103_1', 50],
		['rhs_weap_ak103_2', 50],
			
		['rhs_weap_ak74m_gp25', 50],
		['rhs_weap_ak74m_gp25_npz', 50],
		['rhs_weap_ak74m_2mag_npz', 50],
		['rhs_weap_ak74m_2mag', 50],
		['rhs_weap_akm', 50],
		['rhs_weap_akms', 50],
		['rhs_weap_akm_gp25', 50],
		['rhs_weap_akms_gp25', 50],
		['rhs_weap_pkp', 50],


		['rhs_weap_rpg7', 10],
		['rhs_weap_rpg26', 100],
		['rhs_weap_rshg2', 100],
	]
	magazines = [
		['rhs_weap_rsp30_white', 100],
		['rhs_weap_rsp30_red', 100],
		['rhs_weap_rsp30_green', 100],
		['rhs_mag_rsp30_white', 100],
		['rhs_mag_rsp30_red', 100],
		['rhs_mag_rsp30_green', 100],

		['rhs_mag_rgd5', 100],
		['rhs_mag_rdg2_white', 100],
		['rhs_mag_rdg2_black', 100],

		['rhs_mag_nspd', 100],
		['rhs_mag_nspn_red', 100],
		['rhs_mag_nspn_yellow', 100],
		['rhs_mag_nspn_green', 100],
		
		['rhs_mag_fakel', 100],
		['rhs_mag_fakels', 100],
		['rhs_mag_zarya2', 100],
		['rhs_mag_plamyam', 100],
		
		['rhs_VOG25', 100],
		['rhs_VOG25p', 100],
		['rhs_vg40tb', 100],
		['rhs_vg40sz', 100],
		
		['rhs_vg40op_white', 100],
		['rhs_vg40op_green', 100],
		['rhs_vg40op_red', 100],
		
		['rhs_GRD40_white', 100],
		['rhs_GRD40_green', 100],
		['rhs_GRD40_red', 100],

		['rhs_10Rnd_762x54mmR_7N1', 500],
		
		['rhs_30Rnd_762x39mm', 500],
		['rhs_30Rnd_762x39mm_tracer', 500],
		['rhs_30Rnd_762x39mm_89', 500],
		
		['rhs_30Rnd_545x39_AK', 500],
		['rhs_30Rnd_545x39_AK_green', 500],
		['rhs_30Rnd_545x39_7n10_AK', 500],
		['rhs_30Rnd_545x39_7n22_AK', 500],
		
		['rhs_45Rnd_545X39_AK', 500],
		['rhs_45Rnd_545X39_AK_Green', 500],
		['rhs_45Rnd_545X39_7N10_AK', 500],
		['rhs_45Rnd_545X39_7N22_AK', 500],

		['rhs_100Rnd_762x54mmR', 500],
		['rhs_100Rnd_762x54mmR_green', 500],

		['rhs_rpg7_PG7VL_mag', 200],
		['rhs_rpg7_PG7VR_mag', 200],
		['rhs_rpg7_OG7V_mag', 200],
		['rhs_rpg7_TBG7V_mag', 200],

		['rhs_rshg2_mag', 100],
		['rhs_rpg26_mag', 100],

		['30Rnd_556x45_Stanag_Tracer_Green', 100],
		['RH_30Rnd_556x45_Mk262', 100],
		['RH_17Rnd_9x19_g17', 100],

		['SLAMDirectionalMine_Wire_Mag', 50],
		['ClaymoreDirectionalMine_Remote_Mag', 50],
		['DemoCharge_Remote_Mag', 50],
		['SatchelCharge_Remote_Mag', 50],
		['APERSTripMine_Wire_Mag', 50],
		['rhs_mine_pmn2_mag', 50],
		['rhs_mine_tm62m_mag', 50],
	]

	backpacks = [
		['B_Parachute', 10],
		['B_VTN_6SH104_FLORA', 10],
		['RHS_NSV_Gun_Bag', 10],
		['RHS_NSV_Tripod_Bag', 10],
		
		['RDS_DShkM_Gun_Bag', 10],
		['RDS_DShkM_TripodLow_Bag', 10],

		['RDS_AGS30_Gun_Bag', 10],
		['RDS_AGS30_Tripod_Bag', 10],

		['RDS_Metis_Gun_Bag', 10],
		['RDS_Metis_Tripod_Bag', 10],

		['RDS_SPG9_Gun_Bag', 10],
		['RDS_SPG9_Tripod_Bag', 10],
	]

	items = [
		['V_KORA_K_CHICOM', 5],
		['V_KORA_K_6Sh104AKGP', 5],
		['V_KORA_K_6Sh104SVD', 5],
		['V_KORA_K_6Sh104PK', 5],
		
		['H_VTN_SHAPKA_PSh', 5],
		['rhsusf_opscore_02', 5],
		['H_VTN_K6', 5],
		
		['rhs_acc_1p29', 5],
		['rhs_acc_1p63', 5],
		['rhs_acc_1pn93_1', 5],
		['rhs_acc_ekp1', 5],
		['rhs_acc_pkas', 5],
		['rhs_acc_pso1m2', 5],
		['rhs_acc_1pn93_2', 5],
		['rhs_acc_pgo7v', 5],

		['rhs_acc_npz', 5],
		['rhs_bipod', 5],

		['rhs_acc_tgpa', 5],
		['rhs_acc_tgpv', 5],		
		['rhs_acc_pbs1', 5],
		
		['rhs_acc_dtk', 5],
		['rhs_acc_dtk1', 5],
		['rhs_acc_dtk3', 5],
		
		["rhsusf_acc_LEUPOLDMK4", 1],
		["rhsusf_acc_LEUPOLDMK4_2", 1],
		["rhsusf_acc_EOTECH", 1],
		["rhsusf_acc_eotech_552", 1],
		["rhsusf_acc_compm4", 1],
		["rhsusf_acc_ELCAN", 1],
		["rhsusf_acc_ELCAN_PIP", 1],
		["rhsusf_acc_ACOG", 1],
		["rhsusf_acc_ACOG2", 1],
		["rhsusf_acc_ACOG3", 1],
		["rhsusf_acc_ACOG_USMC", 1],
		["rhsusf_acc_ACOG2_USMC", 1],
		["rhsusf_acc_ACOG3_USMC", 1],
		["rhsusf_acc_ACOG_PIP", 1],

		["RH_qdss_nt4", 1],
		["RH_saker", 1],
		["RH_Saker762", 1],
		["RH_fa556", 1],
		["RH_fa762", 1],
		["RH_m110sd", 1],
		["RH_m110sd_t", 1],
		["RH_spr_mbs", 1],
		["RH_tundra", 1],
		["RH_peq15", 1],
		["RH_peq15_top", 1],
		["RH_peq15b", 1],
		["RH_peq15b_top", 1],
		["RH_peq2", 1],
		["RH_peq2_top", 1],
		["RH_SFM952V", 1],
		["RH_SFM952V_tan", 1],
		["RH_eotech553", 1],
		["RH_eotech553_tan", 1],
		["RH_eotech553mag", 1],
		["RH_eotech553mag_tan", 1],
		["RH_eotexps3", 1],
		["RH_eotexps3_tan", 1],
		["RH_eothhs1", 1],
		["RH_eothhs1_tan", 1],
		["RH_compm4s", 1],
		["RH_compM2", 1],
		["RH_compM2l", 1],
		["RH_compM2_tan", 1],
		["RH_compM2l_tan", 1],
		["RH_t1", 1],
		["RH_t1_tan", 1],
		["RH_reflex", 1],
		["RH_barska_rds", 1],
		["RH_cmore", 1],
		["RH_LTdocter", 1],
		["RH_LTdocterl", 1],
		["RH_zpoint", 1],
		["RH_shortdot", 1],
		["RH_accupoint", 1],
		["RH_m3lr", 1],
		["RH_leu_mk4", 1],
		["RH_ta648", 1],
		["RH_c79", 1],
		["RH_c79_2d", 1],
		["RH_m145", 1],
		["RH_ta01nsn", 1],
		["RH_ta01nsn_2D", 1],
		["RH_ta01nsn_tan", 1],
		["RH_ta01nsn_tan_2D", 1],
		["RH_ta31rco", 1],
		["RH_ta31rco_2D", 1],
		["RH_ta31rco_tan", 1],
		["RH_ta31rco_tan_2D", 1],
		["RH_ta31rmr", 1],
		["RH_ta31rmr_2D", 1],
		["RH_ta31rmr_tan", 1],
		["RH_ta31rmr_tan_2D", 1],
		["RH_anpvs4", 1],
		["RH_anpvs10", 1],
		["RH_pas13cl", 1],
		["RH_pas13cm", 1],
		["RH_pas13cmg", 1],
		["RH_pas13ch", 1],

		['ItemGPS', 5],
		['rhsusf_ANPVS_15', 10],
		['tf_microdagr', 5],
		['tf_pnr1000a', 100],
		['VTN_BP_R168KNE_FLORA', 100],
		['tf_anprc148jem', 50],
	]
