/*
	Author: voiper
	
	Description: Make main map dark when it's dark, and enable a flashlight for use on the map.
	
	Parameters: 
		0: Bool (optional); whether player will respawn; default false.
		1: Scalar (optional); flashlight size (0 = normal, 1 = large); default 0.
	
	Returns:
		None.
*/

_respawn = [_this, 0, false, [true]] call BIS_fnc_param;
_size = [_this, 1, 0, [0]] call BIS_fnc_param;

[_respawn] execVM "vip_lit\vip_lit_lightIntensity.sqf";

_arr = toArray str missionConfigFile; _arr resize (count _arr - 15); _missionRoot = toString _arr;
vip_lit_var_cl_texture = _missionRoot + "vip_lit\resource\flashlight.paa";

//size of flashlight; portion of the screen horizontal; bigger number = smaller beam
vip_lit_var_cl_scale = switch (_size) do {

	case 0: {2.15};
	case 1: {1.75};
};

vip_lit_var_cl_flashlightOn = false;
vip_lit_var_cl_flashlightKeyDown = false;
vip_lit_var_cl_mapMouseX = 0;
vip_lit_var_cl_mapMouseY = 0;
_mapSize = getNumber (configFile >> "CfgWorlds" >> worldName >> "mapSize");
if (worldName == "VR") then {_mapSize = 8192};
vip_lit_var_cl_mapScaleSize = _mapSize / 1280; //map sizes are multiples of 1280

waitUntil {!isNil "vip_lit_var_cl_ambientLight"};
waitUntil {!isNull (finddisplay 12)};

//draw flashlight
vip_lit_eh_cl_drawFlashlight = (findDisplay 12 displayCtrl 51) ctrlAddEventHandler ["Draw", {

	//map 
	_map = _this select 0;
	_mapZoom = ctrlMapScale _map;
	_mapScale = vip_lit_var_cl_mapScaleSize;	
	
	//resolution params (every frame in case player changes res mid-game)
	_resArray = getResolution;
	_resX = _resArray select 0;
	_resY = _resArray select 1;
	_uiScale = _resArray select 5;
	_viewPortX = _resArray select 2;
	_viewPortY = _resArray select 3;
	_realViewPortY = _resY * _uiScale; //A3 engine rounds viewport ratio, when they should be fractions; this can cause problems
	_realViewPortX = _realViewPortY * 4/3;
	
	//size the squares 
	_sizeY = 640 * safeZoneW;
	_sizeX = 640 * safeZoneWAbs;
	_sizeBeam = _sizeY / vip_lit_var_cl_scale; //size of beam is portion of screen horizontal
	
	//assign corrective ratio to fix sub-pixel gaps/overlaps (symptom of 2D viewport X/Y resolution rounding)
	_viewPortRatioFixY = 1;
	if (_realViewPortY != _viewPortY) then { 
		_viewPortRatioFixY = _realViewPortX / (_realViewPortY / _viewPortY * _viewPortX)
	} else { 
		if (_realViewPortX != _viewPortX) then {_viewPortRatioFixY = _realViewPortX / _viewPortX}
	};
	
	//offset the squares
	_offsetX = _mapZoom * _mapScale * (_sizeX * 2 + _sizeBeam);
	_offsetY = _mapZoom * _mapScale * (_sizeY + _sizeBeam) * _viewPortRatioFixY;
	_offsetYUp = _mapZoom * _mapScale * (_sizeY * 4 + _sizeBeam) * _viewPortRatioFixY; //up is bigger because of a potential exploit
	
	//colour the squares, set textures
	_c = vip_lit_var_cl_ambientLight;
	_a = 1 - _c;
	_blankTexture = "#(rgb,8,8,3)color(0,0,0,1)";
	_flashlight = if (vip_lit_var_cl_flashlightOn) then {vip_lit_var_cl_texture} else {_blankTexture};
	
	//fill colour
	_r = 0; _g = 0; _b = 0; _a2 = 0;
	if ((vip_lit_var_cl_artificialLight select 0) > vip_lit_var_cl_ambientLight) then {
	
		_colour = vip_lit_var_cl_artificialLight select 1;
		_r = _r + (_colour select 0);
		_g = _g + (_colour select 1);
		_b = _b + (_colour select 2);
		_a = 1 - (vip_lit_var_cl_artificialLight select 0);
		_a2 = 1;
	};
	
	//draw the squares
	_map drawIcon [format["#(rgb,8,8,3)color(%1,%2,%3,0.6)", _r, _g, _b], [1,1,1,_a2], [vip_lit_var_cl_mapMouseX, vip_lit_var_cl_mapMouseY], _sizeX * 2, _sizeY * 2, 0, "", 0]; //ambient fill colour
	_map drawIcon [_flashlight, [1,1,1,_a], [vip_lit_var_cl_mapMouseX, vip_lit_var_cl_mapMouseY], _sizeBeam, _sizeBeam, 0, "", 0]; //centre
	_map drawIcon [_blankTexture, [_c,_c,_c,_a], [vip_lit_var_cl_mapMouseX - _offsetX, vip_lit_var_cl_mapMouseY], _sizeX * 2, _sizeBeam, 0, "", 0]; //left
	_map drawIcon [_blankTexture, [_c,_c,_c,_a], [vip_lit_var_cl_mapMouseX + _offsetX, vip_lit_var_cl_mapMouseY], _sizeX * 2, _sizeBeam, 0, "", 0]; //right
	_map drawIcon [_blankTexture, [_c,_c,_c,_a], [vip_lit_var_cl_mapMouseX, vip_lit_var_cl_mapMouseY - _offsetY], _sizeX * 4, _sizeY, 0, "", 0]; //down
	_map drawIcon [_blankTexture, [_c,_c,_c,_a], [vip_lit_var_cl_mapMouseX, vip_lit_var_cl_mapMouseY + _offsetYUp], _sizeX * 4, _sizeY * 4, 0, "", 0]; //up
}];

//get mouse position on map while moving
vip_lit_eh_cl_mouseMoveFlashlight = (findDisplay 12 displayCtrl 51) ctrlAddEventHandler ["MouseMoving", {

	_map = _this select 0;
	_mapPos = _map ctrlMapScreenToWorld [_this select 1, _this select 2];
	vip_lit_var_cl_mapMouseX = _mapPos select 0;
	vip_lit_var_cl_mapMouseY = _mapPos select 1;
}];

//get mouse position on map while idle
vip_lit_eh_cl_mouseHoldFlashlight = (findDisplay 12 displayCtrl 51) ctrlAddEventHandler ["MouseHolding", {

	_map = _this select 0;
	_mapPos = _map ctrlMapScreenToWorld [_this select 1, _this select 2];
	vip_lit_var_cl_mapMouseX = _mapPos select 0;
	vip_lit_var_cl_mapMouseY = _mapPos select 1;
}];

//enable 'F' for flashlight; simulate as if real key up/down is the button on a flashlight
vip_lit_eh_cl_keyDnFlashlight = (findDisplay 12) displayAddEventHandler ["KeyDown", {

	if ((_this select 1) in (actionKeys "NextWeapon")) then {

		if !(vip_lit_var_cl_flashlightKeyDown) then {playSound "vip_lit_snd_flashlightClick"; vip_lit_var_cl_flashlightKeyDown = true}; //won't click again until the variable is set back to false by keyup event
	};
	false
}];

vip_lit_eh_cl_keyUpFlashlight = (findDisplay 12) displayAddEventHandler ["KeyUp", {

	if ((_this select 1) in (actionKeys "NextWeapon")) then {
	
		vip_lit_var_cl_flashlightKeyDown = false;
		vip_lit_var_cl_flashlightOn = if (vip_lit_var_cl_flashlightOn) then {false} else {true};
		0 = [] spawn {sleep 0.016; playsound "vip_lit_snd_flashlightClick"}; //sleep to create buffer between sounds; keyUp fires instantly if player presses and releases quickly
	};
	false
}];

if (!_respawn) then {

	vip_lit_eh_cl_killedFlashlight = player addEventHandler ["Killed", {

		(findDisplay 12 displayCtrl 51) ctrlRemoveEventHandler ["Draw", vip_lit_eh_cl_drawFlashlight];
		(findDisplay 12 displayCtrl 51) ctrlRemoveEventHandler ["MouseMoving", vip_lit_eh_cl_mouseMoveFlashlight];
		(findDisplay 12 displayCtrl 51) ctrlRemoveEventHandler ["MouseHolding", vip_lit_eh_cl_mouseHoldFlashlight];
		(findDisplay 12) displayRemoveEventHandler ["KeyDown", vip_lit_eh_cl_keyDnFlashlight];
		(findDisplay 12) displayRemoveEventHandler ["KeyUp", vip_lit_eh_cl_keyUpFlashlight];
		
		[] spawn {player removeEventHandler ["Killed", vip_lit_eh_cl_killedFlashlight]};
	}];
};