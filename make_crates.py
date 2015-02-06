from p4a.formats.rap.text import Reader, Writer
from p4a.formats.rap import Klass

import inspect
import importlib

import loads.cdf_crates as cdf

cfg = Klass()


patch = Klass('sh_alive_boxes')
patch['units'] = []
patch['weapons'] = []
patch['requiredVersion'] = 0.10000000149
patch['requiredAddons'] = ["A3_Weapons_F"]
cfg(Klass('cfgPatches'))
cfg('cfgPatches')(patch)

cfg(Klass('cfgVehicles'))

#print cfg("cfgPatches")('spearhead_alive_boxes')['units']

base_classes = set([])
crates = []

for grp in ['cdf_crates', 'marines_crates', 'cdfsf_crates', 'soar_crates']:
	lib = importlib.import_module('loads.' + grp)
	for name, obj in inspect.getmembers(lib):
		if inspect.isclass(obj) and 'NoWrite' not in obj.__dict__:
			crate = obj(prefix='sh_alive_').generate_config()
			if crate.inherits and crate.inherits not in base_classes:
				base_classes.add(c.inherits)
			crates.append(crate)

# for c in crates:
	# if c.inherits and c.inherits not in base_classes:
		# base_classes.add(c.inherits)

for b in base_classes:
	k = Klass(b)
	k.extern = True
	cfg("cfgVehicles")(k)

for c in crates:
	c['author']="sux"
	cfg("cfgVehicles")(c)
	cfg("cfgPatches")('sh_alive_boxes')['units'] += [c.name]
	#cfg("cfgPatches")('spearhead_alive_boxes')['units'].append(c.cname)
	

Writer('sh_ammo_crates/config.cpp').write(cfg)