from p4a.loadout import Crate

class soar_radios(Crate):
	title = '160th SOAR Radios'
	base = 'rhs_weapons_crate_ak_standard'
	items = [
	]

	backpacks = [
	]

class soar_ammo(Crate):
	title = '160th SOAR Ammo and Ordnance'
	base = 'rhs_weapons_crate_ak_ammo_545x39_standard'
	weapons = [
		['rhs_weap_rsp30_white', 500],
		['rhs_weap_rsp30_red', 500],
		['rhs_weap_rsp30_green', 500],

	]
	magazines = [
		['rhs_mag_rsp30_white', 500],
		['rhs_mag_rsp30_red', 500],
		['rhs_mag_rsp30_green', 500],
		
		['rhs_30Rnd_545x39_AK', 500],
		['rhs_30Rnd_545x39_AK_green', 500],

		['rhs_mag_rgd5', 200],
		['rhs_mag_rdg2_white', 500],
		['rhs_mag_rdg2_black', 500],

		['rhs_mag_nspd', 400],
		['rhs_mag_nspn_red', 100],
		['rhs_mag_nspn_yellow', 100],
		['rhs_mag_nspn_green', 100],
	]
