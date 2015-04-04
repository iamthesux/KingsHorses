_container = _this select 0;
nul = [
	_container,
	[
		["Base_WarfareBBarrier10xTall", 5],
		["Land_HBarrierTower_F", 4],
		["Land_BagBunker_Tower_F", 2],
		["Land_HBarrier_3_F", 4],
		["Land_HBarrier_5_F", 5],
		["Land_BagBunker_Small_F", 2],
		["Land_BagFence_Long_F", 4],
		["Land_BagFence_Round_F", 2]
	]
] execVM "R3F_LOG\USER_FUNCT\auto_load_in_vehicle.sqf";
