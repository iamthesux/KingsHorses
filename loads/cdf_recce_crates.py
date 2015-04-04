from p4a.loadout import Crate
 
class cdf_recce_launchers(Crate):
	title = 'SASR Launchers and Explosives'
 	base = 'CUP_RUSpecialWeaponsBox'
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

		['rhs_VOG25', 200],
		['rhs_VOG25p', 200],
		['rhs_vg40tb', 100],
	]
 
class cdf_recce_weapons(Crate):
	title = 'SASR Rifles and Ammo'
 	base = 'CUP_RUSpecialWeaponsBox'

	weapons = [
		['rhs_weap_ak74m_gp25', 5],
		['rhs_weap_ak74m_2mag', 5],
		['rhs_weap_svd', 2],
	]
	magazines = [
		['rhs_mag_rgd5', 200],
		['rhs_mag_rdg2_white', 500],
		['rhs_mag_rdg2_black', 500],
		
		['rhs_mag_nspd', 100],
		['rhs_mag_nspn_red', 100],
		['rhs_mag_nspn_yellow', 100],
		['rhs_mag_nspn_green', 100],

		['RH_8Rnd_762_tt33', 100],

		['rhs_10Rnd_762x54mmR_7N1', 200],
		
		['rhs_30Rnd_762x39mm', 500],
		['rhs_30Rnd_762x39mm_tracer', 500],
		['rhs_30Rnd_762x39mm_89', 500],
		
		['rhs_30Rnd_545x39_AK', 500],
		['rhs_30Rnd_545x39_AK_green', 500],
		['rhs_30Rnd_545x39_7n10_AK', 500],
		
		['rhs_45Rnd_545X39_AK', 500],
		['rhs_45Rnd_545X39_AK_Green', 500],
		['rhs_45Rnd_545X39_7N10_AK', 500],
	]

	items = [
		['rhs_acc_1p29', 5],
		['rhs_acc_1p63', 5],
		['rhs_acc_1pn93_1', 5],
		['rhs_acc_ekp1', 5],
		['rhs_acc_pkas', 5],
		['rhs_acc_pso1m2', 5],
		['rhs_acc_1pn93_2', 5],
		['rhs_acc_pgo7v', 5],
		
		['rhs_acc_tgpa', 5],
		['rhs_acc_tgpv', 5],		
		['rhs_acc_pbs1', 5],
	]

class cdf_recce_radios(Crate):
	title = 'SASR Radios'
 	base = 'CUP_RUBasicAmmunitionBox'
	items = [
		['tf_anprc148jem', 50],
	]
	backpacks = [
		['VTN_BP_R168KNE_FLORA', 10],
	]
