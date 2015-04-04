_respawn = [_this, 0, false, [true]] call bis_fnc_param;

waitUntil {

	_clouds = if (overcast > 0.75) then {0.25 * overcast} else {0};
	vip_lit_var_cl_ambientLight = (sunOrMoon - _clouds) + (0.3 * moonIntensity);

	if (vip_lit_var_cl_ambientLight < 0.5) then {
	
		_nearestLight = objNull;
		_allGrenades = player nearObjects ["SmokeShell", 10];
		_chemlights = [];
		{if (((toUpper (typeOf _x)) find (toUpper "chemlight")) > -1) then {_chemlights pushback _x}} forEach _allGrenades;
		if (count _chemlights > 0) then {
			{if ((_nearestLight distance player) > (_x distance player)) then {_nearestLight = _x}} forEach _chemlights;
		};
		
		if (!isNull _nearestLight) then {
		
			_type = typeOf _nearestLight;
			_colour = switch (true) do {
			
				case (_type find "red" > -1): {[0.5,0,0]};
				case (_type find "green" > -1): {[0,0.5,0]};
				case (_type find "blue" > -1): {[0,0.6,0.6]};
				case (_type find "yellow" > -1): {[0.5,0.5,0]};
			};
			
			_intensity = 1 / ((player distance _nearestLight) - 1);
			if (_intensity < 0) then {_intensity = 1} else {if (_intensity > 1) then {_intensity = 1}};
			
			vip_lit_var_cl_artificialLight = [vip_lit_var_cl_ambientLight + _intensity, _colour];
		} else {vip_lit_var_cl_artificialLight = [0,[0,0,0]]};
	
	} else {vip_lit_var_cl_artificialLight = [0,[0,0,0]]};

	sleep 0.5;
	
	!(alive player) && !_respawn
};