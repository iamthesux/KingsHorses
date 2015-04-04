from p4a.loadout import Crate

class cdf_explosives(Crate):
	title = 'CDF Explosives and CSW'
 	base = 'CUP_RUVehicleBox'
	weapons = [
		['rhs_weap_rsp30_white', 500],
		['rhs_weap_rsp30_red', 200],
		['rhs_weap_rsp30_green', 200],
	]
	magazines = [
		['rhs_mag_rsp30_white', 500],
		['rhs_mag_rsp30_red', 200],
		['rhs_mag_rsp30_green', 200],
		
		['rhs_mag_rgd5', 200],
		['rhs_mag_rdg2_white', 500],
		['rhs_mag_rdg2_black', 500],

		['rhs_mag_nspd', 400],
		['rhs_mag_nspn_red', 100],
		['rhs_mag_nspn_yellow', 100],
		['rhs_mag_nspn_green', 100],
		['rhs_mine_tm62m_mag', 100],

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

class cdf_launchers(Crate):
	title = 'CDF Launchers and Warheads'
 	base = 'CUP_RUSpecialWeaponsBox'
	weapons = [
		['rhs_weap_rpg7', 10],
		['rhs_weap_rpg26', 500],
		['rhs_weap_rshg2', 100],
	]
	magazines = [
		['rhs_rpg7_PG7VL_mag', 400],
		['rhs_rpg7_PG7VR_mag', 200],
		['rhs_rpg26_mag', 500],
		['rhs_rshg2_mag', 100],
	]

class cdf_weapons(Crate):
	title = 'CDF Rifles and Ammo'
 	base = 'CUP_RUBasicWeaponsBox'
	magazines = [
		['rhs_30Rnd_762x39mm', 500],
		['rhs_30Rnd_762x39mm_tracer', 500],
		
		['rhs_30Rnd_545x39_AK', 500],
		['rhs_30Rnd_545x39_AK_green', 500],

		['rhs_100Rnd_762x54mmR', 500],
		['rhs_100Rnd_762x54mmR_green', 500],
	]

