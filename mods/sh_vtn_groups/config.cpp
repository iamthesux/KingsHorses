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
		requiredAddons[]={};
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