
_unit = [_this, 0] call bis_fnc_param;
_load_name = [_this, 1] call bis_fnc_param;

_unit setVariable ['sux_loadout', _load_name];
[_unit, _load_name] call suxlo_fnc_apply_loadout;

_unit addeventhandler ["respawn", "_load = (_this select 0) getVariable 'sux_loadout'; [_this select 0, _load] call suxlo_fnc_apply_loadout;"];