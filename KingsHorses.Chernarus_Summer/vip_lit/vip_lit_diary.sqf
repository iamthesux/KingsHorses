_mapFind = _this select 0;
_mapTextures = _this select 1;
_flashlight = _this select 2;
_nvgDist = _this select 3;
_nvgGrain = _this select 4;

_colourText = str (["IGUI_WARNING"] call vip_cmn_fnc_cl_profileColoursHTML);

call vip_cmn_fnc_cl_authorDiaryTopic;

_mapHeader = if (_mapFind || _mapTextures || _flashlight) then {format["<br /><font color=%1>Map</font><br />", _colourText]} else {""};
_nvgHeader = if (_nvgGrain || (_nvgDist select 0)) then {format["<br /><font color=%1>NVG</font><br />", _colourText]} else {""};
_mapFindText = if (_mapFind) then {"-The ""Show player on map"" button is disabled.<br />"} else {""};
_mapTexturesText = if (_mapTextures) then {"-Map textures and the grid reference next to the cursor are disabled.<br />"} else {""};
_flashlightText = if (_flashlight) then {"-The map is affected by environmental lighting conditions. If the map is too dark, players can use a small flashlight to illuminate it. Press the ""Next Weapon"" key (default ""F"") to activate the flashlight.<br />"} else {""};
_nvgDistText = if (_nvgDist select 0) then {format["-Night vision devices have a maximum view distance of %1m.<br />", _nvgDist select 1]} else {""};
_nvgGrainText = if (_nvgGrain) then {"-Night vision devices have analog noise."} else {""};

player createDiaryRecord ["vip_modules_var_cl_diary", ["LIT", format["
<font color=%1 size='18'>Little Immersion Tweaks</font>
<br /><br />
This mission uses voiper's Little Immersion Tweaks (LIT) module. This is a lightweight module that adds some flavour and realism to Arma 3's map and NVG.<br /><br />
<font color=%1 size='18'>Features Used In This Mission:</font><br />
%2
%4
%5
%6
%3
%7
%8
", _colourText, _mapHeader, _nvgHeader, _mapFindText, _mapTexturesText, _flashlightText, _nvgDistText, _nvgGrainText]]];