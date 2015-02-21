if (!isServer) exitwith {};

#include "sux_load.hpp"

private ["_unit","_load","_flags","_vals", "_load_name"];

_crate = [_this, 0] call bis_fnc_param;
_load_name = [_this, 1] call bis_fnc_param;
_load = call compile loadFile format ["loads\%1.sqf", _load_name];
_flags = _load select _FLAGS;

diag_log format ["APPLY VCARGO %1 for player: %2", _load_name, _crate];

if (REMOVE_ALL in _flags) then 
{
	clearWeaponCargoGlobal _unit;
	clearMagazineCargoGlobal _unit;
	clearBackpackCargoGlobal _unit;
	clearItemCargoGlobal _unit;
} else {
	if (REMOVE_WEAPONS in _flags) then { clearWeaponCargoGlobal _unit; };
	if (REMOVE_ITEMS in _flags) then { clearItemCargoGlobal _unit; };
	if (REMOVE_RUCK in _flags) then { clearBackpackCargoGlobal _unit; };
	if (REMOVE_LINK_ITEMS in _flags) then { clearMagazineCargoGlobal _unit; };
};

_vals = _load select _CRATE_WEAPONS;
if (count _vals > 0) then {
	[_crate,_vals,true] call BIS_fnc_addVirtualWeaponCargo;
};
_vals = _load select _CRATE_MAGAZINES;
if (count _vals > 0) then {
	[_crate,_vals,true] call BIS_fnc_addVirtualMagazineCargo;
};
_vals = _load select _CRATE_RUCKS;
if (count _vals > 0) then {
	[_crate,_vals,true] call BIS_fnc_addVirtualBackPackCargo;
};
_vals = _load select _CRATE_ITEMS;
if (count _vals > 0) then {
	[_crate,_vals,true] call BIS_fnc_addVirtualItemCargo;
};
