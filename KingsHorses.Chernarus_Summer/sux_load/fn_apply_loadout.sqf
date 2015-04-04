#include "sux_load.hpp"

sux_apply_carryable =
{
	private ["_unit","_load","_type","_v", "_item"];
	_unit = _this select 0;
	_load = _this select 1;
	_type = _this select 2;
	
	if (count _load > 0) then {
		_v = _load select 0;
		if (_v != "") then {
			switch (_type) do {
				case _UNIFORM: { _unit forceAddUniform _v; };
				case _VEST: { _unit addVest _v; };
				case _BACKPACK: { _unit addBackpack _v; };
			};
		};
		{
			_item = _x select 0;
			_v = _x select 1;
			switch (_type) do {
				case _UNIFORM: { 
					while { _v > 0} do { 
						if (_unit canAddItemToUniform _item) then {
							_unit addItemToUniform _item;
							//diag_log format ["--------------------------------------------adding  %2 to %1", _load_name, _item];
						} else {
							diag_log format ["--------------------------------------------Warning in load %1: No room for %2 in uniform", _load_name, _item];
						};
						_v = _v - 1;
					}; 
				};
				case _VEST: {
					while { _v > 0} do {
						if (_unit canAddItemToVest _item) then {
							_unit addItemToVest _item;
						} else {
							diag_log format ["--------------------------------------------Warning in load %1: No room for %2 in vest", _load_name, _item];
						};
						_v = _v - 1;
					};
				};
				case _BACKPACK: {
					while { _v > 0} do {
						if (_unit canAddItemToBackpack _item) then {
							_unit addItemToBackpack _item;
						} else {
							diag_log format ["--------------------------------------------Warning in load %1: No room for %2 in backpack", _load_name, _item];
						};
						_v = _v - 1;
					};
				};
			};
		} foreach (_load select 1);
	};
};

sux_apply_weapon =
{
	private ["_unit","_wep","_type","_v","_i"];

	_unit = _this select 0;
	_wep = _this select 1;
	_type = _this select 2;
	
	//diag_log "apply weappy";
	//diag_log _wep;
	if (count _wep == 5) then
	{
		
		_v = _wep select _MAGS;
		//diag_log _v;
		if (count _v > 0) then {
			{ _unit addMagazine _x; } foreach _v;
		};
		_v = _wep select _WEAPON;
		if (_v != "") then {
			_unit addWeapon _v;
			//diag_log format ["add %1", _v];
		};
		for "_i" from 1 to 3 do {
			_v = _wep select _i;
			if (_v != "") then {
				switch (_type) do
				{
					case _PRIMARY: { _unit addPrimaryWeaponItem _v; };
					case _SECONDARY: { _unit addSecondaryWeaponItem _v; };
					case _HANDGUN: { _unit addHandgunItem _v; };
				};
			};
		};
	};
};


private ["_unit","_load","_flags","_i"];

_unit = [_this, 0] call bis_fnc_param;
//if (!local _unit) exitWith { diag_log "SUXLO: apply_loadout: unit not local exiting"};
_load_name = [_this, 1] call bis_fnc_param;

//if (!isServer) exitWith { diag_log "SUXLO: apply_loadout: not server exiting"};

diag_log format ["--------------------------------------------APPLY LOAD %1 for player: %2", _load_name, _unit];
	
_load = call compile loadFile format ["loads\%1.sqf", _load_name];
_flags = _load select _FLAGS;

if (REMOVE_ALL in _flags) then 
{
	removeAllPrimaryWeaponItems _unit;
	removeAllHandgunItems _unit;
	removeAllWeapons _unit; 
	removeAllItems _unit;
	removeAllAssignedItems _unit;
	removeUniform _unit;
	removeVest _unit;
	removeBackpack _unit;
	removeHeadgear _unit;
	removeGoggles _unit;
} else {
	if (REMOVE_WEAPONS in _flags) then { diag_log "removing weapons";removeAllWeapons _unit; };
	if (REMOVE_ITEMS in _flags) then { removeAllItems _unit; };
	if (REMOVE_LINK_ITEMS in _flags) then { removeAllAssignedItems _unit; };
	if (REMOVE_UNIFORM in _flags) then { removeUniform _unit; };
	if (REMOVE_VEST in _flags) then { removeVest _unit; };
	if (REMOVE_RUCK in _flags) then { removeBackpack _unit; };
	if (REMOVE_HEAD in _flags) then { removeHeadgear _unit; };
	if (REMOVE_GOGGLES in _flags) then { removeGoggles _unit; };
	
	if (CLEAR_UNIFORM in _flags) then {{ _unit removeItemFromUniform _x; } foreach vestItems _unit;};
	if (CLEAR_VEST in _flags) then {{ _unit removeItemFromVest _x; } foreach vestItems _unit;};
	if (CLEAR_RUCK in _flags) then { clearAllItemsFromBackpack  _unit; };
};

_unit addBackpack "B_Carryall_oli";
for "_i" from 1 to 3 do {
	[_unit, (_load select _i), _i] call sux_apply_weapon;
};
removeBackpack _unit;

for "_i" from 4 to 6 do {
	[_unit, (_load select _i), _i] call sux_apply_carryable;
};

{ _unit linkItem _x; } foreach (_load select _ITEMS);
if ( (_load select _HEADGEAR)  != "") then {
	_unit addHeadgear (_load select _HEADGEAR);
};

if ((_load select _BINOC)  != "") then {
	_unit addWeapon (_load select _BINOC);
};
if ((_load select _GOGGLES)  != "") then {
	_unit addGoggles (_load select _GOGGLES);
};

