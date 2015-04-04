/*
	Author: voiper
	
	Description: Handle NVG viewdistance.
	
	Parameters: 
		0: Bool; whether player will respawn; default false
		1: Scalar; max viewdistance for NVG; default 1000.
		2: Bool; whether grain is in NVG; default true;
	
	Returns:
		None
*/

_respawn = [_this, 0, false, [true]] call bis_fnc_param;
_distance = [_this, 1, [true, 1000], [[]]] call bis_fnc_param;
_grain = [_this, 2, true, [true]] call bis_fnc_param;

_cse = isClass (configFile >> "CfgPatches" >> ("cse_sys_nightvision"));
_agm = isClass (configFile >> "CfgPatches" >> ("AGM_NightVision"));

//if CSE is present, cancel this script (already does this)
if (_cse) exitWith {};

vip_lit_var_cl_NVGOn = false;

if (_distance select 0) then {
	vip_lit_var_cl_NVGDist = _distance select 1;
	vip_lit_var_cl_NVGPlainDist = viewDistance;
};

//if AGM present, don't use grain (already does this)
if (_grain && !_agm) then {
	vip_lit_var_cl_NVGGrain = ppEffectCreate ["filmGrain", 3000];
	vip_lit_var_cl_NVGGrain ppEffectAdjust [0.5, 5, 1, 1, 1, 0];
	vip_lit_var_cl_NVGGrain ppEffectForceInNVG true;
	vip_lit_var_cl_NVGGrain ppEffectCommit 0;
	vip_lit_var_cl_NVGGrain ppEffectEnable false;
};

vip_lit_eh_cl_draw3DNVG = addMissionEventHandler ["Draw3D", {

	if (currentVisionMode player == 1) then {
	
		if !(vip_lit_var_cl_NVGOn) then {
			vip_lit_var_cl_NVGOn = true;
			if !(isNil "vip_lit_var_cl_NVGDist") then {vip_lit_var_cl_NVGPlainDist = viewDistance};
			if !(isNil "vip_lit_var_cl_NVGGrain") then {vip_lit_var_cl_NVGGrain ppEffectEnable true};
		};

		if !(isNil "vip_lit_var_cl_NVGDist") then {if (viewDistance != vip_lit_var_cl_NVGDist) then {setViewDistance vip_lit_var_cl_NVGDist}};
	
	} else {
	
		if (vip_lit_var_cl_NVGOn) then {
			vip_lit_var_cl_NVGOn = false;
			if !(isNil "vip_lit_var_cl_NVGDist") then {setViewDistance vip_lit_var_cl_NVGPlainDist};
			if !(isNil "vip_lit_var_cl_NVGGrain") then {vip_lit_var_cl_NVGGrain ppEffectEnable false};
		};
	};
}];

//if player won't respawn, remove the eventhandlers
if !(_respawn) then {

	vip_lit_eh_cl_killedNVG = player addEventHandler ["Killed", {

		removeMissionEventHandler ["Draw3D", vip_lit_eh_cl_draw3DNVG];
		setViewDistance vip_lit_var_cl_NVGPlainDist;
		if !(isNil "vip_lit_var_cl_NVGGrain") then {vip_lit_var_cl_NVGGrain ppEffectEnable false; ppEffectDestroy vip_lit_var_cl_NVGGrain};
		[] spawn {player removeEventHandler ["Killed", vip_lit_eh_cl_killedNVG]};
	}];
};