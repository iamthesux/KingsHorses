
tf_same_sw_frequencies_for_side = true;
tf_same_lw_frequencies_for_side = true;

tf_east_radio_code = '_bluefor';
tf_guer_radio_code = '_bluefor';

det5_sw_freqs = ["420.1","420.2","420.3","420.4","420.5","420.6","420.7","420.8"];
cdf_sw_freqs = ["320.1","320.2","320.3","320.4","320.5","320.6","320.7","320.8"];
marine_sw_freqs = ["320.1","320.2","320.3","320.4","320.5","320.6","320.7","320.8"];

lw_freqs = ["36.6","42.7","48.2","51.8","53.3","57.3","59.5","60.4","62.8"];
if (isServer) then {
	_sw = false call TFAR_fnc_generateSwSettings;
	_lw = false call TFAR_fnc_generateLrSettings;
	//diag_log _sw;
	
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
};