from p4a.loadout import Crate

class cdf_vic(Crate):
	vehicle = True
	weapons = [
		['rhs_weap_rsp30_white', 2],
		['rhs_weap_rsp30_red', 5],
		['rhs_weap_rsp30_green', 5],

		['rhs_weap_rpg26', 5],
	]
	magazines = [
		['rhs_mag_rsp30_white', 2],
		['rhs_mag_rsp30_red', 5],
		['rhs_mag_rsp30_green', 5],
		['rhs_30Rnd_762x39mm', 10],
		['rhs_30Rnd_762x39mm_tracer', 5],
		['rhs_30Rnd_545x39_AK', 20],
		['rhs_30Rnd_545x39_AK_green', 10],
		['rhs_mag_nspd', 5],
		['rhs_mag_nspn_red', 5],
		['rhs_mag_nspn_green', 5],
		['rhs_mag_nspn_yellow', 5],
		['rhs_mag_rdg2_white', 10],
		['rhs_mag_rgd5', 10],
		['DemoCharge_Remote_Mag', 1],
		['rhs_rpg26_mag', 5],
		['rhs_100Rnd_762x54mmR', 10],
		['rhs_100Rnd_762x54mmR_green', 5],
	]
	items = [
		['cse_bandage_basic', 25],
		['cse_bandageElastic', 15],
		['cse_morphine', 5],
		['cse_epinephrine', 5],
		['cse_saline_iv', 5],
		['cse_saline_iv_500', 5],
		['cse_saline_iv_250', 5],
		['cse_tourniquet', 5],	
	]