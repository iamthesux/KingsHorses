from p4a.loadout import Crate
 
class cdf_recce_launchers(Crate):
	title = 'CDFSF Launchers and Explosives'
 	base = 'VTN_WPNE_SN_BOX'
	weapons = [
		['rhs_weap_rpg7', 20],
		['rhs_weap_rpg26', 400],
		['rhs_weap_rshg2', 400],
	]
	magazines = [
		['rhs_rpg7_PG7VL_mag', 200],
		['rhs_rpg7_PG7VR_mag', 200],
		['rhs_rpg7_OG7V_mag', 200],
		['rhs_rpg26_mag', 400],
		['rhs_rshg2_mag', 400],

		['rhs_mine_tm62m_mag', 100],
		['rhs_mine_pmn2_mag', 100],
		['DemoCharge_Remote_Mag', 100],

		['VTN_VOG25', 100],
		['VTN_VOG25P', 100],
		['VTN_VG40MD', 200],
		['VTN_VG40OP', 300],
		['VTN_VGS401', 100],
		['VTN_VGS402', 100],
		['VTN_VG40TB', 50],
	]
 
class cdf_recce_weapons(Crate):
	title = 'CDFSF Rifles and Ammo'
 	base = 'VTN_WPNE_LMG_BOX'

	weapons = [
		['VTN_PKM', 10],
		['VTN_LPR1', 10],
		['VTN_SVD', 2],
	]
	magazines = [
		['rhs_mag_rgd5', 200],
		['VTN_RDG2B', 500],
		['VTN_RDG2CH', 500],
		
		['VTN_NSPD', 500],
		['VTN_NSP_RED', 50],
		['VTN_NSP_YELLOW', 50],
		['VTN_NSP_GREEN', 50],

		['RH_8Rnd_762_tt33', 100],

		['VTN_SVD_10s_SC', 150],
		['VTN_SVD_10s_AP', 100],
		['VTN_PK_100s_SC', 200],
		['VTN_PK_100s_TRC', 200],
		['VTN_PK_100s_AP', 100],		
		['VTN_AK74_30p_SC', 200],
		['VTN_AK74_30p_TRC', 200],
		['VTN_AK74_30p_AP', 100],
		['VTN_AK74_30b_SS', 100],
		['VTN_AKM_30b_SC', 500],
		['VTN_AKM_30b_TRC', 500],
		['VTN_AKM_30b_AP', 500],
		['VTN_AKM_30b_SS', 500],
	]

	items = [
		['rhs_acc_pgo7v', 20],
		['VTN_OPTIC_1P77', 50],
		['VTN_OPTIC_1P43M2', 50],
	]

class cdf_recce_radios(Crate):
	title = 'CDFSF Radios'
 	base = 'rhs_weapons_crate_ak_ammo_545x39_standard'
	items = [
		['tf_anprc148jem', 50],
	]
	backpacks = [
		['VTN_BP_R168KNE_FLORA', 10],
	]
