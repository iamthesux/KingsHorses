class CfgPatches
{
	class sh_fix_rh_m4
	{
		units[]= {};
		weapons[]={};
		requiredVersion=0.10000000149;
		requiredAddons[]={"RH_m4_cfg", "rhsusf_sounds"};
	};
};
class Mode_SemiAuto;
class Mode_Burst;
class Mode_FullAuto;
class CfgWeapons
{
	class UGL_F;
	class Rifle_Base_F;
	class RH_m4 : Rifle_Base_F
	{
		class M203 : UGL_F
		{
			magazines[]=
			{
				"rhs_mag_M441_HE",
				"rhs_mag_M433_HEDP",
				"rhs_mag_M4009",
				"rhs_mag_m576",
				"rhs_mag_M585_white",
				"rhs_mag_M661_green",
				"rhs_mag_M662_red",
				"rhs_mag_M713_red",
				"rhs_mag_M714_white",
				"rhs_mag_M715_green",
				"rhs_mag_M716_yellow"
			};
			sounds[]={"StandardSound"};
			class StandardSound
			{
				weaponSoundEffect="DefaultRifle";
				soundClosure[] = {};

				begin1[]={"rhsusf\addons\rhsusf_sounds\ugl\ugl_1",2.30,1,800};
				begin2[]={"rhsusf\addons\rhsusf_sounds\ugl\ugl_2",2.30,1,800};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
		};
	};
	class RH_M16A4;
	class RH_M4_ris_M203;

	class RH_mk12mod1 : RH_M16A4
	{
		magazines[] += 
		{
			"rhs_mag_30Rnd_556x45_M855A1_Stanag_No_Tracer",
			"rhs_mag_30Rnd_556x45_Mk262_Stanag",
			"rhs_mag_30Rnd_556x45_Mk318_Stanag",
			"rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red"
		};
	};
	class RH_M16A4gl : RH_M16A4
	{
		magazines[] += {"rhs_mag_30Rnd_556x45_M855A1_Stanag_No_Tracer","rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red"};		
		reloadMagazineSound[] = {"rhsusf\addons\rhsusf_sounds\ar15_shared\reload",1.0,1,10};
		changeFiremodeSound[] = {"rhsusf\addons\rhsusf_sounds\ar15_shared\firemode",0.6,1,5};
		class Single: Mode_SemiAuto
		{
			sounds[]=
			{
				"StandardSound",
				"SilencedSound"
			};
			class BaseSoundModeType
			{
				weaponSoundEffect="DefaultRifle";
				soundClosure[]=	{};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\m16\m16_1",2.3,1,1250};
				begin2[]={"rhsusf\addons\rhsusf_sounds\m16\m16_2",2.3,1,1250};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_1",2.2,1,600};
				begin2[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_2",2.2,1,600};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
		};
		class Burst: Mode_Burst
		{
			sounds[]=
			{
				"StandardSound",
				"SilencedSound"
			};
			class BaseSoundModeType
			{
				weaponSoundEffect="DefaultRifle";
				soundClosure[]=	{};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\m16\m16_1",2.3,1,1250};
				begin2[]={"rhsusf\addons\rhsusf_sounds\m16\m16_2",2.3,1,1250};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_1",2.2,1,600};
				begin2[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_2",2.2,1,600};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
		};
		
	};
	class rhs_weap_ak103_npz;
	class rhsusf_opscore_01;
	class rhsusf_opscore_01_1tk : rhsusf_opscore_01 { displayName="Crown";  descriptionShort="Crown of the One True King"; };
	class rhs_weap_ak103_npz_1tk : rhs_weap_ak103_npz { displayName="Ice";  descriptionShort="Spell-forged Valyrian steel"; };
	class RH_M4A1_ris_M203 : RH_M4_ris_M203
	{
		reloadMagazineSound[] = {"rhsusf\addons\rhsusf_sounds\ar15_shared\reload",1.0,1,10};
		changeFiremodeSound[] = {"rhsusf\addons\rhsusf_sounds\ar15_shared\firemode",0.6,1,5};

		magazines[] += {"rhs_mag_30Rnd_556x45_M855A1_Stanag_No_Tracer","rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red"};

		class Single: Mode_SemiAuto
		{
			sounds[]=
			{
				"StandardSound",
				"SilencedSound"
			};
			class BaseSoundModeType
			{
				weaponSoundEffect="DefaultRifle";
				soundClosure[]=	{};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\m4\m4_1",2.2,1,1200};
				begin2[]={"rhsusf\addons\rhsusf_sounds\m4\m4_2",2.2,1,1200};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_1",2.2,1,600};
				begin2[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_2",2.2,1,600};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
		};
		class Burst: Mode_Burst
		{
			sounds[]=
			{
				"StandardSound",
				"SilencedSound"
			};
			class BaseSoundModeType
			{
				weaponSoundEffect="DefaultRifle";
				soundClosure[]=	{};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\m4\m4_1",2.2,1,1200};
				begin2[]={"rhsusf\addons\rhsusf_sounds\m4\m4_2",2.2,1,1200};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_1",2.2,1,600};
				begin2[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_2",2.2,1,600};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
		};
		class FullAuto : Mode_FullAuto
		{
			sounds[]=
			{
				"StandardSound",
				"SilencedSound"
			};
			class BaseSoundModeType
			{
				weaponSoundEffect="DefaultRifle";
				soundClosure[]=	{};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\m4\m4_1",2.2,1,1200};
				begin2[]={"rhsusf\addons\rhsusf_sounds\m4\m4_2",2.2,1,1200};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_1",2.2,1,600};
				begin2[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_2",2.2,1,600};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
		};

	};
};