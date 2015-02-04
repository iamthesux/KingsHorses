class cfgPatches
{
	class spearhead_alive_boxes
	{
		units[]=
		{
			"spearhead_cdf_weapons",
			"spearhead_cdf_launchers",
			"spearhead_cdf_explosives"
		};
		weapons[]={};
		requiredVersion=0.10000000149;
		requiredAddons[]={"A3_Weapons_F"};
	};
};
class cfgVehicles
{
	class Box_NATO_AmmoOrd_F;
	class spearhead_cdf_weapons : Box_NATO_AmmoOrd_F
	{
		scope=2;
		displayName="CDF Rifles and Ammo";
		maximumLoad=9999999;
		transportMaxMagazines=9999999;
		transportMaxBackpacks=9999999;
		class TransportWeapons
		{
			class _xx_rhs_weap_ak74m
			{
				weapon="rhs_weap_ak74m";
				count=5;
			};
			class _xx_rhs_weap_ak74m_folded
			{
				weapon="rhs_weap_ak74m_folded";
				count=5;
			};
			class _xx_rhs_weap_pkp
			{
				weapon="rhs_weap_pkp";
				count=5;
			};
		};
		class TransportMagazines
		{
			class _xx_rhs_30Rnd_545x39_AK
			{
				magazine="rhs_30Rnd_545x39_AK";
				count=100;
			};
			class _xx_rhs_30Rnd_545x39_AK_green
			{
				magazine="rhs_30Rnd_545x39_AK_green";
				count=100;
			};
			class _xx_rhs_100Rnd_762x54mmR
			{
				magazine="rhs_100Rnd_762x54mmR";
				count=100;
			};
		};
		class TransportBackpacks
		{
		};
		class TransportItems
		{
		};
		author="sux";
	};
	class spearhead_cdf_launchers : Box_NATO_AmmoOrd_F
	{
		scope=2;
		displayName="CDF Launchers and Warheads";
		maximumLoad=9999999;
		transportMaxMagazines=9999999;
		transportMaxBackpacks=9999999;
		class TransportWeapons
		{
			class _xx_rhs_weap_rpg7
			{
				weapon="rhs_weap_rpg7";
				count=10;
			};
			class _xx_rhs_weap_rpg26
			{
				weapon="rhs_weap_rpg26";
				count=100;
			};
			class _xx_rhs_weap_rshg2
			{
				weapon="rhs_weap_rshg2";
				count=50;
			};
		};
		class TransportMagazines
		{
			class _xx_rhs_rpg7_PG7VL_mag
			{
				magazine="rhs_rpg7_PG7VL_mag";
				count=100;
			};
			class _xx_rhs_rpg7_PG7VR_mag
			{
				magazine="rhs_rpg7_PG7VR_mag";
				count=100;
			};
			class _xx_rhs_rpg7_OG7V_mag
			{
				magazine="rhs_rpg7_OG7V_mag";
				count=100;
			};
		};
		class TransportBackpacks
		{
		};
		class TransportItems
		{
		};
		author="sux";
	};
	class spearhead_cdf_explosives : Box_NATO_AmmoOrd_F
	{
		scope=2;
		displayName="CDF Explosives and CSW";
		maximumLoad=9999999;
		transportMaxMagazines=9999999;
		transportMaxBackpacks=9999999;
		class TransportWeapons
		{
		};
		class TransportMagazines
		{
			class _xx_rhs_mag_rgd5
			{
				magazine="rhs_mag_rgd5";
				count=100;
			};
			class _xx_rhs_mag_rdg2_white
			{
				magazine="rhs_mag_rdg2_white";
				count=100;
			};
			class _xx_rhs_mag_rdg2_black
			{
				magazine="rhs_mag_rdg2_black";
				count=100;
			};
			class _xx_rhs_mag_nspn_yellow
			{
				magazine="rhs_mag_nspn_yellow";
				count=100;
			};
			class _xx_rhs_mag_nspn_red
			{
				magazine="rhs_mag_nspn_red";
				count=100;
			};
			class _xx_rhs_mag_nspn_green
			{
				magazine="rhs_mag_nspn_green";
				count=100;
			};
			class _xx_rhs_mine_tm62m
			{
				magazine="rhs_mine_tm62m";
				count=100;
			};
			class _xx_rhs_VOG25
			{
				magazine="rhs_VOG25";
				count=100;
			};
			class _xx_rhs_VOG25p
			{
				magazine="rhs_VOG25p";
				count=100;
			};
			class _xx_rhs_vg40op_white
			{
				magazine="rhs_vg40op_white";
				count=100;
			};
			class _xx_rhs_vg40op_green
			{
				magazine="rhs_vg40op_green";
				count=100;
			};
			class _xx_rhs_vg40op_red
			{
				magazine="rhs_vg40op_red";
				count=100;
			};
			class _xx_rhs_GRD40_white
			{
				magazine="rhs_GRD40_white";
				count=100;
			};
			class _xx_rhs_GRD40_green
			{
				magazine="rhs_GRD40_green";
				count=100;
			};
			class _xx_rhs_GRD40_red
			{
				magazine="rhs_GRD40_red";
				count=100;
			};
		};
		class TransportBackpacks
		{
			class _xx_RHS_NSV_Gun_Bag
			{
				backpack="RHS_NSV_Gun_Bag";
				count=10;
			};
			class _xx_RDS_DShkM_Gun_Bag
			{
				backpack="RDS_DShkM_Gun_Bag";
				count=10;
			};
			class _xx_RDS_DShkM_TripodLow_Bag
			{
				backpack="RDS_DShkM_TripodLow_Bag";
				count=10;
			};
			class _xx_RDS_Metis_Gun_Bag
			{
				backpack="RDS_Metis_Gun_Bag";
				count=10;
			};
			class _xx_RDS_Metis_Tripod_Bag
			{
				backpack="RDS_Metis_Tripod_Bag";
				count=10;
			};
			class _xx_RDS_AGS30_Gun_Bag
			{
				backpack="RDS_AGS30_Gun_Bag";
				count=10;
			};
			class _xx_RDS_AGS30_Tripod_Bag
			{
				backpack="RDS_AGS30_Tripod_Bag";
				count=10;
			};
			class _xx_RDS_SPG9_Gun_Bag
			{
				backpack="RDS_SPG9_Gun_Bag";
				count=10;
			};
			class _xx_RDS_SPG9_Tripod_Bag
			{
				backpack="RDS_SPG9_Tripod_Bag";
				count=10;
			};
		};
		class TransportItems
		{
		};
		author="sux";
	};
};
