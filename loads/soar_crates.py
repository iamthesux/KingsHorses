from p4a.loadout import Crate

class soar_radios(Crate):
	title = '160th SOAR Radios'
	base = 'CUP_USBasicAmmunitionBox'
	items = [
		['tf_rf7800str', 75],
		['tf_anprc152', 75],
	]

	backpacks = [
		['tf_rt1523g_black', 25],
	]

class soar_ammo(Crate):
	title = '160th SOAR Ammo and Ordnance'
	base = 'CUP_USBasicWeaponsBox'
	magazines = [
		['30Rnd_556x45_Stanag', 250],
		['30Rnd_556x45_Stanag_Tracer_Red', 100],
		['SmokeShellBlue', 500],
		['SmokeShell', 500],
		['SmokeShellGreen', 500],
		['rhs_mag_m67', 200],
		['DemoCharge_Remote_Mag', 100],
	]
