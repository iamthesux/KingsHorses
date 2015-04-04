import base

class cdf_base(base.Base):
	headgear = 'H_VTN_6B26'
	items = [
		'ItemWatch',
		'ItemMap',
		'ItemCompass',
	]	
	class HandGun:
		weapon = 'RH_mak'
		mags = [['RH_8Rnd_9x18_Mak', 8]]

	class Uniform:
		type = 'sh_cdf_uniform_01'
		items = base.Base.Uniform.items + [
			['RH_8Rnd_9x18_Mak', 2],
		]
	class Vest:
		type = 'V_CHICOM_KHAKI'
		items = [
			['rhs_mag_rdg2_white', 2],
			['Chemlight_blue', 1],
			['Chemlight_red', 1],
		]
	class Backpack:
		type = 'B_VTN_6SH92_FLORA'
		items = [
			['rhs_mag_rgd5', 2],
		]
################  Rifleman

class cdf_rifleman(cdf_base):
	class Primary:
		weapon = 'rhs_weap_akm'
		mags = [
			['rhs_30Rnd_762x39mm_tracer', 30],
		]
	class Vest(cdf_base.Vest):
		items = cdf_base.Vest.items + [
			['rhs_30Rnd_762x39mm', 5],
		]
	class Backpack(cdf_base.Backpack):
		items = cdf_base.Backpack.items + [
			['rhs_30Rnd_762x39mm_tracer', 5],
		]

class cdf_rifleman_light(cdf_base):
	class Primary:
		weapon = 'rhs_weap_ak74m_2mag'
		mags = [
			['rhs_30Rnd_545x39_AK_green', 30],
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

class cdf_grenadier(cdf_rifleman_light):
	class Primary:
		weapon = 'rhs_weap_ak74m_gp25'
		mags = [
			['rhs_30Rnd_545x39_AK_green', 30],
			['rhs_VOG25', 1],
		]

	class Secondary:
		weapon = 'rhs_weap_rpg26'
		mags = [
			['rhs_rpg26_mag', 1],
		]
	class Vest(cdf_rifleman_light.Vest):
		type = 'V_6SH104_AKGP'
		items = cdf_rifleman_light.Vest.items + [
			['rhs_VOG25', 5],
		]

	class Backpack(cdf_rifleman_light.Backpack):
		items = cdf_rifleman_light.Backpack.items + [
			['rhs_VOG25', 5],
			['rhs_GRD40_white', 5],
			['rhs_vg40op_white', 10],
		]

################  Squad Leader

class cdf_tl(cdf_rifleman):
	headgear = 'rhs_6b27m_green'
	items = cdf_rifleman.items + ['tf_anprc154']
	binoc = 'Binocular'

	class Primary:
		weapon = 'rhs_weap_akm_gp25'
		mags = [
			['rhs_30Rnd_762x39mm_tracer', 30],
			['rhs_VOG25', 1],
		]
	class Vest(cdf_rifleman.Vest):
		type = 'V_KORA_K_6Sh92GP'
		items = cdf_rifleman.Vest.items + [
			['rhs_VOG25', 5],
		]

	class Uniform(cdf_rifleman.Uniform):
		type = 'sh_cdf_uniform_02'
		items = cdf_rifleman.Uniform.items + [
			['cw_item_9liner_medivac', 1],
			['cw_item_9liner_cas', 1],
			['cw_item_5liner_gcff', 1],
		]
	class Backpack(cdf_rifleman.Backpack):
		items = cdf_rifleman.Backpack.items + [
			['rhsusf_ANPVS_14', 1],
			['rhs_GRD40_white', 5],
			['rhs_vg40op_white', 10],
			['rhs_GRD40_red', 5],
		]
		
class cdf_sl(cdf_tl):
	headgear = 'rhs_6b28_green'
	class Backpack(cdf_rifleman.Backpack):
		items = cdf_rifleman.Backpack.items + [
			['tf_fadak', 1],
		]
################  Vehicle Crew Driver/Gunner

class cdf_crew(cdf_rifleman):
	headgear = 'rhs_tsh4'
	items = cdf_base.items + ['tf_anprc154']

	class Primary:
		weapon = 'rhs_weap_akms'
		mags = [
			['rhs_30Rnd_762x39mm', 30],
		]
	class Backpack(cdf_rifleman_light.Backpack):
		items = cdf_rifleman_light.Backpack.items + [
			['rhsusf_ANPVS_14', 1],
		]
class cdf_asl_gunner(cdf_crew):
	class Backpack(cdf_crew.Backpack):
		items = cdf_crew.Backpack.items + [
			['rhsusf_ANPVS_14', 1],
			['tf_fadak', 1],
		]



################  Medium Machine Gunner
class cdf_mg(cdf_base):
	binoc = 'Binocular'
	class Primary:
		weapon = 'rhs_weap_pkm'
		mags = [
			['rhs_100Rnd_762x54mmR_green', 100],
		]
	class Vest(cdf_base.Vest):
		type = 'V_6SH104_PK'
		items = cdf_base.Vest.items + [
			['rhs_100Rnd_762x54mmR_green', 1],
		]
	class Backpack(cdf_base.Backpack):
		items = cdf_base.Backpack.items + [
			['rhs_100Rnd_762x54mmR', 2],
		]

################  Medic
class cdf_medic(cdf_rifleman_light):
	items = cdf_crew.items + [
		'tf_anprc154',
	]
	class Vest(cdf_rifleman_light.Vest):
		items = cdf_rifleman_light.Vest.items + [
			['cw_item_9liner_medivac', 1],
			['rhs_mag_rdg2_white', 2],
		]
	class Backpack(cdf_rifleman_light.Backpack):
		items = cdf_base.Backpack.items + base.MedicSupplies + [
			['rhs_mag_rdg2_white', 2],
		]


################  Platoon Leader

class cdf_pl(cdf_rifleman):
	items = cdf_rifleman.items + ['tf_anprc154']
	binoc = 'Binocular'
	headgear = 'H_VTN_BERET'
	class Primary:
		weapon = 'rhs_weap_akms'
		mags = [
			['rhs_30Rnd_762x39mm_tracer', 30],
		]
	class HandGun:
		weapon = 'rhs_weap_rsp30_white'
		mags = [
			['rhs_mag_rsp30_white', 1],
		]
	class Uniform(cdf_rifleman.Uniform):
		type = 'sh_cdf_uniform_02'
		items = cdf_rifleman.Uniform.items + [
			['cw_item_9liner_medivac', 1],
			['cw_item_9liner_cas', 1],
			['cw_item_5liner_gcff', 1],
		]
	class Vest(cdf_rifleman.Vest):
		type = 'V_KORA_K_CHICOM'
		items = cdf_base.Vest.items + [
			['tf_anprc152', 1],
			['rhs_30Rnd_762x39mm_tracer', 5],
		]
	class Backpack(cdf_base.Backpack):
		items = cdf_base.Backpack.items + [
			['rhs_weap_rsp30_white', 5],
			['rhs_mag_rdg2_white', 2],
			['rhsusf_ANPVS_14', 1],
		]

################  Platoon RTO

class cdf_rto(cdf_rifleman_light):
	binoc = 'Binocular'
	items = cdf_rifleman_light.items + ['tf_anprc154']
	class Backpack:
		type = 'tf_anprc155'
		items = cdf_rifleman_light.Backpack.items + [
			['tf_fadak', 1],
		]