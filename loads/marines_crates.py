from p4a.loadout import Crate
 
class marine_explosives(Crate):
	title = 'Marine Explosives and CSW'
	base = 'B_supplyCrate_F'
	magazines = [
		['rhs_mag_m67', 100],
		['SmokeShell', 100],
		['SmokeShellBlue', 100],
		['SmokeShellGreen', 100],
		['SmokeShellOrange', 100],
		['SmokeShellRed', 100],
		['SmokeShellYellow', 100],
		['DemoCharge_Remote_Mag', 100],

		['VTN_M406', 200],
		['VTN_M433', 200],
		['VTN_M583A1', 500],
		['VTN_M585', 500],
		['VTN_M661', 500],
		['VTN_M662', 500],
		['VTN_M713', 300],
		['VTN_M714', 300],
		['VTN_M715', 300],
		['VTN_M716', 300],
		['VTN_M992', 50],
		
	]
	backpacks = [
		['RHS_M2_MiniTripod_Bag', 10],
		['RHS_M2_Gun_Bag', 10],
	]
 
class marine_launchers(Crate):
	title = 'Marine Launchers and Warheads'
	base = 'B_supplyCrate_F'
	weapons = [
		['rhs_weap_fgm148', 10],
		['rhs_weap_M136', 200],
		['rhs_weap_M136_hedp', 200],
		['rhs_weap_M136_hp', 200],
		['VTN_MK153MOD0', 10],
	]
	magazines = [
		['VTN_MK3MOD0', 200],
		['VTN_MK6MOD0', 200],
		['VTN_MK80MOD0', 100],
		
		['rhs_m136_mag', 200],
		['rhs_m136_hedp_mag', 200],
		['rhs_m136_hp_mag', 200],
		['rhs_fgm148_magazine_AT', 200],
	]
class marine_weapons(Crate):
	title = 'Marine Rifles and Ammo'
	base = 'B_supplyCrate_F'
	weapons = [
		['VTN_C_M4A1', 10],
		['VTN_C_M4A1_M203', 10],
		['VTN_FN_M16A4', 50],
		['VTN_FN_M16A4_M203', 10],
		['VTN_M249_SAW', 10],
		['VTN_M240G', 10],
		
		['RH_m9', 10],
	]
	magazines = [
		['VTN_M249_100c_SC', 200],
		['VTN_M249_100c_TRC', 200],
		['VTN_M249_100c_TRCN', 200],
		
		['VTN_M249_200c_SC', 200],
		['VTN_M249_200c_TRC', 200],
		['VTN_M249_200c_TRCN', 200],

		['VTN_M240_50c_SC', 200],
		['VTN_M240_50c_TRC', 200],
		['VTN_M240_50c_TRCN', 200],
		
		['VTN_M240_100c_SC', 200],
		['VTN_M240_100c_TRC', 200],
		['VTN_M240_100c_TRCN', 200],
		
		['VTN_STANAG4172_30p_SC', 500],
		['VTN_STANAG4172_30p_TRC', 500],
		['VTN_STANAG4172_30p_TRCN', 500],

		['RH_15Rnd_9x19_M9', 85],
	]

class marine_radios(Crate):
	title = 'Marine Radios'
	base = 'B_supplyCrate_F'
	items = [
		['tf_rf7800str', 100],
		['tf_anprc152', 40],
		['tf_anprc152', 40],
	]

	backpacks = [
		['tf_rt1523g_big', 4],
	]