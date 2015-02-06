from base import Base

class cdf_base(Base):
	headgear = 'LOP_H_PASGTHelmet_cover_CDF'
	
	class HandGun:
		weapon = 'RH_mak'
		mags = [['RH_8Rnd_9x18_Mak', 8]]

	class Uniform:
		type = 'LOP_U_CDF_Fatigue_01'
		items = Base.Uniform.items + [
			['RH_8Rnd_9x18_Mak', 2],
		]
	class Vest:
		type = 'LOP_V_CarrierLite_CDF'
		items = [
			['rhs_mag_rgd5', 1],
			['rhs_mag_rdg2_white', 1],
		]
	class Backpack:
		type = 'B_Kitbag_mcamo'
		items = [
			['rhs_mag_rdg2_white', 1],
			['rhs_mag_rgd5', 2],
		]
################  Rifleman

class cdf_rifleman(cdf_base):
	class Primary:
		weapon = 'rhs_weap_ak74m'
		mags = [
			['rhs_30Rnd_545x39_AK', 30],
		]
	class Vest(cdf_base.Vest):
		items = cdf_base.Vest.items + [
			['rhs_30Rnd_545x39_AK', 5],
		]
	class Backpack(cdf_base.Backpack):
		items = cdf_base.Backpack.items + [
			['rhs_30Rnd_545x39_AK_green', 5],
		]

################  Grenadier 

class cdf_grenadier(cdf_rifleman):
	class Primary:
		weapon = 'rhs_weap_ak74m_gp25'
		mags = [
			['rhs_30Rnd_545x39_AK', 30],
			['rhs_VOG25', 1],
		]
	class Secondary:
		weapon = 'rhs_weap_rpg26'
		mags = [
			['rhs_rpg26_mag', 1],
		]
	class Vest(cdf_rifleman.Vest):
		type = 'LOP_V_CarrierRig_CDF'
		items = cdf_rifleman.Vest.items + [
			['rhs_VOG25', 5],
		]

	class Backpack(cdf_rifleman.Backpack):
		items = cdf_rifleman.Backpack.items + [
			['rhs_VOG25', 5],
		]

################  Squad Leader

class cdf_sl(cdf_rifleman):
	items = cdf_rifleman.items + [
		'tf_anprc152_2',
	]
	binoc = 'Binocular'

	class Primary:
		weapon = 'rhs_weap_ak74m_gp25'
		mags = [
			['rhs_30Rnd_545x39_AK', 30],
			['rhs_VOG25', 1],
		]
	class Vest(cdf_rifleman.Vest):
		type = 'LOP_V_CarrierRig_CDF'
		items = cdf_rifleman.Vest.items + [
			['rhs_VOG25', 5],
		]

	class Backpack(cdf_rifleman.Backpack):
		items = cdf_rifleman.Backpack.items + [
			['rhs_vg40op_white', 5],
			['rhs_GRD40_white', 2],
			['rhs_GRD40_green', 2],
			['rhs_GRD40_red', 2],
			['rhs_VOG25', 5],
			['rhs_VOG25p', 2],
		]

################  Vehicle Crew Driver/Gunner

class cdf_crew(cdf_rifleman):
	class Primary:
		weapon = 'rhs_weap_ak74m_folded'
		mags = [
			['rhs_30Rnd_545x39_AK', 30],
		]

class cdf_asl_gunner(cdf_crew):
	items = cdf_crew.items + [
		'tf_anprc152_2',
	]


################  Medium Machine Gunner
class cdf_mg(cdf_base):
	class Primary:
		weapon = 'rhs_weap_pkp'
		mags = [
			['rhs_100Rnd_762x54mmR', 100],
		]
	class Vest(cdf_base.Vest):
		items = cdf_base.Vest.items + [
			['rhs_100Rnd_762x54mmR', 1],
		]
	class Backpack(cdf_base.Backpack):
		items = cdf_base.Backpack.items + [
			['rhs_100Rnd_762x54mmR', 2],
		]

################  Medic
class cdf_medic(cdf_rifleman):
	class Vest(cdf_base.Vest):
		items = cdf_base.Vest.items + [
			['rhs_100Rnd_762x54mmR', 1],
			['rhs_mag_rdg2_white', 4],
		]
	class Backpack(cdf_rifleman.Backpack):
		items = cdf_rifleman.Backpack.items + [
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
	binoc = 'Binocular'

	class Primary:
		weapon = 'rhs_weap_ak74m_gp25'
		mags = [
			['rhs_30Rnd_545x39_AK', 30],
			['rhs_VOG25', 1],
		]
	class Vest(cdf_rifleman.Vest):
		type = 'LOP_V_CarrierRig_CDF'
		items = cdf_rifleman.Vest.items + [
			['rhs_VOG25', 5],
		]

	class Backpack(cdf_rifleman.Backpack):
		items = cdf_rifleman.Backpack.items + [
			['rhs_vg40op_white', 5],
			['rhs_GRD40_white', 2],
			['rhs_GRD40_green', 2],
			['rhs_GRD40_red', 2],
			['rhs_VOG25', 5],
			['rhs_VOG25p', 2],
			['alive_tablet', 1],
		]

################  Platoon RTO

class cdf_rto(cdf_rifleman):
	binoc = 'Binocular'
	items = cdf_rifleman.items + [
		'tf_anprc152_2',
	]
	class Primary:
		weapon = 'rhs_weap_ak74m'
		mags = [
			['rhs_30Rnd_545x39_AK', 30],
		]

	class Backpack:
		type = 'tf_anprc155_coyote'
		items = cdf_rifleman.Backpack.items + [
			['tf_anprc148_2', 1],
		]