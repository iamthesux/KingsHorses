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

class CfgGroups
{
	class Indep
	{
		class sh_opfor_chdkz
		{
			name="ChDKZ";
			class Infantry
			{
				name="Infantry";
				class sh_chdkz_rifle_squad
				{
					name="Rifle Squad";
					faction="sh_opfor_chdkz";
					side=2;
					class Unit0
					{
						side=2;
						vehicle="VTN_MILITIA_RTO";
						rank="SERGEANT";
						position[]={0, 0, 0};
					};
					class Unit1
					{
						side=2;
						vehicle="VTN_MILITIA_SL";
						rank="SERGEANT";
						position[]={5, -5, 0};
					};
					class Unit2
					{
						side=2;
						vehicle="VTN_MILITIA_GMG1";
						rank="CORPORAL";
						position[]={-5, -5, 0};
					};
					class Unit3
					{
						side=2;
						vehicle="VTN_MILITIA_ATS1";
						rank="PRIVATE";
						position[]={10, -10, 0};
					};
					class Unit4
					{
						side=2;
						vehicle="VTN_MILITIA_RFL";
						rank="PRIVATE";
						position[]={-10, -10, 0};
					};
					class Unit5
					{
						side=2;
						vehicle="VTN_MILITIA_AT";
						rank="CORPORAL";
						position[]={15, -15, 0};
					};
					class Unit6
					{
						side=2;
						vehicle="VTN_MILITIA_CM";
						rank="PRIVATE";
						position[]={-15, -15, 0};
					};
					class Unit7
					{
						side=2;
						vehicle="VTN_MILITIA_RFL";
						rank="PRIVATE";
						position[]={20, -20, 0};
					};
				};
				
				class sux_chdkz_at_team
				{
					name="AT Team";
					faction="sh_opfor_chdkz";
					side=2;
					class Unit0
					{
						side=2;
						vehicle="VTN_MILITIA_SL";
						rank="SERGEANT";
						position[]={0, 0, 0};
					};
					class Unit1
					{
						side=2;
						vehicle="VTN_MILITIA_AT";
						rank="SERGEANT";
						position[]={5, -5, 0};
					};
					class Unit2
					{
						side=2;
						vehicle="VTN_MILITIA_ATS1";
						rank="CORPORAL";
						position[]={-5, -5, 0};
					};
					class Unit3
					{
						side=2;
						vehicle="VTN_MILITIA_RFL";
						rank="PRIVATE";
						position[]={10, -10, 0};
					};
				};
				class sux_chdkz_mg_team
				{
					name="MG Team";
					faction="sh_opfor_chdkz";
					side=2;
					class Unit0
					{
						side=2;
						vehicle="VTN_MILITIA_SL";
						rank="SERGEANT";
						position[]={0, 0, 0};
					};
					class Unit1
					{
						side=2;
						vehicle="VTN_MILITIA_GMG1";
						rank="CORPORAL";
						position[]={5, -5, 0};
					};
					class Unit2
					{
						side=2;
						vehicle="VTN_MILITIA_GMG1";
						rank="PRIVATE";
						position[]={-5, -5, 0};
					};
					class Unit3
					{
						side=2;
						vehicle="VTN_MILITIA_RFL";
						rank="PRIVATE";
						position[]={10, -10, 0};
					};
				};
			};
			class Mechanized
			{
				name="Mechanized Infantry";
				class sh_chdkz_bmp_squad
				{
					name="BMP-1 Squad";
					faction="sh_opfor_chdkz";
					side=2;
					class Unit0
					{
						side=2;
						vehicle="sh_chdkz_bmp1";
						rank="SERGEANT";
						position[]={0, 0, 0};
					};
					class Unit1
					{
						side=2;
						vehicle="VTN_MILITIA_RTO";
						rank="SERGEANT";
						position[]={13, -18.5, 0};
					};
					class Unit2
					{
						side=2;
						vehicle="VTN_MILITIA_SL";
						rank="CORPORAL";
						position[]={-12, -17.5, 0};
					};
					class Unit3
					{
						side=2;
						vehicle="VTN_MILITIA_GMG1";
						rank="PRIVATE";
						position[]={18.5, -23.5, 0};
					};
					class Unit4
					{
						side=2;
						vehicle="VTN_MILITIA_ATS1";
						rank="PRIVATE";
						position[]={-17.5, -22.5, 0};
					};
					class Unit5
					{
						side=2;
						vehicle="VTN_MILITIA_RFL";
						rank="PRIVATE";
						position[]={24, -28.5, 0};
					};
					class Unit6
					{
						side=2;
						vehicle="VTN_MILITIA_AT";
						rank="PRIVATE";
						position[]={-23, -27.5, 0};
					};
					class Unit7
					{
						side=2;
						vehicle="VTN_MILITIA_CM";
						rank="PRIVATE";
						position[]={29.5, -33.5, 0};
					};
					class Unit8
					{
						side=2;
						vehicle="VTN_MILITIA_RFL";
						rank="PRIVATE";
						position[]={-28.5, -32.5, 0};
					};
				};
				class sh_chdkz_btr_squad
				{
					name="BTR-80 Squad";
					faction="sh_opfor_chdkz";
					side=2;
					class Unit0
					{
						side=2;
						vehicle="sh_chdkz_btr80";
						rank="SERGEANT";
						position[]={0, 0, 0};
					};
					class Unit1
					{
						side=2;
						vehicle="VTN_MILITIA_RTO";
						rank="SERGEANT";
						position[]={13, -18.5, 0};
					};
					class Unit2
					{
						side=2;
						vehicle="VTN_MILITIA_SL";
						rank="CORPORAL";
						position[]={-12, -17.5, 0};
					};
					class Unit3
					{
						side=2;
						vehicle="VTN_MILITIA_GMG1";
						rank="PRIVATE";
						position[]={18.5, -23.5, 0};
					};
					class Unit4
					{
						side=2;
						vehicle="VTN_MILITIA_GMG1";
						rank="PRIVATE";
						position[]={-17.5, -22.5, 0};
					};
					class Unit5
					{
						side=2;
						vehicle="VTN_MILITIA_RFL";
						rank="PRIVATE";
						position[]={24, -28.5, 0};
					};
					class Unit6
					{
						side=2;
						vehicle="VTN_MILITIA_AT";
						rank="PRIVATE";
						position[]={-23, -27.5, 0};
					};
					class Unit7
					{
						side=2;
						vehicle="VTN_MILITIA_CM";
						rank="PRIVATE";
						position[]={29.5, -33.5, 0};
					};
					class Unit8
					{
						side=2;
						vehicle="VTN_MILITIA_RFL";
						rank="PRIVATE";
						position[]={-28.5, -32.5, 0};
					};
				};
			};
			class Armored
			{
				name="Armor";
				class sh_chdkz_t72_section
				{
					name="T-72BA Section";
					faction="sh_opfor_chdkz";
					side=2;
					class Unit0
					{
						side=2;
						vehicle="sh_chdkz_t72ba";
						rank="SERGEANT";
						position[]={0, 0, 0};
					};
					class Unit1
					{
						side=2;
						vehicle="sh_chdkz_t72ba";
						rank="SERGEANT";
						position[]={13, -18.5, 0};
					};
				};
			};
		};
	};
};