/*
	Author: voiper
	
	Description: Remove some unrealistic UI aspects from main map.
	
	Parameters: 
		0: Bool (optional); whether player will respawn; default false.
		1: Bool (optional); whether to disable "show player on map" button; default true.
		2: Bool (optional); whether to disable map textures button; default true.
	
	Returns:
		None.
*/

_respawn = [_this, 0, false, [true]] call BIS_fnc_param;
_find = [_this, 1, true, [true]] call BIS_fnc_param;
_textures = [_this, 2, true, [true]] call BIS_fnc_param;

waitUntil {!isNull (findDisplay 12)};

disableSerialization;

//1201 = textures, 1202 = player find button, 1204/1205 = separators
_ctrlsToModifyArray = [1204, 1205];
if (_find) then {_ctrlsToModifyArray pushBack 1202};
if (_textures) then {_ctrlsToModifyArray pushBack 1201};

if (_textures) then {

	ctrlActivate ((uiNamespace getVariable "RSCDiary") displayCtrl 107);
	//remove map grid next to cursor; unfortunately, since BIS provided no return index for the original MouseMoving eventhandler in ui_f.pbo, we have to remove all of them
	if (_textures) then {(findDisplay 12 displayCtrl 51) ctrlRemoveAllEventHandlers "MouseMoving"};
};

//disable map textures, player name, "Where am I?" button
_display = findDisplay 12;
{
	_ctrl = _display displayCtrl _x;
	_ctrl ctrlEnable false;
	_ctrl ctrlSetTextColor [0,0,0,0];
	_ctrl ctrlSetToolTip "";
	_ctrl ctrlCommit 0;
} forEach _ctrlsToModifyArray;

//if player won't respawn, restore everything to normal
if !(_respawn) then {

	 vip_lit_eh_cl_killedMap = player addEventHandler ["Killed", {
			
		_display = findDisplay 12;
		{
			_ctrl = _display displayCtrl _x;
			_ctrl ctrlEnable true;
			_ctrl ctrlSetTextColor [1,1,1,0.7];
			_ctrl ctrlCommit 0;
		} forEach [1201, 1202, 1204, 1205];
		
		_textures = (_display displayCtrl 1201) ctrlSetToolTip "Toggle map textures";
		_find = (_display displayCtrl 1202) ctrlSetToolTip "Move map to player position";
		{_x ctrlCommit 0} forEach [_textures, _find];
		
		//taken from RscDiary.sqf in ui_f.pbo; all credit to BIS
		_trackColor = getarray (configfile >> "cfgWrapperUI" >> "Cursors" >> "Track" >> "color");
		{
			_trackColor set [_foreachindex,_x call bis_fnc_parsenumber];
		} foreach _trackColor;
		
		(_display displayCtrl 51) ctrladdeventhandler ["mousemoving", format ["
			_map = _this select 0;
			_text = (ctrlparent _map) displayctrl 1016;
			if (_this select 3) then {
				_mapPos = _map ctrlmapscreentoworld [_this select 1,_this select 2];
				_textPos = ctrlposition _text;
				_textPos set [0,(_this select 1) + 0.02];
				_textPos set [0,(_this select 1) + (_textPos select 2) / 4];
				_textPos set [1,(_this select 2) - (_textPos select 3) / 2];
				_text ctrlsetposition _textPos;
				_text ctrlsettext format [
					'%2\n%3 m',
					mapgridposition _mapPos,
					round getterrainheightasl _mapPos
				];
				_text ctrlsettextcolor %1;
				_text ctrlsetfade 0;
				_text ctrlenable false;
				_text ctrlcommit 0;
			} else {
				_text ctrlsetfade 1;
				_text ctrlcommit 0;
			};
			", _trackColor,"%1","%2"]
		];
		
		[] spawn {player removeEventHandler ["Killed", vip_lit_eh_cl_killedMap]};
	}];
};