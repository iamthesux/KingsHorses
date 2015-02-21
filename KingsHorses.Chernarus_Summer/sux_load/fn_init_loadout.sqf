_unit = [_this, 0] call bis_fnc_param;
if (!local _unit) exitWith {};
_load_name = [_this, 1] call bis_fnc_param;

diag_log format ["--------------------------------------------INIT LOAD %1 for player: %2", _load_name, _unit];
_unit setVariable ['sux_loadout', _load_name, true];
[_unit, _load_name] call suxlo_fnc_apply_loadout;

_unit addmpeventhandler ["mprespawn", "_load = (_this select 0) getVariable 'sux_loadout'; [_this select 0, _load] call suxlo_fnc_apply_loadout;"];