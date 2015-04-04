// Normal briefing
if (!isDedicated) then {
	[] spawn {
		waitUntil { player == player; };
		player createDiaryRecord [
			"Diary", 
			[
				"Radio Nets", 
				"
036.60 - MNC-C Net<br/>
042.70 - Aviation Net<br/>
048.20 - Fires Net<br/>
051.80 - 3/2 Marines<br/>
053.30 - Chernarus Defense Force<br/>
057.30 - Recon Net<br/>
059.50 - MEDEVAC/DUSTOFF Net<br/>
060.40 - CDF SF Net<br/>
062.80 - CSAR/SERE Net"
			]
		];

		player createDiaryRecord [
			"Diary",
			[
				"Callsigns",
				"
Chernarus Defense Force: HOMELAND<br/>
Chernarus Defense Force Mechanized (3 ACR): THUNDER<br/>
Chernarus Defense Force Recon (SASR): SNAKEYES <br/>
Chernarus Defense Force SF (DET-5): SPEARHEAD<br/>
1st Platoon, I CO, 26th MEU (MCRU): IRONMAN<br/>
Weapons Platoon, A CO, 26th MEU (16AA): HELLRAISER<br/>
Chenarus Defense Force Aviation (CAD-N): JESTER"
			]
		];
	};
};