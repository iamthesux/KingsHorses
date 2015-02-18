from p4a.loadout import Crate
from base import Base

class soar_pilot(Base):
	headgear = 'H_ZSH7V'
	
	items = Base.items + [
		'tf_anprc152',
	]
	class Primary:
		weapon = 'VTN_AKS74U_79'
		suppressor = 'VTN_MUZZLE_FS_AKS74U'
		mags = [['VTN_AK74_30b_TRC', 30],]

	class HandGun:
		weapon = 'RH_mak'
		rail = 'RH_pmIR'
		mags = [['RH_8Rnd_9x18_Mak', 8]]

	class Uniform:
		type = 'VTN_VVS_VKK15'
		items = Base.Uniform.items + [
			['VTN_AK74_30b_TRC', 2],
			['RH_8Rnd_9x18_Mak', 2],
		]
	class Vest:
		type = 'rhs_vest_commander'
		items = [
			['VTN_NSPD', 2],
			['tf_anprc152', 1],
		]

class soar_crew(soar_pilot):
	headgear = 'H_ZSH7VS'
	

class soar_vehicle(Crate):
	weapons = [
		['VTN_SP81', 1],
		['VTN_RSP30_RED', 1],
		['VTN_RSP30_GREEN', 1],
		['VTN_RSP30_WHITE', 1],
	]
	magazines = [
		['VTN_OP_1k_WHITE', 10],
		['VTN_SP_1k_GREEN', 10],
		['VTN_SP_1k_RED', 10],
		['VTN_AK74_30b_SC', 45],
		['VTN_AK74_30b_TRC', 15],
		['VTN_NSPD', 5],
		['VTN_NSP_RED', 5],
		['VTN_NSP_GREEN', 5],
		['VTN_NSP_YELLOW', 5],
		['VTN_RGO', 10],
		['cse_bandage_basic', 25],
		['cse_bandageElastic', 15],
		['cse_tourniquet', 5],
		['DemoCharge_Remote_Mag', 1],
	]
	backpacks = [
		['rhs_sidor', 2]
	]

