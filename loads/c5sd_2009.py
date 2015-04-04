import base


#add fuccking lasers for rails
#snipers to box
#add chemlights for pubs

class det5_base(base.Base):
	class NoWrite: pass
	headgear = 'rhsusf_opscore_01'
	binoc = 'AGM_Vector'
	items = base.Base.items + [
		'ItemGPS',
		'tf_microdagr',
		'G_Balaclava_blk',
		'tf_pnr1000a',
	]

	class HandGun:
		weapon = 'RH_usp'
		mags = [['RH_12Rnd_45cal_usp', 12]]
		rail = 'RH_M6X'
		suppressor = 'RH_gemtech9'

	class Uniform:
		type = 'VTN_U_GORKA_S'
		items = base.Base.Uniform.items + [
			['cw_item_9liner_medivac', 1],
			['cw_item_9liner_cas', 1],
			['cw_item_5liner_gcff', 1],
			['cse_morphine', 2],
			['cse_epinephrine', 2],
			['RH_12Rnd_45cal_usp', 1],
		]
	class Vest:
		type = 'V_KORA_K_CHICOM'
		items = [
			['rhs_mag_rdg2_white', 2],
		]
	class Backpack:
		type = 'B_VTN_6SH104_FLORA'
		items = [
			['tf_anprc148jem', 2],
			['rhsusf_ANPVS_15', 1],
			['alive_tablet', 1],
			['rhs_mag_rgd5', 2],
		]
	

class rifleman_det5(det5_base):
	class Primary:
		weapon = 'rhs_weap_ak103_npz'
		optic = 'rhsusf_acc_eotech_552'
		suppressor = 'rhs_acc_pbs1'
		mags = [
			['rhs_30Rnd_762x39mm', 30],
		]
	class Vest(det5_base.Vest):
		items = det5_base.Vest.items + [
			['rhs_30Rnd_762x39mm_tracer', 2],
			['rhs_30Rnd_762x39mm', 2],
		]

	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + [
			['ACRE_PRC152', 1],
			['rhs_30Rnd_762x39mm', 2],
		]
		
class officer_det5(det5_base):
	class Primary:
		weapon = 'rhs_weap_ak74m_gp25_npz'
		optic = 'rhsusf_acc_eotech_552'
		suppressor = 'rhs_acc_tgpa'
		mags = [
			['rhs_30Rnd_545x39_7n22_AK', 30],
			['rhs_VOG25p', 1],
		]
	class Vest(det5_base.Vest):
		type = 'V_KORA_K_6Sh92GP'
		items = det5_base.Vest.items + [
			['rhs_30Rnd_545x39_7n22_AK', 2],
			['rhs_30Rnd_545X39_AK_Green', 2],
			['rhs_VOG25p', 4],
			['rhs_vg40tb', 4],

		]
	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + [
			['rhs_30Rnd_545x39_7n22_AK', 2],
			['rhs_VOG25p', 6],
			['rhs_vg40op_white', 2],
			['rhs_GRD40_white', 2],
			['rhs_GRD40_red', 2],
			['rhs_GRD40_green', 2],
			['rhs_mag_rgd5', 1],
			['rhs_mag_rdg2_white', 3],
		]

class sniper_det5(det5_base):
	headgear = ''
	class Primary:
		weapon = 'RH_Mk12mod1'
		optic = 'RH_leu_mk4'
		suppressor = 'RH_spr_mbs'
		rail = 'RH_peq15b'
		mags = [
			['RH_30Rnd_556x45_Mk262', 30],
		]
	class Vest(det5_base.Vest):
		type = 'V_KORA_K_6Sh104SVD'
		items = det5_base.Vest.items + [
			['RH_30Rnd_556x45_Mk262', 5],
		]
	class Backpack(det5_base.Backpack):
		type = 'B_AssaultPack_mcamo'
		items = det5_base.Backpack.items + [
			['30Rnd_556x45_Stanag_Tracer_Green', 5],
			['ClaymoreDirectionalMine_Remote_Mag', 2],
		]
		
class gunner_det5(det5_base):
	headgear = 'H_VTN_K6'
	class Primary:
		weapon = 'rhs_weap_pkp'
		optic = 'rhs_acc_pkas'
		rail = 'rhs_bipod'
		mags = [
			['rhs_100Rnd_762x54mmR', 100],
		]
	class Vest(det5_base.Vest):
		type = 'V_KORA_K_6Sh104PK'
		items = det5_base.Vest.items + [
			['rhs_100Rnd_762x54mmR', 1],
			['rhs_100Rnd_762x54mmR_green', 1],
		]
	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + [
			['rhs_100Rnd_762x54mmR', 1],
			['rhs_100Rnd_762x54mmR_green', 1],
		]

class demolitions_det5(det5_base):
	headgear = 'H_VTN_SHAPKA_PSh'
	class Primary:
		weapon = 'rhs_weap_ak74m_2mag_npz'
		optic = 'rhsusf_acc_eotech_552'
		suppressor = 'rhs_acc_tgpa'
		mags = [
			['rhs_45Rnd_545x39_7n22_AK', 45],
		]
	class Secondary:
		weapon = 'rhs_weap_rpg7'
		mags = [
			['rhs_rpg7_PG7VL_mag', 1],
		]
	class Vest(det5_base.Vest):
		type = 'V_KORA_K_6Sh92AK'
		items = det5_base.Vest.items + [
			['rhs_45Rnd_545x39_7n22_AK', 2],
			['rhs_45Rnd_545X39_AK_Green', 2],
		]
	class Backpack(det5_base.Backpack):
		type = 'rhs_assault_umbts_demo'
		items = det5_base.Backpack.items + [
			['rhs_rpg7_PG7VL_mag', 2],
			['rhs_45Rnd_545x39_7n22_AK', 2],
			['rhs_45Rnd_545X39_AK_Green', 2],
			['DemoCharge_Remote_Mag', 3],
		]

class medic_det5(det5_base):
	class Primary:
		weapon = 'rhs_weap_ak103_npz'
		optic = 'rhsusf_acc_compm4'
		suppressor = 'rhs_acc_pbs1'
		mags = [
			['rhs_30Rnd_762x39mm', 30],
		]
	class Vest(det5_base.Vest):
		type = 'V_KORA_K_CHICOM'
		items = det5_base.Vest.items + [
			['rhs_30Rnd_762x39mm_tracer', 2],
			['rhs_30Rnd_762x39mm', 4],
		]
	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + base.MedicSupplies

class medic_det5_1tk(medic_det5):
	headgear = 'rhsusf_opscore_01_1tk'
	class Uniform(medic_det5.Uniform):
		type = 'VTN_U_GORKA_S_1tk'
	class Primary(medic_det5.Primary):
		weapon = 'rhs_weap_ak103_npz_1tk'

class commo_det5(det5_base):
	headgear = 'rhsusf_opscore_02'
	class Primary:
		weapon = 'rhs_weap_ak74m_2mag_npz'
		optic = 'rhsusf_acc_eotech_552'
		suppressor = 'rhs_acc_tgpa'
		mags = [
			['rhs_45Rnd_545x39_7n22_AK', 45],
		]
	class Vest(det5_base.Vest):
		type = 'V_KORA_K_6Sh92AK'
		items = det5_base.Vest.items + [
			['tf_anprc148jem', 2],
			['rhs_45Rnd_545x39_7n22_AK', 4],
			['rhs_45Rnd_545X39_AK_Green', 2],
		]
	class Backpack:
		type = 'VTN_BP_R168KNE_FLORA'
