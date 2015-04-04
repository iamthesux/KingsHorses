class CfgPatches
{
	class sh_fixes
	{
		units[]= {};
		weapons[]={};
		requiredVersion=0.10000000149;
		requiredAddons[]={"RDS_StaticWeapons_Core"};
	};
};

class CfgMagazines
{
	class CA_LauncherMagazine;
	class RDS_OG9_HE : CA_LauncherMagazine
	{
		model="\RDS_StaticW\SPG9\OG9_projectile";
	};
	class RDS_PG9_AT : CA_LauncherMagazine
	{
		model="\RDS_StaticW\SPG9\PG9_projectile";
	};
};
