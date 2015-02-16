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
		displayName="CDF";
		priority=1;
		side=0;
	};
	class sh_faction_det5
	{
		displayName="CDSF";
		priority=1;
		side=0;
	};
	class sh_faction_sasr
	{
		displayName="CDSF";
		priority=1;
		side=0;
	};
	class sh_faction_marines
	{
		displayName="Marines";
		priority=1;
		side=0;
	};
	class sh_faction_cdn
	{
		displayName="CDN";
		priority=1;
		side=0;
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

