from p4a.loadout import Crate

class soar_radios(Crate):
	title = '160th SOAR Radios'
	items = [
		['tf_rf7800str_1', 75],
		['tf_anprc152_2', 75],
		['tf_anprc148jem', 100],
	]

	backpacks = [
		['tf_anarc210', 25],               
		['tf_rt1523g_rhs', 25],
	]

class soar_ammo(Crate):
	title = '160th SOAR Ammo and Ordnance'
	magazines = [
		['30Rnd_556x45_Stanag', 250],
		['30Rnd_556x45_Stanag_Tracer_Red', 100],
		['SmokeShellBlue', 100],
		['SmokeShell', 100],
		['SmokeShellGreen', 100],
		['rhs_mag_m67', 100],
		['DemoCharge_Remote_Mag', 100],
	]

class soar_vehicle(Crate):
	title = '160th Aircraft Loads'
	magazines = [
		['30Rnd_556x45_Stanag', 45],
		['30Rnd_556x45_Stanag_Tracer_Red', 15],
		['SmokeShellBlue', 5],
		['SmokeShell', 5],
		['SmokeShellGreen', 5],
		['rhs_mag_m67', 10],
		['cse_bandage_basic', 25],
		['cse_bandageElastic', 15],
		['cse_tourniquet', 5],
		['DemoCharge_Remote_Mag', 4],
	]
