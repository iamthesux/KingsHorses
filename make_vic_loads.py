from p4a.formats.rap.text import Reader, Writer
from p4a.formats.rap import Klass

from p4a.loadout import Crate

from loads.cdf_vic import cdf_vic
from loads.us_vic import us_vic
import os

config = Reader(os.path.join('mods', 'sh_factions','config.cpp')).read()

vics = [
	"sh_cdf_bmp1",
	"sh_cdf_t80bv",
	"sh_cdf_gaz66_ammo",
	"sh_cdf_ural_fuel",
	"sh_cdf_gaz66_repair",
	"sh_cdf_gaz66",
	"sh_cdf_uaz_open",
	"sh_cdf_uaz",
	"sh_cdf_ural",
	"sh_cdn_mi24",
	"sh_cdn_mi8",
]
us_vics = [
	"sh_marines_rg31",
	"sh_marines_m1a1",
]

for k in config.klasses:
	print k.name

for v in vics:
	k = config('CfgVehicles')(v)
	cdf_vic().generate_config(k)
for v in us_vics:
	k = config('CfgVehicles')(v)
	us_vic().generate_config(k)

Writer('mods/sh_factions/config.cpp').write(config)