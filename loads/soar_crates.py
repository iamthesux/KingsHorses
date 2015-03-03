from p4a.loadout import Crate

class soar_radios(Crate):
	title = '160th SOAR Radios'
	base = 'rhs_weapons_crate_ak_standard'
	items = [
		['tf_fadak', 75],
		['tf_anprc154', 75],
	]

	backpacks = [
		['tf_anprc155', 25],
	]

class soar_ammo(Crate):
	title = '160th SOAR Ammo and Ordnance'
	base = 'rhs_weapons_crate_ak_ammo_545x39_standard'
	weapons = [
		['VTN_SP81', 50],
		['VTN_RSP30_RED', 500],
		['VTN_RSP30_GREEN', 500],
		['VTN_RSP30_WHITE', 500],

	]
	magazines = [
		['VTN_AK74_30b_TRC', 500],
		['VTN_OP_1k_WHITE', 50],
		['VTN_SP_1k_GREEN', 200],
		['VTN_SP_1k_RED', 200],

		['VTN_RDG2B', 500],
		['VTN_RDG2CH', 500],

		['VTN_NSPD', 50],
		['VTN_NSP_RED', 200],
		['VTN_NSP_GREEN', 200],
		['VTN_NSP_YELLOW', 200],
	]
