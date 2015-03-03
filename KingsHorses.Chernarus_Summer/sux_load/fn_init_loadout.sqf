diag_log "--------------------------------------------IN IT";

if (!isServer) exitWith {diag_log "--------------------------------------------NOT SERVER";};

_unit = [_this, 0] call bis_fnc_param;
_load_name = [_this, 1] call bis_fnc_param;

_unit setVariable ['sux_loadout', _load_name, true];

//_unit addmpeventhandler ["mprespawn", "_load = (_this select 0) getVariable 'sux_loadout'; [_this select 0, _load] call suxlo_fnc_apply_loadout;"];