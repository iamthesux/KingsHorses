from base import Base

class cdf_base(Base):
	headgear = 'H_VTN_6B26'
	
	class HandGun:
		weapon = 'RH_mak'
		mags = [['RH_8Rnd_9x18_Mak', 8]]

	class Uniform:
		type = 'sh_cdf_uniform_01'
		items = Base.Uniform.items + [
			['RH_8Rnd_9x18_Mak', 2],
		]
	class Vest:
		type = 'sh_chdkz_v_carrierlite_cdf'
		items = [
			['rhs_mag_rgd5', 1],
			['rhs_mag_rdg2_white', 1],
		]
	class Backpack:
		type = 'B_Kitbag_rgr'
		items = [
			['rhs_mag_rdg2_white', 1],
			['rhs_mag_rgd5', 2],
		]
################  Rifleman

class cdf_rifleman(cdf_base):
	class Primary:
		weapon = 'VTN_AKM'
		mags = [
			['VTN_AKM_30b_TRC', 30],
		]
	class Vest(cdf_base.Vest):
		items = cdf_base.Vest.items + [
			['VTN_AKM_30b_SC', 5],
		]
	class Backpack(cdf_base.Backpack):
		items = cdf_base.Backpack.items + [
			['VTN_AKM_30b_TRC', 5],
		]

class cdf_rifleman_light(cdf_base):
	class Primary:
		weapon = 'VTN_AK74_76'
		mags = [
			['VTN_AKM_30b_TRC', 30],
		]
	class Vest(cdf_base.Vest):
		items = cdf_base.Vest.items + [
			['VTN_AK74_30b_SC', 5],
		]
	class Backpack(cdf_base.Backpack):
		items = cdf_base.Backpack.items + [
			['VTN_AK74_30b_TRC', 5],
		]

		
################  Grenadier 

class cdf_grenadier(cdf_rifleman_light):
	class Primary:
		weapon = 'VTN_AK74_GP25'
		mags = [
			['VTN_AK74_30b_TRC', 30],
			['VTN_VOG25', 1],
		]
	class Secondary:
		weapon = 'rhs_weap_rpg26'
		mags = [
			['rhs_rpg26_mag', 1],
		]
	class Vest(cdf_rifleman_light.Vest):
		type = 'sh_chdkz_v_carrier_cdf'
		items = cdf_rifleman_light.Vest.items + [
			['VTN_AK74_30b_TRC', 5],
			['VTN_VOG25', 5],
		]

	class Backpack(cdf_rifleman_light.Backpack):
		items = cdf_rifleman_light.Backpack.items + [
			['VTN_AK74_30b_SC', 5],
			['VTN_VOG25P', 5],
			['VTN_VG40MD', 5],
			['VTN_VG40OP', 10],
		]

################  Squad Leader

class cdf_sl(cdf_rifleman):
	headgear = 'rhs_6b28_green'
	items = cdf_rifleman.items + [
		'tf_rf7800str',
	]
	binoc = 'VTN_B8'

	class Primary:
		weapon = 'VTN_AKM_GP25_30b'
		mags = [
			['VTN_AKM_30b_TRC', 30],
			['VTN_VOG25', 1],
		]
	class Vest(cdf_rifleman.Vest):
		type = 'sh_chdkz_v_carrier_cdf'
		items = cdf_rifleman.Vest.items + [
			['VTN_VOG25P', 5],
		]

	class Backpack(cdf_rifleman.Backpack):
		items = cdf_rifleman.Backpack.items + [
			['VTN_VG40MD', 5],
			['VTN_VG40OP', 10],
			['VTN_VGS401', 5],
			['VTN_VGS402', 5],
			['VTN_BN1', 1],
		]
		
class cdf_tl(cdf_sl):
	headgear = 'rhs_6b27m_green'
################  Vehicle Crew Driver/Gunner

class cdf_crew(cdf_rifleman_light):
	headgear = 'rhs_tsh4'
	class Primary:
		weapon = 'VTN_AKS74U_B'
		mags = [
			['VTN_AK74_30b_SC', 30],
		]
	class Backpack:
		pass
class cdf_asl_gunner(cdf_crew):
	items = cdf_crew.items + [
		'tf_rf7800str',
	]


################  Medium Machine Gunner
class cdf_mg(cdf_base):
	binoc = 'VTN_B8'
	class Primary:
		weapon = 'VTN_PKM'
		mags = [
			['VTN_PK_100s_TRC', 100],
		]
	class Vest(cdf_base.Vest):
		items = cdf_base.Vest.items + [
			['VTN_PK_100s_TRC', 1],
		]
	class Backpack(cdf_base.Backpack):
		items = cdf_base.Backpack.items + [
			['VTN_PK_100s_SC', 2],
			['VTN_MUZZLE_FLASHSUPRESSOR_PKM1', 1],
		]

################  Medic
class cdf_medic(cdf_rifleman_light):
	class Primary:
		weapon = 'VTN_AKS74U_B'
		mags = [
			['VTN_AK74_30b_TRC', 30],
		]
	class Vest(cdf_rifleman_light.Vest):
		items = cdf_rifleman_light.Vest.items + [
			['rhs_mag_rdg2_white', 4],
		]
	class Backpack(cdf_rifleman_light.Backpack):
		items = cdf_rifleman_light.Backpack.items + [
			['rhs_mag_rdg2_black', 5],
			['cse_bandage_basic', 5],
			['cse_bandageElastic', 7],
			['cse_packing_bandage', 7],
			['cse_quikclot', 7],
			['cse_tourniquet', 3],
			['cse_nasopharyngeal_tube', 2],
		]


################  Platoon Leader

class cdf_pl(cdf_rifleman):
	items = cdf_rifleman.items + [
		'tf_anprc152_2',
	]
	binoc = 'VTN_B8'
	headgear = 'H_VTN_BERET'
	class Primary:
		weapon = 'VTN_AKMS_P'
		optic = 'VTN_6CH3'
		suppressor = 'VTN_MUZZLE_DTK1L'
		mags = [
			['VTN_AKM_30s_TRC', 30],
		]
	class HandGun:
		weapon = 'VTN_SP81'
		mags = [
			['VTN_OP_1k_WHITE', 1],
		]
	class Backpack(cdf_rifleman.Backpack):
		items = cdf_rifleman.Backpack.items + [
			['VTN_OP_1k_WHITE', 10],
			['VTN_SP_1k_RED', 2],
			['VTN_SP_1k_GREEN', 2],
			['VTN_SP_1k_YELLOW', 2],
			['rhs_mag_rdg2_white', 4],
			['VTN_AKM_30s_TRC', 5],
			['VTN_BN1', 1],
			['alive_tablet', 1],
		]

################  Platoon RTO

class cdf_rto(cdf_rifleman_light):
	binoc = 'VTN_B8'
	items = cdf_rifleman.items + [
		'tf_anprc152',
	]
	class Backpack:
		type = 'tf_rt1523g_green'
		items = cdf_rifleman.Backpack.items + [
			['tf_anprc152', 1],
		]