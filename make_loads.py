import os
import inspect
import importlib
import settings as cfg

ldir = os.path.join(cfg.mish, 'loads')
if not os.path.isdir(ldir):
	os.mkdir(ldir)
os.chdir(ldir)

for grp in ['cdf_2009', 'cdf_recce_2009', 'marines_2009', 'c5sd_2009', 'c5sd_crates', 'soar_2009']:
	lib = importlib.import_module('loads.' + grp)
	for name, obj in inspect.getmembers(lib):
		if inspect.isclass(obj) and 'NoWrite' not in obj.__dict__:
			obj().write()
