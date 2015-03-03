class CfgPatches
{
	class sh_fix_vtn
	{
		units[]= {};
		weapons[]={};
		requiredVersion=0.10000000149;
		requiredAddons[]={"rhs_c_weapons", "VTN_Weapons_F", "VTN_U_FROG_CF", "VTN_U_GORKA_S_CF"};
	};
};
class Mode_SemiAuto;
class Mode_Burst;
class Mode_FullAuto;

class CfgSounds
{
	class s_MX_F
	{
		name="s_MX_F";
		sound[]=
		{
			"vtn_sound_bank\M249_s12_mx_sf32stw.wav",
			1.91201102734,
			1.00999999046
		};
		titles[]={};
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
class CfgWeapons
{
	class GrenadeLauncher;
	class Rifle_Base_F;
	class VTN_SAIGA_MK03;
	class rhs_weap_svd;

	class Uniform_Base;
	class UniformItem;

	class ItemCore;
	class InventoryOpticsItem_Base_F;

	class Throw : GrenadeLauncher
	{
		muzzles[] += {"rhsusf_Throw_Grenade","Rhs_Throw_Grenade","Rhs_Throw_Smoke","Rhs_Throw_Flare","Rhs_Throw_Flash","rhsusf_Throw_Flash"};
	};
	class rhs_weap_svdp : rhs_weap_svd
	{
		magazines[] =
		{
			"rhs_10Rnd_762x54mmR_7N1",
			"VTN_SVD_10s_TRC",
			"VTN_SVD_10s_AP",
			"VTN_SVD_10s_SC"
		};
	};
	class VTN_U_GORKA_S : Uniform_Base
	{
		class ItemInfo : UniformItem
		{
			containerClass="Supply50";
		};
	};
	class VTN_U_FROG_WDL : Uniform_Base
	{
		class ItemInfo : UniformItem
		{
			containerClass="Supply50";
		};
	};
	
	class VTN_OPTIC_1P76 : ItemCore
	{
		class ItemInfo : InventoryOpticsItem_Base_F
		{
			class OpticsModes
			{
				class 1P76
				{
					opticsZoomMin=0.375;
					opticsZoomMax=1.1;
					opticsZoomInit=0.75;
				};
			};
		};
	};
	class VTN_OPTIC_1P77 : ItemCore
	{
		class ItemInfo : InventoryOpticsItem_Base_F
		{
			class OpticsModes
			{
				class 1P77_col
				{
					opticsZoomMin=0.375;
					opticsZoomMax=1.1;
					opticsZoomInit=0.75;
				};
			};
		};
	};
	class VTN_OPTIC_1P78 : ItemCore
	{
		class ItemInfo : InventoryOpticsItem_Base_F
		{
			class OpticsModes
			{
				class 1P78_col
				{
					opticsZoomMin=0.375;
					opticsZoomMax=1.1;
					opticsZoomInit=0.75;
				};
			};
		};
	};
	class VTN_OPTIC_1P63 : ItemCore
	{
		class ItemInfo : InventoryOpticsItem_Base_F
		{
			class OpticsModes
			{
				class 1P63
				{
					opticsZoomMin=0.375;
					opticsZoomMax=1.1;
					opticsZoomInit=0.75;
				};
			};
		};
	};
	class VTN_OPTIC_PKAT : ItemCore
	{
		class ItemInfo : InventoryOpticsItem_Base_F
		{
			class OpticsModes
			{
				class PKA
				{
					opticsZoomMin=0.375;
					opticsZoomMax=1.1;
					opticsZoomInit=0.75;
				};
			};
		};
	};
	class VTN_OPTIC_RAKURS_PM : ItemCore
	{
		class ItemInfo : InventoryOpticsItem_Base_F
		{
			class OpticsModes
			{
				class 1P76
				{
					opticsZoomMin=0.375;
					opticsZoomMax=1.1;
					opticsZoomInit=0.75;
				};
			};
		};
	};
	class VTN_6CH3 : ItemCore
	{
		class ItemInfo : InventoryOpticsItem_Base_F
		{
			class OpticsModes
			{
				class 6ch3
				{
					opticsZoomMin=0.375;
					opticsZoomMax=1.1;
					opticsZoomInit=0.75;
				};
			};
		};
	};
	
	class VTN_AKS74U_BASE : Rifle_Base_F
	{
		opticsZoomMin = 0.375;
		opticsZoomMax = 1.1;
		opticsZoomInit = 0.75;
		
		class Single: Mode_SemiAuto
		{
			sounds[] = {"StandardSound","SilencedSound"};
			class BaseSoundModeType
			{
				weaponSoundEffect = "DefaultRifle";
				closure1[] = {"A3\sounds_f\weapons\closure\closure_rifle_2",0.9622777,1,300};
				closure2[] = {"A3\sounds_f\weapons\closure\closure_rifle_3",0.9622777,1,300};
				soundClosure[] = {"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[] = {"rhsafrf\addons\rhs_sounds\ak74\ak74_1",2.35,1,1200};
				begin2[] = {"rhsafrf\addons\rhs_sounds\ak74\ak74_2",2.35,1,1200};
				soundBegin[] = {"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[] = {"A3\sounds_f\weapons\silenced\silent-18",0.794328,1,100};
				begin2[] = {"A3\sounds_f\weapons\silenced\silent-19",0.794328,1,100};
				begin3[] = {"A3\sounds_f\weapons\silenced\silent-11",0.794328,1,100};
				soundBegin[] = {"begin1",0.333,"begin2",0.333,"begin3",0.333};
			};
		};
		class FullAuto: Mode_FullAuto
		{
			sounds[] = {"StandardSound","SilencedSound"};
			class BaseSoundModeType
			{
				weaponSoundEffect = "DefaultRifle";
				closure1[] = {"A3\sounds_f\weapons\closure\closure_rifle_2",0.9622777,1,300};
				closure2[] = {"A3\sounds_f\weapons\closure\closure_rifle_3",0.9622777,1,300};
				soundClosure[] = {"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[] = {"rhsafrf\addons\rhs_sounds\ak74\ak74_1",2.35,1,1200};
				begin2[] = {"rhsafrf\addons\rhs_sounds\ak74\ak74_2",2.35,1,1200};
				soundBegin[] = {"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[] = {"A3\sounds_f\weapons\silenced\silent-18",0.794328,1,100};
				begin2[] = {"A3\sounds_f\weapons\silenced\silent-19",0.794328,1,100};
				begin3[] = {"A3\sounds_f\weapons\silenced\silent-11",0.794328,1,100};
				soundBegin[] = {"begin1",0.333,"begin2",0.333,"begin3",0.333};
			};
		};
	};
	class VTN_PKM_BASE : Rifle_Base_F
	{
		opticsZoomMin = 0.375;
		opticsZoomMax = 1.1;
		opticsZoomInit = 0.75;
	};
	class VTN_SAIGA_MK03_AUTO : VTN_SAIGA_MK03
	{
		opticsZoomMin = 0.375;
		opticsZoomMax = 1.1;
		opticsZoomInit = 0.75;
		
		class Single: Mode_SemiAuto
		{
			sounds[] = {"StandardSound","SilencedSound"};
			class BaseSoundModeType
			{
				weaponSoundEffect = "DefaultRifle";
				closure1[] = {"A3\sounds_f\weapons\closure\closure_rifle_4",1.41253757477,1,50};
				closure2[] = {"A3\sounds_f\weapons\closure\closure_rifle_4",1.41253757477,1,50};
				soundClosure[] = {"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\akM\akM_1",2.35,1,1300};
				begin2[]={"rhsafrf\addons\rhs_sounds\akM\akM_2",2.35,1,1300};
				soundBegin[] = {"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_1", 2.2,1,600};
				begin2[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_2", 2.2,1,600};
				soundBegin[]={begin1,0.5, begin2,0.5};
			};
		};
		class FullAuto: Mode_FullAuto
		{
			sounds[] = {"StandardSound","SilencedSound"};
			class BaseSoundModeType
			{
				weaponSoundEffect = "DefaultRifle";
				closure1[] = {"A3\sounds_f\weapons\closure\closure_rifle_4",1.41253757477,1,50};
				closure2[] = {"A3\sounds_f\weapons\closure\closure_rifle_4",1.41253757477,1,50};
				soundClosure[] = {"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\akM\akM_1",2.35,1,1300};
				begin2[]={"rhsafrf\addons\rhs_sounds\akM\akM_2",2.35,1,1300};
				soundBegin[] = {"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_1", 2.2,1,600};
				begin2[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_2", 2.2,1,600};
				soundBegin[]={begin1,0.5, begin2,0.5};
			};
		};
	};
	class VTN_AK_BASE : Rifle_Base_F
	{
		opticsZoomMin = 0.375;
		opticsZoomMax = 1.1;
		opticsZoomInit = 0.75;
		
		class Single: Mode_SemiAuto
		{
			sounds[] = {"StandardSound","SilencedSound"};
			class BaseSoundModeType
			{
				weaponSoundEffect = "DefaultRifle";
				closure1[] = {"A3\sounds_f\weapons\closure\closure_rifle_2",0.9622777,1,300};
				closure2[] = {"A3\sounds_f\weapons\closure\closure_rifle_3",0.9622777,1,300};
				soundClosure[] = {"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[] = {"rhsafrf\addons\rhs_sounds\ak74\ak74_1",2.35,1,1200};
				begin2[] = {"rhsafrf\addons\rhs_sounds\ak74\ak74_2",2.35,1,1200};
				begin3[] = {"rhsafrf\addons\rhs_weapons\sounds\ak74m_3",6.7782794,1,1000};
				begin4[] = {"rhsafrf\addons\rhs_weapons\sounds\ak74m_4",6.7782794,1,1000};
				soundBegin[] = {"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[] = {"A3\sounds_f\weapons\silenced\silent-18",0.794328,1,100};
				begin2[] = {"A3\sounds_f\weapons\silenced\silent-19",0.794328,1,100};
				begin3[] = {"A3\sounds_f\weapons\silenced\silent-11",0.794328,1,100};
				soundBegin[] = {"begin1",0.333,"begin2",0.333,"begin3",0.333};
			};
		};
		class FullAuto: Mode_FullAuto
		{
			sounds[] = {"StandardSound","SilencedSound"};
			class BaseSoundModeType
			{
				weaponSoundEffect = "DefaultRifle";
				closure1[] = {"A3\sounds_f\weapons\closure\closure_rifle_2",0.9622777,1,300};
				closure2[] = {"A3\sounds_f\weapons\closure\closure_rifle_3",0.9622777,1,300};
				soundClosure[] = {"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[] = {"rhsafrf\addons\rhs_sounds\ak74\ak74_1",2.35,1,1200};
				begin2[] = {"rhsafrf\addons\rhs_sounds\ak74\ak74_2",2.35,1,1200};
				begin3[] = {"rhsafrf\addons\rhs_weapons\sounds\ak74m_3",6.7782794,1,1000};
				begin4[] = {"rhsafrf\addons\rhs_weapons\sounds\ak74m_4",6.7782794,1,1000};
				soundBegin[] = {"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[] = {"A3\sounds_f\weapons\silenced\silent-18",0.794328,1,100};
				begin2[] = {"A3\sounds_f\weapons\silenced\silent-19",0.794328,1,100};
				begin3[] = {"A3\sounds_f\weapons\silenced\silent-11",0.794328,1,100};
				soundBegin[] = {"begin1",0.333,"begin2",0.333,"begin3",0.333};
			};
		};
	};
	class VTN_AKM_BASE : Rifle_Base_F
	{
		opticsZoomMin = 0.375;
		opticsZoomMax = 1.1;
		opticsZoomInit = 0.75;
		
		class Single : Mode_SemiAuto
		{
			sounds[]={"StandardSound", "SilencedSound"};
			class BaseSoundModeType
			{
				weaponSoundEffect = "DefaultRifle";
				closure1[] = {"A3\sounds_f\weapons\closure\closure_rifle_2",0.9622777,1,300};
				closure2[] = {"A3\sounds_f\weapons\closure\closure_rifle_3",0.9622777,1,300};
				soundClosure[] = {"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\akM\akM_1",2.35,1,1300};
				begin2[]={"rhsafrf\addons\rhs_sounds\akM\akM_2",2.35,1,1300};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_1", 2.2,1,600};
				begin2[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_2", 2.2,1,600};
				soundBegin[]={begin1,0.5, begin2,0.5};
			};
		};
		class FullAuto: Mode_FullAuto
		{
			sounds[] = {"StandardSound","SilencedSound"};
			class BaseSoundModeType
			{
				weaponSoundEffect = "DefaultRifle";
				closure1[] = {"A3\sounds_f\weapons\closure\closure_rifle_2",0.9622777,1,300};
				closure2[] = {"A3\sounds_f\weapons\closure\closure_rifle_3",0.9622777,1,300};
				soundClosure[] = {"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\akM\akM_1",2.35,1,1300};
				begin2[]={"rhsafrf\addons\rhs_sounds\akM\akM_2",2.35,1,1300};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_1", 2.2,1,600};
				begin2[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_2", 2.2,1,600};
				soundBegin[]={begin1,0.5, begin2,0.5};
			};
		};
	};
	class VTN_AK103_BASE : Rifle_Base_F
	{
		opticsZoomMin = 0.375;
		opticsZoomMax = 1.1;
		opticsZoomInit = 0.75;
		class Single : Mode_SemiAuto
		{
			sounds[]={"StandardSound", "SilencedSound"};
			class BaseSoundModeType
			{
				weaponSoundEffect = "DefaultRifle";
				closure1[] = {"A3\sounds_f\weapons\closure\closure_rifle_2",0.9622777,1,300};
				closure2[] = {"A3\sounds_f\weapons\closure\closure_rifle_3",0.9622777,1,300};
				soundClosure[] = {"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[] = {"rhsafrf\addons\rhs_weapons\sounds\ak74m_1",6.7782794,1,1000};
				begin2[] = {"rhsafrf\addons\rhs_weapons\sounds\ak74m_3",6.7782794,1,1000};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_1", 2.2,1,600};
				begin2[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_2", 2.2,1,600};
				soundBegin[]={begin1,0.5, begin2,0.5};
			};
		};
		class FullAuto: Mode_FullAuto
		{
			sounds[] = {"StandardSound","SilencedSound"};
			class BaseSoundModeType
			{
				weaponSoundEffect = "DefaultRifle";
				closure1[] = {"A3\sounds_f\weapons\closure\closure_rifle_2",0.9622777,1,300};
				closure2[] = {"A3\sounds_f\weapons\closure\closure_rifle_3",0.9622777,1,300};
				soundClosure[] = {"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[] = {"rhsafrf\addons\rhs_weapons\sounds\ak74m_1",6.7782794,1,1000};
				begin2[] = {"rhsafrf\addons\rhs_weapons\sounds\ak74m_3",6.7782794,1,1000};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_1", 2.2,1,600};
				begin2[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_2", 2.2,1,600};
				soundBegin[]={begin1,0.5, begin2,0.5};
			};
		};
	};
	class VTN_AK105_BASE : Rifle_Base_F
	{
		opticsZoomMin = 0.375;
		opticsZoomMax = 1.1;
		opticsZoomInit = 0.75;
		class Single : Mode_SemiAuto
		{
			sounds[]={"StandardSound", "SilencedSound"};
			class BaseSoundModeType
			{
				weaponSoundEffect = "DefaultRifle";
				closure1[] = {"A3\sounds_f\weapons\closure\closure_rifle_2",0.9622777,1,10};
				closure2[] = {"A3\sounds_f\weapons\closure\closure_rifle_3",0.9622777,1,10};
				soundClosure[] = {"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\rpk\rpk_1",2.35,1,1300};
				begin2[]={"rhsafrf\addons\rhs_sounds\rpk\rpk_2",2.35,1,1300};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_1", 2.2,1,300};
				begin2[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_2", 2.2,1,300};
				soundBegin[]={begin1,0.5, begin2,0.5};
			};
		};
		class FullAuto: Mode_FullAuto
		{
			sounds[] = {"StandardSound","SilencedSound"};
			reloadTime = 0.095;
			class BaseSoundModeType
			{
				weaponSoundEffect = "DefaultRifle";
				closure1[] = {"A3\sounds_f\weapons\closure\closure_rifle_2",0.9622777,1,10};
				closure2[] = {"A3\sounds_f\weapons\closure\closure_rifle_3",0.9622777,1,10};
				soundClosure[] = {"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\rpk\rpk_1",2.35,1,1300};
				begin2[]={"rhsafrf\addons\rhs_sounds\rpk\rpk_2",2.35,1,1300};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_1", 2.2,1,300};
				begin2[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_2", 2.2,1,300};
				soundBegin[]={begin1,0.5, begin2,0.5};
			};
		};
	};
	class VTN_AK105_P_BASE : Rifle_Base_F
	{
		opticsZoomMin = 0.375;
		opticsZoomMax = 1.1;
		opticsZoomInit = 0.75;
		class Single : Mode_SemiAuto
		{
			sounds[]={"StandardSound", "SilencedSound"};
			class BaseSoundModeType
			{
				weaponSoundEffect = "DefaultRifle";
				closure1[] = {"A3\sounds_f\weapons\closure\closure_rifle_2",0.9622777,1,10};
				closure2[] = {"A3\sounds_f\weapons\closure\closure_rifle_3",0.9622777,1,10};
				soundClosure[] = {"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\rpk\rpk_1",2.35,1,1300};
				begin2[]={"rhsafrf\addons\rhs_sounds\rpk\rpk_2",2.35,1,1300};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_1", 2.2,1,300};
				begin2[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_2", 2.2,1,300};
				soundBegin[]={begin1,0.5, begin2,0.5};
			};
		};
		class FullAuto: Mode_FullAuto
		{
			sounds[] = {"StandardSound","SilencedSound"};
			reloadTime = 0.095;
			class BaseSoundModeType
			{
				weaponSoundEffect = "DefaultRifle";
				closure1[] = {"A3\sounds_f\weapons\closure\closure_rifle_2",0.9622777,1,10};
				closure2[] = {"A3\sounds_f\weapons\closure\closure_rifle_3",0.9622777,1,10};
				soundClosure[] = {"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\rpk\rpk_1",2.35,1,1300};
				begin2[]={"rhsafrf\addons\rhs_sounds\rpk\rpk_2",2.35,1,1300};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_1", 2.2,1,300};
				begin2[]={"rhsafrf\addons\rhs_sounds\ak_shared\silenced_2", 2.2,1,300};
				soundBegin[]={begin1,0.5, begin2,0.5};
			};
		};
	};
	class VTN_C_M4A1_BASE : Rifle_Base_F
	{
		opticsZoomMin = 0.375;
		opticsZoomMax = 1.1;
		opticsZoomInit = 0.75;
		changeFireModeSound[] = {"rhsusf\addons\rhsusf_sounds\ar15_shared\firemode",0.6,1,5};
		reloadMagazineSound[] = {"rhsusf\addons\rhsusf_sounds\ar15_shared\reload",1,1,10};
		class Single: Mode_SemiAuto
		{
			sounds[]= {"StandardSound", "SilencedSound"};
			class BaseSoundModeType
			{
				weaponSoundEffect="DefaultRifle";
				closure1[]={"A3\sounds_f\weapons\closure\closure_rifle_6",0.70794576,1,10};
				closure2[]={"A3\sounds_f\weapons\closure\closure_rifle_7",0.70794576,1,10};
				soundClosure[]=	{"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\m4\m4_1",2.2,1,1200};
				begin2[]={"rhsusf\addons\rhsusf_sounds\m4\m4_2",2.2,1,1200};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_1", 2.2,1,300};
				begin2[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_2", 2.2,1,300};
				soundBegin[]={begin1,0.5, begin2,0.5};
			};
		};
		class FullAuto : Mode_FullAuto
		{
			sounds[]= {"StandardSound", "SilencedSound"};
			class BaseSoundModeType
			{
				weaponSoundEffect="DefaultRifle";
				closure1[]={"A3\sounds_f\weapons\closure\closure_rifle_6",0.70794576,1,10};
				closure2[]={"A3\sounds_f\weapons\closure\closure_rifle_7",0.70794576,1,10};
				soundClosure[]=	{"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\m4\m4_1",2.2,1,1200};
				begin2[]={"rhsusf\addons\rhsusf_sounds\m4\m4_2",2.2,1,1200};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_1", 2.2,1,300};
				begin2[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_2", 2.2,1,300};
				soundBegin[]={begin1,0.5, begin2,0.5};
			};
		};
	};
	class VTN_M16_BASE : Rifle_Base_F
	{
		opticsZoomMin = 0.375;
		opticsZoomMax = 1.1;
		opticsZoomInit = 0.75;
		changeFireModeSound[] = {"rhsusf\addons\rhsusf_sounds\ar15_shared\firemode",0.6,1,5};
		class Single: Mode_SemiAuto
		{
			sounds[]= {"StandardSound", "SilencedSound"};
			class BaseSoundModeType
			{
				weaponSoundEffect="DefaultRifle";
				closure1[]={"A3\sounds_f\weapons\closure\closure_rifle_6",0.70794576,1,10};
				closure2[]={"A3\sounds_f\weapons\closure\closure_rifle_7",0.70794576,1,10};
				soundClosure[]=	{"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\m16\m16_1",2.3,1,1250};
				begin2[]={"rhsusf\addons\rhsusf_sounds\m16\m16_2",2.3,1,1200};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_1", 2.2,1,300};
				begin2[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_2", 2.2,1,300};
				soundBegin[]={begin1,0.5, begin2,0.5};
			};
		};
		class Burst : Mode_Burst
		{
			sounds[]= {"StandardSound", "SilencedSound"};
			reloadTime = 0.095;
			class BaseSoundModeType
			{
				weaponSoundEffect="DefaultRifle";
				closure1[]={"A3\sounds_f\weapons\closure\closure_rifle_6",0.70794576,1,10};
				closure2[]={"A3\sounds_f\weapons\closure\closure_rifle_7",0.70794576,1,10};
				soundClosure[]=	{"closure1",0.5,"closure2",0.5};
			};
			class StandardSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\m16\m16_1",2.3,1,1250};
				begin2[]={"rhsusf\addons\rhsusf_sounds\m16\m16_2",2.3,1,1200};
				soundBegin[]={"begin1",0.5,"begin2",0.5};
				soundClosure[]=	{};
				echo[]={};
			};
			class SilencedSound: BaseSoundModeType
			{
				begin1[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_1", 2.2,1,300};
				begin2[]={"rhsusf\addons\rhsusf_sounds\ar15_shared\silenced_2", 2.2,1,300};
				soundBegin[]={begin1,0.5, begin2,0.5};
			};
		};
	};
};
