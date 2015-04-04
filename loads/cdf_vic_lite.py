from p4a.loadout import Crate

class cdf_vic_lite(Crate):
	vehicle = True
	def __init__(self):
		super(cdf_vic_lite, self).__init__()
		self.remove('all')	
	weapons = [
		['rhs_weap_rsp30_white', 2],
		['rhs_weap_rsp30_red', 2],
	]
	magazines = [
		['rhs_mag_rsp30_white', 2],
		['rhs_mag_rsp30_red', 2],
		['rhs_30Rnd_762x39mm', 5],
		['rhs_30Rnd_545x39_AK', 5],
		['rhs_100Rnd_762x54mmR', 2],
		['rhs_mag_nspd', 2],
		['rhs_mag_rdg2_white', 2],
		['rhs_mag_rgd5', 4],
	]
	items = [
		['cse_bandage_basic', 10],
		['cse_bandageElastic', 5],
		['cse_morphine', 2],
		['cse_epinephrine', 2],
		['cse_saline_iv', 1],
		['cse_saline_iv_500', 2],
		['cse_saline_iv_250', 2],
		['cse_tourniquet', 2],	
	]