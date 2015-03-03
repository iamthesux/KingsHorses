from p4a.formats.rap.text import Reader, Writer
from p4a.formats.rap import Klass

from p4a.loadout import Crate

import inspect
import importlib

import loads.cdf_crates as cdf
from loads.cse_medical import med_supplies
from loads.cse_rations import int_supplies
from loads.cse_usrations import us_supplies

cfg = Klass()

class empty_crate(Crate):
	base = 'rhs_weapons_crate_ak_ammo_545x39_standard'
	title = 'Empty Crate'

class empty_crate_lg(Crate):
	base = 'B_supplyCrate_F'
	title = 'Empty Crate (Large)'

class cdf_medical(med_supplies):
	base = 'rhs_weapons_crate_ak_ammo_545x39_standard'
	title = 'CDF Medical Supplies'

patch = Klass('sh_alive_boxes')
patch['units'] = []
patch['weapons'] = []
patch['requiredVersion'] = 0.10000000149
patch['requiredAddons'] = ["A3_Weapons_F"]
cfg(Klass('cfgPatches'))
cfg('cfgPatches')(patch)

cfg(Klass('cfgVehicles'))

#print cfg("cfgPatches")('spearhead_alive_boxes')['units']

base_classes = {}
crates = [
	empty_crate(prefix='sh_alive_').generate_config(),
	empty_crate_lg(prefix='sh_alive_').generate_config(),
	med_supplies(prefix='sh_alive_').generate_config(),
	cdf_medical(prefix='sh_alive_').generate_config(),
	int_supplies(prefix='sh_alive_').generate_config(),
	us_supplies(prefix='sh_alive_').generate_config(),
]

for grp in ['cdf_crates', 'marines_crates', 'cdf_recce_crates', 'soar_crates']:
	lib = importlib.import_module('loads.' + grp)
	for name, obj in inspect.getmembers(lib):
		if inspect.isclass(obj) and 'NoWrite' not in obj.__dict__:
			crates.append(obj(prefix='sh_alive_').generate_config())

for c in crates:
	if c.inherits and c.inherits not in base_classes:
		base_classes[c.inherits] = True

for b in base_classes.keys():
	k = Klass(b)
	k.extern = True
	cfg("cfgVehicles")(k)

for c in crates:
	cfg("cfgVehicles")(c)
	cfg("cfgPatches")('sh_alive_boxes')['units'] += [c.name]
	#cfg("cfgPatches")('spearhead_alive_boxes')['units'].append(c.cname)
	

Writer('mods/sh_ammo_crates/config.cpp').write(cfg)