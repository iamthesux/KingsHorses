class CfgPatches
{
	class sh_vtn_groups
	{
		units[]= {
			"sh_chdkz_bmp1",
			"sh_chdkz_t72ba",
			"sh_chdkz_btr80"
		};
		weapons[]={};
		requiredVersion=0.10000000149;
		requiredAddons[]={"VTN_SOLDIER"};
	};
};

class CfgFactionClasses
{
	class sh_opfor_chdkz
	{
		displayName="ChDKZ";
		priority=1;
		side=2;
		icon="\vtn_core_structure\ico\cfgfactionclasses_insurgents_ca.paa";
		backpack_tf_faction_radio_api="VTN_BP_R168KNE_FLORA";
	};
};
class CfgVehicles
{
	class rhs_bmp1_vv;
	class rhs_t72ba_tv;
	class rhs_btr80_msv;
	class B_VTN_6SH11;
	class VTN_MILITIA_RFL;
	class sh_chdkz_bmp1 : rhs_bmp1_vv
	{
		_generalMacro="sh_chdkz_bmp1";
		scope=2;
		side=2;
		faction="sh_opfor_chdkz";
		crew="VTN_MILITIA_RTO";
		typicalCargo[]={"VTN_MILITIA_RTO"};
		vehicleClass="Armored";
	};
	class sh_chdkz_t72ba : rhs_t72ba_tv
	{
		_generalMacro="sh_chdkz_t72ba";
		scope=2;
		side=2;
		faction="sh_opfor_chdkz";
		crew="VTN_MILITIA_RTO";
		typicalCargo[]={"VTN_MILITIA_RTO"};
		vehicleClass="Armored";
	};
	class sh_chdkz_btr80 : rhs_btr80_msv
	{
		_generalMacro="sh_chdkz_btr80";
		scope=2;
		side=2;
		faction="sh_opfor_chdkz";
		crew="VTN_MILITIA_RTO";
		typicalCargo[]={"VTN_MILITIA_RTO"};
		vehicleClass="Armored";
	};
	class B_VTN_6SH11_V : B_VTN_6SH11
	{
		author="$STR_DN_VTN";
		scope=1;
		showinArsenal=0;
		class TransportMagazines
		{
			class _xx_rhs_rpg7_PG7VL_mag
			{
				magazine="rhs_rpg7_PG7VL_mag";
				count=4;
			};
		};
	};
	class VTN_MILITIA_ATS1: VTN_MILITIA_RFL
	{
		author = "$STR_DN_VTN";
		_generalMacro = "VTN_MILITIA_ATS1";
		displayName = "$STR_DN_VTN_RFMI_ATS1";
		uniformClass = "VTN_U_ABIBAS8";
		model = "\vtn_u_adidas_md\abibas_trackjacket.p3d";
		hiddenSelections[] = {"camo","camo1","civ1"};
		hiddenSelectionsTextures[] = {"\vtn_u_adidas_tx\tj_2_co.paa","\vtn_u_adidas_tx\pants_2_co.paa","\vtn_u_adidas_tx\trainers_co.paa"};
		icon = "\vtn_core_taktisigns\ru\personnel\vtn_g_ca.paa";
		weapons[] = {"VTN_AKS74U_79","rhs_weap_rpg7","Throw","Put"};
		respawnWeapons[] = {"VTN_AKS74U_79","rhs_weap_rpg7","Throw","Put"};
		magazines[] = {"VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_KHATTABKA_VOG17","VTN_KHATTABKA_VOG17","VTN_KHATTABKA_VOG17","VTN_KHATTABKA_VOG17"};
		respawnMagazines[] = {"VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_KHATTABKA_VOG17","VTN_KHATTABKA_VOG17","VTN_KHATTABKA_VOG17","VTN_KHATTABKA_VOG17"};
		linkedItems[] = {"V_CHICOM_KHAKI","H_VTN_SHAPKA_PSh","ItemWatch"};
		respawnLinkedItems[] = {"V_CHICOM_KHAKI","H_VTN_SHAPKA_PSh","ItemWatch"};
		backpack = "B_VTN_6SH11_V";
	};
	class VTN_MILITIA_AT: VTN_MILITIA_RFL
	{
		author = "$STR_DN_VTN";
		_generalMacro = "VTN_MILITIA_AT";
		displayName = "$STR_DN_VTN_RFMI_AT2";
		icon = "\vtn_core_taktisigns\ru\personnel\vtn_g_ca.paa";
		uniformClass = "VTN_U_ABIBAS9";
		model = "\vtn_u_adidas_md\abibas_trackjacket.p3d";
		hiddenSelections[] = {"camo","camo1","civ1"};
		hiddenSelectionsTextures[] = {"\vtn_u_adidas_tx\tj_4_co.paa","\vtn_u_adidas_tx\pants_4_co.paa","\vtn_u_adidas_tx\trainers_co.paa"};
		weapons[] = {"VTN_AKS74U_79","rhs_weap_rpg26","Throw","Put"};
		respawnWeapons[] = {"VTN_AKS74U_79","rhs_weap_rpg26","Throw","Put"};
		magazines[] = {"rhs_rpg26_mag","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30ps_SC","VTN_AK74_30ps_SC","VTN_AK74_30ps_SC","VTN_AK74_30ps_SC","VTN_KHATTABKA_VOG17","VTN_KHATTABKA_VOG17","VTN_KHATTABKA_VOG17","VTN_KHATTABKA_VOG17"};
		respawnMagazines[] = {"rhs_rpg26_mag","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30b_SC","VTN_AK74_30ps_SC","VTN_AK74_30ps_SC","VTN_AK74_30ps_SC","VTN_AK74_30ps_SC","VTN_KHATTABKA_VOG17","VTN_KHATTABKA_VOG17","VTN_KHATTABKA_VOG17","VTN_KHATTABKA_VOG17"};
		linkedItems[] = {"V_CHICOM_KHAKI","ItemWatch"};
		respawnLinkedItems[] = {"V_CHICOM_KHAKI","ItemWatch"};
	};
};

