import base

class det5_base(base.Base):
	class NoWrite: pass
	headgear = 'rhsusf_opscore_01'
	binoc = 'VTN_B15'
	items = base.Base.items + ['tf_pnr1000a']

	class HandGun:
		weapon = 'RH_mak'
		mags = [['RH_8Rnd_9x18_Mak', 8]]
		rail = 'RH_pmIR'
		suppressor = 'RH_pmsd'

	class Uniform:
		type = 'VTN_U_GORKA_S'
		items = base.Base.Uniform.items + [
			['cse_morphine', 2],
			['cse_epinephrine', 2],
			['RH_8Rnd_9x18_Mak', 2],
		]
	class Vest:
		type = 'V_KORA_K_CHICOM'
		items = [
			['VTN_RDG2B', 2],
		]
	class Backpack:
		type = 'B_VTN_6SH104_FLORA'
		items = [
			['VTN_PNV10T', 1],
			['alive_tablet', 1],
			['tf_anprc148jem', 1],
			['rhs_mag_rgd5', 2],
		]
	

class rifleman_det5(det5_base):
	class Primary:
		weapon = 'VTN_AK105_P'
		optic = 'VTN_OPTIC_EOTECH_553_B'
		rail = 'VTN_TPIAL_ANPEQ15_B'
		suppressor = 'VTN_MUZZLE_ATG'
		mags = [
			['VTN_AK74_30p_AP2', 30],
		]
	class Vest(det5_base.Vest):
		items = det5_base.Vest.items + [
			['VTN_AK74_30p_AP2', 2],
			['VTN_AK74_30p_TRC', 2],
		]

	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + [
			['VTN_AK74_30p_AP2', 2],
		]
		
class officer_det5(det5_base):
	class Primary:
		weapon = 'VTN_AK103_GP25'
		optic = 'VTN_OPTIC_1P76'
		suppressor = 'VTN_MUZZLE_ATG'
		mags = [
			['VTN_AK103_30p_SS', 30],
			['VTN_VOG25P', 1],
		]
	class Vest(det5_base.Vest):
		type = 'V_KORA_K_6Sh92GP'
		items = det5_base.Vest.items + [
			['tf_anprc148jem', 1],
			['VTN_AK103_30p_SS', 2],
			['VTN_AK103_30p_TRC', 2],
			['VTN_VOG25P', 4],
			['VTN_VG40TB', 4],

		]
	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + [
			['VTN_AK103_30p_SS', 2],
			['VTN_VG40MD', 6],
			['rhs_mag_rgd5', 1],
			['VTN_RDG2B', 3],
		]

class sniper_det5(det5_base):
	headgear = ''
	class Primary:
		weapon = 'rhs_weap_svdp'
		optic = 'rhs_acc_pso1m2'
		mags = [
			['rhs_10Rnd_762x54mmR_7N1', 10],
		]
	class Vest(det5_base.Vest):
		type = 'V_KORA_K_6Sh104SVD'
		items = det5_base.Vest.items + [
			['rhs_10Rnd_762x54mmR_7N1', 5],
		]
	class Backpack(det5_base.Backpack):
		type = 'B_AssaultPack_mcamo'
		items = det5_base.Backpack.items + [
			['rhs_10Rnd_762x54mmR_7N1', 5],
			['ClaymoreDirectionalMine_Remote_Mag', 2],
		]
		
class gunner_det5(det5_base):
	headgear = 'H_VTN_K6'
	class Primary:
		weapon = 'VTN_PKP'
		optic = 'VTN_OPTIC_1P77'
		mags = [
			['VTN_PK_100s_AP', 100],
		]
	class Vest(det5_base.Vest):
		type = 'V_KORA_K_6Sh104PK'
		items = det5_base.Vest.items + [
			['VTN_PK_100s_AP', 1],
			['VTN_PK_100s_API', 1],
		]
	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + [
			['VTN_PK_100s_AP', 1],
			['VTN_PK_100s_API', 1],
		]

class demolitions_det5(det5_base):
	headgear = 'H_VTN_SHAPKA_PSh'
	class Primary:
		weapon = 'VTN_SAIGA_MK03_T_AUTO'
		optic = 'VTN_OPTIC_TA_31RMR'
		rail = 'VTN_TPIAL_ANPEQ15_B'
		suppressor = 'VTN_MUZZLE_DTK4M'
		mags = [
			['VTN_SAIGA_10p_FMJ', 10],
		]
	class Secondary:
		weapon = 'VTN_MROA_C'
	class Vest(det5_base.Vest):
		type = 'V_KORA_K_6Sh92AK'
		items = det5_base.Vest.items + [
			['VTN_SAIGA_10p_FMJ', 10],
		]
	class Backpack(det5_base.Backpack):
		type = 'rhs_assault_umbts_demo'
		items = det5_base.Backpack.items + [
			['VTN_SAIGA_10p_FMJ', 10],
			['DemoCharge_Remote_Mag', 3],
		]
		
class medic_det5(det5_base):
	class Primary:
		weapon = 'VTN_AKMS_T_P'
		optic = 'VTN_OPTIC_DOCTOR'
		rail = 'VTN_TPIAL_ANPEQ15_B'
		suppressor = 'VTN_MUZZLE_PBS1'
		mags = [
			['VTN_AKM_30s_API', 30],
		]
	class Vest(det5_base.Vest):
		type = 'V_KORA_K_CHICOM'
		items = det5_base.Vest.items + [
			['VTN_AKM_30s_API', 4],
			['VTN_AKM_30s_TRC', 2],
		]
	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + base.MedicSupplies

class commo_det5(det5_base):
	headgear = 'rhsusf_opscore_02'
	class Primary:
		weapon = 'VTN_AK105_P'
		optic = 'VTN_OPTIC_TA_01NSN'
		rail = 'VTN_TPIAL_ANPEQ15_D'
		suppressor = 'VTN_MUZZLE_DTK4M'
		mags = [
			['VTN_AK74_30p_AP2', 30],
		]
	class Vest(det5_base.Vest):
		type = 'V_KORA_K_6Sh92AK'
		items = det5_base.Vest.items + [
			['VTN_AK74_30p_AP2', 4],
			['VTN_AK74_30p_TRC', 2],
			['tf_anprc148jem', 1],
		]
	class Backpack:
		type = 'VTN_BP_R168KNE_FLORA'
