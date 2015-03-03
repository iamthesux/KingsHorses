class CfgPatches
{
	class sh_vtn_groups
	{
		units[]=
		{
			"sh_faction_cdf_unit",
			"sh_faction_det5_unit",
			"sh_faction_sasr_unit",
			"sh_faction_marines_unit",
			"sh_faction_cdn_unit"
		};
		weapons[]={};
		requiredVersion=0.10000000149;
		requiredAddons[]={};
	};
};

class CfgFactionClasses
{
	class sh_faction_cdf
	{
		displayName="pubs";
		priority=1;
		side=0;
		backpack_tf_faction_radio_api = "tf_anprc155";
        personal_tf_faction_radio_api = "tf_anprc154";
        rifleman_tf_faction_radio_api = "tf_fadak";
        airborne_tf_faction_radio_api = "tf_anarc164";
	};
	class sh_faction_det5
	{
		displayName="DET5";
		priority=1;
		side=0;
		backpack_tf_faction_radio_api = "VTN_BP_R168KNE_FLORA";
        personal_tf_faction_radio_api = "tf_pnr1000a";
        rifleman_tf_faction_radio_api = "tf_anprc148jem";
        airborne_tf_faction_radio_api = "tf_mr6000l";
	};
	class sh_faction_sasr
	{
		displayName="SASR";
		priority=1;
		side=0;
		backpack_tf_faction_radio_api = "VTN_BP_R168KNE_FLORA";
        personal_tf_faction_radio_api = "tf_pnr1000a";
        rifleman_tf_faction_radio_api = "tf_anprc148jem";
        airborne_tf_faction_radio_api = "tf_mr6000l";
	};
	class sh_faction_marines
	{
		displayName="Marines";
		priority=1;
		side=0;
		backpack_tf_faction_radio_api = "tf_rt1523g_big";
        personal_tf_faction_radio_api = "tf_rf7800str";
        rifleman_tf_faction_radio_api = "tf_anprc152";
        airborne_tf_faction_radio_api = "tf_anarc210";
	};
	class sh_faction_cdn
	{
		displayName="CDN";
		priority=1;
		side=0;
		backpack_tf_faction_radio_api = "tf_anprc155";
        personal_tf_faction_radio_api = "tf_anprc154";
        rifleman_tf_faction_radio_api = "tf_fadak";
        airborne_tf_faction_radio_api = "tf_anarc164";
	};
};

class CfgVehicles
{
	class B_Soldier_F;
	
	class sh_faction_cdf_unit : B_Soldier_F		
	{
		faction = "sh_faction_cdf";
		scope = 1;
	};
	class sh_faction_det5_unit : B_Soldier_F
	{
		faction = "sh_faction_det5";
		scope = 1;
	};
	class sh_faction_sasr_unit : B_Soldier_F
	{
		faction = "sh_faction_sasr";
		scope = 1;
	};
	class sh_faction_marines_unit : B_Soldier_F
	{
		faction = "sh_faction_marines";
		scope = 1;
	};
	class sh_faction_cdn_unit : B_Soldier_F
	{
		faction = "sh_faction_cdn";
		scope = 1;
	};
};

