/*
	Author: voiper
	
	Description: Initialise map/flashlight/NVG features of LIT.
	
	Parameters: 
		0: Bool (optional); whether player can respawn during mission; default false.
		1: Bool (optional); whether to remove "Show player on map" button; default true.
		2: Bool (optional); whether to remove and disable map textures and cursor grid; default true.
		3: Array (optional); 0: whether to enable flashlight; default true; 1: flashlight size to use (0 = normal, 1 = large); default 0.
		4: Array (optional); 0: whether to enable NVG viewdistance; default true; 1: max viewdistance of NVG; default 1000.
		5: Bool (optional); whether to enable NVG grain; default true.
	
	Returns:
		None
*/

if (isDedicated) exitWith {};

_respawn = [_this, 0, false, [true]] call bis_fnc_param;
_mapFindButton = [_this, 1, true, [true]] call bis_fnc_param;
_mapTextures = [_this, 2, true, [true]] call bis_fnc_param;
_flash = [_this, 3, [true, 0], [[]]] call bis_fnc_param;
_nvgDist = [_this, 4, [true, 1000], [[]]] call bis_fnc_param;
_nvgGrain = [_this, 5, true, [true]] call bis_fnc_param;

waitUntil {!isNull player};

[_mapFindButton, _mapTextures, (_flash select 0), _nvgDist, _nvgGrain] call compile preProcessFileLineNumbers "vip_lit\vip_lit_diary.sqf";
if (_mapFindButton || _mapTextures) then {[_respawn, _mapFindButton, _mapTextures] execVM "vip_lit\vip_lit_map.sqf"};
if (_flash select 0) then {[_respawn, (_flash select 1)] execVM "vip_lit\vip_lit_flashlight.sqf"};
if (_nvgGrain || (_nvgDist select 0)) then {[_respawn, _nvgDist, _nvgGrain] call compile preProcessFileLineNumbers "vip_lit\vip_lit_NVG.sqf"};