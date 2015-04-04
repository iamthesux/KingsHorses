from p4a.loadout import Crate
 
class marine_explosives(Crate):
	title = 'Marine Explosives and CSW'
	base = 'CUP_USSpecialWeaponsBox'
	magazines = [
		['rhs_mag_m67', 100],
		['rhs_mag_an_m8hc', 100],
		['rhs_mag_m18_purple', 100],
		['rhs_mag_m18_green', 100],
		['rhs_mag_m18_red', 100],
		['rhs_mag_m18_yellow', 100],
		['rhs_mine_M19_mag', 100],
		['SatchelCharge_Remote_Mag', 100],
		['DemoCharge_Remote_Mag', 100],

		['rhs_mag_M433_HEDP', 200],
		['rhs_mag_M585_white', 200],
		['rhs_mag_M661_green', 500],
		['rhs_mag_M662_red', 500],
		['rhs_mag_M713_red', 500],
		['rhs_mag_M714_white', 500],
		['rhs_mag_M715_green', 300],
		['rhs_mag_M716_yellow', 300],
	]
	backpacks = [
		['RHS_M2_MiniTripod_Bag', 10],
		['RHS_M2_Gun_Bag', 10],
		['RHS_Mk19_Tripod_Bag', 10],
		['RHS_Mk19_Gun_Bag', 10],
	]
 
class marine_launchers(Crate):
	title = 'Marine Launchers and Warheads'
	base = 'CUP_USBasicWeaponsBox'
	weapons = [
		['rhs_weap_fgm148', 10],
		['rhs_weap_M136', 400],
		['rhs_weap_M136_hedp', 400],
		['rhs_weap_M136_hp', 400],
	]
	magazines = [		
		['rhs_m136_mag', 400],
		['rhs_m136_hedp_mag', 400],
		['rhs_m136_hp_mag', 400],
		['rhs_fgm148_magazine_AT', 400],
	]
class marine_weapons(Crate):
	title = 'Marine Rifles and Ammo'
	base = 'CUP_USBasicWeaponsBox'
	weapons = [
	]
	magazines = [
		['rhs_mag_30Rnd_556x45_M855A1_Stanag', 200],
		['rhs_mag_30Rnd_556x45_M855A1_Stanag_No_Tracer', 200],
		['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 200],
		
		['rhsusf_100Rnd_556x45_soft_pouch', 500],
		['rhsusf_200Rnd_556x45_soft_pouch', 300],

		['rhsusf_100Rnd_762x51', 500],

		['RH_15Rnd_9x19_M9', 85],
	]

class marine_radios(Crate):
	title = 'Marine Radios'
	base = 'CUP_USBasicAmmunitionBox'
	items = [
		['tf_anprc152', 50],
	]
	backpacks = [
		['tf_rt1523g_big', 10],
	]