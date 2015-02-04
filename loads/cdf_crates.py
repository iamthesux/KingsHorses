from p4a.loadout import Crate

class cdf_explosives(Crate):
	title = 'CDF Explosives and CSW'
	magazines = [
		
		['rhs_mag_rgd5', 100],
		['rhs_mag_rdg2_white', 100],
		['rhs_mag_rdg2_black', 100],
		['rhs_mag_nspn_yellow', 100],
		['rhs_mag_nspn_red', 100],
		['rhs_mag_nspn_green', 100],
		['rhs_mine_tm62m', 100],
		
		['rhs_VOG25', 100],
		['rhs_VOG25p', 100],
		['rhs_vg40op_white', 100],
		['rhs_vg40op_green', 100],
		['rhs_vg40op_red', 100],
		['rhs_GRD40_white', 100],
		['rhs_GRD40_green', 100],
		['rhs_GRD40_red', 100],
	]

	backpacks = [
		['RHS_NSV_Gun_Bag', 10],
		['RHS_NSV_Gun_Bag', 10],
		
		['RDS_DShkM_Gun_Bag', 10],
		['RDS_DShkM_TripodLow_Bag', 10],
		
		['RDS_Metis_Gun_Bag', 10],
		['RDS_Metis_Tripod_Bag', 10],

		['RDS_AGS30_Gun_Bag', 10],
		['RDS_AGS30_Tripod_Bag', 10],

		['RDS_SPG9_Gun_Bag', 10],
		['RDS_SPG9_Tripod_Bag', 10],
	]

class cdf_launchers(Crate):
	title = 'CDF Launchers and Warheads'
	weapons = [
		['rhs_weap_rpg7', 10],
		['rhs_weap_rpg26', 100],
		['rhs_weap_rshg2', 50],
	]
	magazines = [
		['rhs_rpg7_PG7VL_mag', 100],
		['rhs_rpg7_PG7VR_mag', 100],
		['rhs_rpg7_OG7V_mag', 100],
	]

class cdf_weapons(Crate):
	title = 'CDF Rifles and Ammo'
	weapons = [
		['rhs_weap_ak74m', 5],
		['rhs_weap_ak74m_folded', 5],
		['rhs_weap_pkp', 5],
	]
	magazines = [
		['rhs_30Rnd_545x39_AK', 100],
		['rhs_30Rnd_545x39_AK_green', 100],
		['rhs_100Rnd_762x54mmR', 100],
	]


