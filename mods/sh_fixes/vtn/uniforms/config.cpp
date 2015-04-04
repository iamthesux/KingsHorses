class CfgPatches
{
	class sh_fix_vtn_uniforms
	{
		units[]= {};
		weapons[]={};
		requiredVersion=0.10000000149;
		requiredAddons[]={"VTN_U_GORKA_S_CF"};
	};
};

class CfgWeapons
{
	class Uniform_Base;
	class UniformItem;
	
	class VTN_U_GORKA_S : Uniform_Base
	{
		class ItemInfo : UniformItem
		{
			containerClass="Supply100";
		};
	};
	class VTN_U_GORKA_S_1tk : VTN_U_GORKA_S { displayName="Northern Plate";  descriptionShort="Armor of House Stark"; };
	class VTN_VVS_VKK15 : Uniform_Base
	{
		class ItemInfo : UniformItem
		{
			containerClass="Supply100";
		};
	};
};
