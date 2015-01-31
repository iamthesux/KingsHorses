#include "sux_load.hpp"

private ["_unit","_load","_flags","_vals", "_load_name"];

_unit = [_this, 0] call bis_fnc_param;
_load_name = [_this, 1] call bis_fnc_param;
_load = call compile loadFile format ["loads\%1.sqf", _load_name];

_flags = _load select _FLAGS;
diag_log "ehere";
diag_log _load;


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
	{ _unit addWeaponCargoGlobal _x } foreach _vals;
};
_vals = _load select _CRATE_MAGAZINES;
if (count _vals > 0) then {
	{ _unit addMagazineCargoGlobal _x } foreach _vals;
};
_vals = _load select _CRATE_RUCKS;
if (count _vals > 0) then {
	{ _unit addBackpackCargoGlobal _x } foreach _vals;
};
_vals = _load select _CRATE_ITEMS;
if (count _vals > 0) then {
	{ _unit addItemCargoGlobal _x; } foreach _vals;
};
