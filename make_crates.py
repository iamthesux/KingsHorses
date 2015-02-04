from p4a.formats.rap.text import Reader, Writer
from p4a.formats.rap import Klass

import loads.cdf_crates as cdf

cfg = Klass()


patch = Klass('spearhead_alive_boxes')
patch['units'] = []
patch['weapons'] = []
patch['requiredVersion'] = 0.10000000149
patch['requiredAddons'] = ["A3_Weapons_F"]
cfg(Klass('cfgPatches'))
cfg('cfgPatches')(patch)

cfg(Klass('cfgVehicles'))

#print cfg("cfgPatches")('spearhead_alive_boxes')['units']

bases = set([])
crates = [
	cdf.cdf_weapons(prefix='spearhead_').generate_config(),
	cdf.cdf_launchers(prefix='spearhead_').generate_config(),
	cdf.cdf_explosives(prefix='spearhead_').generate_config(),
]
for c in crates:
	if c.inherits and c.inherits not in bases:
		bases.add(c.inherits)

for b in bases:
	k = Klass(b)
	k.extern = True
	cfg("cfgVehicles")(k)

for c in crates:
	c['author']="sux"
	cfg("cfgVehicles")(c)
	cfg("cfgPatches")('spearhead_alive_boxes')['units'] += [c.name]
	#cfg("cfgPatches")('spearhead_alive_boxes')['units'].append(c.cname)
	

Writer('sh_ammo_crates/config.cpp').write(cfg)