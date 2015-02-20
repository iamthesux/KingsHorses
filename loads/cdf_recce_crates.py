from p4a.loadout import Crate
 
class cdf_recce_launchers(Crate):
	title = 'CDFSF Launchers and Explosives'
 	base = 'VTN_WPNE_SN_BOX'
	weapons = [
		['rhs_weap_rpg7', 10],
		['rhs_weap_rpg26', 100],
		['rhs_weap_rshg2', 50],
	]
	magazines = [
		['rhs_rpg7_PG7VL_mag', 200],
		['rhs_rpg7_PG7VR_mag', 200],
		['rhs_rpg7_OG7V_mag', 200],
		
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
	]
	magazines = [
		['rhs_mag_rgd5', 100],
		['rhs_mag_rdg2_white', 300],
		['rhs_mag_rdg2_black', 300],
		['rhs_mag_nspn_yellow', 200],
		['rhs_mag_nspn_red', 200],
		['rhs_mag_nspn_green', 200],

		['RH_8Rnd_762_tt33', 100],

		['VTN_PK_100s_SC', 200],
		['VTN_PK_100s_TRC', 200],
		['VTN_PK_100s_AP', 100],		
		['VTN_AK74_30p_SC', 200],
		['VTN_AK74_30p_TRC', 200],
		['VTN_AK74_30p_AP', 100],
	
	]

class cdf_recce_radios(Crate):
	title = 'CDFSF Radios'
 	base = 'rhs_weapons_crate_ak_ammo_545x39_standard'
	items = [
		['tf_anprc152', 50],
		['tf_rt1523g_green', 10],
	]
