//call compile preprocessFileLineNumbers "loads\sux_load.sqf";

if (!isDedicated) then {
	waitUntil { player == player };
	_lo = player getVariable ["sux_loadout", ""];
	if (_lo != '') then {
		[player, _lo] call suxlo_fnc_apply_loadout;
		player addmpeventhandler ["mprespawn", "_load = (_this select 0) getVariable 'sux_loadout'; [_this select 0, _load] call suxlo_fnc_apply_loadout;"];
	};
};