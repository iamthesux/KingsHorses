class CfgPatches
{
	class sh_fix_vtn_vests
	{
		units[]= {};
		weapons[]={};
		requiredVersion=0.10000000149;
		requiredAddons[]={"VTN_AMUN_V_JTU_CF", "VTN_BP_6SH104_CF", "VTN_AMUN_V_CHICOM_CF"};
	};
};

class CfgVehicles
{
	class B_AssaultPack_Base;
	class B_VTN_6SH104_FLORA : B_AssaultPack_Base
	{
		maximumLoad=200;
	};
	class B_VTN_6SH92_FLORA : B_AssaultPack_Base
	{
		maximumLoad=200;
	};
};

class CfgWeapons
{
	class ItemInfo;
	class V_KORA_K_6Sh104AKGP;
	class V_6B23_EMR;
	class Vest_Base;
	class VestItem;

	class V_CHICOM_KHAKI : Vest_Base
	{
		class ItemInfo : VestItem
		{
			containerClass="Supply140";
		};
	};
	class V_KORA_K_6Sh104SVD : V_KORA_K_6Sh104AKGP
	{
		class ItemInfo : ItemInfo
		{
			containerClass="Supply120";
		};
	};
	class V_KORA_K_6Sh104PK : V_KORA_K_6Sh104SVD
	{
		class ItemInfo : ItemInfo
		{
			containerClass="Supply180";
		};
	};
	class V_KORA_K_CHICOM : V_KORA_K_6Sh104PK
	{
		class ItemInfo : ItemInfo
		{
			containerClass="Supply140";
		};
	};
	
	class V_KORA_K_6Sh92AK : V_6B23_EMR
	{
		class ItemInfo : ItemInfo
		{
			containerClass="Supply150";
		};
	};
	class V_KORA_K_6Sh92GP : V_KORA_K_6Sh92AK
	{
		class ItemInfo : ItemInfo
		{
			containerClass="Supply160";
		};
	};
};