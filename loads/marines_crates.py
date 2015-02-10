from p4a.loadout import Crate
 
class marine_explosives(Crate):
	title = 'Marine Explosives and CSW'
	base = 'CUP_USVehicleBox'
	magazines = [
		['rhs_mag_m67', 100],
		['SmokeShell', 100],
		['SmokeShellBlue', 100],
		['SmokeShellGreen', 100],
		['SmokeShellOrange', 100],
		['SmokeShellRed', 100],
		['SmokeShellYellow', 100],
		['DemoCharge_Remote_Mag', 100],

		['1Rnd_HE_Grenade_shell', 100],
		['1Rnd_SmokeGreen_Grenade_shell', 100],
		['1Rnd_SmokeRed_Grenade_shell', 100],
		['1Rnd_Smoke_Grenade_shell', 100],
		['UGL_FlareRed_F', 100],
		['UGL_FlareWhite_F', 100],
		['UGL_FlareYellow_F', 100],
		['UGL_FlareGreen_F', 100],
	]
	backpacks = [
		['RHS_M2_MiniTripod_Bag', 10], 
		['RHS_M2_Gun_Bag', 10],
		['RHS_Mk19_Gun_Bag', 10],
		['RHS_Mk19_Tripod_Bag', 10],
		['RDS_Tow_Gun_Bag', 10],
		['RDS_TOW_Tripod_Bag', 10],
	]
 
class marine_launchers(Crate):
	title = 'Marine Launchers and Warheads'
	base = 'CUP_USVehicleBox'
	weapons = [
		['rhs_weap_fgm148', 50],
		['rhs_weap_M136', 35],
		['rhs_weap_M136_hedp', 35],
		['rhs_weap_M136_hp', 35],
	]
	magazines = [
		['rhs_m136_mag', 35],
		['rhs_m136_hedp_mag', 35],
		['rhs_m136_hp_mag', 35],
		['rhs_fgm148_magazine_AT', 50],
	]
 
class marine_weapons(Crate):
	title = 'Marine Rifles and Ammo'
	base = 'CUP_USVehicleBox'
	weapons = [
		['RH_M16A4gl', 15],
		['rhs_weap_m249_pip', 10],
		['rhs_weap_m16a4_carryhandle', 25],
		['CUP_hgun_M9', 10],
	]
	magazines = [
		['rhs_mag_30Rnd_556x45_M855A1_Stanag', 200],
		['rhsusf_100Rnd_556x45_soft_pouch', 100],
		['30Rnd_556x45_Stanag_Tracer_Red', 100],
		['CUP_15Rnd_9x19_M9', 85],
	]

class marine_radios(Crate):
	title = 'Marine Radios'
	base = 'CUP_USBasicAmmunitionBox'
	items = [
		['tf_rf7800str_1', 75],
		['tf_anprc152_2', 75],
		['tf_anprc148jem', 100],
	]

	backpacks = [            
		['tf_rt1523g_rhs', 25],
	]