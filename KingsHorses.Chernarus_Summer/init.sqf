
#include "initBriefing.hpp";
//call compile preprocessFileLineNumbers "disable_map_textures.sqf";
[true, true, false, [true, 0],[true,1000], true] execVM "vip_lit\vip_lit_init.sqf";
execVM "R3F_LOG\init.sqf";

RHSDecalsOff = true;
tf_same_sw_frequencies_for_side = true;
tf_same_lw_frequencies_for_side = true;

tf_east_radio_code = '_bluefor';
tf_guer_radio_code = '_bluefor';

det5_sw_freqs = ["423.1","423.2","423.3","423.4","423.5","423.6","423.7","423.8"];
cdf_sw_freqs = ["320.1","320.2","320.3","320.4","320.5","320.6","320.7","320.8"];
marine_sw_freqs = ["404.1","404.2","404.3","404.4","404.5","404.6","404.7","404.8"];

if (!isDedicated) then {
	[] spawn {
		waitUntil { player == player; };
		_load_name = player getVariable 'sux_loadout';
		[player, _load_name] call suxlo_fnc_apply_loadout;
		player addmpeventhandler ["mprespawn", "_load = (_this select 0) getVariable 'sux_loadout'; [_this select 0, _load] call suxlo_fnc_apply_loadout;"];
	};
};
lw_freqs = ["36.6","42.7","48.2","51.8","53.3","57.3","59.5","60.4","62.8"];
if(isServer) then {
	_sw = false call TFAR_fnc_generateSwSettings;
	_lw = false call TFAR_fnc_generateLrSettings;
	
	_lw set [2, lw_freqs];
	tf_freq_west_lr = _lw;
	tf_freq_east_lr = _lw;
	tf_freq_guer_lr = _lw;
	_sw set [2, marine_sw_freqs];
	tf_freq_west = _sw;
	_sw set [2, det5_sw_freqs];
	tf_freq_east = _sw;
	_sw set [2, cdf_sw_freqs];
	tf_freq_guer = _sw;
	publicVariable "tf_freq_west";
	publicVariable "tf_freq_east";
	publicVariable "tf_freq_guer";
	publicVariable "tf_freq_west_lr";
	publicVariable "tf_freq_east_lr";
	publicVariable "tf_freq_guer_lr";

	[] spawn {
		waitUntil {!isNil "ALiVE_STATIC_DATA_LOADED"};
		[ALIVE_factionDefaultTransport, "sh_opfor_chdkz", ["sh_chdkz_ural"]] call ALIVE_fnc_hashSet;
		diag_log format ["____________ %1", ALIVE_factionDefaultTransport];
	};
};

