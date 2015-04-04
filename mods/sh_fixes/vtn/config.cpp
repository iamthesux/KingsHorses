class CfgPatches
{
	class sh_fix_vtn
	{
		units[]= {};
		weapons[]={};
		requiredVersion=0.10000000149;
		requiredAddons[]={"VTN_U_GORKA_S_CF", "VTN_AMUN_V_JTU_CF"};
	};
};
class RadioProtocolBase;
class RadioProtocolBaseRUS : RadioProtocolBase
{
	class Words;
};

class RadioProtocolRUS : RadioProtocolBaseRUS
{
	class Words : Words
	{
		NoEnemiesInSight[]={};
	};
};
